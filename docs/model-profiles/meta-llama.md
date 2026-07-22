# Meta Llama

> Research cut-off: 2026-07-22
> **Status: Phase 3, not yet researched.** Every section below states precisely what
> must be sourced and under what conditions it may be recorded. No specification,
> price, benchmark result, or capability claim appears in this file, because none has
> been verified. Sections are never deleted: where the evidence does not exist, the
> section will read `Not publicly disclosed` or `Insufficient independent evidence`.

**Required source set before this profile may be written**, each recorded in
`data/sources.csv` with an access date: the official model card or technical report;
the API reference; the pricing page; the licence text or terms of service; the
official code repository; and the official weights repository where the weights are
public. Independent evaluations are recorded in `data/benchmarks.csv` and referenced
here rather than restated.

## Overview

_Scope._ One paragraph identifying the family, its position in the market, and what distinguishes it. Required source: the provider's own model documentation index.

## Organization

_Scope._ The organisation that develops and serves the models, its corporate status, and its principal serving partners. Required source: official corporate and documentation pages.

## Current model lineup

_Scope._ One row per model identifier with release date and status (generally available, preview, deprecated, retired). Generated from data/models.csv. Required source: the provider's model list and deprecation policy pages.

## Architecture

_Scope._ Architecture family as disclosed, never as inferred from behaviour. Required source: technical report or model card.

## Total parameters

_Scope._ Disclosed total parameter count, or 'Not publicly disclosed'. Estimation from benchmark behaviour or inference price is prohibited.

## Active parameters

_Scope._ Disclosed parameters used per token. Equals the total for a dense model. 'Not publicly disclosed' otherwise.

## Dense or mixture-of-experts

_Scope._ The disclosed layer structure, with expert count and routing where published.

## Training and post-training

_Scope._ Pretraining scale, data description, and post-training method as disclosed. Record which elements are undisclosed rather than omitting the question.

## Modalities

_Scope._ Accepted input modalities and produced output modalities, per model identifier. Required source: model card or API reference.

## Context window

_Scope._ Advertised context length per model identifier, with a date, and any independently measured effective context, clearly separated.

## Maximum output

_Scope._ Advertised maximum output length per model identifier, with a date.

## Tokenizer

_Scope._ Tokenizer name or family where disclosed, and whether a token counting tool is published.

## Reasoning modes

_Scope._ Whether extended reasoning is unavailable, caller-selectable, always applied, or offered as a distinct model; whether traces are visible; whether reasoning tokens are billed.

## Tool use

_Scope._ Documented structured tool-calling support, including parallel calls and any constraints. Provider documentation, not measured performance.

## Agent capabilities

_Scope._ Documented agentic features such as computer use or long-horizon loops. Measured agent performance belongs in the evidence sections below.

## Coding performance

_Scope._ Recorded results on the coding benchmarks documented in this repository, each with harness, sampling policy, tool permissions, evidence grade, and date. Provider-reported results are labelled.

## Scientific reasoning

_Scope._ Recorded results on knowledge and reasoning benchmarks, under the same conditions requirement.

## Long-context performance

_Scope._ Recorded results on long-context benchmarks, with the measurement threshold stated for every effective-context figure.

## Multimodal performance

_Scope._ Recorded results on multimodal benchmarks, per modality.

## Factuality and hallucination

_Scope._ Recorded results on factuality benchmarks, with the grounding condition stated, since grounded and closed-book rates are different quantities.

## Latency

_Scope._ Recorded latency measurements with percentile, concurrency, region, prompt and output length, and date. Vendor claims are labelled provider-reported.

## Throughput

_Scope._ Recorded throughput measurements with concurrency and batching policy stated.

## Token pricing

_Scope._ Input, cached input, and output prices in USD per million tokens with an effective date, cross-referenced to data/pricing.csv.

## Caching

_Scope._ Cache mechanism, granularity, retention period, and discount, as documented.

## Batch pricing

_Scope._ Batch discount and its conditions, as documented.

## Hardware requirements

_Scope._ For open-weight models, the minimum accelerator configuration at a named precision. For API-only models, 'Not applicable'.

## Quantization

_Scope._ Published quantization formats and any measured accuracy cost. Do not assert that a format is lossless without a measurement.

## Memory footprint

_Scope._ Weight and KV cache memory at stated precision, sequence length, and batch size, computed with scripts/estimate_memory.py and labelled as an estimate.

## Energy evidence

_Scope._ Published energy measurements stating all eleven required conditions, or 'Insufficient independent evidence'. No universal per-model figure is published.

## Privacy and data retention

_Scope._ Data retention period, training-use default, opt-out mechanism, and regional processing, each as a dated snapshot with a URL.

## Licensing

_Scope._ Exact licence name, its restrictions, and a link to the licence text. For API-only models, the terms of service governing use of outputs.

## Strengths

_Scope._ Claims supported by Grade A or Grade B evidence recorded above, each naming the benchmark and conditions. No unqualified comparatives.

## Limitations

_Scope._ Documented weaknesses, with the same evidence requirement as strengths.

## Best use cases

_Scope._ Task classes for which the recorded evidence supports selection, with the evidence named. Not a recommendation absent a reader's evaluation.

## Inappropriate use cases

_Scope._ Task classes for which the recorded evidence indicates the family is unsuitable, or for which licence or privacy terms preclude use.

## Independent evidence

_Scope._ Grade A and Grade B sources for this family, listed separately from provider material so that a reader can see the independent record alone.

## Provider-reported evidence

_Scope._ Grade C sources, listed separately and labelled. Included for completeness, never used alone to rank this family against another.

## Open research questions

_Scope._ Questions this profile could not answer, and what would be required to answer them. Consolidated into chapter 21.

## Sources

_Scope._ Numbered footnote definitions, each resolving to a source_id in data/sources.csv.
