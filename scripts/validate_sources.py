#!/usr/bin/env python3
"""Validate the source register and every reference to it.

The register in ``data/sources.csv`` is the only route by which a source enters
this repository. This script enforces that rule from four directions:

1. Every row of the register is structurally valid and complete.
2. Every ``source_id`` used in any dataset resolves to a register row.
3. Every citation key in ``references.bib`` corresponds to a register row, and
   every register row that is cited in prose has a bibliography entry.
4. Every numerical claim in prose carries a footnote reference.

Checks are grouped so that a contributor can run one of them in isolation
during a large edit. With no flags, every check runs.

Usage:
    python scripts/validate_sources.py
    python scripts/validate_sources.py --check-dates
    python scripts/validate_sources.py --check-citations --check-duplicates

Exit status:
    0  no violations
    1  violations found, each printed as ``path:line: message``
    2  a file could not be read or parsed
"""

from __future__ import annotations

import argparse
import re
from collections import Counter

from _common import (
    DATASETS,
    DATE_PATTERN,
    DOCS_DIR,
    EVIDENCE_GRADES,
    REPO_ROOT,
    DataError,
    Reporter,
    csv_line_number,
    fail,
    is_date,
    is_missing,
    markdown_files,
    read_csv,
    relative,
)

SOURCE_TYPES: frozenset[str] = frozenset(
    {
        "peer_reviewed",
        "preprint",
        "technical_report",
        "model_card",
        "benchmark_methodology",
        "dataset",
        "documentation",
        "pricing_page",
        "license",
        "standards_body",
        "government_report",
        "institutional_report",
    }
)

SOURCE_ID_PATTERN: re.Pattern[str] = re.compile(r"^[a-z][a-z0-9]*[0-9]{4}[a-z0-9]+$")
DOI_PATTERN: re.Pattern[str] = re.compile(r"^10\.[0-9]{4,9}/[-._;()/:A-Za-z0-9]+$")
BIB_KEY_PATTERN: re.Pattern[str] = re.compile(r"^@\w+\{([^,]+),", re.MULTILINE)
FOOTNOTE_REF_PATTERN: re.Pattern[str] = re.compile(r"\[\^([A-Za-z0-9_:.-]+)\]")
FOOTNOTE_DEF_PATTERN: re.Pattern[str] = re.compile(r"^\[\^([A-Za-z0-9_:.-]+)\]:", re.MULTILINE)

#: A number in prose that plausibly reports a measurement. Deliberately narrow:
#: it ignores section numbers, list markers, years in dates, and small integers
#: written as words, because a check that fires constantly is a check that
#: contributors learn to ignore.
CLAIM_NUMBER_PATTERN: re.Pattern[str] = re.compile(
    r"(?<![\w./-])(\d{1,3}(?:,\d{3})+|\d+\.\d+|\d+(?:\.\d+)?\s*(?:%|percent|GiB|GB|TB|"
    r"tokens|USD|Wh|kWh|joules|J\b|ms|seconds))",
)

#: Relative time expressions that are prohibited in prose about current models.
RELATIVE_TIME_PATTERN: re.Pattern[str] = re.compile(
    r"\b(currently|at present|at the time of writing|recently|nowadays|as of today|"
    r"the latest model|latest models|today's models|right now)\b",
    re.IGNORECASE,
)

#: Lines that are exempt from the prose checks.
SKIP_LINE_PREFIXES: tuple[str, ...] = ("    ", "\t", "|", ">", "<!--", "[^")


def _in_code_block(line: str, state: dict[str, bool]) -> bool:
    """Track fenced code blocks so that code is not checked as prose.

    Args:
        line: The current line.
        state: Mutable state carrying the ``inside`` flag between calls.

    Returns:
        True when the line is part of a fenced code block, including the fence.
    """
    if line.lstrip().startswith("```"):
        state["inside"] = not state["inside"]
        return True
    return state["inside"]


