#!/usr/bin/env python3
"""Validate dataset structure, table consistency, style, and profile templates.

This script enforces the rules that keep the Markdown layer honest about the
data layer beneath it.

Checks:

* ``--check-headers``      every CSV header matches the expected column set
* ``--check-schema``       every row validates against its JSON Schema, using
                           ``jsonschema`` when installed and a built-in
                           structural check otherwise
* ``--check-ranges``       benchmark scores lie inside the range their unit
                           permits
* ``--check-energy``       every energy row states all eleven required
                           conditions
* ``--check-comparability`` no ranked table mixes incompatible evaluation
                           settings without an adjacent warning
* ``--check-style``        no em dashes and no forbidden placeholder cells
* ``--check-profiles``     every model profile carries the full template in
                           order, with no empty section

Usage:
    python scripts/validate_tables.py
    python scripts/validate_tables.py --check-style --check-profiles

Exit status:
    0  no violations
    1  violations found, each printed as ``path:line: message``
    2  a file could not be read or parsed
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from _common import (
    DATASETS,
    DOCS_DIR,
    ENERGY_REQUIRED_CONDITIONS,
    EXPECTED_HEADERS,
    DataError,
    Reporter,
    csv_line_number,
    fail,
    is_missing,
    load_schema,
    markdown_files,
    read_csv,
)

PROFILE_DIR: Path = DOCS_DIR / "model-profiles"

#: The thirty-nine headings of the model profile template, in order.
#: Defined in CONTRIBUTING.md section 5.
PROFILE_HEADINGS: tuple[str, ...] = (
    "Overview",
    "Organization",
    "Current model lineup",
    "Architecture",
    "Total parameters",
    "Active parameters",
    "Dense or mixture-of-experts",
    "Training and post-training",
    "Modalities",
    "Context window",
    "Maximum output",
    "Tokenizer",
    "Reasoning modes",
    "Tool use",
    "Agent capabilities",
    "Coding performance",
    "Scientific reasoning",
    "Long-context performance",
    "Multimodal performance",
    "Factuality and hallucination",
    "Latency",
    "Throughput",
    "Token pricing",
    "Caching",
    "Batch pricing",
    "Hardware requirements",
    "Quantization",
    "Memory footprint",
    "Energy evidence",
    "Privacy and data retention",
    "Licensing",
    "Strengths",
    "Limitations",
    "Best use cases",
    "Inappropriate use cases",
    "Independent evidence",
    "Provider-reported evidence",
    "Open research questions",
    "Sources",
)

EM_DASH = "—"
CUTOFF_PATTERN: re.Pattern[str] = re.compile(r"Research cut-?off(?: date)?:\s*\d{4}-\d{2}-\d{2}")
TABLE_ROW_PATTERN: re.Pattern[str] = re.compile(r"^\s*\|.*\|\s*$")

#: Columns whose presence marks a table as a ranked benchmark comparison, and
#: which therefore trigger the comparability check.
SCORE_COLUMN_HINTS: frozenset[str] = frozenset(
    {"score", "accuracy", "pass@1", "resolved", "elo", "benchmark"}
)
CONDITION_COLUMN_HINTS: frozenset[str] = frozenset(
    {"sampling", "tool", "harness", "conditions", "evidence grade"}
)
WARNING_MARKERS: tuple[str, ...] = (
    "!!! warning",
    "!!! caution",
    "**warning",
    "incomparable",
    "not comparable",
    "conditions differ",
)


def check_headers(reporter: Reporter) -> None:
    """Verify that every dataset has exactly its expected columns, in order.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-headers")
    for dataset, expected in EXPECTED_HEADERS.items():
        path = DATASETS[dataset]
        header, _ = read_csv(path)
        if tuple(header) == expected:
            continue
        missing = [column for column in expected if column not in header]
        unexpected = [column for column in header if column not in expected]
        if missing:
            reporter.add(path, 1, f"missing column(s): {', '.join(missing)}")
        if unexpected:
            reporter.add(path, 1, f"unexpected column(s): {', '.join(unexpected)}")
        if not missing and not unexpected:
            reporter.add(
                path,
                1,
                "columns are correct but out of order; the generators depend on column order",
            )


