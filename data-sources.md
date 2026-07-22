# Data sources

> **Research cut-off date: 2026-07-22.**

This document is the register of where evidence comes from, how each source is recorded, and which sources remain unverified. It is the companion to [research-methodology.md](research-methodology.md), which defines how sources are graded and used.

## 1. The source register

`data/sources.csv` is the single register of every source cited anywhere in the repository. No other file may introduce a source. A footnote in a chapter, a `source_id` in a dataset row, and a citation key in [references.bib](references.bib) all resolve to the same register row.

### 1.1 Required fields

Every row carries all fourteen fields. An empty field is a validation error, not a missing value; use the reserved strings in section 1.2 instead.

| Field | Type | Rule |
|---|---|---|
| `source_id` | string | Lowercase, `author + year + keyword`, for example `hoffmann2022training`. Must equal the BibTeX citation key. Unique across the register. |
| `title` | string | Verbatim from the source, including subtitle. |
| `authors` | string | `Family, Given; Family, Given` order as printed. `Organisation name` where the author is corporate. |
| `organization` | string | The institution or company responsible for the work. |
| `publication` | string | Venue, journal, conference, or the document series. `Web` for provider documentation. |
| `year` | integer | Four digits. |
| `publication_date` | date | `YYYY-MM-DD`. Where only a month is published, use the first day and record the imprecision in `notes`. |
| `source_type` | enum | One of: `peer_reviewed`, `preprint`, `technical_report`, `model_card`, `benchmark_methodology`, `dataset`, `documentation`, `pricing_page`, `license`, `standards_body`, `government_report`, `institutional_report`. |
| `peer_reviewed` | boolean | `true` or `false`. A preprint later published is `true` once the published version is the cited one. |
| `evidence_grade` | enum | `A`, `B`, or `C` per [research-methodology.md](research-methodology.md#4-evidence-grading). |
| `url` | string | Direct link to the source. Must resolve. |
| `doi` | string | Preferred over `url` where one exists. `Not available` where none is issued. |
| `access_date` | date | `YYYY-MM-DD` on which a contributor confirmed the URL resolved and the content matched the record. |
| `notes` | string | Preprint identifier of a published paper; conflicts with other sources; `superseded_by:<source_id>`; imprecision in dates; verification status. |

### 1.2 Reserved values

| String | Meaning |
|---|---|
| `Not publicly disclosed` | The responsible organisation has not published the value. |
| `Insufficient independent evidence` | A value is claimed but no Grade A or Grade B source establishes it. |
| `unstated` | An evaluation condition that the source did not report. |
| `Not available` | The field does not apply, for example a DOI for a pricing page. |

These strings are checked literally by `scripts/validate_sources.py`. Variants such as "N/A", "unknown", or an empty cell fail validation.

## 2. Source priority

Sources are drawn in the tier order defined in [research-methodology.md](research-methodology.md#21-priority-tiers). The named starting points below are the standing sources for this survey. Each is checked at the start of each research phase and its access date recorded per use, not once per publication.

### 2.1 Cross-cutting evidence aggregators

| Source | Organisation | Used for | Expected grade |
|---|---|---|---|
| AI Index Report | Stanford Institute for Human-Centered AI | Field-level trends in capability, compute, cost, and investment | B |
| HELM and MedHELM | Stanford Center for Research on Foundation Models | Standardised multi-scenario evaluation under a disclosed harness | A |
| Foundation Model Transparency Index | Stanford Center for Research on Foundation Models | Disclosure practices per provider | A |
| FACTS | Google DeepMind | Grounded factuality evaluation | B |
| Electricity and data-centre reporting | International Energy Agency | Sector-level electricity demand and grid carbon intensity | B |

### 2.2 Archival and peer-reviewed venues

ACL Anthology; NeurIPS; ICML; ICLR; EMNLP; USENIX; ACM Digital Library; IEEE Xplore; Google Scholar as an index rather than a source. arXiv is used only where no peer-reviewed version exists, and the preprint identifier is retained when a published version supersedes it.

### 2.3 Institutional research

Stanford, MIT, Harvard, NYU, Princeton, Carnegie Mellon, UC Berkeley, Oxford, and Cambridge; Google DeepMind; Microsoft Research; Meta AI; Anthropic; OpenAI; Mistral; Hugging Face.

### 2.4 Provider documentation

For each of the sixteen model families in [README.md](README.md#6-model-families-covered): the official model card, the API reference, the pricing page, the licence text, the official GitHub organisation, and the official Hugging Face organisation. These are the authoritative record of commercial terms and are Grade B for terms and Grade C for performance claims.

## 3. What is recorded where

| Dataset | Records | Keyed by |
|---|---|---|
| `data/models.csv` | Model identity, provider, release and deprecation dates, architecture family, parameter counts, modalities, licence, deployment options | `model_id` |
| `data/benchmarks.csv` | One row per model, per benchmark, per reported result, with harness, sampling policy, and tool permissions | `model_id` + `benchmark_id` + `source_id` |
| `data/pricing.csv` | Input, cached-input, output, and batch prices in USD per million tokens, with effective date | `model_id` + `effective_date` |
| `data/context-windows.csv` | Advertised context window, advertised maximum output, and any independently measured effective context | `model_id` + `source_id` |
| `data/energy-studies.csv` | One row per published energy measurement, with all eleven required conditions | `study_id` |
| `data/sources.csv` | The source register described in section 1 | `source_id` |

JSON Schemas for `models`, `benchmarks`, and `sources` are in [data/schema/](data/schema/). They are the machine-readable statement of the rules in this document and are enforced by `scripts/validate_sources.py` and `scripts/validate_tables.py`.

## 4. Seed bibliography

[references.bib](references.bib) contains a Phase 1 seed of foundational and methodological literature, organised into twelve sections: architecture; scaling and training; reasoning and agents; benchmarks and evaluation methodology; factuality and hallucination; multimodal and agentic benchmarks; long context; tokenization; inference, serving, and quantization; energy, carbon, and environmental cost; security and privacy; and model technical reports.

The seed deliberately contains no benchmark results, no prices, no parameter counts, and no context-window figures. Those values enter the repository only through `data/*.csv`, where they carry an evidence grade, an access date, and the evaluation conditions under which they were produced. A paper in the seed bibliography is a source for a *method* or a *finding about methods*, not a shortcut around the data layer.

## 5. Verification queue

**Status at 2026-07-22: every entry in [references.bib](references.bib) is unverified, and `data/sources.csv` contains headers only.**

The seed bibliography was compiled from working knowledge of the literature. Titles, venues, years, and preprint identifiers are recorded as an aid to retrieval, and each one must be confirmed against the published record before it may be cited in prose. This is not a formality: a transposed preprint identifier or a misattributed venue is exactly the class of error that a survey of this kind must not propagate.

### 5.1 Verification procedure

For each entry in `references.bib`, in the order the chapters need them:

1. Retrieve the record from the publisher, the ACL Anthology, the proceedings site, or arXiv.
2. Confirm the title verbatim, the full author list, the venue, the year, and the identifier.
3. Replace `and others` with the full author list taken from the published record. Do not expand it from memory.
4. Add the `doi` field where a DOI is issued.
5. Where a peer-reviewed version exists for an entry currently recorded as a preprint, change the entry type to the published version and move the preprint identifier to `note`.
6. Create the matching row in `data/sources.csv` with all fourteen fields, including `access_date` and `evidence_grade`.
7. Run `python scripts/validate_sources.py`.

An entry is verified only when its `data/sources.csv` row exists and validation passes. Until then, `scripts/validate_sources.py --check-citations` will fail any chapter that cites it.

### 5.2 Outstanding source acquisitions

Sources known to be required by Phase 2 and Phase 3 that are not yet in the seed bibliography. Each must be located, verified, and registered before the chapter that depends on it can be completed.

| # | Required source | Needed by | Notes |
|---|---|---|---|
| 1 | Current edition of the Stanford AI Index | Chapters 02, 05, 15, 16 | Cite the specific edition and chapter, not the report generally |
| 2 | HELM leaderboard methodology and current results export | Chapters 09, benchmarks/, comparisons/ | Record the harness version alongside every extracted score |
| 3 | Foundation Model Transparency Index, current edition | Chapters 18, 19 | Per-provider disclosure scores |
| 4 | Google DeepMind FACTS methodology and results | benchmarks/factuality.md | Confirm whether current results are independently reproducible |
| 5 | Humanity's Last Exam construction paper and leaderboard | benchmarks/knowledge-and-reasoning.md | Confirm scoring and tool policy |
| 6 | ARC-AGI-1, ARC-AGI-2, and ARC-AGI-3 specifications and rules | benchmarks/knowledge-and-reasoning.md | Confirm which versions exist and are public at the cut-off date; verify prize-competition compute limits |
| 7 | FrontierMath construction and access policy | benchmarks/knowledge-and-reasoning.md | Held-out problem set; confirm what is disclosed about evaluation independence |
| 8 | SWE-Bench Verified and SWE-Bench Pro definitions | benchmarks/coding.md | Confirm provenance and how each differs from the original SWE-bench |
| 9 | Terminal-Bench specification | benchmarks/coding.md | Confirm maintainer and scoring |
| 10 | BrowseComp specification | benchmarks/agents-and-computer-use.md | Confirm task construction and tool permissions |
| 11 | Berkeley Function Calling Leaderboard methodology | benchmarks/agents-and-computer-use.md | UC Berkeley; confirm current version and scoring |
| 12 | ToolBench paper and repository | benchmarks/agents-and-computer-use.md | Confirm which of several similarly named artefacts is intended |
| 13 | MMMU-Pro paper | benchmarks/multimodal.md | Distinct from MMMU |
| 14 | DocVQA and ChartQA papers | benchmarks/multimodal.md | Both predate the current model generation |
| 15 | Video-MME paper | benchmarks/multimodal.md | Confirm exact name and evaluation protocol |
| 16 | LongCodeBench specification | benchmarks/long-context.md | Confirm existence, maintainer, and scoring at the cut-off date |
| 17 | MRCR specification | benchmarks/long-context.md | Multi-round coreference resolution; confirm originating organisation |
| 18 | Needle-in-a-Haystack original protocol | benchmarks/long-context.md | Originates outside the peer-reviewed literature; grade accordingly |
| 19 | SimpleQA paper | benchmarks/factuality.md | Confirm identifier and whether an independent evaluation exists |
| 20 | HalluHard specification | benchmarks/factuality.md | Confirm existence and maintainer; do not assume from name similarity to HaluEval |
| 21 | MedHELM methodology | benchmarks/benchmark-overview.md | Domain-specific extension of HELM |
| 22 | Model card, API reference, pricing page, and licence for each of the sixteen families | All of docs/model-profiles/ | Sixteen sets, each with its own access date |
| 23 | Independent third-party latency and throughput measurements | Chapter 14, evaluation/latency-methodology.md | Grade A only where methodology is disclosed and reproducible |
| 24 | Peer-reviewed inference-energy measurements post-2024 | Chapter 16 | Existing literature is dominated by training energy; inference measurement is sparser |
| 25 | Grid carbon-intensity data for the regions in which the compared APIs are served | Chapter 16 | International Energy Agency and national grid operators |
| 26 | Water-consumption methodology for data-centre cooling | Chapter 16 | Confirm whether any provider publishes model-level or region-level figures |
| 27 | Accelerator specifications for the hardware referenced in Chapter 17 | Chapter 17 | Vendor documentation, Grade B for specifications |
| 28 | Data-retention and training-use terms for each commercial API | Chapter 19 | Dated snapshots; these terms change without notice |

### 5.3 Known gaps that verification will not close

The following are expected to remain unresolved and will be recorded in [limitations.md](limitations.md) rather than filled with estimates.

1. Parameter counts, active parameter counts, and architecture details for closed-weight models where the provider has not disclosed them.
2. Energy per token for any model served only through a commercial API, because the serving hardware, batch size, and utilisation are not observable by the caller.
3. Training compute and training energy for models whose providers publish no technical report.
4. Training-data composition for nearly all commercial models, which prevents any direct assessment of benchmark contamination.
5. The evaluation harness and sampling policy behind most provider-reported benchmark tables.

## 6. Source-correction process

Errors in the register are reported through the [source correction issue template](.github/ISSUE_TEMPLATE/source-correction.md). A correction that changes a number, a grade, or a conclusion is recorded in [CHANGELOG.md](CHANGELOG.md) with the date and the superseded value. Superseded rows are retained in the CSV with `superseded_by:<source_id>` in `notes`, because a claim about a past date remains true for that date.
