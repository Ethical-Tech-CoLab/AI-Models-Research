# Training and post-training

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Explains how a foundation model is produced and then shaped. Covers pretraining, data curation, supervised fine-tuning, instruction tuning, and the preference and reinforcement methods that follow: reinforcement learning from human feedback, reinforcement learning from AI feedback, direct preference optimization, proximal policy optimization, group relative policy optimization, rejection sampling, process and outcome supervision, and reinforcement learning with verifiable rewards. Covers synthetic data, curriculum learning, and the role of test-time compute as a post-training design choice rather than an inference detail.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- Definitions and objective functions for each preference and reinforcement method.
- The distinction between process supervision and outcome supervision, and what each rewards.
- The argument that post-training choices, not pretraining scale alone, account for much of the observed difference between similarly sized models.
- The evidentiary problem created by undisclosed training data.

## Developed elsewhere

- Compute-optimal allocation: [05-scaling-laws.md](05-scaling-laws.md)
- Test-time compute as a measured capability: [06-reasoning-models.md](06-reasoning-models.md)
- Contamination as a benchmark problem: [09-benchmarking.md](09-benchmarking.md)

## Research checklist

- [ ] Cite the primary source for each named method and state its objective precisely.
- [ ] Record, for each of the sixteen families, whether the post-training recipe is disclosed, partially disclosed, or not disclosed, with a source per family.
- [ ] Establish with a Grade A or B source that reinforcement learning with verifiable rewards is distinguishable in effect from preference-only tuning, or record that the evidence is insufficient.
- [ ] Add the Mermaid diagram of the training pipeline.
- [ ] Verify that the argument about undisclosed data is developed here and only referenced, not restated, in chapters 09 and 18.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
