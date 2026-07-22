# Efficient model comparison

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 4, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Compares smaller and cheaper models on the axes that make them worth selecting: cost per accepted task, latency, memory footprint, and on-device or constrained-hardware deployment. Efficiency is defined here as work delivered per unit of cost, not as parameter count, because a small model that fails a task is not efficient.

## Comparison rules in force

- Every row carries an evidence grade, a source, and a source date.
- Results produced under different harnesses, sampling policies, or tool permissions are not placed in the same ranked column without a warning adjacent to the table.
- Results whose conditions are `unstated` are never ranked against results whose conditions are known.
- Provider-reported rows are labelled Grade C and are never used alone to rank one provider above another.

## Research checklist

- [ ] Define the efficiency criterion explicitly and apply it consistently.
- [ ] Compute cost per accepted task for every included model, stating the acceptance criterion used.
- [ ] Record memory footprint at a named precision and sequence length.
- [ ] State the quality bar at which each efficiency claim holds; an efficiency claim without a quality bar is not a claim.
- [ ] Regenerate the table with `python scripts/generate_model_tables.py` and commit the result.
- [ ] Run `python scripts/validate_tables.py --check-comparability`.

## Generated comparison

This page draws on `data/models.csv`, `data/pricing.csv`, and `data/benchmarks.csv`. Its generated region is defined during Phase 4, once the efficiency criterion in the checklist above is fixed, because the criterion determines the columns.
