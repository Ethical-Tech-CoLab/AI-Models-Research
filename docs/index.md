# AI Models: Performance, Capabilities, Accuracy, Speed, Energy Use, and Token Economics

> **Research cut-off date: 2026-07-22.**

A technical reference, comparative research survey, and reproducible evaluation framework covering contemporary proprietary and open-weight AI model families. An [Ethical Tech CoLab](https://github.com/Ethical-Tech-CoLab) project.

## What this handbook is for

Public discussion of model capability mixes three kinds of claim that have very different reliability: independently verified measurement, institutional disclosure, and provider marketing. This handbook separates them, records every quantitative value with its evaluation conditions and its date, and generates every comparison table from a machine-readable data layer so that no figure can appear without a source behind it.

It is written for graduate researchers, procurement and policy analysts, engineers selecting production models, and sustainability researchers quantifying the resource footprint of inference.

## How to read it

| If you are | Start at |
|---|---|
| Selecting a model for a specific task | [20. Model selection framework](20-model-selection-framework.md), then [Model selection matrix](comparisons/model-selection-matrix.md) |
| Assessing whether a published score means anything | [09. Benchmarking](09-benchmarking.md), then [Benchmark limitations](benchmarks/benchmark-limitations.md) |
| Budgeting an application | [15. Token economics](15-token-economics.md), then [Token cost methodology](evaluation/token-cost-methodology.md) |
| Sizing hardware for self-hosting | [17. Hardware and memory](17-hardware-and-memory.md), then [Formulas](appendices/formulas.md) |
| Quantifying environmental cost | [16. Energy use](16-energy-use.md), then [Energy methodology](evaluation/energy-methodology.md) |
| Studying architecture or training | [03. Transformer architecture](03-transformer-architecture.md) and [04. Training and post-training](04-training-and-post-training.md) |

## Interactive companion

The [cost, speed, and energy instrument](interactive/index.html) puts the review's central claim
under your own assumptions: set input, output, reasoning, and acceptance-rate values and watch cost
per accepted task reorder the models with published rates. Four charts accompany it, each labelled
with its evidence grade.

## The three evidence grades

Every quantitative claim in this handbook carries one of three grades. The assignment rules and edge cases are in the [source quality framework](appendices/source-quality-framework.md).

| Grade | Meaning | Admits |
|---|---|---|
| **A** | Independently verified | Peer-reviewed studies, standardised academic benchmarks, reproducible third-party evaluations, independently measured system performance |
| **B** | Institutional primary research | University research reports, technical reports, model cards, benchmark methodology pages, official architecture disclosures |
| **C** | Provider-reported | Launch benchmark tables, vendor latency claims, self-reported energy claims, product documentation |

Grade C material is recorded rather than excluded, because excluding it would leave the handbook silent on most commercial models. It is labelled at the point of use and is never used alone to rank one provider above another.

## Rules the handbook applies to itself

1. No numerical claim without a citation resolving to the source register.
2. No claim about a current model without an absolute date.
3. No comparison of results produced under different or unstated evaluation conditions without a stated warning.
4. No universal energy value for any model; every energy figure carries eleven measurement conditions.
5. No estimated parameter count, price, or specification. Where the evidence does not exist, the handbook says `Not publicly disclosed` or `Insufficient independent evidence`.

## Current status

**Phase 2 is under way.** Thirteen chapters are written from registered sources, and the data layer holds 41 sources, 18 models, 8 price schedules, 14 context-window records, and 9 benchmark results, all generated into the comparison tables.

Three datasets are deliberately empty. Energy, latency, and factuality results were located but do not state the conditions this handbook requires before a figure may be published, so the findings appear in prose with their assumptions attached and the dataset rows wait. Those absences are recorded in [21. Research gaps](21-research-gaps.md).

Model profiles remain unwritten, and every bibliography entry is pending verification against the published record. Each file states its own status at the top.

## Project documents

- [Research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md)
- [Data sources and verification queue](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/data-sources.md)
- [Limitations](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/limitations.md)
- [Glossary](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/glossary.md)
- [Contributing](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CONTRIBUTING.md)

## Disclaimer

Benchmark rankings, arena positions, API prices, rate limits, context windows, and model availability change without notice. Every such value here is a historical record of what a named source stated on a named date, not a statement about the present. Verify against current provider documentation before any procurement, budgeting, or deployment decision. Nothing here is legal, financial, or procurement advice.
