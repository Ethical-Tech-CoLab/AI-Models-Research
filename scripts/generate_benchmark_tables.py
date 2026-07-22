#!/usr/bin/env python3
"""Generate benchmark comparison tables from the data layer.

Each generated table carries the evaluation conditions alongside the score:
harness, sampling policy, tool permissions, reporting party, evidence grade,
and date. The conditions are not optional columns that a contributor may drop
to make a table narrower. A score without them cannot be compared, and this
generator will not emit one.

Rows are grouped by benchmark and sorted by score within a benchmark, so that
regenerating an unchanged dataset produces no diff. Sorting by score inside a
benchmark is not a ranking claim: rows of different evidence grades and
different sampling policies remain visibly distinct in their own columns.

Usage:
    python scripts/generate_benchmark_tables.py
    python scripts/generate_benchmark_tables.py --category coding
    python scripts/generate_benchmark_tables.py --check

Exit status:
    0  every region is up to date, or was updated successfully
    1  --check found a region that is out of date
    2  a file could not be read, or a region delimiter is missing
"""

from __future__ import annotations

import argparse
from pathlib import Path

from _common import (
    DATASETS,
    DOCS_DIR,
    DataError,
    fail,
    read_csv,
    relative,
    render_table,
    replace_generated_region,
)

#: Benchmarks that belong to each comparison page. A benchmark_id absent from
#: every category is reported by --check-orphans rather than silently dropped,
#: because a result that appears in no table is a result nobody reads.
CATEGORIES: dict[str, tuple[str, ...]] = {
    "coding": (
        "swe_bench", "swe_bench_verified", "swe_bench_pro", "terminal_bench",
        "livecodebench", "humaneval", "mbpp",
    ),
    "reasoning": (
        "mmlu", "mmlu_pro", "gpqa_diamond", "humanitys_last_exam", "arc_agi_1",
        "arc_agi_2", "arc_agi_3", "frontiermath", "aime", "math", "gsm8k",
    ),
    "multimodal": ("mmmu", "mmmu_pro", "mathvista", "docvqa", "chartqa", "videomme"),
    "long-context": (
        "longbench", "longcodebench", "ruler", "mrcr", "needle_in_a_haystack",
    ),
    "agents": (
        "browsecomp", "webarena", "osworld", "gaia", "agentbench", "bfcl", "toolbench",
    ),
    "factuality": ("facts", "simpleqa", "truthfulqa", "halueval", "halluhard"),
}

#: Where each category's table is written, and under which region name.
TARGETS: dict[str, tuple[Path, str]] = {
    "coding": (DOCS_DIR / "comparisons" / "coding-models.md", "coding-benchmarks"),
    "reasoning": (DOCS_DIR / "comparisons" / "reasoning-models.md", "reasoning-benchmarks"),
    "multimodal": (DOCS_DIR / "comparisons" / "multimodal-models.md", "multimodal-benchmarks"),
    "long-context": (
        DOCS_DIR / "comparisons" / "long-context-models.md",
        "long-context-benchmarks",
    ),
    "agents": (DOCS_DIR / "benchmarks" / "agents-and-computer-use.md", "agent-benchmarks"),
    "factuality": (DOCS_DIR / "benchmarks" / "factuality.md", "factuality-benchmarks"),
}

HEADER: tuple[str, ...] = (
    "Benchmark", "Subset", "Model", "Score", "Metric", "Unit", "Harness",
    "Sampling policy", "n", "Tools", "Reported by", "Evidence grade",
    "Evaluation date", "Published",
)

EMPTY_NOTE = (
    "No results for this category. Populate data/benchmarks.csv and rerun "
    "scripts/generate_benchmark_tables.py"
)


def build_category(category: str) -> str:
    """Build the results table for one benchmark category.

    Args:
        category: Key of ``CATEGORIES``.

    Returns:
        The rendered Markdown table.

    Raises:
        DataError: If the category is not defined.
    """
    if category not in CATEGORIES:
        raise DataError(f"unknown category {category!r}; expected one of {', '.join(CATEGORIES)}")
    wanted = set(CATEGORIES[category])
    _, results = read_csv(DATASETS["benchmarks"])

    def sort_key(row: dict[str, str]) -> tuple[str, str, float, str]:
        try:
            score = -float(row.get("score", "0"))
        except ValueError:
            score = 0.0
        return (
            row.get("benchmark_id", ""),
            row.get("subset", ""),
            score,
            row.get("model_id", ""),
        )

    rows = [
        [
            row.get("benchmark_name", ""),
            row.get("subset", ""),
            row.get("model_id", ""),
            row.get("score", ""),
            row.get("metric", ""),
            row.get("unit", ""),
            row.get("harness", ""),
            row.get("sampling_policy", ""),
            row.get("samples_n", ""),
            row.get("tool_permissions", ""),
            row.get("reported_by", ""),
            row.get("evidence_grade", ""),
            row.get("evaluation_date", ""),
            row.get("publication_date", ""),
        ]
        for row in sorted(results, key=sort_key)
        if row.get("benchmark_id", "").strip() in wanted
    ]
    return render_table(list(HEADER), rows, EMPTY_NOTE)


def find_orphans() -> list[str]:
    """Return benchmark identifiers present in the data but in no category.

    Returns:
        Sorted list of orphaned ``benchmark_id`` values.
    """
    _, results = read_csv(DATASETS["benchmarks"])
    assigned = {benchmark for ids in CATEGORIES.values() for benchmark in ids}
    present = {row.get("benchmark_id", "").strip() for row in results if row.get("benchmark_id")}
    return sorted(present - assigned)


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line parser.

    Returns:
        The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="generate_benchmark_tables.py",
        description="Generate benchmark comparison tables from data/benchmarks.csv.",
    )
    parser.add_argument(
        "--category",
        choices=sorted(TARGETS),
        help="regenerate a single category instead of all of them",
    )
    parser.add_argument(
        "--check", action="store_true", help="write nothing; exit 1 if a region is out of date"
    )
    return parser


def main() -> int:
    """Regenerate the configured regions and return the process exit status.

    Returns:
        0 on success, 1 when ``--check`` found an out-of-date region or when
        orphaned benchmark identifiers exist.
    """
    args = build_parser().parse_args()
    selected = [args.category] if args.category else sorted(TARGETS)
    stale: list[str] = []

    try:
        for category in selected:
            path, region = TARGETS[category]
            content = build_category(category)
            if args.check:
                if content not in path.read_text(encoding="utf-8"):
                    stale.append(f"{relative(path)}: region {region!r} is out of date")
                continue
            changed = replace_generated_region(path, region, content)
            state = "updated" if changed else "unchanged"
            print(f"{relative(path)}: region {region!r} {state}")

        orphans = find_orphans()
    except DataError as exc:
        fail(str(exc))

    for orphan in orphans:
        stale.append(
            f"data/benchmarks.csv: benchmark_id {orphan!r} belongs to no category in "
            f"generate_benchmark_tables.py, so its results appear in no table"
        )

    if stale:
        for message in stale:
            print(message)
        print("\ngenerate_benchmark_tables.py: FAIL.")
        return 1
    if args.check:
        print("generate_benchmark_tables.py: PASS. All regions are up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
