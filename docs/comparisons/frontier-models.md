# Frontier model comparison

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 4, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Compares the closed-weight models positioned by their providers at the capability frontier, on specification and on results that were produced under compatible conditions. The comparison is constrained by the verification asymmetry: for these models, parameter counts, memory footprint, and energy per token are not observable, so the comparison is necessarily thinner than the open-weight one.

## Comparison rules in force

- Every row carries an evidence grade, a source, and a source date.
- Results produced under different harnesses, sampling policies, or tool permissions are not placed in the same ranked column without a warning adjacent to the table.
- Results whose conditions are `unstated` are never ranked against results whose conditions are known.
- Provider-reported rows are labelled Grade C and are never used alone to rank one provider above another.

## Research checklist

- [ ] Define the inclusion rule for 'frontier' explicitly and defensibly, rather than adopting provider positioning.
- [ ] Populate data/models.csv for every included model from its model card and API reference.
- [ ] Record which specification fields are 'Not publicly disclosed' rather than omitting the row.
- [ ] State in the file that Grade C rows are present and are not ranked against Grade A rows.
- [ ] Regenerate the table with `python scripts/generate_model_tables.py` and commit the result.
- [ ] Run `python scripts/validate_tables.py --check-comparability`.

## Generated comparison

Generated from the data layer by `scripts/generate_model_tables.py`. Do not edit the region by hand.

<!-- BEGIN GENERATED: frontier-models -->
| Provider | Model | Release date | Status | Open weights | Licence | Architecture | Total params (B) | Active params (B) | Modalities in | Context window | Max output | Reasoning mode | Tool use | Deployment | Evidence grade | Source date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anthropic | Claude Fable 5 | Not publicly disclosed | generally_available | no | Proprietary | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | text\|image | 1000000 | 128000 | optional | function_calling | first_party_api | B | 2026-07-22 |
| Anthropic | Claude Opus 4.8 | Not publicly disclosed | generally_available | no | Proprietary | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | text\|image | 1000000 | 128000 | optional | function_calling | first_party_api | B | 2026-07-22 |
| Anthropic | Claude Sonnet 5 | Not publicly disclosed | generally_available | no | Proprietary | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | text\|image | 1000000 | 128000 | optional | function_calling | first_party_api | B | 2026-07-22 |
| Google | Gemini 3.1 Flash-Lite | Not publicly disclosed | generally_available | no | Proprietary | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | text\|image | Not publicly disclosed | Not publicly disclosed | optional | function_calling | first_party_api | B | 2026-07-22 |
| Google | Gemini 3.1 Pro | Not publicly disclosed | generally_available | no | Proprietary | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | text\|image | 1000000 | 64000 | optional | function_calling | first_party_api | C | 2026-07-22 |
| Meta | Meta Muse Spark 1.1 | Not publicly disclosed | preview | no | Proprietary | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | text\|image | 1000000 | Not publicly disclosed | Not publicly disclosed | function_calling | first_party_api | B | 2026-07-22 |
| OpenAI | GPT-5.6 Luna | Not publicly disclosed | generally_available | no | Proprietary | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | text\|image | 1050000 | 128000 | optional | function_calling | first_party_api | B | 2026-07-22 |
| OpenAI | GPT-5.6 Sol | Not publicly disclosed | generally_available | no | Proprietary | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | text\|image | 1050000 | 128000 | optional | function_calling | first_party_api | B | 2026-07-22 |
| OpenAI | GPT-5.6 Terra | Not publicly disclosed | generally_available | no | Proprietary | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | text\|image | 1050000 | 128000 | optional | function_calling | first_party_api | B | 2026-07-22 |
| xAI | Grok 4.5 | Not publicly disclosed | generally_available | no | Proprietary | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | text | 500000 | Not publicly disclosed | optional | function_calling | first_party_api | B | 2026-07-22 |
<!-- END GENERATED: frontier-models -->