def check_register(reporter: Reporter) -> dict[str, dict[str, str]]:
    """Validate every row of the source register.

    Args:
        reporter: Collector for violations.

    Returns:
        Mapping of ``source_id`` to the register row, for use by later checks.
        Rows that fail validation are still returned, so that a single bad row
        does not cascade into spurious unresolved-reference findings.
    """
    reporter.note_check("--check-register")
    path = DATASETS["sources"]
    _, rows = read_csv(path)
    register: dict[str, dict[str, str]] = {}

    for index, row in enumerate(rows):
        line = csv_line_number(index)
        source_id = row.get("source_id", "").strip()

        for field, value in row.items():
            if value is None or is_missing(value):
                reporter.add(
                    path,
                    line,
                    f"field {field!r} is empty or uses a rejected placeholder. Use a value or one "
                    f"of the reserved strings in data-sources.md section 1.2",
                )

        if source_id and not SOURCE_ID_PATTERN.match(source_id):
            reporter.add(
                path,
                line,
                f"source_id {source_id!r} does not match author-year-keyword form, "
                f"for example 'hoffmann2022training'",
            )
        if source_id in register:
            reporter.add(path, line, f"duplicate source_id {source_id!r}")
        if source_id:
            register[source_id] = row

        source_type = row.get("source_type", "").strip()
        if source_type and source_type not in SOURCE_TYPES:
            reporter.add(
                path,
                line,
                f"source_type {source_type!r} is not one of: {', '.join(sorted(SOURCE_TYPES))}",
            )

        grade = row.get("evidence_grade", "").strip()
        if grade and grade not in EVIDENCE_GRADES:
            reporter.add(path, line, f"evidence_grade {grade!r} is not A, B, or C")

        peer_reviewed = row.get("peer_reviewed", "").strip()
        if peer_reviewed and peer_reviewed not in {"true", "false"}:
            reporter.add(
                path, line, f"peer_reviewed {peer_reviewed!r} must be the literal 'true' or 'false'"
            )
        if peer_reviewed == "true" and source_type == "preprint":
            reporter.add(
                path,
                line,
                "peer_reviewed is true but source_type is 'preprint'. Cite the published "
                "version and move the preprint identifier to notes",
            )
        if peer_reviewed == "true" and grade == "C":
            reporter.add(
                path,
                line,
                "peer_reviewed is true but evidence_grade is C. A peer-reviewed result is "
                "not provider-reported; regrade or correct the flag",
            )

        url = row.get("url", "").strip()
        if url and not url.startswith(("http://", "https://")):
            reporter.add(path, line, f"url {url!r} is not an absolute http or https URL")

        doi = row.get("doi", "").strip()
        if doi and doi != "Not available" and not DOI_PATTERN.match(doi):
            reporter.add(
                path,
                line,
                f"doi {doi!r} is neither a bare DOI beginning '10.' nor the reserved string "
                f"'Not available'. Record the DOI itself, not a resolver URL",
            )

        year = row.get("year", "").strip()
        publication_date = row.get("publication_date", "").strip()
        if year and not year.isdigit():
            reporter.add(path, line, f"year {year!r} is not a four-digit integer")
        elif year and publication_date[:4].isdigit() and publication_date[:4] != year:
            reporter.add(
                path,
                line,
                f"year {year!r} disagrees with publication_date {publication_date!r}",
            )

    return register


