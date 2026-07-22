# Agentic AI

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Covers models used inside action loops: tool calling, planning, multi-step execution, computer use, and multi-agent arrangements. Distinguishes the model's contribution from the scaffold's, which is the central measurement problem in this area, since published agent results are properties of a model-and-scaffold pair. Answers research question RQ5 on the predictive value of agentic benchmarks for deployed reliability.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The definition of an agent used in this handbook and the scaffold boundary.
- The argument that agent benchmark results are not attributable to a model alone.
- The failure taxonomy for long-horizon execution: error compounding, context exhaustion, and unrecoverable tool states.

## Developed elsewhere

- Agent benchmark construction: [benchmarks/agents-and-computer-use.md](benchmarks/agents-and-computer-use.md)
- Context exhaustion and compaction: [11-long-context.md](11-long-context.md)
- Tool-call token cost: [15-token-economics.md](15-token-economics.md)

## Research checklist

- [ ] Cite the primary sources for the tool-use and reasoning-and-acting formulations.
- [ ] For every agent benchmark result recorded, capture the scaffold description in the notes field; results with no scaffold description are marked unstated.
- [ ] Locate evidence on the relationship between per-step accuracy and end-to-end task success at increasing step counts, or record the gap.
- [ ] Add the Mermaid diagram of the agent loop.
- [ ] State whether any Grade A evidence links agent benchmark performance to deployed reliability; if none exists, say so in the chapter, not only in the limitations.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
