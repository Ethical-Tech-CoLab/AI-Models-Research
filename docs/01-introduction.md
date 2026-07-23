# Introduction

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

This chapter states the problem the handbook addresses, defines its audience, and explains how to read the rest of it.

## 1. The problem is evidentiary before it is technical

Public discussion of model capability mixes three kinds of claim that differ in reliability: independently verified measurement, institutional disclosure, and provider marketing. They are routinely presented in the same table, with the same number of decimal places, as though they were the same kind of fact.

They are not. A provider's launch table is produced by the party that benefits from the result, under conditions the provider chose and usually did not disclose. A benchmark maintainer's evaluation is produced under a published protocol by a party with no stake in which model wins. Both are useful. Treating them as interchangeable is what produces confident rankings that do not survive contact with a real workload.

This handbook separates them, records every quantitative value with its evaluation conditions and its date, and generates every comparison table from a machine-readable data layer so that no figure can appear without a source behind it.

## 2. There is no universally best model

Selection is a constrained optimisation across verified task quality, factual reliability, latency, throughput, token consumption, energy per accepted output, privacy, controllability, and total deployment cost. The frontier moved from a single scale race toward competition on several of those axes at once, and different axes have different leaders.

The decision problem this handbook serves has three inputs: a defined task, a defined budget, and a defined deployment constraint. Given those, it can tell you what has been measured, under what conditions, and by whom. It cannot tell you which model to pick, because whether a benchmark result transfers to your task is an empirical question about your task.

## 3. Audience and reading paths

| If you are | Start at |
|---|---|
| Selecting a model for a task | [20. Model selection framework](20-model-selection-framework.md) |
| Assessing whether a published score means anything | [09. Benchmarking](09-benchmarking.md) |
| Budgeting an application | [15. Token economics](15-token-economics.md) |
| Sizing hardware for self-hosting | [17. Hardware and memory](17-hardware-and-memory.md) |
| Quantifying environmental cost | [16. Energy use](16-energy-use.md) |
| Assessing factual reliability | [10. Factuality and hallucination](10-factuality-and-hallucination.md) |

## 4. Method in one paragraph

Evidence enters through a source register, is graded A, B, or C, and is extracted into machine-readable datasets before any prose cites it. Comparison tables are generated from those datasets rather than written by hand. Results produced under different or unstated evaluation conditions are never placed in the same ranked column. Where the evidence does not exist, the text says `Not publicly disclosed` or `Insufficient independent evidence` rather than estimating. The full protocol is in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md).

## 5. What this handbook will not do

It will not rank models. It will not restate a provider claim as a finding. It will not convert a general research result into a per-model number. It will not publish a figure whose conditions it cannot state. Several chapters therefore report an empty dataset, and those absences are findings about the state of public disclosure rather than gaps in the collection.
