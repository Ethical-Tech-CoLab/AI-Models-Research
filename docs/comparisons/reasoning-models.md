# Reasoning model comparison

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 4, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Compares models on knowledge and reasoning benchmarks, with sampling policy visible in every row. Sampling policy is decisive here: a majority-vote result and a single-sample result on the same benchmark are not comparable, and the difference is frequently larger than the difference between models.

## Comparison rules in force

- Every row carries an evidence grade, a source, and a source date.
- Results produced under different harnesses, sampling policies, or tool permissions are not placed in the same ranked column without a warning adjacent to the table.
- Results whose conditions are `unstated` are never ranked against results whose conditions are known.
- Provider-reported rows are labelled Grade C and are never used alone to rank one provider above another.

## Research checklist

- [ ] Record the sampling policy and n for every row; rows marked unstated are excluded from ranked columns.
- [ ] Record the reasoning token budget where it is disclosed, and cross-reference the cost consequence in chapter 15.
- [ ] Flag saturated benchmarks in the file so that small differences are not read as capability differences.
- [ ] Regenerate the table with `python scripts/generate_benchmark_tables.py` and commit the result.
- [ ] Run `python scripts/validate_tables.py --check-comparability`.

## Generated comparison

Generated from the data layer by `scripts/generate_benchmark_tables.py`. Do not edit the region by hand.

<!-- BEGIN GENERATED: reasoning-benchmarks -->
| Benchmark | Subset | Model | Score | Metric | Unit | Harness | Sampling policy | n | Tools | Reported by | Evidence grade | Evaluation date | Published |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ARC-AGI-2 | full | gemini-3-1-pro | 77.1 | accuracy | percent | unstated | unstated | unstated | unstated | Google | C | unstated | 2026-01-01 |
| GPQA Diamond | diamond | gpt-5.6-sol | 94.6 | accuracy | percent | unstated | unstated | unstated | unstated | OpenAI | C | unstated | 2026-01-01 |
| GPQA Diamond | diamond | gemini-3-1-pro | 94.3 | accuracy | percent | unstated | unstated | unstated | unstated | OpenAI | C | unstated | 2026-01-01 |
<!-- END GENERATED: reasoning-benchmarks -->
