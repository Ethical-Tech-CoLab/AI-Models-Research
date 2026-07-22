# Inference

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Covers what happens between a request and a response: prefill and decode, decoding strategies and their effect on reproducibility, batching policy, prefix and prompt caching, speculative decoding, quantization at serving time, and retrieval augmentation as an inference-time architecture. Explains why the serving stack, not the weights alone, determines observed behaviour.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The prefill and decode decomposition, and the different resources each is bound by.
- The argument that identical weights served by two stacks are not the same system.
- The reproducibility consequences of sampling parameters and non-deterministic kernels.

## Developed elsewhere

- Latency measurement: [14-latency-and-throughput.md](14-latency-and-throughput.md)
- Architecture of the caching and decoding mechanisms: [03-transformer-architecture.md](03-transformer-architecture.md)
- Memory sizing: [17-hardware-and-memory.md](17-hardware-and-memory.md)

## Research checklist

- [ ] Cite the primary sources for paged attention, speculative decoding, and the quantization methods discussed.
- [ ] State the reproducibility conditions required for any evaluation run reported in this repository, and cross-reference evaluation/reproducibility.md.
- [ ] Record which profiled providers document prompt caching, its granularity, and its retention period, with sources.
- [ ] Add Mermaid diagrams of the inference pipeline and of retrieval augmentation.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
