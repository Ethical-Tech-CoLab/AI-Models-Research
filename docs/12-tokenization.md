# Tokenization

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Explains how text and other modalities become tokens, and why that mapping is a cost and equity issue rather than an implementation detail. Covers byte-pair encoding, unigram and sentencepiece methods, byte-level fallback, vocabulary size trade-offs, and the systematically higher token counts that non-English and non-Latin-script text incurs. Enumerates every token class that a caller pays for: input, cached, output, reasoning, image, audio, video, tool-call, and compaction tokens. Answers research question RQ7.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- Definitions of every billable token class used in the cost formulas.
- The multilingual token-inequality argument and its cost consequence.
- The argument that token counts are not comparable across tokenizers, and therefore neither are per-token prices without a token-count measurement.

## Developed elsewhere

- Cost formulas: [15-token-economics.md](15-token-economics.md)
- Multilingual benchmark coverage: [benchmarks/multilingual.md](benchmarks/multilingual.md)
- Modality token accounting: [08-multimodal-models.md](08-multimodal-models.md)

## Research checklist

- [ ] Cite the primary sources for byte-pair encoding and for sentencepiece.
- [ ] Record the tokenizer used by each profiled family where it is disclosed.
- [ ] Locate a Grade A source measuring token count for equivalent text across languages under a named tokenizer; record the exact corpus and tokenizer.
- [ ] Confirm that every token class enumerated here appears in the cost formulas and in scripts/calculate_token_costs.py.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
