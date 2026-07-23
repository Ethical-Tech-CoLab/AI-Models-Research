# Benchmarking

> **Research cut-off date: 2026-07-22.**
> **Status: written.** Benchmark results recorded in this repository are Grade C and carry unstated evaluation conditions, which disqualifies them from ranked comparison. That is a finding about the state of public reporting, not a gap in the data collection.

## Scope

This chapter explains what a benchmark score is, what changes it, and why scores from different evaluators are frequently not comparable. It answers research question RQ2 on the predictive value of published scores under procurement conditions.

Developed elsewhere: per-benchmark documentation in [benchmark overview](benchmarks/benchmark-overview.md); the catalogue of failure modes in [benchmark limitations](benchmarks/benchmark-limitations.md); running your own evaluation in [internal bakeoff](evaluation/internal-bakeoff.md).

## 1. Performance is not a scalar

The holistic evaluation framework argued that a model should be assessed across accuracy, calibration, robustness, fairness, bias, toxicity, and efficiency rather than on a single number.[^liang2022holistic] That argument is stronger now that models use tools, accept several modalities, and vary their reasoning effort per request, because a single score hides differences in reliability, cost, and behaviour that determine whether a system works in production. Stanford's capability evaluations continue to report across multiple scenarios for the same reason.[^crfm2026helmcapabilities]

| Dimension | What it asks | Representative measures |
|---|---|---|
| Task accuracy | Correct answers, successful repairs, completed workflows | Exact match, pass rate, expert score, task success |
| Reliability | Consistency across runs, prompts, and subgroups | Variance, failure rate, calibration, abstention |
| Agent performance | Ability to plan and execute multi-step actions | End-to-end success, tool errors, recovery rate |
| Long-context competence | Use of dispersed information over long inputs | Retrieval, aggregation, instruction retention, coherence |
| Speed | Responsiveness and completion time | Time to first token, time per output token, percentile latency |
| Efficiency | Resources required for a useful result | Tokens, joules, and cost per accepted task |
| Operational fit | Deployability under real constraints | Privacy, region, licence, fine-tuning, uptime, observability |

## 2. Why rankings disagree

Evaluations change the computational and informational conditions under which a model operates, so they change the ordering.

- A model tested with web search and code execution is not comparable to a closed-book model.
- A model allowed maximum reasoning effort, or several samples, has a larger inference budget than a model tested once at default settings.
- Agent benchmarks are sensitive to the scaffolding that manages tools, context, retries, and termination, so the result belongs to a model-and-scaffold pair rather than to a model.
- Prompt formulation alters scores and can reorder models, especially on open-ended and instruction-following tasks.
- Contamination inflates performance when evaluation items or near variants appear in training data.
- Judging by another model introduces judge bias, positional effects, verbosity preference, and family favouritism.[^asirvatham2026gpt]
- Pass-at-k and majority voting spend more compute than single-attempt evaluation and are not equivalent to it.
- Provider tables mix internal tasks with public benchmarks and may evaluate competitor models under the publishing provider's own harness.
- A high average conceals severe failures in minority languages, long inputs, rare domains, and adversarial cases.

## 3. The state of the reported evidence

The Stanford AI Index documents rapid capability gains alongside a persistent gap from human performance on difficult interactive tasks, and reports that progress is benchmark-dependent: models approach saturation on some mathematics and knowledge tests while remaining weak on application construction, long-horizon agents, and open-world computer use.[^stanford2026aiindex]

Best reported results against human baselines are documented in [07. Agentic AI](07-agentic-ai.md) and visualised in the [interactive companion](interactive/index.html), which owns that comparison so that this chapter does not restate it.

## 4. What this repository records, and why it cannot rank

`data/benchmarks.csv` holds nine provider-reported results at this revision, drawn from two launch pages. Every one of them has `unstated` in the harness, sampling policy, and tool permission columns, because neither source disclosed them.

Under the incomparable-settings rule, a result whose conditions are unknown is never placed in a ranked column beside a result whose conditions are known. Since all nine are unstated, no ranking is possible from the current dataset, and the generated comparison tables present them with their conditions visible rather than sorted into a league table.

Two of those rows deserve particular care: they are figures for a competitor's model, published by a different provider, evaluated under the publishing provider's own harness. They are recorded with the reporting party named, because a competitor-reported figure is a different evidentiary object from a self-reported one and neither is independent.

## 5. Interpretation rule

Treat vendor benchmark numbers as hypotheses for local testing. They are useful for narrowing a candidate set and are not sufficient for procurement.

## 6. Open research questions

- How large is the score variation attributable to harness and prompt formatting alone, for a fixed model on a fixed benchmark?
- Do any providers publish the harness, sampling policy, and tool permissions behind their launch tables, and if not, what would induce them to?
- Is there measurable correlation between benchmark performance and deployed task success for any documented workload?
- How should a benchmark be designed so that it resists becoming a training target without becoming secret?

## Sources

[^liang2022holistic]: Liang, P., and others (2022). Holistic evaluation of language models. Preprint. Grade B. Accessed 2026-07-22.

[^crfm2026helmcapabilities]: Stanford Center for Research on Foundation Models (2026). HELM Capabilities. Grade A, maintainer-run standardised evaluation. Accessed 2026-07-22.

[^asirvatham2026gpt]: Asirvatham, H., and others (2026). GPT as a measurement tool. Harvard University. Grade B, institutional. Accessed 2026-07-22.

[^stanford2026aiindex]: Stanford Institute for Human-Centered Artificial Intelligence (2026). AI Index Report 2026, Technical Performance chapter. Grade B, institutional compilation. Accessed 2026-07-22.
