# Reasoning models

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Examines models that expend additional inference compute before answering. Covers chain-of-thought prompting, trained reasoning behaviour, hidden versus visible reasoning traces, caller-selectable reasoning effort, and the accuracy-per-token and accuracy-per-second trade-offs these create. Answers research question RQ4: whether reasoning-mode inference improves accuracy enough to justify its token and latency cost, and under what task conditions.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The definition of reasoning tokens and the taxonomy of reasoning modes.
- The accuracy-versus-cost trade-off analysis for extended reasoning.
- The evidentiary problem created by hidden reasoning traces, which prevent a caller from auditing what they are billed for.

## Developed elsewhere

- Cost arithmetic: [15-token-economics.md](15-token-economics.md)
- Latency decomposition: [14-latency-and-throughput.md](14-latency-and-throughput.md)
- Reasoning benchmark construction: [benchmarks/knowledge-and-reasoning.md](benchmarks/knowledge-and-reasoning.md)

## Research checklist

- [ ] Cite the primary sources for chain-of-thought and for process supervision.
- [ ] Record, per profiled family, whether reasoning tokens are visible, whether they are billed, and at which price, each with a source and date.
- [ ] Locate at least one Grade A study measuring accuracy as a function of reasoning token budget on a fixed benchmark, or record that none was found.
- [ ] Compute the reasoning overhead ratio for each family where token counts are available, using scripts/calculate_token_costs.py.
- [ ] State explicitly which task classes show no measured benefit from extended reasoning, with sources.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
