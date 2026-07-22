# Quality metrics

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Defines the quality measures used in the bakeoff and in this repository's own records: exact match, pass at k, resolved rate, rubric scoring, pairwise preference, and model-judged scoring, with the failure mode and bias of each. Defines the acceptance criterion that makes cost per accepted task computable.

## Research checklist

- [ ] Define each metric formally and state what it rewards and what it ignores.
- [ ] Cite evidence on judge-model bias, including position and verbosity effects, rather than asserting them.
- [ ] Define inter-rater agreement requirements for human scoring and cite the agreement statistic used.
- [ ] Define the acceptance criterion precisely enough that two teams applying it to the same outputs would agree.

## Completion criteria

This file is complete when every checklist item above is closed and the quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
