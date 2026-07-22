# Multimodal models

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Covers models that accept or produce more than text: image, document, audio, and video input, and the tokenization and cost consequences of each. Explains how non-text input is converted to tokens, why image and video token accounting differs between providers, and what multimodal benchmarks do and do not establish.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The mechanism by which non-text modalities enter the context, and its cost consequences.
- The argument that modality support is not a binary property: a model may accept a modality without performing well on it.
- Per-modality accounting rules used when computing cost in chapter 15.

## Developed elsewhere

- Multimodal benchmark construction: [benchmarks/multimodal.md](benchmarks/multimodal.md)
- Token accounting: [12-tokenization.md](12-tokenization.md)
- Cost formulas: [15-token-economics.md](15-token-economics.md)

## Research checklist

- [ ] Record, per family, the accepted input modalities and the produced output modalities, from the official model card, with a date.
- [ ] Record the image, audio, and video token accounting rule per provider, with a source; mark 'Not publicly disclosed' where the rule is not published.
- [ ] Cite the construction papers for the multimodal benchmarks documented in this repository.
- [ ] Establish whether independent multimodal evaluations exist for the profiled closed-weight models, or record the gap.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
