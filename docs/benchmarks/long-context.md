# Long-context benchmarks

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Documents benchmarks that probe behaviour at long input lengths: multitask long-document suites, long-code understanding, synthetic retrieval stress tests, multi-round coreference resolution, and needle-style retrieval probes. Explains why retrieval-only probes overstate usable context relative to tasks requiring reasoning across the whole input.

## Benchmarks documented in this file

Each benchmark below is documented under the nine required headings listed in the next section. A benchmark is documented only after its construction methodology has been located and recorded in `data/sources.csv`.

- LongBench
- LongCodeBench
- RULER
- MRCR
- Needle-in-a-Haystack

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
- [ ] Record the context length at which each result was obtained; a long-context score without a length is not interpretable.
- [ ] Record the performance threshold used to declare an effective context length.
- [ ] State the distinction between retrieval probes and reasoning-over-context tasks in the file, since conflating them is the field's most common long-context error.
- [ ] Record every extracted result in `data/benchmarks.csv` with harness, sampling policy, tool permissions, evidence grade, and date.
- [ ] Run `python scripts/validate_tables.py --check-ranges --check-comparability`.

## Completion criteria

This file is complete when every listed benchmark answers all nine questions from a registered source, when no result appears here that is absent from `data/benchmarks.csv`, and when the quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
