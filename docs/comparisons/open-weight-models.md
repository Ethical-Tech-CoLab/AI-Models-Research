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
| Alibaba | Qwen 3.6 family | Not publicly disclosed | generally_available | yes | Not publicly disclosed | Dense and sparse mixture-of-experts variants | Not publicly disclosed | Not publicly disclosed | text\|image | 1000000 | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | first_party_api\|self_hosted | B | 2026-07-22 |
| Alibaba | Qwen 3.7 family | Not publicly disclosed | generally_available | yes | Not publicly disclosed | Dense and sparse mixture-of-experts variants | Not publicly disclosed | Not publicly disclosed | text\|image | 1000000 | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | first_party_api\|self_hosted | B | 2026-07-22 |
| DeepSeek | DeepSeek V4 Flash | Not publicly disclosed | generally_available | yes | Not publicly disclosed | Sparse mixture-of-experts | 284 | 13 | text | 1000000 | Not publicly disclosed | optional | Not publicly disclosed | first_party_api\|self_hosted | B | 2026-07-22 |
| DeepSeek | DeepSeek V4 Pro | Not publicly disclosed | generally_available | yes | Not publicly disclosed | Sparse mixture-of-experts with sparse attention | 1600 | 49 | text | 1000000 | Not publicly disclosed | optional | Not publicly disclosed | first_party_api\|self_hosted | B | 2026-07-22 |
| Meta | Llama 4 Maverick | Not publicly disclosed | generally_available | yes | Llama 4 Community License | Sparse mixture-of-experts | 400 | 17 | text\|image | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | self_hosted\|cloud_marketplace | B | 2026-07-22 |
| Meta | Llama 4 Scout | Not publicly disclosed | generally_available | yes | Llama 4 Community License | Sparse mixture-of-experts | Not publicly disclosed | 17 | text\|image | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | self_hosted\|cloud_marketplace | B | 2026-07-22 |
| Mistral | Mistral Medium 3.5 | Not publicly disclosed | generally_available | yes | Not publicly disclosed | Dense transformer | 128 | 128 | text | 256000 | Not publicly disclosed | optional | Not publicly disclosed | first_party_api\|self_hosted | B | 2026-07-22 |
| Mistral | Mistral Small 4 | Not publicly disclosed | generally_available | yes | Apache-2.0 | Sparse mixture-of-experts | 119 | 6 | text\|image | 256000 | Not publicly disclosed | optional | Not publicly disclosed | first_party_api\|self_hosted | B | 2026-07-22 |
<!-- END GENERATED: open-weight-models -->
