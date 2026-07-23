# Long context

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

This chapter separates advertised context length from measured usable context, and states the criteria under which an effective-context claim may be made. It answers research question RQ6.

Developed elsewhere: benchmark construction in [long-context benchmarks](benchmarks/long-context.md); key-value cache arithmetic in [17. Hardware and memory](17-hardware-and-memory.md); compaction cost in agent loops in [07. Agentic AI](07-agentic-ai.md).

## 1. Capacity is not reliability

Context windows near one million tokens are now common across the frontier families recorded in this survey. Advertised capacity is a specification: it states what the service will accept, not what the model will use well.

The evaluation literature is consistent on this point. Stanford's long-context evaluation states that support for long inputs does not imply strong long-context capability.[^crfm2025helmlongcontext] LongCodeBench finds degradation on real code tasks as context scales toward one million tokens.[^rando2025longcodebench] LongProc finds that models accept long inputs yet lose coherence when they must integrate dispersed information and produce structured output over thousands of tokens.[^ye2025longproc]

## 2. Failure modes

| Failure mode | Description |
|---|---|
| Lost evidence | Relevant information is overlooked among distractors |
| Position bias | Material at the start and end is used more reliably than material in the middle |
| Aggregation failure | Individual facts are extracted correctly but combined incorrectly |
| Instruction decay | Constraints stated early are forgotten during long generation |
| Context pollution | Stale tool results, abandoned plans, and irrelevant documents interfere with current decisions |
| Cost explosion | Large prompts raise prefill latency, memory use, and input charges |

The first three defeat retrieval probes specifically. A needle-style test measures whether a single fact can be located; it does not measure whether dispersed facts can be reasoned over. Conflating the two is the most common error in long-context reporting, and it systematically overstates usable context.

## 3. Advertised against measured

The table below is generated from `data/context-windows.csv`. Advertised values come from provider documentation and are Grade B. The measured column is `Insufficient independent evidence` for every model, which is an accurate record of the current state rather than a placeholder.

<!-- BEGIN GENERATED: context-windows -->
| Model | Advertised context | Advertised max output | Measured effective context | Measurement benchmark | Threshold | Evidence grade | Source date |
|---|---|---|---|---|---|---|---|
| claude-fable-5 | 1000000 | 128000 | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| claude-opus-4-8 | 1000000 | 128000 | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| claude-sonnet-5 | 1000000 | 128000 | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| deepseek-v4-flash | 1000000 | Not publicly disclosed | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| deepseek-v4-pro | 1000000 | Not publicly disclosed | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| gemini-3-1-pro | 1000000 | 64000 | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | C | 2026-07-22 |
| gpt-5.6-luna | 1050000 | 128000 | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| gpt-5.6-sol | 1050000 | 128000 | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| gpt-5.6-terra | 1050000 | 128000 | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| grok-4-5 | 500000 | Not publicly disclosed | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| meta-muse-spark-1-1 | 1000000 | Not publicly disclosed | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| mistral-medium-3-5 | 256000 | Not publicly disclosed | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| mistral-small-4 | 256000 | Not publicly disclosed | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
| qwen-3-6 | 1000000 | Not publicly disclosed | Insufficient independent evidence | Insufficient independent evidence | Insufficient independent evidence | B | 2026-07-22 |
<!-- END GENERATED: context-windows -->

The literature in section 1 establishes that advertised capacity exceeds reliable capacity in general. It does not establish a number for any specific model in this table, and this handbook will not convert a general finding into a per-model figure.

## 4. Architectural consequence

Long context is expensive independently of parameter count, because key-value cache memory grows with sequence length, batch size, and the number of key and value heads. That relationship, and the grouped-query and multi-query attention designs that mitigate it, are developed in [17. Hardware and memory](17-hardware-and-memory.md).

## 5. Practical implication

Long context reduces the need for aggressive chunking. It does not remove the need for retrieval. The most reliable architecture observed in the reviewed material is hierarchical: retrieve the relevant sections, preserve document structure, summarise locally, verify cross-document claims, and keep source links throughout. Context compaction is useful for agents, but every compression step can drop detail and should be auditable.

## 6. Open research questions

- What is the effective context of each model in the table, measured under a stated threshold and a stated task type?
- How far do retrieval-probe results and reasoning-over-context results diverge for the same model at the same length?
- Does position bias persist at the top of the advertised range, or is it concentrated at particular offsets?
- What does compaction cost over a long agent session, in tokens and in lost detail?

## Sources

[^crfm2025helmlongcontext]: Stanford Center for Research on Foundation Models (2025). HELM Long Context. Grade A, maintainer-run standardised evaluation. Accessed 2026-07-22.

[^rando2025longcodebench]: Rando, S., and others (2025). LongCodeBench: evaluating coding LLMs at 1M context windows. Preprint. Grade B. Accessed 2026-07-22.

[^ye2025longproc]: Ye, X., Yin, F., He, Y., Zhang, J., Yen, H., Gao, T., Durrett, G., and Chen, D. (2025). LongProc: benchmarking long-context language models on long procedural generation. Preprint. Grade B. Accessed 2026-07-22.
