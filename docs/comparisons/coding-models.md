# Coding model comparison

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 4, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Compares models on the coding benchmarks documented in this repository, with the scaffold and tool permissions visible in every row, because repository-level results are properties of a model-and-scaffold pair rather than of a model.

## Comparison rules in force

- Every row carries an evidence grade, a source, and a source date.
- Results produced under different harnesses, sampling policies, or tool permissions are not placed in the same ranked column without a warning adjacent to the table.
- Results whose conditions are `unstated` are never ranked against results whose conditions are known.
- Provider-reported rows are labelled Grade C and are never used alone to rank one provider above another.

## Research checklist

- [ ] Ensure every row carries a scaffold description in its notes field.
- [ ] Separate single-function synthesis results from repository-level results; they measure different constructs and are not ranked together.
- [ ] Record the contamination position for each benchmark used.
- [ ] Regenerate the table with `python scripts/generate_benchmark_tables.py` and commit the result.
- [ ] Run `python scripts/validate_tables.py --check-comparability`.

## Generated comparison

Generated from the data layer by `scripts/generate_benchmark_tables.py`. Do not edit the region by hand.

<!-- BEGIN GENERATED: coding-benchmarks -->
| Benchmark | Subset | Model | Score | Metric | Unit | Harness | Sampling policy | n | Tools | Reported by | Evidence grade | Evaluation date | Published |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _No results for this category. Populate data/benchmarks.csv and rerun scripts/generate_benchmark_tables.py_ | | | | | | | | | | | | | |
<!-- END GENERATED: coding-benchmarks -->
