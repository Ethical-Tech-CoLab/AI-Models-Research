# Foundation models

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Defines the object of study. Sets out what distinguishes a foundation model from earlier task-specific models, traces the shift from task-specific supervised learning to pretraining followed by adaptation, and establishes the vocabulary used throughout: base model, instruction-tuned model, reasoning model, and served endpoint. Establishes that a served endpoint is not the same object as a set of weights, which is the distinction that makes most reproducibility problems in this field intelligible.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The definition of a foundation model used in this handbook, and its boundary conditions.
- The distinction between weights, a checkpoint, a served endpoint, and a product name.
- The taxonomy of base, instruction-tuned, reasoning, and multimodal variants within a family.

## Developed elsewhere

- Architectural mechanisms: [03-transformer-architecture.md](03-transformer-architecture.md)
- Training procedures: [04-training-and-post-training.md](04-training-and-post-training.md)
- Licensing and openness: [18-open-vs-closed-models.md](18-open-vs-closed-models.md)

## Research checklist

- [ ] Source the definitional treatment from the foundation-model literature and cite it rather than paraphrasing a definition into existence.
- [ ] Establish the endpoint-versus-weights distinction with a documented case of an endpoint changing behaviour without a model identifier change, or record that no such documented case was found.
- [ ] Confirm the taxonomy covers every variant type present across the sixteen profiled families.
- [ ] Add the Mermaid diagram of the pretraining-to-deployment lifecycle.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
