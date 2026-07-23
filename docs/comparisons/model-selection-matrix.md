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
| Qwen 3.6 family | Alibaba | yes | text\|image | 1000000 | Not publicly disclosed | Not publicly disclosed | Multilingual, coding, and multimodal agents | first_party_api\|self_hosted | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| Qwen 3.7 family | Alibaba | yes | text\|image | 1000000 | Not publicly disclosed | Not publicly disclosed | Agent-focused positioning | first_party_api\|self_hosted | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| Claude Fable 5 | Anthropic | no | text\|image | 1000000 | optional | function_calling | Positioned for long-running agents | first_party_api | Not applicable | Not applicable | B | 2026-07-22 |
| Claude Opus 4.8 | Anthropic | no | text\|image | 1000000 | optional | function_calling | Positioned for complex agentic coding and enterprise workflows | first_party_api | Not applicable | Not applicable | B | 2026-07-22 |
| Claude Sonnet 5 | Anthropic | no | text\|image | 1000000 | optional | function_calling | Fast balanced tier | first_party_api | Not applicable | Not applicable | B | 2026-07-22 |
| DeepSeek V4 Flash | DeepSeek | yes | text | 1000000 | optional | Not publicly disclosed | Thinking and non-thinking modes documented by the provider | first_party_api\|self_hosted | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| DeepSeek V4 Pro | DeepSeek | yes | text | 1000000 | optional | Not publicly disclosed | Reasoning and agent positioning stated by the provider | first_party_api\|self_hosted | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| Gemini 3.1 Flash-Lite | Google | no | text\|image | Not publicly disclosed | optional | function_calling | Positioned for high-volume low-latency serving | first_party_api | Not applicable | Not applicable | B | 2026-07-22 |
| Gemini 3.1 Pro | Google | no | text\|image | 1000000 | optional | function_calling | Search and code execution tools documented by the provider | first_party_api | Not applicable | Not applicable | C | 2026-07-22 |
| Llama 4 Maverick | Meta | yes | text\|image | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | Natively multimodal open-weight model | self_hosted\|cloud_marketplace | Not publicly disclosed | Single H100 host target stated by the provider; precision not stated | B | 2026-07-22 |
| Llama 4 Scout | Meta | yes | text\|image | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | Natively multimodal open-weight model | self_hosted\|cloud_marketplace | Not publicly disclosed | INT4 deployment on one H100 target stated by the provider | B | 2026-07-22 |
| Meta Muse Spark 1.1 | Meta | no | text\|image | 1000000 | Not publicly disclosed | function_calling | Multimodal agents, computer use, and context management | first_party_api | Not applicable | Not applicable | B | 2026-07-22 |
| Mistral Medium 3.5 | Mistral | yes | text | 256000 | optional | Not publicly disclosed | Coding agents documented by the provider | first_party_api\|self_hosted | Not publicly disclosed | Self-hosting on as few as four GPUs per the provider; GPU model and precision not stated | B | 2026-07-22 |
| Mistral Small 4 | Mistral | yes | text\|image | 256000 | optional | Not publicly disclosed | Configurable reasoning and efficient serving | first_party_api\|self_hosted | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| GPT-5.6 Luna | OpenAI | no | text\|image | 1050000 | optional | function_calling | Fast tier positioned for high volume | first_party_api | Not applicable | Not applicable | B | 2026-07-22 |
| GPT-5.6 Sol | OpenAI | no | text\|image | 1050000 | optional | function_calling | Extensive hosted tool surface documented by the provider | first_party_api | Not applicable | Not applicable | B | 2026-07-22 |
| GPT-5.6 Terra | OpenAI | no | text\|image | 1050000 | optional | function_calling | Similar tool surface to the Sol tier per provider documentation | first_party_api | Not applicable | Not applicable | B | 2026-07-22 |
| Grok 4.5 | xAI | no | text | 500000 | optional | function_calling | Positioned for coding and agentic knowledge work | first_party_api | Not applicable | Not applicable | B | 2026-07-22 |
<!-- END GENERATED: model-selection-matrix -->
