# Transformer architecture

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

The mechanical chapter. Explains the components of contemporary decoder-only models and the variants that matter for capability, memory, or throughput, with equations where an equation is clearer than prose. Covers self-attention, causal masking, multi-head, multi-query, grouped-query, sliding-window and sparse attention, positional methods, mixture-of-experts layers and expert routing, state-space and hybrid architectures, and the inference-side structures that follow from these choices: the KV cache, prefix caching, speculative decoding, continuous batching, quantization, and distillation. Each variant is presented with what it changes and what it costs, not as a chronology of papers.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- Definitions and equations for every attention variant used by profiled models.
- The argument that KV cache size, not parameter count alone, sets the binding memory constraint during serving.
- The distinction between total and active parameters, and its consequences for memory versus compute.
- Definitions of speculative decoding, continuous batching, and prefix caching as architectural facts, distinct from their measured effect.

## Developed elsewhere

- Measured throughput and latency effects: [14-latency-and-throughput.md](14-latency-and-throughput.md)
- Memory arithmetic and hardware sizing: [17-hardware-and-memory.md](17-hardware-and-memory.md)
- Serving stacks in practice: [13-inference.md](13-inference.md)

## Research checklist

- [ ] Cite the primary source for each of: multi-query attention, grouped-query attention, sliding-window attention, rotary position embedding, linear position bias, sparsely-gated mixture-of-experts, and selective state-space models.
- [ ] State the attention equation and the KV cache size equation, and cross-reference both to the appendix of formulas.
- [ ] For mixture-of-experts, document the routing mechanism and state which profiled families disclose their expert count and which do not.
- [ ] Add Mermaid diagrams for transformer flow, mixture-of-experts routing, and the KV cache.
- [ ] Confirm that no measured performance claim appears in this chapter: mechanisms here, measurements in chapters 13, 14, and 17.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
