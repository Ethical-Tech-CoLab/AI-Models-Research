# Token economics

> **Research cut-off date: 2026-07-22.**
> **Status: written.** Prices below are dated records of what a provider's own documentation stated on the access date, not statements about the present.

## Scope

This chapter converts prices into costs. It defines the billable token classes, the discount structures, and the formulas that turn a price schedule into a cost per accepted task. It answers research question RQ8 by showing that ranking models on advertised price per million tokens is not a ranking on cost.

Developed elsewhere: the token classes themselves in [12. Tokenization](12-tokenization.md); reasoning token volumes in [06. Reasoning models](06-reasoning-models.md); hardware cost of self-hosting in [17. Hardware and memory](17-hardware-and-memory.md); the measurement protocol in [token cost methodology](evaluation/token-cost-methodology.md).

## 1. Nominal price is not cost

Three effects separate the advertised rate from what a workload actually costs.

**Output is priced above input.** Across every schedule recorded below, the output rate is several times the input rate, and output is generated sequentially rather than in a single pass. Verbosity is therefore a cost driver, a latency driver, and an energy driver simultaneously.

**Reasoning tokens are billed at the output rate** where a provider bills them at all. A model that emits a long internal trace before a short answer can cost several times what its visible output suggests.

**Tokenizers differ.** The same text produces different token counts under different tokenizers, so two identical per-token prices are not identical prices for the same work. Anthropic states that Claude Sonnet 5 uses a tokenizer that can produce about 30 percent more tokens for the same text than its predecessor, which raises the cost of an equivalent request even with an unchanged per-token rate.[^anthropic2026sonnet]

That point generalises: a per-token price becomes comparable across providers only once token counts for the same corpus have been measured under each tokenizer. This survey has not performed that measurement, so what follows compares published rates, not cost for equivalent meaning.

## 2. Billable token classes

| Class | What it includes |
|---|---|
| Input | System prompt, user prompt, files, retrieved evidence, conversation history, tool results |
| Cached input | A repeated prefix served from a provider cache, usually discounted |
| Output | The visible response, and sometimes hidden intermediate content billed at output rates |
| Reasoning | Internal inference tokens, frequently included in output billing |
| Tool | Tool arguments and results, plus any separate search or tool fee |
| Compaction | Tokens spent compressing a long agent history to preserve state |

Compaction tokens recur across a session rather than once per request, and are the class most often left out of a cost estimate for an agent.

## 3. Recorded prices

Prices live in `data/pricing.csv` with an effective date and an access date; the table below is generated from it. Cached-input rates and batch discounts are recorded as not publicly disclosed because the sources used for this revision did not state them, not because they do not exist.

<!-- BEGIN GENERATED: pricing-table -->
| Model | Provider | Currency | Input / 1M | Cached input / 1M | Output / 1M | Reasoning tokens billed | Batch discount % | Effective date | Region | Evidence grade |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-fable-5 | Anthropic | USD | 10.00 | Not publicly disclosed | 50.00 | Not publicly disclosed | Not publicly disclosed | 2026-07-22 | Global | B |
| claude-opus-4-8 | Anthropic | USD | 5.00 | Not publicly disclosed | 25.00 | Not publicly disclosed | Not publicly disclosed | 2026-07-22 | Global | B |
| claude-sonnet-5 | Anthropic | USD | 3.00 | Not publicly disclosed | 15.00 | Not publicly disclosed | Not publicly disclosed | 2026-07-22 | Global | B |
| deepseek-v4-pro | DeepSeek | USD | 0.435 | Not publicly disclosed | 0.87 | Not publicly disclosed | Not publicly disclosed | 2026-07-22 | Global | B |
| gpt-5.6-luna | OpenAI | USD | 1.00 | Not publicly disclosed | 6.00 | Not publicly disclosed | Not publicly disclosed | 2026-07-22 | Global | B |
| gpt-5.6-sol | OpenAI | USD | 5.00 | Not publicly disclosed | 30.00 | Not publicly disclosed | Not publicly disclosed | 2026-07-22 | Global | B |
| gpt-5.6-terra | OpenAI | USD | 2.50 | Not publicly disclosed | 15.00 | Not publicly disclosed | Not publicly disclosed | 2026-07-22 | Global | B |
| grok-4-5 | xAI | USD | 2.00 | Not publicly disclosed | 6.00 | Not publicly disclosed | Not publicly disclosed | 2026-07-22 | Global | B |
<!-- END GENERATED: pricing-table -->

