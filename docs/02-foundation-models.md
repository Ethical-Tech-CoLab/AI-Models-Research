# Foundation models

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

This chapter defines the object of study and maps the model landscape as the sources recorded it on the research cut-off date.

Developed elsewhere: architectural mechanisms in [03. Transformer architecture](03-transformer-architecture.md); training procedures in [04. Training and post-training](04-training-and-post-training.md); licensing and openness in [18. Open versus closed models](18-open-vs-closed-models.md).

## 1. The unit of analysis is the deployed system

The object being evaluated is rarely the neural network alone. A deployed system may include a tokenizer, a routing layer, a hidden reasoning process, search, code execution, retrieval, prompt caching, safety classifiers, and agent orchestration. Two systems built on identical weights can differ in accuracy, latency, cost, and failure mode.

This distinction is what makes most reproducibility problems in the field intelligible. An endpoint can change behaviour without a change to the model identifier, and a versioned identifier can be retired without notice. Results are therefore recorded against a dated identifier and treated as historical.

## 2. Vocabulary

| Term | Operational definition |
|---|---|
| Model family | Related tiers or checkpoints sharing training lineage, architecture, or product positioning |
| Frontier model | A model near the current capability boundary on a broad set of difficult evaluations. Relative and time-sensitive |
| Open-weight model | A model whose learned parameters can be downloaded. Not the same as open training data, open code, or unrestricted licensing |
| Reasoning model | A model trained or configured to allocate additional inference compute before or during generation |
| Agentic model | A model used in a loop that plans, calls tools, observes results, updates state, and continues to a stopping condition |
| Context window | The maximum tokenized sequence the service accepts. Distinct from the portion the model uses reliably |

## 3. Three overlapping classes

The market recorded in this survey contains frontier hosted models optimising broad capability and tool integration; efficient hosted models optimising latency, price, and volume; and open-weight models optimising control, customisation, and deployment flexibility. Many providers offer one family at several capability tiers, or allow reasoning effort to be set per request, so the classes overlap within a single family.

Full specifications are generated from `data/models.csv` into [frontier models](comparisons/frontier-models.md) and [open-weight models](comparisons/open-weight-models.md).

## 4. Parameter count is an incomplete proxy

A mixture-of-experts model stores many parameters and activates a subset per token. That reduces compute per token relative to a dense model of the same stored size, but it does not remove memory, routing, communication, or serving overhead. Active parameter count must therefore be reported alongside total parameters, precision, hardware, batch size, and measured throughput before any efficiency claim is made.

Disclosed architectures in `data/models.csv` show the gap plainly: DeepSeek V4 Pro is recorded at 1.6 trillion total parameters with 49 billion active, and DeepSeek V4 Flash at 284 billion total with 13 billion active.[^deepseek2026preview] Mistral Small 4 is recorded at 119 billion total with 6 billion active across 128 experts, against Mistral Medium 3.5 as a 128 billion parameter dense model.[^mistral2026small] [^mistral2026medium] Llama 4 Maverick is recorded at 400 billion total with 17 billion active.[^meta2025llama]

The [interactive companion](interactive/index.html) plots active share against stored parameters for the disclosed architectures.

## 5. What is not disclosed

Total and active parameter counts are recorded as not publicly disclosed for every closed-weight model in this survey. So are architecture family, tokenizer, and training data for most of them. Those values are not estimated from benchmark behaviour or from inference price, and the empty fields are the finding.

## 6. Open research questions

- Which providers publish a stable versioning policy, and which change endpoint behaviour without a new identifier?
- Is there any independent method for bounding the parameter count of a closed-weight model that does not rest on an assumption about serving cost?
- How much of the capability difference between families is attributable to post-training rather than to scale?

## Sources

[^deepseek2026preview]: DeepSeek (2026). DeepSeek V4 Preview release. Grade B, official architecture disclosure. Accessed 2026-07-22.

[^mistral2026small]: Mistral AI (2026). Introducing Mistral Small 4. Grade B, official documentation. Accessed 2026-07-22.

[^mistral2026medium]: Mistral AI (2026). Mistral Medium 3.5 and remote agents. Grade B, official documentation. Accessed 2026-07-22.

[^meta2025llama]: Meta (2025). The Llama 4 herd: natively multimodal open-weight models. Grade B, official technical report. Accessed 2026-07-22.