def _declared_types(schema: dict[str, Any], field: str) -> set[str]:
    """Collect every JSON type a field may take under its schema.

    A field defined through ``anyOf`` accepts several types, and one of them is
    frequently a reserved string such as ``Not publicly disclosed``. The set is
    therefore a union rather than a single type.

    Args:
        schema: The full schema document.
        field: Property name.

    Returns:
        The declared type names, empty when the field constrains no type.
    """
    spec = schema.get("properties", {}).get(field)
    if not isinstance(spec, dict):
        return set()
    found: set[str] = set()

    def walk(node: Any) -> None:
        if not isinstance(node, dict):
            return
        declared = node.get("type")
        if isinstance(declared, str):
            found.add(declared)
        elif isinstance(declared, list):
            found.update(declared)
        if "const" in node or "enum" in node:
            found.add("string")
        for branch in node.get("anyOf", []):
            walk(branch)

    walk(spec)
    return found


def _coerce(value: str, types: set[str]) -> Any:
    """Convert a CSV cell to the JSON type its schema expects.

    CSV has no types, so a schema check needs the string interpreted first. The
    conversion is driven by the schema rather than by the shape of the text: a
    benchmark version of ``2.1`` is a string, and reading it as a number would
    reject valid data. A field that accepts a string is therefore left alone
    unless it also accepts a number.

    Args:
        value: Raw cell value.
        types: JSON types the field may take, from ``_declared_types``.

    Returns:
        A bool, int, float, or the original string.
    """
    text = value.strip()
    if "boolean" in types and text in {"true", "false"}:
        return text == "true"
    if "integer" in types or "number" in types:
        try:
            return int(text)
        except ValueError:
            pass
        try:
            return float(text)
        except ValueError:
            return text
    return text


def check_schema(reporter: Reporter) -> None:
    """Validate rows against the JSON Schemas in ``data/schema``.

    Uses ``jsonschema`` when it is importable. When it is not, a reduced check
    runs that verifies required fields are present and non-empty, so that a
    clean checkout can be validated before dependencies are installed. The
    reduced mode is announced rather than applied silently.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-schema")
    jsonschema: Any | None
    try:
        import jsonschema as jsonschema_module
    except ImportError:
        jsonschema = None
        print(
            "validate_tables.py: jsonschema is not installed; running reduced structural "
            "checks only. Install it with: pip install -r requirements.txt"
        )
    else:
        jsonschema = jsonschema_module

    for dataset in ("models", "benchmarks", "sources"):
        path = DATASETS[dataset]
        schema = load_schema(dataset)
        required: list[str] = list(schema.get("required", []))
        _, rows = read_csv(path)
        for index, row in enumerate(rows):
            line = csv_line_number(index)
            for field in required:
                if field not in row or is_missing(row.get(field, "")):
                    reporter.add(path, line, f"required field {field!r} is empty or missing")
            if jsonschema is None:
                continue
            document = {
                key: _coerce(value, _declared_types(schema, key))
                for key, value in row.items()
                if value is not None
            }
            validator = jsonschema.Draft202012Validator(schema)
            for error in sorted(validator.iter_errors(document), key=lambda e: list(e.path)):
                field = ".".join(str(part) for part in error.path) or "row"
                reporter.add(path, line, f"{field}: {error.message}")


def check_ranges(reporter: Reporter) -> None:
    """Verify that benchmark scores lie inside the range their unit permits.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-ranges")
    path = DATASETS["benchmarks"]
    _, rows = read_csv(path)
    bounds: dict[str, tuple[float, float]] = {
        "percent": (0.0, 100.0),
        "fraction": (0.0, 1.0),
        "elo": (0.0, 4000.0),
    }
    for index, row in enumerate(rows):
        line = csv_line_number(index)
        raw = row.get("score", "").strip()
        unit = row.get("unit", "").strip()
        try:
            score = float(raw)
        except ValueError:
            reporter.add(path, line, f"score {raw!r} is not a number")
            continue
        if unit in bounds:
            low, high = bounds[unit]
            if not low <= score <= high:
                reporter.add(
                    path,
                    line,
                    f"score {score} is outside the valid range [{low}, {high}] for unit {unit!r}",
                )
        if unit == "fraction" and score > 1.0:
            reporter.add(
                path, line, "unit is 'fraction' but the score exceeds 1.0; did you mean 'percent'?"
            )
        if unit == "percent" and 0.0 < score <= 1.0:
            reporter.add(
                path,
                line,
                f"unit is 'percent' but the score is {score}. Confirm this is not a fraction "
                f"recorded with the wrong unit",
            )


