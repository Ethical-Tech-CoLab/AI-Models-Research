# Model selection framework

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Converts the handbook into a procedure. Given a task specification, a quality bar, a latency budget, a cost ceiling, and a deployment constraint, the framework produces a shortlist and an evaluation plan rather than a ranking. It is explicitly a procedure for the reader to run, not a recommendation, because construct validity cannot be established on the reader's behalf.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The selection cascade: constraints first, capability second, cost third.
- The argument that a shortlist plus a local evaluation beats any published ranking for a specific task.
- The definition of the acceptance criterion that makes cost per accepted task computable.

## Developed elsewhere

- Running the evaluation: [evaluation/internal-bakeoff.md](evaluation/internal-bakeoff.md)
- Cost arithmetic: [15-token-economics.md](15-token-economics.md)
- The generated selection matrix: [comparisons/model-selection-matrix.md](comparisons/model-selection-matrix.md)

## Research checklist

- [ ] Write the cascade as an ordered decision procedure with explicit stopping conditions.
- [ ] Add the Mermaid diagram of the model selection cascade.
- [ ] Provide a worked example for at least three task classes, using stated assumptions and labelled as illustrative.
- [ ] Confirm the framework never outputs a single recommended model without a stated task and evaluation.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