Commercial terms taken from a provider's own documentation are Grade B, because the provider is the definitive authority on its own prices. That grade says nothing about the same provider's performance claims, which are Grade C and are recorded separately in `data/benchmarks.csv`.

The [interactive companion](interactive/index.html) applies these rates live: setting input, output, reasoning, and acceptance-rate values recomputes cost per accepted task and reorders the models accordingly.

## 4. The formulas

Defined once in the [appendix of formulas](appendices/formulas.md) and implemented in `scripts/calculate_token_costs.py`, which is the reference implementation. Where the appendix and the script disagree, the script is authoritative.

1. **Effective tokens per task.** Every token class a task consumes, whether or not the provider bills it. An unbilled class still consumes context and latency.
2. **Total API cost.** Fresh input and tool tokens at the input rate, cached input at the cached rate, visible output and billed reasoning at the output rate.
3. **Cost per accepted task.** Total cost divided by the acceptance rate. This is the figure a budget needs.
4. **Cache savings.** Cached tokens multiplied by the difference between the fresh and cached input rates, realised only on the share of requests that hit the cache.
5. **Reasoning overhead.** Reported both as a token ratio and as a share of cost, because the two differ whenever reasoning is billed at a rate other than visible output.

## 5. Cost per accepted task

An accepted task is one that passes a domain-specific quality check without manual correction beyond a defined tolerance. The acceptance criterion must be stated wherever an acceptance rate is used: two teams applying different criteria to the same outputs will compute different costs from identical prices, and the difference will be attributed to the model unless the criterion is visible.

The consequence is that a cheap model can be the expensive choice. If it needs repeated prompts, longer outputs, more tool calls, human correction, or escalation to a stronger model, its low rate buys fewer accepted outputs per unit of spend. A costly model that succeeds on the first attempt, with fewer tools and fewer tokens, can be cheaper on this measure while being more expensive on every per-token measure.

This handbook publishes no cost-per-accepted-task ranking, because acceptance rates are task-specific and no source in this survey reports one. The procedure for measuring them locally is in [internal bakeoff](evaluation/internal-bakeoff.md).

## 6. What the price table does not tell you

1. **Quality is not held constant.** The rows differ by a large factor in nominal cost and by an unmeasured amount in capability. The table is a cost record, not a value judgement.
2. **Tool, search, and code execution fees are excluded**, as are long-context surcharges, caching writes, enterprise agreements, and tax.
3. **Multimodal accounting is excluded.** Image, audio, video, and document inputs are converted to billable units by provider-specific rules that this revision did not extract.
4. **Prices move.** Every figure here records a named date. Re-verify before budgeting.

## 7. Open research questions

- What is the token count for an identical multilingual corpus under each provider's tokenizer, and how much of the apparent price spread survives that normalisation?
- Which providers bill reasoning tokens, at what rate, and do any expose the count to the caller for audit?
- What cache hit rate is achievable in practice for agent workloads with stable prefixes, and what does it do to the ordering above?
- Do published prices track serving cost, or are they set competitively and therefore uninformative about efficiency?

## Sources

[^anthropic2026sonnet]: Anthropic (2026). Claude Sonnet 5 documentation and pricing notes. Claude Platform Documentation. Grade B, official documentation of the provider's own commercial terms. Accessed 2026-07-22.