def check_energy(reporter: Reporter) -> None:
    """Verify that every energy row states all eleven required conditions.

    An energy figure without its conditions is not a measurement of anything.
    See research-methodology.md section 6.4.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-energy")
    path = DATASETS["energy-studies"]
    header, rows = read_csv(path)
    for condition in ENERGY_REQUIRED_CONDITIONS:
        if condition not in header:
            reporter.add(
                path,
                1,
                f"required energy condition column {condition!r} is missing; all eleven "
                f"conditions are mandatory",
            )
    for index, row in enumerate(rows):
        line = csv_line_number(index)
        for condition in ENERGY_REQUIRED_CONDITIONS:
            value = row.get(condition, "")
            if is_missing(value):
                reporter.add(
                    path,
                    line,
                    f"energy condition {condition!r} is empty. Publish no energy figure without "
                    f"all eleven conditions",
                )
            if value.strip() == "unstated":
                reporter.add(
                    path,
                    line,
                    f"energy condition {condition!r} is 'unstated'. A figure whose conditions "
                    f"are unknown cannot be published; record it as Insufficient independent "
                    f"evidence instead",
                )


#: A cell that is nothing but a measurement: an optional currency symbol, a
#: number, and an optional unit suffix. A benchmark *name* containing a digit,
#: such as "ARC-AGI-2" or "Terminal-Bench 2.0", does not match, which is the
#: whole point: a name is not a result.
NUMERIC_CELL_PATTERN: re.Pattern[str] = re.compile(
    r"^[*_`\s]*[$€£]?\s*\d[\d,]*(?:\.\d+)?\s*(?:%|pts?|points?|x|×)?[*_`\s]*$",
    re.IGNORECASE,
)


def _table_has_numeric_body(lines: list[str], header_line: int) -> bool:
    """Report whether the rows under a table header report any measurement.

    Args:
        lines: All lines of the file.
        header_line: One-indexed line number of the header row.

    Returns:
        True when at least one body cell is a bare number. A table of
        definitions has none, and is therefore not a ranked comparison even
        when its entries carry digits in their names.
    """
    for candidate in lines[header_line + 1 :]:
        if not TABLE_ROW_PATTERN.match(candidate):
            break
        cells = candidate.strip().strip("|").split("|")
        if any(NUMERIC_CELL_PATTERN.match(cell) for cell in cells):
            return True
    return False


def check_comparability(reporter: Reporter) -> None:
    """Flag ranked benchmark tables that omit evaluation conditions.

    A table that reports scores for several models without stating sampling
    policy, tool permissions, or evidence grade invites a comparison the data
    does not support. The check is conservative: it fires only when a table
    header contains a score-like column and no condition column, and when no
    warning marker appears in the preceding lines.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-comparability")
    for path in markdown_files(DOCS_DIR):
        lines = path.read_text(encoding="utf-8").splitlines()
        for number, line in enumerate(lines, start=1):
            if not TABLE_ROW_PATTERN.match(line):
                continue
            if number >= len(lines):
                continue
            separator = lines[number].strip()
            # A header row is followed by an alignment row: pipes, hyphens, and
            # optional colons. A blank line is not an alignment row, so the
            # emptiness test must be explicit.
            if not separator or "-" not in separator or set(separator) - set("|-: "):
                continue
            columns = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
            joined = " ".join(columns)
            has_score = any(hint in joined for hint in SCORE_COLUMN_HINTS)
            has_conditions = any(hint in joined for hint in CONDITION_COLUMN_HINTS)
            if not has_score or has_conditions:
                continue
            # A definitional table can carry a score-like word in a heading
            # ("Benchmark", "What it tests") while reporting no results at all.
            # A ranked comparison necessarily contains numbers, so require at
            # least one numeric cell in the body before flagging the table.
            if not _table_has_numeric_body(lines, number):
                continue
            context = "\n".join(lines[max(0, number - 6) : number]).lower()
            if any(marker in context for marker in WARNING_MARKERS):
                continue
            reporter.add(
                path,
                number,
                "benchmark table has no evidence grade, sampling policy, or tool permission "
                "column, and no adjacent warning. Add the conditions or state that the results "
                "are not comparable",
            )


