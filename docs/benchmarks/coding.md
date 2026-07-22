# Coding benchmarks

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Documents benchmarks that measure code generation and software engineering, from single-function synthesis through repository-level issue resolution and terminal task completion. The central measurement problem is that the strongest results are produced by an agent scaffold rather than by a model alone, and scaffolds are rarely described in enough detail to reproduce.

## Benchmarks documented in this file

Each benchmark below is documented under the nine required headings listed in the next section. A benchmark is documented only after its construction methodology has been located and recorded in `data/sources.csv`.

- SWE-Bench
- SWE-Bench Verified
- SWE-Bench Pro
- Terminal-Bench
- LiveCodeBench
- HumanEval
- MBPP

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
- [ ] Record the scaffold for every issue-resolution result; results without a described scaffold are marked unstated and excluded from ranked columns.
- [ ] Establish the provenance and construction of the Verified and Pro variants, and state how each differs from the original.
- [ ] Record the contamination-resistance mechanism of any benchmark that claims one, including the date window it relies on.
- [ ] State which of these benchmarks are saturated at the research cut-off date.
- [ ] Record every extracted result in `data/benchmarks.csv` with harness, sampling policy, tool permissions, evidence grade, and date.
- [ ] Run `python scripts/validate_tables.py --check-ranges --check-comparability`.

## Completion criteria

This file is complete when every listed benchmark answers all nine questions from a registered source, when no result appears here that is absent from `data/benchmarks.csv`, and when the quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
