# Open versus closed models

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Examines the difference between downloadable weights and API-only access along the dimensions that matter for research and for deployment: licensing terms and their restrictions, reproducibility, auditability, disclosure practice, deployment control, and long-term availability. Answers research question RQ11. Treats openness as a spectrum of disclosed artefacts rather than a binary.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The disclosure spectrum: weights, training data, training code, evaluation code, and licence terms as separable artefacts.
- The argument that open weights and open source are different claims.
- The reproducibility asymmetry and its effect on the evidence base.

## Developed elsewhere

- Consequences for evidence availability: [https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/limitations.md](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/limitations.md)
- Privacy and data retention: [19-security-and-privacy.md](19-security-and-privacy.md)
- Selection consequences: [20-model-selection-framework.md](20-model-selection-framework.md)

## Research checklist

- [ ] Record the exact licence and its restrictions for every open-weight model profiled, with a link to the licence text.
- [ ] Cite the transparency-index literature for disclosure practice, using the specific edition and its per-provider scores.
- [ ] Record deprecation and retirement policy per provider, with a source, since long-term availability is a selection criterion.
- [ ] Avoid restating the verification-asymmetry argument that the limitations document owns; link to it.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
