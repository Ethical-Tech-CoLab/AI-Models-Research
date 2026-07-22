# Benchmarking

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

The methodological chapter on evaluation. Explains what a benchmark score is, how harness choice, prompt formatting, answer extraction, sampling policy, and tool permissions change it, and why scores from different evaluators are frequently not comparable. Covers contamination, saturation, construct validity, and the distinction between accuracy benchmarks and preference leaderboards. Answers research question RQ2 on the predictive value of published scores under procurement conditions.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The anatomy of a benchmark result and the conditions that must accompany it.
- The incomparable-settings argument, which the rest of the handbook applies as a rule.
- The distinction between accuracy measurement and aggregate preference.
- The contamination argument in its general form.

## Developed elsewhere

- Per-benchmark documentation: [benchmarks/benchmark-overview.md](benchmarks/benchmark-overview.md)
- Per-benchmark limitations: [benchmarks/benchmark-limitations.md](benchmarks/benchmark-limitations.md)
- Running an evaluation: [evaluation/internal-bakeoff.md](evaluation/internal-bakeoff.md)

## Research checklist

- [ ] Cite the holistic-evaluation literature for the harness-sensitivity claim, with the specific finding rather than the report in general.
- [ ] Locate a Grade A source quantifying score variation for one model on one benchmark across harnesses; record the exact conditions.
- [ ] Cite the preference-leaderboard literature for the formatting and length effects on human preference.
- [ ] Add the Mermaid diagram of the model evaluation pipeline.
- [ ] Confirm the contamination argument is developed here and only referenced in chapters 04 and 07 and in the benchmark files.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
