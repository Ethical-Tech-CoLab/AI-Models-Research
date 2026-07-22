# Open-weight model comparison

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 4, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Compares models whose weights are downloadable, on specification, licence terms, hardware requirement, and independently measured performance. Because these models can be instrumented directly, this comparison can carry Grade A evidence on memory, throughput, and energy that the frontier comparison cannot.

## Comparison rules in force

- Every row carries an evidence grade, a source, and a source date.
- Results produced under different harnesses, sampling policies, or tool permissions are not placed in the same ranked column without a warning adjacent to the table.
- Results whose conditions are `unstated` are never ranked against results whose conditions are known.
- Provider-reported rows are labelled Grade C and are never used alone to rank one provider above another.

## Research checklist

- [ ] Record the exact licence and its use restrictions for every model, with a link to the licence text.
- [ ] Record hardware requirements at a named precision, computed with scripts/estimate_memory.py and labelled as an estimate.
- [ ] Prefer independently measured throughput and memory figures; label any vendor figure as provider-reported.
- [ ] State the distinction between open weights and open source in the file header.
- [ ] Regenerate the table with `python scripts/generate_model_tables.py` and commit the result.
- [ ] Run `python scripts/validate_tables.py --check-comparability`.

## Generated comparison

Generated from the data layer by `scripts/generate_model_tables.py`. Do not edit the region by hand.

<!-- BEGIN GENERATED: open-weight-models -->
| Provider | Model | Release date | Status | Open weights | Licence | Architecture | Total params (B) | Active params (B) | Modalities in | Context window | Max output | Reasoning mode | Tool use | Deployment | Evidence grade | Source date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _No rows. Populate the source dataset in data/ and rerun scripts/generate_model_tables.py_ | | | | | | | | | | | | | | | | |
<!-- END GENERATED: open-weight-models -->
