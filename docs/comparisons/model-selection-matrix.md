# Model selection matrix

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 4, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

The consolidated matrix used by the selection framework in chapter 20: one row per model, with the constraint-relevant fields that eliminate candidates before capability is considered. The matrix is a filtering instrument, not a ranking.

## Comparison rules in force

- Every row carries an evidence grade, a source, and a source date.
- Results produced under different harnesses, sampling policies, or tool permissions are not placed in the same ranked column without a warning adjacent to the table.
- Results whose conditions are `unstated` are never ranked against results whose conditions are known.
- Provider-reported rows are labelled Grade C and are never used alone to rank one provider above another.

## Research checklist

- [ ] Confirm every field in the matrix corresponds to a constraint in the selection cascade in chapter 20.
- [ ] State in the file that the matrix does not rank models and cannot be read as a recommendation.
- [ ] Confirm the matrix regenerates cleanly from data/models.csv with no hand edits.
- [ ] Regenerate the table with `python scripts/generate_model_tables.py` and commit the result.
- [ ] Run `python scripts/validate_tables.py --check-comparability`.

## Generated comparison

Generated from the data layer by `scripts/generate_model_tables.py`. Do not edit the region by hand.

<!-- BEGIN GENERATED: model-selection-matrix -->
| Model | Provider | Open weights | Modalities in | Context window | Reasoning mode | Tool use | Agent capability | Deployment | Quantization | Hardware requirement | Evidence grade | Source date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _No rows. Populate the source dataset in data/ and rerun scripts/generate_model_tables.py_ | | | | | | | | | | | | |
<!-- END GENERATED: model-selection-matrix -->
