# Multilingual benchmarks and coverage

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Documents the language coverage of the benchmark set used in this repository, the benchmarks designed specifically for multilingual evaluation, and the interaction between tokenizer efficiency and both cost and measured performance in non-English languages. Records where translated benchmarks are used and what translation introduces.

## Required structure for each benchmark

Every benchmark answers all nine questions, in this order. The ninth is a judgement and is argued rather than asserted.

1. What it measures
2. Task format
3. Scoring method
4. Known limitations
5. Contamination risk
6. Tool permissions
7. Sampling policy
8. Human baseline comparability
9. Suitability for procurement

## Research checklist

- [ ] Locate and register the construction paper or methodology page for every benchmark listed above, before any result from it is recorded.
- [ ] Answer all nine required questions for each benchmark, citing the construction source for the first three.
- [ ] Record, per benchmark documented in this repository, which languages it covers and whether non-English versions are human-authored or machine-translated.
- [ ] Locate Grade A evidence on tokenizer efficiency across scripts and record the corpus and tokenizer used.
- [ ] State the coverage gap for low-resource languages as a property of the evidence base, and cross-reference the limitations document rather than restating it.
- [ ] Record whether any profiled provider publishes per-language pricing or token count guidance.
- [ ] Record every extracted result in `data/benchmarks.csv` with harness, sampling policy, tool permissions, evidence grade, and date.
- [ ] Run `python scripts/validate_tables.py --check-ranges --check-comparability`.

## Completion criteria

This file is complete when every listed benchmark answers all nine questions from a registered source, when no result appears here that is absent from `data/benchmarks.csv`, and when the quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
