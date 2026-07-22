# Latency and throughput

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Decomposes response time into queueing, prefill, time to first token, and time per output token, adds tool latency for agent loops, and treats percentile reporting, concurrency, batching, and cold starts as necessary conditions on any figure. Provides worked calculations. Establishes that latency is a property of a served system rather than of a model.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The latency decomposition and its notation.
- The rule that a latency figure without percentile, concurrency, and region is not usable.
- The relationship between batching, throughput, and per-request latency.

## Developed elsewhere

- Measurement protocol: [evaluation/latency-methodology.md](evaluation/latency-methodology.md)
- Serving mechanisms: [13-inference.md](13-inference.md)
- Cost per second and per token: [15-token-economics.md](15-token-economics.md)

## Research checklist

- [ ] Define every latency term with a formula and cross-reference the formulas appendix.
- [ ] Produce at least one worked example from end to end, using stated inputs, and label it as a worked example rather than a measurement.
- [ ] Record independent third-party latency measurements where the methodology is disclosed; grade vendor claims C and label them.
- [ ] Add the Mermaid diagram of latency decomposition.
- [ ] State the cold-start conditions under which any measurement in this repository was taken.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
