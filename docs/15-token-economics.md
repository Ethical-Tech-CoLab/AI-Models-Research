# Token economics

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Converts prices into costs. Defines the billable token classes, the cache and batch discount structures, and the formulas for total API cost, effective tokens per task, cache savings, reasoning overhead, and cost per accepted task. Answers research question RQ8 by showing that ranking models on advertised price per million tokens is not a ranking on cost. Hosts the generated pricing table.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The five cost formulas and their required inputs.
- The cost-per-accepted-task argument, including the acceptance rate as a first-class term.
- The treatment of self-hosting cost as a different accounting problem from API cost.

## Developed elsewhere

- Token classes: [12-tokenization.md](12-tokenization.md)
- Reasoning token volumes: [06-reasoning-models.md](06-reasoning-models.md)
- Hardware cost of self-hosting: [17-hardware-and-memory.md](17-hardware-and-memory.md)
- Measurement protocol: [evaluation/token-cost-methodology.md](evaluation/token-cost-methodology.md)

## Research checklist

- [ ] Populate data/pricing.csv for every profiled model from the official pricing page, with an effective date and an access date.
- [ ] Record whether reasoning tokens are billed, and at which rate, per provider.
- [ ] Record cache discount structure and batch discount per provider, with the conditions attached to each.
- [ ] Verify every formula against its implementation in scripts/calculate_token_costs.py, and state that the script is the reference implementation.
- [ ] Regenerate the pricing table with scripts/generate_model_tables.py.
- [ ] State the price volatility disclaimer in the chapter, not only in the README.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.

## Generated table

Generated from the data layer by `scripts/generate_model_tables.py`. Do not edit the region by hand; change the source CSV and rerun the generator.

<!-- BEGIN GENERATED: pricing-table -->
| Model | Provider | Currency | Input / 1M | Cached input / 1M | Output / 1M | Reasoning tokens billed | Batch discount % | Effective date | Region | Evidence grade |
|---|---|---|---|---|---|---|---|---|---|---|
| _No rows. Populate the source dataset in data/ and rerun scripts/generate_model_tables.py_ | | | | | | | | | | |
<!-- END GENERATED: pricing-table -->
