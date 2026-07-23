# Latency and throughput

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

This chapter decomposes response time, states the conditions any latency figure must carry, and explains why latency is a property of a served system rather than of a model.

Developed elsewhere: the measurement protocol in [latency methodology](evaluation/latency-methodology.md); serving mechanisms in [13. Inference](13-inference.md); the cost consequences in [15. Token economics](15-token-economics.md).

## 1. Latency anatomy

| Phase | Meaning | Main drivers |
|---|---|---|
| Queueing | Time before compute begins | Provider capacity, priority tier, concurrency |
| Prefill | Processing the input and building the key-value cache | Input length, attention design, cache hits, hardware |
| Time to first token | The startup delay a user perceives | Queueing plus prefill plus routing |
| Decode | Sequential generation of output tokens | Model size, active parameters, precision, batching |
| Tool time | Search, code, browser, database, or external API calls | Tool speed, retries, network, permissions |
| Post-processing | Validation, citation checks, safety, formatting | System architecture |

Reasoning tokens appear in decode time whether or not the caller can see them, which is why a reasoning model can be slow without appearing to produce more output.

## 2. Tokens per second is not task completion time

Generation speed is interpretable only once time to first token and the workload conditions are specified. Google reports 363 output tokens per second for Gemini 3.1 Flash-Lite in its own evaluation.[^deepmind2026flashlite] xAI reports 80 tokens per second for Grok 4.5 on its launch page.[^xai2026launch]

Those two figures come from different test environments and different model classes and are not a controlled head-to-head comparison. Both are provider-reported. They indicate that fast tiers exist and are positioned for interactive and high-volume use; they do not measure how long a task takes.

A model streaming at a high token rate can still be slow if it emits excessive reasoning tokens or needs repeated attempts. A slower model can finish sooner if it needs fewer steps, fewer tool calls, and less rework. The decision-relevant quantity is end-to-end task completion time, including tools and retries.

## 3. Fast against slow reasoning

Configurable reasoning moves the latency-quality frontier rather than sitting at a point on it. Low or disabled reasoning suits extraction, rewriting, classification, and deterministic tool routing. High reasoning effort earns its cost on mathematics, scientific analysis, difficult coding, and planning, where an incorrect result costs more than the additional compute.

The optimal policy is adaptive: estimate difficulty, then allocate compute only where the expected quality gain justifies the added time, cost, and energy. Research on test-time compute identifies diminishing returns and overthinking, in which longer chains introduce new errors, lose the objective, or exhaust the context budget. The correct stopping rule is therefore quality-conditioned, using verifier signals, uncertainty, progress, and task complexity, rather than a fixed token allowance.

## 4. Operational reporting requirements

A latency figure without these is not usable, and this repository does not record one.

- Report p50, p90, and p95 time to first token, never a mean alone.
- Report p50 and p95 end-to-end completion time, including tools and retries.
- Separate cold starts from warm requests, and cache hits from cache misses.
- Compare models at the same latency and cost budget, not at their own defaults.
- Track output tokens, tool calls, failed steps, and retries per accepted task.
- Test at the concurrency you expect, because batching raises throughput while raising individual latency.

## 5. What this repository records

No latency or throughput rows exist at this revision. The two provider figures in section 2 are recorded in prose with the reporting party named, and are not entered into a dataset, because neither states percentile, concurrency, region, prompt length, or output length. A dataset row would imply a comparability the measurements do not have.

## 6. Open research questions

- Do independent third-party latency measurements exist for these endpoints under a disclosed methodology?
- How much of the observed difference between providers is serving infrastructure rather than model?
- What is the distribution, not the mean, of time to first token under production concurrency?
- How does end-to-end task completion time compare across models once retries and tool calls are counted?

## Sources

[^deepmind2026flashlite]: Google DeepMind (2026). Gemini 3.1 Flash-Lite model card. Grade B for the specification; the throughput figure is provider-reported and Grade C at the point of use. Accessed 2026-07-22.

[^xai2026launch]: xAI (2026). Introducing Grok 4.5. Grade C, provider-reported launch page. Accessed 2026-07-22.
