#!/usr/bin/env python3
"""Validate internal links and anchors across the repository.

The check is offline by default. External URLs are reported as skipped rather
than silently ignored, and are checked in continuous integration by
``.github/workflows/links.yml``, which is the only place where this repository
makes network calls.

What is checked:

* Every relative Markdown, image, and directory link resolves on disk.
* Every in-page anchor resolves to a heading in the target file.
* Every file listed in the MkDocs navigation exists.
* Every Markdown file under ``docs/`` appears in the MkDocs navigation.
* ``SUMMARY.md`` and the MkDocs navigation cover the same set of files.

Usage:
    python scripts/validate_links.py
    python scripts/validate_links.py --list-external

Exit status:
    0  no violations
    1  violations found, each printed as ``path:line: message``
    2  a file could not be read or parsed
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote

from _common import (
    DOCS_DIR,
    REPO_ROOT,
    DataError,
    Reporter,
    fail,
    markdown_files,
    relative,
)

LINK_PATTERN: re.Pattern[str] = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_PATTERN: re.Pattern[str] = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.MULTILINE)
NAV_ENTRY_PATTERN: re.Pattern[str] = re.compile(r":\s*([A-Za-z0-9_./-]+\.md)\s*$")
EXTERNAL_PREFIXES: tuple[str, ...] = ("http://", "https://", "mailto:", "tel:", "ftp://")


def slugify(heading: str) -> str:
    """Convert a Markdown heading to its GitHub-style anchor slug.

    Args:
        heading: Heading text without the leading hashes.

    Returns:
        The anchor slug, lowercased, with punctuation removed and spaces
        replaced by hyphens.
    """
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    text = re.sub(r"[`*_~]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s]+", "-", text)


def anchors_of(path: Path) -> set[str]:
    """Collect every anchor slug defined by headings in a Markdown file.

    Args:
        path: Markdown file to scan.

    Returns:
        The set of anchor slugs, including the numeric suffixes GitHub adds to
        repeated headings.
    """
    text = path.read_text(encoding="utf-8")
    slugs: list[str] = []
    seen: dict[str, int] = {}
    for match in HEADING_PATTERN.finditer(text):
        base = slugify(match.group(2))
        if not base:
            continue
        count = seen.get(base, 0)
        seen[base] = count + 1
        slugs.append(base if count == 0 else f"{base}-{count}")
    return set(slugs)


def check_markdown_links(reporter: Reporter, list_external: bool) -> int:
    """Resolve every relative link and anchor in every Markdown file.

    Args:
        reporter: Collector for violations.
        list_external: Print each external URL that was skipped.

    Returns:
        The number of external links skipped.
    """
    reporter.note_check("--check-markdown-links")
    external = 0
    anchor_cache: dict[Path, set[str]] = {}

    for path in markdown_files():
        lines = path.read_text(encoding="utf-8").splitlines()
        inside_code = False
        for number, line in enumerate(lines, start=1):
            if line.lstrip().startswith("```"):
                inside_code = not inside_code
                continue
            if inside_code:
                continue
            for match in LINK_PATTERN.finditer(line):
                target = unquote(match.group(1))
                if target.startswith(EXTERNAL_PREFIXES):
                    external += 1
                    if list_external:
                        print(f"{relative(path)}:{number}: external (not checked): {target}")
                    continue
                if target.startswith("#"):
                    slugs = anchor_cache.setdefault(path, anchors_of(path))
                    if target[1:] not in slugs:
                        reporter.add(
                            path, number, f"anchor {target!r} does not match a heading in this file"
                        )
                    continue

                file_part, _, anchor = target.partition("#")
                resolved = (path.parent / file_part).resolve()
                if not resolved.exists():
                    reporter.add(
                        path,
                        number,
                        f"link target {file_part!r} does not exist at {relative(resolved)}",
                    )
                    continue
                if anchor and resolved.suffix == ".md":
                    slugs = anchor_cache.setdefault(resolved, anchors_of(resolved))
                    if anchor not in slugs:
                        reporter.add(
                            path,
                            number,
                            f"anchor {'#' + anchor!r} does not match a heading in "
                            f"{relative(resolved)}",
                        )
    return external


def nav_files(reporter: Reporter) -> set[str]:
    """Extract the documentation files listed in the MkDocs navigation.

    The navigation is parsed with a line pattern rather than a YAML loader,
    because ``mkdocs.yml`` uses a Python-specific YAML tag for the Mermaid
    fence that a plain safe loader rejects.

    Args:
        reporter: Collector for violations.

    Returns:
        Navigation entries as paths relative to ``docs/``.

    Raises:
        DataError: If ``mkdocs.yml`` is missing.
    """
    path = REPO_ROOT / "mkdocs.yml"
    if not path.is_file():
        raise DataError("mkdocs.yml: file not found")
    entries: set[str] = set()
    inside_nav = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.startswith("nav:"):
            inside_nav = True
            continue
        if inside_nav and line and not line.startswith((" ", "-", "\t")):
            inside_nav = False
        if not inside_nav:
            continue
        if "://" in line:
            # An external navigation target, used for files that live outside
            # docs_dir. Checked by the scheduled link workflow, not on disk.
            continue
        match = NAV_ENTRY_PATTERN.search(line)
        if not match:
            continue
        entry = match.group(1)
        entries.add(entry)
        if not (DOCS_DIR / entry).is_file():
            reporter.add(path, number, f"navigation entry {entry!r} has no file at docs/{entry}")
    return entries


def check_nav_coverage(reporter: Reporter, entries: set[str]) -> None:
    """Verify that navigation and the docs tree cover the same files.

    Args:
        reporter: Collector for violations.
        entries: Navigation entries relative to ``docs/``.
    """
    reporter.note_check("--check-nav")
    on_disk = {
        str(path.relative_to(DOCS_DIR)).replace("\\", "/") for path in markdown_files(DOCS_DIR)
    }
    for missing in sorted(on_disk - entries):
        reporter.add(
            DOCS_DIR / missing,
            0,
            "file exists under docs/ but is absent from the mkdocs.yml navigation, so it will "
            "not appear on the site",
        )


def check_summary(reporter: Reporter, entries: set[str]) -> None:
    """Verify that SUMMARY.md lists the same documentation files as the navigation.

    Args:
        reporter: Collector for violations.
        entries: Navigation entries relative to ``docs/``.
    """
    reporter.note_check("--check-summary")
    path = REPO_ROOT / "SUMMARY.md"
    if not path.is_file():
        reporter.add(path, 0, "SUMMARY.md not found")
        return
    text = path.read_text(encoding="utf-8")
    listed = {
        match.group(1)[len("docs/") :]
        for match in LINK_PATTERN.finditer(text)
        if match.group(1).startswith("docs/") and match.group(1).endswith(".md")
    }
    for missing in sorted(entries - listed):
        reporter.add(path, 0, f"docs/{missing} is in the mkdocs navigation but not in SUMMARY.md")
    for extra in sorted(listed - entries):
        reporter.add(path, 0, f"docs/{extra} is in SUMMARY.md but not in the mkdocs navigation")


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line parser.

    Returns:
        The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="validate_links.py",
        description="Validate internal links, anchors, and navigation coverage.",
    )
    parser.add_argument(
        "--list-external",
        action="store_true",
        help="print each external URL that was skipped rather than only counting them",
    )
    return parser


def main() -> int:
    """Run the link checks and return the process exit status.

    Returns:
        0 when no violations were found, 1 when violations were found.
    """
    args = build_parser().parse_args()
    reporter = Reporter("validate_links.py")
    try:
        external = check_markdown_links(reporter, args.list_external)
        entries = nav_files(reporter)
        check_nav_coverage(reporter, entries)
        check_summary(reporter, entries)
    except DataError as exc:
        fail(str(exc))
    print(
        f"validate_links.py: {external} external URL(s) skipped; they are checked by "
        f".github/workflows/links.yml"
    )
    return reporter.finish()


if __name__ == "__main__":
    raise SystemExit(main())
