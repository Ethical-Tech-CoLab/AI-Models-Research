# Tokenization

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

This chapter explains how text and other modalities become tokens, and why that mapping is a cost and equity issue rather than an implementation detail. It answers research question RQ7.

Developed elsewhere: the cost formulas in [15. Token economics](15-token-economics.md); language coverage in [multilingual benchmarks](benchmarks/multilingual.md); modality accounting in [08. Multimodal models](08-multimodal-models.md).

## 1. Tokens are not words

A token is produced by a model-specific tokenizer. English prose averages several characters per token, but the ratio varies with vocabulary, code, numerals, symbols, and language. The same sentence yields different counts across providers.

This has a direct economic consequence. A language fragmented into more tokens costs more to process, occupies more of the context window for the same meaning, and takes longer to generate. The penalty falls hardest on languages least represented in tokenizer training, which is the opposite of an equitable distribution.

Tokenizer changes also move cost without moving price. Anthropic states that Claude Sonnet 5 uses a tokenizer that can produce about 30 percent more tokens for the same text than its predecessor, so an unchanged per-token rate still raises the cost of an equivalent request.[^anthropic2026sonnet] That is developed as a pricing argument in [15. Token economics](15-token-economics.md) and appears here only as the mechanism.

## 2. Every billable class

A pricing table listing text tokens alone does not reveal the cost of a real workload. The classes a caller pays for are enumerated in [15. Token economics](15-token-economics.md), and the ones specific to tokenizer design are these:

- **Input** covers everything placed in the context, including tool definitions and retrieved evidence, not only the user's message.
- **Reasoning** tokens are produced by the same tokenizer and billed at output rates where they are billed at all, so tokenizer inefficiency compounds with reasoning length.
- **Image, audio, and video** inputs are converted to billable units by provider-specific rules. Those rules were not extracted for this revision and are recorded as not publicly disclosed in `data/models.csv`.
- **Compaction** tokens are generated when a long history is summarised, and are therefore subject to the same per-language penalty as the original text.

## 3. What this repository records

`data/models.csv` records the tokenizer field as not publicly disclosed for most models in this survey, because the sources used did not name one. That is itself a finding: a caller cannot compute the cost of their own corpus without knowing which tokenizer will be applied to it, and most providers do not say.

No token-count measurement across languages has been performed for this survey. Any claim about multilingual cost inequity in this handbook is therefore a claim about the mechanism, supported by the tokenizer literature, and not a measured per-provider figure.

## 4. Open research questions

- What is the token count for one fixed multilingual corpus under each provider's tokenizer?
- How much of the published price spread between providers survives normalisation by token count for equivalent meaning?
- Do providers publish a token counting tool, and does it agree with billed usage?
- What are the per-modality conversion rules, and how do they compare across providers for the same document?

## Sources

[^anthropic2026sonnet]: Anthropic (2026). Claude Sonnet 5 documentation and pricing notes. Claude Platform Documentation. Grade B, official documentation of the provider's own commercial terms. Accessed 2026-07-22.
