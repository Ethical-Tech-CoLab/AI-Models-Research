# Scaling laws

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Sets out the empirical relationships between compute, data, parameters, and loss, and the limits of extrapolating from them. Covers the original power-law formulations, the compute-optimal revision, the shift of marginal compute from pretraining toward post-training and inference, and the data-availability constraint. Distinguishes scaling of loss, which is well characterised, from scaling of downstream capability, which is not.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The formal statement of the scaling relationships and their fitted forms.
- The argument that loss scaling and capability scaling are different claims with different evidence.
- The compute-allocation argument between pretraining, post-training, and inference-time compute.

## Developed elsewhere

- Test-time compute in practice: [06-reasoning-models.md](06-reasoning-models.md)
- Energy consequences of training compute: [16-energy-use.md](16-energy-use.md)

## Research checklist

- [ ] Cite both the original and the compute-optimal scaling results, and state the conditions under which each was fitted.
- [ ] Record training compute for every profiled model where it is disclosed, and 'Not publicly disclosed' where it is not; do not infer it.
- [ ] Cite the data-availability projection literature and state its assumptions explicitly rather than reporting its headline figure.
- [ ] State clearly which claims in this chapter are extrapolations and mark their uncertainty in the sentence that carries them.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
