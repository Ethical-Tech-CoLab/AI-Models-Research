# Long context

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Separates advertised context length from measured usable context. Covers the methods that extend context, the retrieval and position effects that degrade performance well before the advertised limit, and the evaluation designs that detect that degradation. Answers research question RQ6. Hosts the generated table comparing advertised context against independently measured effective context.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The definition of effective context and the criteria for measuring it.
- The argument that advertised context length is a specification, not a capability claim.
- The relationship between context length, KV cache memory, and cost.

## Developed elsewhere

- Long-context benchmark construction: [benchmarks/long-context.md](benchmarks/long-context.md)
- KV cache arithmetic: [17-hardware-and-memory.md](17-hardware-and-memory.md)
- Compaction cost in agent loops: [07-agentic-ai.md](07-agentic-ai.md)

## Research checklist

- [ ] Cite the position-effect literature for degradation within a nominally supported window.
- [ ] Record advertised context and advertised maximum output per model in data/context-windows.csv, with a source and date.
- [ ] Record independently measured effective context where a Grade A evaluation exists; otherwise record 'Insufficient independent evidence'.
- [ ] State the measurement threshold used for every effective-context figure, since the figure is meaningless without one.
- [ ] Regenerate the context-window table with scripts/generate_model_tables.py.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.

## Generated table

Generated from the data layer by `scripts/generate_model_tables.py`. Do not edit the region by hand; change the source CSV and rerun the generator.

<!-- BEGIN GENERATED: context-windows -->
| Model | Advertised context | Advertised max output | Measured effective context | Measurement benchmark | Threshold | Evidence grade | Source date |
|---|---|---|---|---|---|---|---|
| _No rows. Populate the source dataset in data/ and rerun scripts/generate_model_tables.py_ | | | | | | | |
<!-- END GENERATED: context-windows -->