def check_style(reporter: Reporter) -> None:
    """Enforce the prose style rules that can be checked mechanically.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-style")
    for path in markdown_files():
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if EM_DASH in line:
                reporter.add(
                    path,
                    number,
                    "em dash found. Use a comma, semicolon, colon, or parentheses "
                    "(CONTRIBUTING.md section 4)",
                )

    for dataset, path in DATASETS.items():
        header, rows = read_csv(path)
        for index, row in enumerate(rows):
            line_number = csv_line_number(index)
            for field in header:
                value = row.get(field) or ""
                if EM_DASH in value:
                    reporter.add(path, line_number, f"em dash in field {field!r}")
                if is_missing(value):
                    reporter.add(
                        path,
                        line_number,
                        f"field {field!r} in {dataset} is empty or uses a rejected placeholder. "
                        f"Use a reserved string from data-sources.md section 1.2",
                    )


def check_profiles(reporter: Reporter) -> None:
    """Verify the model profile template in every file under model-profiles.

    Args:
        reporter: Collector for violations.
    """
    reporter.note_check("--check-profiles")
    if not PROFILE_DIR.is_dir():
        reporter.add(PROFILE_DIR, 0, "docs/model-profiles/ directory not found")
        return

    for path in sorted(PROFILE_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        if not CUTOFF_PATTERN.search(text):
            reporter.add(
                path,
                0,
                "no research cut-off line. Add '> Research cut-off: YYYY-MM-DD' below the title",
            )

        found: list[tuple[int, str]] = [
            (number, line[3:].strip())
            for number, line in enumerate(lines, start=1)
            if line.startswith("## ")
        ]
        found_titles = [title for _, title in found]

        for heading in PROFILE_HEADINGS:
            if heading not in found_titles:
                reporter.add(path, 0, f"missing required section '## {heading}'")

        present = [title for title in found_titles if title in PROFILE_HEADINGS]
        expected_order = [title for title in PROFILE_HEADINGS if title in present]
        if present != expected_order:
            reporter.add(
                path,
                0,
                "template sections are out of order. The thirty-nine headings must appear in "
                "the order given in CONTRIBUTING.md section 5",
            )

        for position, (number, title) in enumerate(found):
            if title not in PROFILE_HEADINGS:
                reporter.add(
                    path, number, f"section '## {title}' is not part of the profile template"
                )
                continue
            end = found[position + 1][0] - 1 if position + 1 < len(found) else len(lines)
            body = "\n".join(lines[number:end]).strip()
            if not body:
                reporter.add(
                    path,
                    number,
                    f"section '## {title}' is empty. Write the content, or 'Not publicly "
                    f"disclosed', or 'Insufficient independent evidence'",
                )


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line parser.

    Returns:
        The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="validate_tables.py",
        description="Validate dataset structure, table consistency, style, and profiles.",
    )
    for flag, help_text in (
        ("--check-headers", "verify CSV column sets and order"),
        ("--check-schema", "validate rows against data/schema/*.schema.json"),
        ("--check-ranges", "verify benchmark scores lie in a valid range"),
        ("--check-energy", "verify all eleven energy conditions are present"),
        ("--check-comparability", "flag ranked tables missing evaluation conditions"),
        ("--check-style", "reject em dashes and placeholder cells"),
        ("--check-profiles", "verify the model profile template"),
    ):
        parser.add_argument(flag, action="store_true", help=help_text)
    return parser


def main() -> int:
    """Run the selected checks and return the process exit status.

    Returns:
        0 when no violations were found, 1 when violations were found.
    """
    args = build_parser().parse_args()
    checks = {
        "headers": (args.check_headers, check_headers),
        "schema": (args.check_schema, check_schema),
        "ranges": (args.check_ranges, check_ranges),
        "energy": (args.check_energy, check_energy),
        "comparability": (args.check_comparability, check_comparability),
        "style": (args.check_style, check_style),
        "profiles": (args.check_profiles, check_profiles),
    }
    run_all = not any(selected for selected, _ in checks.values())
    reporter = Reporter("validate_tables.py")
    try:
        for selected, function in checks.values():
            if run_all or selected:
                function(reporter)
    except DataError as exc:
        fail(str(exc))
    return reporter.finish()


if __name__ == "__main__":
    raise SystemExit(main())
