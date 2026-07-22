"""Shared helpers for the validation and generation scripts.

This module exists so that the eight command-line scripts in this directory
agree on repository layout, on the reserved strings that stand in for missing
values, on how a violation is reported, and on how a generated region of a
Markdown file is rewritten.

Design constraints that apply to every script in this directory:

* No dependency on a paid API, on network access at validation time, or on
  credentials of any kind.
* No silent failure. Every rejected input produces a ``Finding`` naming the
  file, the line where it can be seen, and what is wrong with it.
* Deterministic output. Rows are sorted by an explicit key before rendering,
  so that regenerating a table on an unchanged dataset produces no diff.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT: Path = Path(__file__).resolve().parent.parent
DATA_DIR: Path = REPO_ROOT / "data"
SCHEMA_DIR: Path = DATA_DIR / "schema"
DOCS_DIR: Path = REPO_ROOT / "docs"

#: Strings that stand in for an absent value. An empty cell is always an error;
#: one of these strings must be used instead so that the reason for the absence
#: is recorded. See data-sources.md section 1.2.
NOT_DISCLOSED = "Not publicly disclosed"
NO_INDEPENDENT_EVIDENCE = "Insufficient independent evidence"
UNSTATED = "unstated"
NOT_AVAILABLE = "Not available"
NOT_APPLICABLE = "Not applicable"
NONE_NOTE = "None"

RESERVED_VALUES: frozenset[str] = frozenset(
    {
        NOT_DISCLOSED,
        NO_INDEPENDENT_EVIDENCE,
        UNSTATED,
        NOT_AVAILABLE,
        NOT_APPLICABLE,
        NONE_NOTE,
    }
)

#: Near misses that contributors reach for instead of the reserved strings.
#: Rejected explicitly so that an absent value is never ambiguous.
FORBIDDEN_PLACEHOLDERS: frozenset[str] = frozenset(
    {"", "-", "--", "n/a", "N/A", "na", "NA", "none", "null", "NULL", "TBD", "tbd", "?", "unknown"}
)

DATE_PATTERN: re.Pattern[str] = re.compile(r"^\d{4}-\d{2}-\d{2}$")
EVIDENCE_GRADES: frozenset[str] = frozenset({"A", "B", "C"})

GENERATED_BEGIN = "<!-- BEGIN GENERATED: {name} -->"
GENERATED_END = "<!-- END GENERATED: {name} -->"

#: Datasets and the file each one lives in.
DATASETS: dict[str, Path] = {
    "models": DATA_DIR / "models.csv",
    "benchmarks": DATA_DIR / "benchmarks.csv",
    "pricing": DATA_DIR / "pricing.csv",
    "context-windows": DATA_DIR / "context-windows.csv",
    "energy-studies": DATA_DIR / "energy-studies.csv",
    "sources": DATA_DIR / "sources.csv",
}

# fmt: off
#: Expected header for each dataset. Held here rather than derived from the
#: JSON Schemas because three of the six datasets have no schema file, and a
#: header check must work for all six.
EXPECTED_HEADERS: dict[str, tuple[str, ...]] = {
    "models": (
        "model_id", "provider", "model_name", "release_date", "status",
        "deprecation_date", "open_weights", "license", "license_url",
        "architecture", "parameters_total", "parameters_active", "expert_count",
        "modalities_input", "modalities_output", "context_window_tokens",
        "max_output_tokens", "tokenizer", "reasoning_mode", "tool_use",
        "agent_capability", "quantization_support", "deployment_options",
        "hardware_requirements", "evidence_grade", "source_id", "source_date",
        "notes",
    ),
    "benchmarks": (
        "benchmark_id", "benchmark_name", "benchmark_version", "model_id",
        "score", "metric", "unit", "harness", "harness_version",
        "sampling_policy", "samples_n", "tool_permissions", "subset",
        "reported_by", "evaluation_date", "publication_date", "evidence_grade",
        "source_id", "notes",
    ),
    "pricing": (
        "model_id", "provider", "currency", "input_price_per_1m",
        "cached_input_price_per_1m", "output_price_per_1m",
        "reasoning_token_billing", "batch_discount_percent", "effective_date",
        "region", "evidence_grade", "source_id", "access_date", "notes",
    ),
    "context-windows": (
        "model_id", "advertised_context_tokens", "advertised_max_output_tokens",
        "measured_effective_context_tokens", "measurement_benchmark",
        "measurement_threshold", "evidence_grade", "source_id", "source_date",
        "notes",
    ),
    "energy-studies": (
        "study_id", "model_id", "hardware", "model_version", "precision",
        "prompt_tokens", "output_tokens", "batch_size", "utilization_percent",
        "serving_framework", "pue", "measurement_method", "energy_per_token_j",
        "energy_per_query_wh", "uncertainty", "grid_region",
        "carbon_intensity_gco2e_per_kwh", "evidence_grade", "source_id",
        "publication_date", "notes",
    ),
    "sources": (
        "source_id", "title", "authors", "organization", "publication", "year",
        "publication_date", "source_type", "peer_reviewed", "evidence_grade",
        "url", "doi", "access_date", "notes",
    ),
}

# fmt: on

#: The eleven conditions that must accompany any published energy figure.
#: See research-methodology.md section 6.4.
# fmt: off
ENERGY_REQUIRED_CONDITIONS: tuple[str, ...] = (
    "hardware", "model_version", "precision", "prompt_tokens", "output_tokens",
    "batch_size", "utilization_percent", "serving_framework", "pue",
    "measurement_method", "uncertainty",
)
# fmt: on


@dataclass(frozen=True, order=True)
class Finding:
    """A single validation violation.

    Attributes:
        path: Path to the offending file, relative to the repository root.
        line: One-indexed line number. Use 0 where the finding applies to the
            file as a whole rather than to a specific line.
        message: What is wrong, stated so that it can be acted on without
            opening the validator source.
    """

    path: str
    line: int
    message: str

    def render(self) -> str:
        """Return the finding in ``path:line: message`` form."""
        return f"{self.path}:{self.line}: {self.message}"


class Reporter:
    """Collects findings and turns them into a process exit status.

    A validator never raises on bad data: it records every violation so that a
    contributor sees the whole list in one run, then exits non-zero.
    """

    def __init__(self, tool: str) -> None:
        """Initialise the reporter.

        Args:
            tool: Name of the calling script, used in the summary line.
        """
        self.tool = tool
        self.findings: list[Finding] = []
        self.checks_run: list[str] = []

    def add(self, path: Path | str, line: int, message: str) -> None:
        """Record a violation.

        Args:
            path: Offending file, absolute or repository-relative.
            line: One-indexed line number, or 0 for a whole-file finding.
            message: Description of the violation.
        """
        self.findings.append(Finding(relative(path), line, message))

    def note_check(self, name: str) -> None:
        """Record that a named check ran, so that the summary is honest.

        Args:
            name: Identifier of the check, for example ``--check-dates``.
        """
        self.checks_run.append(name)

    def finish(self) -> int:
        """Print all findings and return the process exit status.

        Returns:
            0 when no findings were recorded, 1 otherwise.
        """
        for finding in sorted(set(self.findings)):
            print(finding.render())
        checks = ", ".join(self.checks_run) if self.checks_run else "none"
        count = len(set(self.findings))
        if count:
            print(f"\n{self.tool}: FAIL. {count} violation(s). Checks run: {checks}.")
            return 1
        print(f"{self.tool}: PASS. Checks run: {checks}.")
        return 0


class DataError(Exception):
    """Raised when a file cannot be read or parsed at all.

    Distinct from a ``Finding``: a ``Finding`` is bad data inside a readable
    file, whereas this is a file that cannot be processed.
    """


def relative(path: Path | str) -> str:
    """Return a path relative to the repository root where possible.

    Args:
        path: Absolute or relative path.

    Returns:
        The repository-relative path as a string, or the input unchanged when
        it lies outside the repository.
    """
    candidate = Path(path)
    try:
        return str(candidate.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(candidate)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    """Read a CSV file into its header and its rows.

    Args:
        path: Path to the CSV file.

    Returns:
        A pair of the header field names and the list of rows as dictionaries.

    Raises:
        DataError: If the file is missing, is empty, or has no header row.
    """
    if not path.is_file():
        raise DataError(f"{relative(path)}: file not found")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise DataError(f"{relative(path)}: file is empty, expected a header row")
        header = list(reader.fieldnames)
        rows = [dict(row) for row in reader]
    return header, rows


def csv_line_number(index: int) -> int:
    """Convert a zero-indexed data row position to a file line number.

    Args:
        index: Zero-indexed position of the row within the data rows.

    Returns:
        The one-indexed line number in the file, accounting for the header.
    """
    return index + 2


def load_schema(name: str) -> dict[str, Any]:
    """Load a JSON Schema from ``data/schema``.

    Args:
        name: Schema base name, for example ``models``.

    Returns:
        The parsed schema document.

    Raises:
        DataError: If the schema file is missing or is not valid JSON.
    """
    path = SCHEMA_DIR / f"{name}.schema.json"
    if not path.is_file():
        raise DataError(f"{relative(path)}: schema not found")
    try:
        with path.open(encoding="utf-8") as handle:
            document: dict[str, Any] = json.load(handle)
    except json.JSONDecodeError as exc:
        raise DataError(f"{relative(path)}: invalid JSON: {exc}") from exc
    return document


def markdown_files(root: Path | None = None) -> Iterator[Path]:
    """Yield every Markdown file in the repository, in sorted order.

    Files under ``.venv``, ``site``, and version-control directories are
    skipped so that build output is never validated.

    Args:
        root: Directory to walk. Defaults to the repository root.

    Yields:
        Paths to Markdown files, sorted for deterministic reporting.
    """
    base = root if root is not None else REPO_ROOT
    skip = {".git", ".venv", "venv", "site", "node_modules", "__pycache__", ".ruff_cache"}
    for path in sorted(base.rglob("*.md")):
        if any(part in skip for part in path.parts):
            continue
        yield path


def is_missing(value: str) -> bool:
    """Report whether a cell uses a forbidden placeholder instead of a reserved value.

    Args:
        value: Raw cell value.

    Returns:
        True when the value is empty or is a rejected near miss such as
        ``N/A``. Reserved strings return False because they are valid.
    """
    return value.strip() in FORBIDDEN_PLACEHOLDERS


def is_date(value: str) -> bool:
    """Report whether a value is an absolute ``YYYY-MM-DD`` date.

    Args:
        value: Raw cell value.

    Returns:
        True when the value matches the date pattern and names a real calendar
        date.
    """
    if not DATE_PATTERN.match(value.strip()):
        return False
    year, month, day = (int(part) for part in value.strip().split("-"))
    if not 1 <= month <= 12:
        return False
    days_in_month = [31, 29 if _is_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 1 <= day <= days_in_month[month - 1]


def _is_leap(year: int) -> bool:
    """Report whether a year is a leap year in the proleptic Gregorian calendar.

    Args:
        year: Four-digit year.

    Returns:
        True for a leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def render_table(header: Sequence[str], rows: Sequence[Sequence[str]], empty_note: str) -> str:
    """Render a Markdown table, or a single explanatory row when there is no data.

    An empty dataset renders as a stated absence rather than as an empty table,
    because a table with no rows reads as an assertion that nothing exists.

    Args:
        header: Column headings.
        rows: Row values, already stringified and ordered.
        empty_note: Sentence to show when ``rows`` is empty.

    Returns:
        The rendered Markdown table as a string without a trailing newline.
    """
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    if not rows:
        lines.append("| _" + empty_note + "_ |" + " |" * (len(header) - 1))
        return "\n".join(lines)
    for row in rows:
        cells = [str(cell).replace("|", "\\|") for cell in row]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def replace_generated_region(path: Path, name: str, content: str) -> bool:
    """Replace a delimited generated region in a Markdown file.

    Args:
        path: Markdown file to rewrite.
        name: Region name used in the delimiter comments.
        content: Replacement content, without the delimiters.

    Returns:
        True when the file changed on disk, False when the content was already
        identical. A False return on a generator run means the table is in
        sync with its dataset.

    Raises:
        DataError: If the file is missing, if either delimiter is absent, or if
            the delimiters appear in the wrong order.
    """
    if not path.is_file():
        raise DataError(f"{relative(path)}: file not found")
    begin = GENERATED_BEGIN.format(name=name)
    end = GENERATED_END.format(name=name)
    original = path.read_text(encoding="utf-8")
    start_at = original.find(begin)
    end_at = original.find(end)
    if start_at == -1:
        raise DataError(f"{relative(path)}: missing region delimiter {begin!r}")
    if end_at == -1:
        raise DataError(f"{relative(path)}: missing region delimiter {end!r}")
    if end_at < start_at:
        raise DataError(f"{relative(path)}: region {name!r} delimiters are in the wrong order")
    updated = original[: start_at + len(begin)] + "\n" + content + "\n" + original[end_at:]
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def fail(message: str) -> None:
    """Print a fatal error to standard error and exit with status 2.

    Status 2 distinguishes a tool or input failure from status 1, which means
    the tool ran correctly and found violations.

    Args:
        message: Description of the failure.
    """
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(2)
