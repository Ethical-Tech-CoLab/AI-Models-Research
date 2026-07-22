#!/usr/bin/env python3
"""Generate model comparison tables from the data layer.

Markdown comparison tables in this repository are never written by hand. This
script reads ``data/models.csv``, ``data/pricing.csv``, and
``data/context-windows.csv`` and rewrites the delimited regions listed in
``TARGETS``. Everything outside a region is left untouched.

A generator run on an unchanged dataset produces no diff: rows are sorted by an
explicit key, and a region is rewritten only when its content actually changes.

Usage:
    python scripts/generate_model_tables.py
    python scripts/generate_model_tables.py --view compact
    python scripts/generate_model_tables.py --check

``--check`` writes nothing and exits 1 if any region is out of date, which is
how continuous integration detects a hand-edited table.

Exit status:
    0  every region is up to date, or was updated successfully
    1  --check found a region that is out of date
    2  a file could not be read, or a region delimiter is missing
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
from pathlib import Path

from _common import (
    DATASETS,
    DOCS_DIR,
    REPO_ROOT,
    DataError,
    fail,
    read_csv,
    relative,
    render_table,
    replace_generated_region,
)

EMPTY_NOTE = (
    "No rows. Populate the source dataset in data/ and rerun scripts/generate_model_tables.py"
)


def _by_provider_and_release(row: dict[str, str]) -> tuple[str, str, str]:
    """Sort key giving a stable ordering independent of CSV row order.

    Args:
        row: A model row.

    Returns:
        Provider, then release date, then model identifier.
    """
    return (
        row.get("provider", "").lower(),
        row.get("release_date", ""),
        row.get("model_id", ""),
    )


def _price_index(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    """Index pricing rows by model, keeping the most recent effective date.

    Args:
        rows: Rows of ``data/pricing.csv``.

    Returns:
        Mapping of ``model_id`` to the latest pricing row for that model.
    """
    latest: dict[str, dict[str, str]] = {}
    for row in rows:
        model_id = row.get("model_id", "").strip()
        if not model_id:
            continue
        current = latest.get(model_id)
        if current is None or row.get("effective_date", "") > current.get("effective_date", ""):
            latest[model_id] = row
    return latest


def build_compact() -> str:
    """Build the compact comparison table used in the README.

    Returns:
        The rendered Markdown table.
    """
    _, models = read_csv(DATASETS["models"])
    _, pricing = read_csv(DATASETS["pricing"])
    prices = _price_index(pricing)
    header = [
        "Provider",
        "Model",
        "Release date",
        "Open weights",
        "Context window",
        "Input USD / 1M",
        "Output USD / 1M",
        "Evidence grade",
        "Source date",
    ]
    rows = []
    for model in sorted(models, key=_by_provider_and_release):
        price = prices.get(model.get("model_id", ""), {})
        rows.append(
            [
                model.get("provider", ""),
                model.get("model_name", ""),
                model.get("release_date", ""),
                "yes" if model.get("open_weights", "") == "true" else "no",
                model.get("context_window_tokens", ""),
                price.get("input_price_per_1m", "Not publicly disclosed"),
                price.get("output_price_per_1m", "Not publicly disclosed"),
                model.get("evidence_grade", ""),
                model.get("source_date", ""),
            ]
        )
    return render_table(header, rows, EMPTY_NOTE)


def build_full(open_weights: bool | None = None) -> str:
    """Build the full model specification table, optionally filtered by weights.

    Args:
        open_weights: ``True`` for open-weight models only, ``False`` for
            closed-weight models only, ``None`` for all models.

    Returns:
        The rendered Markdown table.
    """
    _, models = read_csv(DATASETS["models"])
    header = [
        "Provider",
        "Model",
        "Release date",
        "Status",
        "Open weights",
        "Licence",
        "Architecture",
        "Total params (B)",
        "Active params (B)",
        "Modalities in",
        "Context window",
        "Max output",
        "Reasoning mode",
        "Tool use",
        "Deployment",
        "Evidence grade",
        "Source date",
    ]
    rows = []
    for model in sorted(models, key=_by_provider_and_release):
        is_open = model.get("open_weights", "") == "true"
        if open_weights is not None and is_open != open_weights:
            continue
        rows.append(
            [
                model.get("provider", ""),
                model.get("model_name", ""),
                model.get("release_date", ""),
                model.get("status", ""),
                "yes" if is_open else "no",
                model.get("license", ""),
                model.get("architecture", ""),
                model.get("parameters_total", ""),
                model.get("parameters_active", ""),
                model.get("modalities_input", ""),
                model.get("context_window_tokens", ""),
                model.get("max_output_tokens", ""),
                model.get("reasoning_mode", ""),
                model.get("tool_use", ""),
                model.get("deployment_options", ""),
                model.get("evidence_grade", ""),
                model.get("source_date", ""),
            ]
        )
    return render_table(header, rows, EMPTY_NOTE)


def build_pricing() -> str:
    """Build the pricing table.

    Returns:
        The rendered Markdown table.
    """
    _, rows_in = read_csv(DATASETS["pricing"])
    header = [
        "Model",
        "Provider",
        "Currency",
        "Input / 1M",
        "Cached input / 1M",
        "Output / 1M",
        "Reasoning tokens billed",
        "Batch discount %",
        "Effective date",
        "Region",
        "Evidence grade",
    ]
    rows = [
        [
            row.get("model_id", ""),
            row.get("provider", ""),
            row.get("currency", ""),
            row.get("input_price_per_1m", ""),
            row.get("cached_input_price_per_1m", ""),
            row.get("output_price_per_1m", ""),
            row.get("reasoning_token_billing", ""),
            row.get("batch_discount_percent", ""),
            row.get("effective_date", ""),
            row.get("region", ""),
            row.get("evidence_grade", ""),
        ]
        for row in sorted(
            rows_in,
            key=lambda r: (
                r.get("provider", ""),
                r.get("model_id", ""),
                r.get("effective_date", ""),
            ),
        )
    ]
    return render_table(header, rows, EMPTY_NOTE)


def build_context_windows() -> str:
    """Build the advertised versus measured context window table.

    Returns:
        The rendered Markdown table.
    """
    _, rows_in = read_csv(DATASETS["context-windows"])
    header = [
        "Model",
        "Advertised context",
        "Advertised max output",
        "Measured effective context",
        "Measurement benchmark",
        "Threshold",
        "Evidence grade",
        "Source date",
    ]
    rows = [
        [
            row.get("model_id", ""),
            row.get("advertised_context_tokens", ""),
            row.get("advertised_max_output_tokens", ""),
            row.get("measured_effective_context_tokens", ""),
            row.get("measurement_benchmark", ""),
            row.get("measurement_threshold", ""),
            row.get("evidence_grade", ""),
            row.get("source_date", ""),
        ]
        for row in sorted(rows_in, key=lambda r: r.get("model_id", ""))
    ]
    return render_table(header, rows, EMPTY_NOTE)


def build_selection_matrix() -> str:
    """Build the model selection matrix.

    Returns:
        The rendered Markdown table.
    """
    _, models = read_csv(DATASETS["models"])
    header = [
        "Model",
        "Provider",
        "Open weights",
        "Modalities in",
        "Context window",
        "Reasoning mode",
        "Tool use",
        "Agent capability",
        "Deployment",
        "Quantization",
        "Hardware requirement",
        "Evidence grade",
        "Source date",
    ]
    rows = [
        [
            model.get("model_name", ""),
            model.get("provider", ""),
            "yes" if model.get("open_weights", "") == "true" else "no",
            model.get("modalities_input", ""),
            model.get("context_window_tokens", ""),
            model.get("reasoning_mode", ""),
            model.get("tool_use", ""),
            model.get("agent_capability", ""),
            model.get("deployment_options", ""),
            model.get("quantization_support", ""),
            model.get("hardware_requirements", ""),
            model.get("evidence_grade", ""),
            model.get("source_date", ""),
        ]
        for model in sorted(models, key=_by_provider_and_release)
    ]
    return render_table(header, rows, EMPTY_NOTE)


#: Region name, target file, and the builder that produces its content.
TARGETS: dict[str, tuple[Path, Callable[[], str]]] = {
    "compact-comparison": (REPO_ROOT / "README.md", build_compact),
    "frontier-models": (DOCS_DIR / "comparisons" / "frontier-models.md", lambda: build_full(False)),
    "open-weight-models": (
        DOCS_DIR / "comparisons" / "open-weight-models.md",
        lambda: build_full(True),
    ),
    "model-selection-matrix": (
        DOCS_DIR / "comparisons" / "model-selection-matrix.md",
        build_selection_matrix,
    ),
    "pricing-table": (DOCS_DIR / "15-token-economics.md", build_pricing),
    "context-windows": (DOCS_DIR / "11-long-context.md", build_context_windows),
}


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line parser.

    Returns:
        The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="generate_model_tables.py",
        description="Generate model comparison tables from data/*.csv.",
    )
    parser.add_argument(
        "--view",
        choices=sorted(TARGETS),
        help="regenerate a single region instead of all of them",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="write nothing; exit 1 if any region is out of date",
    )
    return parser


def main() -> int:
    """Regenerate the configured regions and return the process exit status.

    Returns:
        0 on success, 1 when ``--check`` found an out-of-date region.
    """
    args = build_parser().parse_args()
    selected = {args.view: TARGETS[args.view]} if args.view else TARGETS
    stale: list[str] = []

    try:
        for name, (path, builder) in selected.items():
            content = builder()
            if args.check:
                current = path.read_text(encoding="utf-8")
                if content not in current:
                    stale.append(f"{relative(path)}: region {name!r} is out of date")
                continue
            changed = replace_generated_region(path, name, content)
            state = "updated" if changed else "unchanged"
            print(f"{relative(path)}: region {name!r} {state}")
    except DataError as exc:
        fail(str(exc))

    if stale:
        for message in stale:
            print(message)
        print(
            "\ngenerate_model_tables.py: FAIL. Run the generator and commit the result. "
            "Generated regions are never edited by hand."
        )
        return 1
    if args.check:
        print("generate_model_tables.py: PASS. All regions are up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
