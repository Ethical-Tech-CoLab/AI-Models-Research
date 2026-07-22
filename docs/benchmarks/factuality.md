# Factuality benchmarks

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Documents benchmarks that measure grounded factuality, short-form factual recall, imitative falsehood, and hallucination detection. Records the grounding condition for every result, because grounded and closed-book measurements answer different questions. Hosts the generated factuality results table.

## Benchmarks documented in this file

Each benchmark below is documented under the nine required headings listed in the next section. A benchmark is documented only after its construction methodology has been located and recorded in `data/sources.csv`.

- FACTS
- SimpleQA
- TruthfulQA
- HaluEval
- HalluHard

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
- [ ] Confirm the existence, maintainer, and construction of every benchmark in this list before documenting it; name similarity between benchmarks in this area is high and is a known source of error.
- [ ] Record whether abstention is scored, and how, for each benchmark.
- [ ] Record the judge model and prompt for any benchmark scored by a model judge, since the judge is part of the measurement instrument.
- [ ] Record every extracted result in `data/benchmarks.csv` with harness, sampling policy, tool permissions, evidence grade, and date.
- [ ] Run `python scripts/validate_tables.py --check-ranges --check-comparability`.

## Completion criteria

This file is complete when every listed benchmark answers all nine questions from a registered source, when no result appears here that is absent from `data/benchmarks.csv`, and when the quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.

## Recorded results

Generated from `data/benchmarks.csv` by `scripts/generate_benchmark_tables.py`. Do not edit the region by hand.

<!-- BEGIN GENERATED: factuality-benchmarks -->
| Benchmark | Subset | Model | Score | Metric | Unit | Harness | Sampling policy | n | Tools | Reported by | Evidence grade | Evaluation date | Published |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _No results for this category. Populate data/benchmarks.csv and rerun scripts/generate_benchmark_tables.py_ | | | | | | | | | | | | | |
<!-- END GENERATED: factuality-benchmarks -->
