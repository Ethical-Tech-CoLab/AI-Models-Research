#!/usr/bin/env python3
"""Build the model release timeline from the model dataset.

Writes two generated regions into ``docs/appendices/model-release-timeline.md``:
a Mermaid timeline grouped by year and quarter, and a table of every model with
its release date, status, and the source that establishes the date.

The timeline is analytical rather than decorative: release dates bound the
training cut-off, they determine which benchmarks could have existed at
training time, and they are the axis along which a benchmark contamination
argument is made.

Models whose release date is not publicly disclosed are excluded from the
Mermaid diagram, which cannot express an unknown position, and are listed in
the table with the reason. They are counted in the output so that the exclusion
is visible rather than silent.

Usage:
    python scripts/build_release_timeline.py
    python scripts/build_release_timeline.py --check

Exit status:
    0  regions are up to date, or were updated successfully
    1  --check found an out-of-date region
    2  a file could not be read, or a region delimiter is missing
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

from _common import (
    DATASETS,
    DOCS_DIR,
    DataError,
    fail,
    is_date,
    read_csv,
    relative,
    render_table,
    replace_generated_region,
)

TARGET: Path = DOCS_DIR / "appendices" / "model-release-timeline.md"
DIAGRAM_REGION = "release-timeline-diagram"
TABLE_REGION = "release-timeline-table"


def quarter_of(date: str) -> str:
    """Return the calendar quarter label for an ISO date.

    Args:
        date: Date in ``YYYY-MM-DD`` form.

    Returns:
        A label such as ``2025 Q3``.

    Raises:
        ValueError: If the date is not an absolute ISO date.
    """
    if not is_date(date):
        raise ValueError(f"{date!r} is not an absolute YYYY-MM-DD date")
    year, month, _ = date.split("-")
    return f"{year} Q{(int(month) - 1) // 3 + 1}"


def build_diagram(rows: list[dict[str, str]]) -> str:
    """Build the Mermaid timeline.

    Args:
        rows: Model rows with a valid release date.

    Returns:
        A fenced Mermaid block, or a stated absence when there are no dated
        models.
    """
    if not rows:
        return (
            "_No dated model releases. Populate data/models.csv with release dates and rerun "
            "scripts/build_release_timeline.py._"
        )
    grouped: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        grouped[quarter_of(row["release_date"])].append(
            f"{row.get('provider', '')} {row.get('model_name', '')}".strip()
        )
    lines = ["```mermaid", "timeline", "    title Model releases by quarter"]
    for period in sorted(grouped):
        entries = " : ".join(sorted(grouped[period]))
        lines.append(f"    {period} : {entries}")
    lines.append("```")
    return "\n".join(lines)


def build_table(rows: list[dict[str, str]], undated: list[dict[str, str]]) -> str:
    """Build the release table, including models with no disclosed date.

    Args:
        rows: Model rows with a valid release date.
        undated: Model rows without one.

    Returns:
        The rendered Markdown table.
    """
    header = [
        "Release date", "Quarter", "Provider", "Model", "Status", "Open weights",
        "Evidence grade", "Source", "Source date",
    ]
    body = [
        [
            row.get("release_date", ""),
            quarter_of(row["release_date"]),
            row.get("provider", ""),
            row.get("model_name", ""),
            row.get("status", ""),
            "yes" if row.get("open_weights", "") == "true" else "no",
            row.get("evidence_grade", ""),
            row.get("source_id", ""),
            row.get("source_date", ""),
        ]
        for row in sorted(rows, key=lambda r: (r.get("release_date", ""), r.get("model_id", "")))
    ]
    body += [
        [
            row.get("release_date", "Not publicly disclosed"),
            "Not applicable",
            row.get("provider", ""),
            row.get("model_name", ""),
            row.get("status", ""),
            "yes" if row.get("open_weights", "") == "true" else "no",
            row.get("evidence_grade", ""),
            row.get("source_id", ""),
            row.get("source_date", ""),
        ]
        for row in sorted(undated, key=lambda r: (r.get("provider", ""), r.get("model_id", "")))
    ]
    return render_table(
        header,
        body,
        "No models recorded. Populate data/models.csv and rerun "
        "scripts/build_release_timeline.py",
    )


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line parser.

    Returns:
        The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="build_release_timeline.py",
        description="Build the model release timeline from data/models.csv.",
    )
    parser.add_argument(
        "--check", action="store_true", help="write nothing; exit 1 if a region is out of date"
    )
    return parser


def main() -> int:
    """Regenerate the timeline regions and return the process exit status.

    Returns:
        0 on success, 1 when ``--check`` found an out-of-date region.
    """
    args = build_parser().parse_args()
    try:
        _, models = read_csv(DATASETS["models"])
        dated = [row for row in models if is_date(row.get("release_date", "").strip())]
        undated = [row for row in models if not is_date(row.get("release_date", "").strip())]

        diagram = build_diagram(dated)
        table = build_table(dated, undated)

        if args.check:
            current = TARGET.read_text(encoding="utf-8")
            stale = [
                name
                for name, content in ((DIAGRAM_REGION, diagram), (TABLE_REGION, table))
                if content not in current
            ]
            if stale:
                for name in stale:
                    print(f"{relative(TARGET)}: region {name!r} is out of date")
                print("\nbuild_release_timeline.py: FAIL. Run the generator and commit the result.")
                return 1
            print("build_release_timeline.py: PASS. All regions are up to date.")
            return 0

        for name, content in ((DIAGRAM_REGION, diagram), (TABLE_REGION, table)):
            changed = replace_generated_region(TARGET, name, content)
            print(f"{relative(TARGET)}: region {name!r} {'updated' if changed else 'unchanged'}")
    except (DataError, ValueError) as exc:
        fail(str(exc))

    print(
        f"build_release_timeline.py: {len(dated)} dated model(s) in the diagram; "
        f"{len(undated)} model(s) without a disclosed release date are listed in the table only."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
