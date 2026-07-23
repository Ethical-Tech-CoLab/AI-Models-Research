# Research gaps

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

This chapter consolidates what the survey could not establish and what would be required to establish it. Structural limitations that no further study can close are recorded in the [limitations document](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/limitations.md) instead; outstanding source acquisitions are in the [data sources register](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/data-sources.md).

## 1. Field-level gaps

| Gap | Why it matters |
|---|---|
| Comparable energy disclosure | Named commercial models rarely publish measured joules per token under a standardised workload |
| Agent reliability | Benchmarks do not capture multi-day workflows, changing environments, permissions, and recovery |
| Evaluation contamination | Public benchmarks become training targets and lose diagnostic value |
| Effective long context | Better tests are needed for dispersed reasoning, long outputs, memory, and compaction |
| Multilingual equity | Tokenization, cost, accuracy, and safety remain uneven across languages and scripts |
| Model updates | Endpoint behaviour changes without a new public model name, defeating reproducibility |
| Human baselines | Human scores are measured under different time, tool, and incentive conditions than model scores |
| Environmental systems accounting | Embodied carbon, water, grid constraints, and rebound effects remain underreported |

## 2. Gaps in this repository's own data

These are specific and closable, and each names what would close it.

1. **No energy rows.** `data/energy-studies.csv` is empty because neither Grade A study restates all eleven required conditions in a transcribable form. Closed by reading the two primary papers and extracting the conditions.
2. **No latency rows.** The two provider throughput figures state no percentile, concurrency, region, or prompt length. Closed by an independent measurement under the protocol in [latency methodology](evaluation/latency-methodology.md).
3. **No factuality rows.** Reported rates do not state the grounding condition per model. Closed by locating per-model results with the condition attached.
4. **All benchmark rows have unstated conditions.** Nine provider-reported results, none disclosing harness, sampling policy, or tool permissions. Closed only if providers disclose, or if a third party re-runs under a published harness.
5. **No release dates.** Every model row records the release date as not publicly disclosed, so the release timeline diagram is empty and the contamination argument has no axis to run along. Closed by extracting announcement dates from provider changelogs.
6. **Tokenizer unknown for most models.** A caller cannot compute the cost of their own corpus without it.
7. **Cached-input and batch rates unknown.** Recorded as not publicly disclosed for every priced model, which blocks the cache-savings formula from being applied to real schedules.
8. **Family-level rows for Qwen.** Two rows describe families rather than model identifiers and must be split once the model list is extracted.
9. **Every bibliography entry is unverified.** Titles, venues, and identifiers were transcribed and must be confirmed against the published record.

## 3. Direction

The likely near-term direction is adaptive systems that vary model size, reasoning budget, context, and tool use by task difficulty. That improves quality per unit of cost and energy while making evaluation harder, because the object being evaluated becomes a policy rather than a model. Future benchmarks should report the complete resource budget, including hidden reasoning, retries, verification, and tool calls.

Open-weight models will continue to narrow capability gaps while supporting sovereign and specialised deployment. Hosted frontier models will retain advantages in integrated tools and rapid updates, and buyers should demand stronger transparency and version stability in exchange.

## 4. The conclusion this handbook reaches

Model selection is empirical engineering and governance, not brand preference. The right system is the least resource-intensive configuration that reliably meets the task contract and the risk threshold. That requires local evaluation, explicit evidence standards, controlled reasoning budgets, token and energy measurement, and continuous monitoring. Frontier capability is valuable. Unverified capability is not reliability.
