# Long-context model comparison

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 4, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Compares advertised context length against measured performance at length. The comparison is only meaningful when the evaluation length and the performance threshold are stated, so both are mandatory columns here.

## Comparison rules in force

- Every row carries an evidence grade, a source, and a source date.
- Results produced under different harnesses, sampling policies, or tool permissions are not placed in the same ranked column without a warning adjacent to the table.
- Results whose conditions are `unstated` are never ranked against results whose conditions are known.
- Provider-reported rows are labelled Grade C and are never used alone to rank one provider above another.

## Research checklist

- [ ] Record the evaluation context length for every row.
- [ ] Record the threshold used for any effective-context claim.
- [ ] Separate retrieval probes from reasoning-over-context tasks in the presentation.
- [ ] Regenerate the table with `python scripts/generate_benchmark_tables.py` and commit the result.
- [ ] Run `python scripts/validate_tables.py --check-comparability`.

## Generated comparison

Generated from the data layer by `scripts/generate_benchmark_tables.py`. Do not edit the region by hand.

<!-- BEGIN GENERATED: long-context-benchmarks -->
| Benchmark | Subset | Model | Score | Metric | Unit | Harness | Sampling policy | n | Tools | Reported by | Evidence grade | Evaluation date | Published |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _No results for this category. Populate data/benchmarks.csv and rerun scripts/generate_benchmark_tables.py_ | | | | | | | | | | | | | |
<!-- END GENERATED: long-context-benchmarks -->