def check_dates(reporter: Reporter) -> None:
    """Verify that every date field in every dataset is an absolute date.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-dates")
    date_fields = {
        "models": ("release_date", "source_date", "deprecation_date"),
        "benchmarks": ("evaluation_date", "publication_date"),
        "pricing": ("effective_date", "access_date"),
        "context-windows": ("source_date",),
        "energy-studies": ("publication_date",),
        "sources": ("publication_date", "access_date"),
    }
    exempt = {"Not publicly disclosed", "Not applicable", "unstated"}

    for dataset, fields in date_fields.items():
        path = DATASETS[dataset]
        _, rows = read_csv(path)
        for index, row in enumerate(rows):
            line = csv_line_number(index)
            for field in fields:
                value = row.get(field, "").strip()
                if value in exempt:
                    continue
                if not value:
                    reporter.add(path, line, f"{field} is empty; an absolute date is required")
                elif not DATE_PATTERN.match(value):
                    reporter.add(
                        path, line, f"{field} {value!r} is not in YYYY-MM-DD form"
                    )
                elif not is_date(value):
                    reporter.add(path, line, f"{field} {value!r} is not a real calendar date")


def check_references(reporter: Reporter, register: dict[str, dict[str, str]]) -> None:
    """Verify that every dataset source_id resolves to a register row.

    Args:
        reporter: Collector for violations.
        register: Mapping of ``source_id`` to register row.
    """
    reporter.note_check("--check-references")
    for dataset, path in DATASETS.items():
        if dataset == "sources":
            continue
        header, rows = read_csv(path)
        if "source_id" not in header:
            reporter.add(path, 1, "dataset has no source_id column; every row must cite a source")
            continue
        for index, row in enumerate(rows):
            source_id = row.get("source_id", "").strip()
            line = csv_line_number(index)
            if not source_id:
                reporter.add(path, line, "row has no source_id; every row must cite a source")
            elif source_id not in register:
                reporter.add(
                    path,
                    line,
                    f"source_id {source_id!r} does not resolve to a row in data/sources.csv",
                )


def check_duplicates(reporter: Reporter) -> None:
    """Detect duplicate model identifiers and duplicate benchmark results.

    A model may appear once in ``models.csv``. A benchmark result is unique on
    the triple of benchmark, model, and source: the same model may legitimately
    have several results for one benchmark when different parties evaluated it.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-duplicates")

    path = DATASETS["models"]
    _, rows = read_csv(path)
    seen_models = Counter(row.get("model_id", "").strip() for row in rows)
    for index, row in enumerate(rows):
        model_id = row.get("model_id", "").strip()
        if model_id and seen_models[model_id] > 1:
            reporter.add(
                path,
                csv_line_number(index),
                f"duplicate model_id {model_id!r} appears {seen_models[model_id]} times",
            )

    path = DATASETS["benchmarks"]
    _, rows = read_csv(path)
    keys = Counter(
        (
            row.get("benchmark_id", "").strip(),
            row.get("model_id", "").strip(),
            row.get("source_id", "").strip(),
            row.get("subset", "").strip(),
        )
        for row in rows
    )
    for index, row in enumerate(rows):
        key = (
            row.get("benchmark_id", "").strip(),
            row.get("model_id", "").strip(),
            row.get("source_id", "").strip(),
            row.get("subset", "").strip(),
        )
        if all(key) and keys[key] > 1:
            reporter.add(
                path,
                csv_line_number(index),
                f"duplicate result for benchmark {key[0]!r}, model {key[1]!r}, subset {key[3]!r} "
                f"from source {key[2]!r}. Two evaluations by the same party need distinct sources",
            )


