# Hardware and memory

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Covers the physical constraints on serving a model: accelerator memory capacity and bandwidth, interconnect, host requirements, and the arithmetic that converts a parameter count and a context length into a hardware requirement. Covers quantization as a memory strategy and its measured accuracy cost. Answers research question RQ10 for open-weight models and records the unobservability of the same quantities for closed-weight models.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The memory formulas: weight memory, KV cache memory, and total requirement.
- The argument that memory bandwidth, not arithmetic throughput, bounds decoding.
- The quantization accuracy-versus-memory trade-off as a measured relationship.

## Developed elsewhere

- Architectural sources of memory cost: [03-transformer-architecture.md](03-transformer-architecture.md)
- Energy per unit of work: [16-energy-use.md](16-energy-use.md)
- Self-hosting cost accounting: [15-token-economics.md](15-token-economics.md)

## Research checklist

- [ ] Verify the memory formulas against scripts/estimate_memory.py and state that the script is the reference implementation.
- [ ] Record accelerator specifications from vendor documentation, graded B, with access dates.
- [ ] Cite Grade A measurements of quantization accuracy cost; do not assert that a quantization format is lossless without a measurement.
- [ ] Record hardware requirements only for models whose parameter counts are disclosed; record 'Not publicly disclosed' otherwise and do not estimate.
- [ ] State the precision assumed in every hardware requirement figure.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
