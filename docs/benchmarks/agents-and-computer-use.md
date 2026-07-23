# Agent and computer-use benchmarks

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Documents benchmarks that evaluate models inside action loops: web browsing and information seeking, simulated web environments, full desktop environments, general assistant tasks, and structured function-calling suites. Hosts the generated agent results table.

## Benchmarks documented in this file

Each benchmark below is documented under the nine required headings listed in the next section. A benchmark is documented only after its construction methodology has been located and recorded in `data/sources.csv`.

- BrowseComp
- WebArena
- OSWorld
- GAIA
- AgentBench
- BFCL
- ToolBench

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
- [ ] Record the environment version for every result; these environments change and results are not comparable across versions.
- [ ] Record whether the evaluation permits retries and how partial completion is scored.
- [ ] Distinguish results produced with a provider's own scaffold from results produced under the benchmark's reference scaffold.
- [ ] Record every extracted result in `data/benchmarks.csv` with harness, sampling policy, tool permissions, evidence grade, and date.
- [ ] Run `python scripts/validate_tables.py --check-ranges --check-comparability`.

## Completion criteria

This file is complete when every listed benchmark answers all nine questions from a registered source, when no result appears here that is absent from `data/benchmarks.csv`, and when the quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.

## Recorded results

Generated from `data/benchmarks.csv` by `scripts/generate_benchmark_tables.py`. Do not edit the region by hand.

<!-- BEGIN GENERATED: agent-benchmarks -->
| Benchmark | Subset | Model | Score | Metric | Unit | Harness | Sampling policy | n | Tools | Reported by | Evidence grade | Evaluation date | Published |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BrowseComp | full | gpt-5.6-sol | 90.4 | accuracy | percent | unstated | unstated | unstated | unstated | OpenAI | C | unstated | 2026-01-01 |
| BrowseComp | full | gemini-3-1-pro | 85.9 | accuracy | percent | unstated | unstated | unstated | unstated | Google | C | unstated | 2026-01-01 |
| OSWorld | full | gpt-5.6-sol | 62.6 | task_success | percent | unstated | unstated | unstated | unstated | OpenAI | C | unstated | 2026-01-01 |
<!-- END GENERATED: agent-benchmarks -->