def check_model_references(reporter: Reporter) -> None:
    """Verify that every model_id used in a dataset exists in models.csv.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-model-references")
    _, model_rows = read_csv(DATASETS["models"])
    known = {row.get("model_id", "").strip() for row in model_rows}
    for dataset in ("benchmarks", "pricing", "context-windows", "energy-studies"):
        path = DATASETS[dataset]
        _, rows = read_csv(path)
        for index, row in enumerate(rows):
            model_id = row.get("model_id", "").strip()
            if model_id and model_id not in known:
                reporter.add(
                    path,
                    csv_line_number(index),
                    f"model_id {model_id!r} does not resolve to a row in data/models.csv",
                )


def check_citations(reporter: Reporter, register: dict[str, dict[str, str]]) -> None:
    """Check bibliography consistency and footnote resolution across prose.

    Three conditions are enforced. A citation key in ``references.bib`` must be
    unique. A footnote referenced in a Markdown file must be defined in that
    file. A footnote definition whose key names a source must resolve to the
    register, so that a chapter cannot cite a source that has not been recorded
    and graded.

    Args:
        reporter: Collector for violations.
        register: Mapping of ``source_id`` to register row.
    """
    reporter.note_check("--check-citations")

    bib_path = REPO_ROOT / "references.bib"
    if not bib_path.is_file():
        reporter.add(bib_path, 0, "references.bib not found")
        bib_keys: set[str] = set()
    else:
        text = bib_path.read_text(encoding="utf-8")
        found = [match.group(1).strip() for match in BIB_KEY_PATTERN.finditer(text)]
        counts = Counter(found)
        for key, count in sorted(counts.items()):
            if count > 1:
                reporter.add(bib_path, 0, f"duplicate BibTeX citation key {key!r} ({count} times)")
            if not SOURCE_ID_PATTERN.match(key):
                reporter.add(
                    bib_path,
                    0,
                    f"citation key {key!r} does not match author-year-keyword form and so cannot "
                    f"equal a source_id",
                )
        bib_keys = set(found)

    for source_id in sorted(register):
        if source_id not in bib_keys:
            reporter.add(
                DATASETS["sources"],
                0,
                f"source_id {source_id!r} is in the register but has no entry in references.bib",
            )

    for path in markdown_files():
        lines = path.read_text(encoding="utf-8").splitlines()
        defined = {match.group(1) for match in FOOTNOTE_DEF_PATTERN.finditer("\n".join(lines))}
        state = {"inside": False}
        for number, line in enumerate(lines, start=1):
            if _in_code_block(line, state):
                continue
            if line.startswith("[^"):
                continue
            for match in FOOTNOTE_REF_PATTERN.finditer(line):
                key = match.group(1)
                if key not in defined:
                    reporter.add(path, number, f"footnote [^{key}] is referenced but not defined")
                elif register and key not in register and SOURCE_ID_PATTERN.match(key):
                    reporter.add(
                        path,
                        number,
                        f"footnote [^{key}] looks like a source_id but does not resolve to "
                        f"data/sources.csv",
                    )


def check_prose_claims(reporter: Reporter) -> None:
    """Flag numerical claims without a citation and relative time expressions.

    This check is heuristic by necessity and is scoped to ``docs/`` so that
    methodology and contribution documents, which discuss the rules using
    example numbers, do not generate noise.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-claims")
    for path in markdown_files(DOCS_DIR):
        state = {"inside": False}
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if _in_code_block(line, state):
                continue
            stripped = line.strip()
            if not stripped or stripped.startswith(SKIP_LINE_PREFIXES) or stripped.startswith("#"):
                continue
            if CLAIM_NUMBER_PATTERN.search(stripped) and not FOOTNOTE_REF_PATTERN.search(stripped):
                reporter.add(
                    path,
                    number,
                    "numerical claim without a footnote citation. Add [^source_id] or move the "
                    "value into a generated table",
                )
            match = RELATIVE_TIME_PATTERN.search(stripped)
            if match:
                reporter.add(
                    path,
                    number,
                    f"relative time expression {match.group(0)!r}. Use an absolute date, "
                    f"for example 'as of 2026-03-14'",
                )


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line parser.

    Returns:
        The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="validate_sources.py",
        description="Validate the source register and every reference to it.",
    )
    parser.add_argument("--check-register", action="store_true", help="validate data/sources.csv")
    parser.add_argument("--check-dates", action="store_true", help="require absolute dates")
    parser.add_argument(
        "--check-references", action="store_true", help="resolve every dataset source_id"
    )
    parser.add_argument(
        "--check-duplicates", action="store_true", help="detect duplicate models and results"
    )
    parser.add_argument(
        "--check-citations", action="store_true", help="check references.bib and footnotes"
    )
    parser.add_argument(
        "--check-claims",
        action="store_true",
        help="flag uncited numbers and relative time expressions in docs/",
    )
    return parser


def main() -> int:
    """Run the selected checks and return the process exit status.

    Returns:
        0 when no violations were found, 1 when violations were found.
    """
    args = build_parser().parse_args()
    selected = [
        args.check_register,
        args.check_dates,
        args.check_references,
        args.check_duplicates,
        args.check_citations,
        args.check_claims,
    ]
    run_all = not any(selected)
    reporter = Reporter("validate_sources.py")

    try:
        register = check_register(reporter) if (run_all or args.check_register) else _register()
        if run_all or args.check_dates:
            check_dates(reporter)
        if run_all or args.check_references:
            check_references(reporter, register)
            check_model_references(reporter)
        if run_all or args.check_duplicates:
            check_duplicates(reporter)
        if run_all or args.check_citations:
            check_citations(reporter, register)
        if run_all or args.check_claims:
            check_prose_claims(reporter)
    except DataError as exc:
        fail(str(exc))

    return reporter.finish()


def _register() -> dict[str, dict[str, str]]:
    """Load the register without validating it, for single-check invocations.

    Returns:
        Mapping of ``source_id`` to register row.
    """
    _, rows = read_csv(DATASETS["sources"])
    return {row.get("source_id", "").strip(): row for row in rows if row.get("source_id")}


if __name__ == "__main__":
    raise SystemExit(main())
