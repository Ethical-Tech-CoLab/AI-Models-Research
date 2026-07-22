# Internal bakeoff protocol

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

A protocol a reader can execute at their own cost to evaluate a shortlist of models on their own task. This repository runs no paid evaluations in continuous integration, so this protocol is how Grade A evidence for closed-weight models enters the repository: a reader runs it, documents the conditions, and contributes the results back.

## Research checklist

- [ ] Specify task set construction, including how to avoid contaminating a public benchmark with proprietary tasks.
- [ ] Specify the sample size required to distinguish two models at a stated effect size, with the statistical basis cited.
- [ ] Specify the blinding and randomisation procedure for human judgement.
- [ ] Specify the exact record to be produced, matching the columns of data/benchmarks.csv, so contributed results are directly ingestible.
- [ ] Specify the cost estimate procedure so a reader knows the price of the protocol before running it.

## Completion criteria

This file is complete when every checklist item above is closed and the quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
