# Factuality and hallucination

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Distinguishes the several distinct phenomena that the word hallucination is used for: unsupported generation in a grounded setting, incorrect recall in a closed-book setting, fabricated citations and identifiers, and confident assertion under uncertainty. Explains how each is measured, why measured rates are not comparable across those settings, and what calibration and abstention contribute. Answers research question RQ3.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The taxonomy of hallucination phenomena and the measurement appropriate to each.
- The argument that a single hallucination rate for a model is not a well-defined quantity.
- The treatment of abstention and calibration as measured behaviours rather than as model virtues.

## Developed elsewhere

- Factuality benchmark construction: [benchmarks/factuality.md](benchmarks/factuality.md)
- Retrieval as a mitigation: [13-inference.md](13-inference.md)
- Suitability of factuality scores for procurement: [20-model-selection-framework.md](20-model-selection-framework.md)

## Research checklist

- [ ] Cite the primary construction sources for each factuality benchmark documented here.
- [ ] Establish whether grounded and closed-book hallucination rates for the same model are reported anywhere under compatible conditions; record the answer either way.
- [ ] Record whether each profiled family publishes an abstention or calibration measurement, with a source.
- [ ] State the conditions under which a reported hallucination rate may be compared across families, and enforce them in the comparison tables.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
