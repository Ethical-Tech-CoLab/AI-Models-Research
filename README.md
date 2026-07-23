# AI Models: Performance, Capabilities, Accuracy, Speed, Energy Use, and Token Economics

> **Research cut-off date: 2026-07-22.**
> All statements in this repository are scoped to evidence published on or before this date. Model availability, benchmark leaderboards, and API prices change frequently. See [Disclaimer](#17-disclaimer).

A technical reference, comparative research survey, and reproducible evaluation framework covering contemporary proprietary and open-weight AI model families. Maintained by [Ethical Tech CoLab](https://github.com/Ethical-Tech-CoLab).

**Build status: Phase 1 (foundation) complete. Phases 2 to 5 are not yet written.** See [Repository status](#18-repository-status).

---

## Contents

1. [Purpose](#1-purpose)
2. [Research questions](#2-research-questions)
3. [Scope](#3-scope)
4. [Research cut-off date](#4-research-cut-off-date)
5. [Key findings](#5-key-findings)
6. [Model families covered](#6-model-families-covered)
7. [Benchmark categories covered](#7-benchmark-categories-covered)
8. [Methodology summary](#8-methodology-summary)
9. [Evidence-quality classification](#9-evidence-quality-classification)
10. [Compact comparison table](#10-compact-comparison-table)
11. [Repository navigation](#11-repository-navigation)
12. [Local installation](#12-local-installation)
13. [Building the documentation](#13-building-the-documentation)
14. [Citing this repository](#14-citing-this-repository)
15. [Contribution rules](#15-contribution-rules)
16. [Limitations](#16-limitations)
17. [Disclaimer](#17-disclaimer)
18. [Repository status](#18-repository-status)

---

## 1. Purpose

This repository exists to answer a practical question with academic rigour: given a defined task, a defined budget, and a defined deployment constraint, which AI model should be selected, and on what evidence?

Public discussion of model capability is dominated by provider launch materials and single-number leaderboard rankings. Those artefacts are frequently produced under evaluation conditions that are undisclosed, unreproducible, or not comparable across providers. This repository separates three categories of claim that are routinely conflated:

1. Independently verified measurement.
2. Institutional primary research and official technical disclosure.
3. Provider-reported marketing and product documentation.

Every quantitative claim in this repository carries a source, a date, and an evidence grade. Claims that cannot meet that standard are recorded as `Not publicly disclosed` or `Insufficient independent evidence` rather than estimated.

The repository is intended for graduate researchers, procurement and policy analysts, machine learning engineers selecting production models, and sustainability researchers quantifying the resource footprint of inference.

## 2. Research questions

The survey is organised around eleven research questions.

| ID | Research question | Primary chapters |
|---|---|---|
| RQ1 | How do contemporary model architectures differ, and which architectural choices measurably affect capability rather than efficiency alone? | [03](docs/03-transformer-architecture.md), [05](docs/05-scaling-laws.md) |
| RQ2 | To what extent do published benchmark scores predict task performance under procurement conditions? | [09](docs/09-benchmarking.md), [benchmarks/](docs/benchmarks/benchmark-limitations.md) |
| RQ3 | How is factual accuracy measured, and how comparable are hallucination rates across model families? | [10](docs/10-factuality-and-hallucination.md) |
| RQ4 | Does reasoning-mode inference improve accuracy enough to justify its token and latency cost? | [06](docs/06-reasoning-models.md), [15](docs/15-token-economics.md) |
| RQ5 | How reliable are agentic and tool-use benchmarks as predictors of deployed agent reliability? | [07](docs/07-agentic-ai.md) |
| RQ6 | Does advertised context-window length correspond to usable retrieval and reasoning performance at that length? | [11](docs/11-long-context.md) |
| RQ7 | How does tokenizer design distribute cost unevenly across languages and modalities? | [12](docs/12-tokenization.md) |
| RQ8 | What is the true cost per accepted task, as distinct from the advertised price per million tokens? | [15](docs/15-token-economics.md) |
| RQ9 | What is the energy, carbon, and water cost of inference, and what measurement conditions must accompany any such figure? | [16](docs/16-energy-use.md) |
| RQ10 | What hardware and memory conditions constrain self-hosted deployment of open-weight models? | [17](docs/17-hardware-and-memory.md) |
| RQ11 | Under what conditions do open-weight models substitute for proprietary models, and at what governance cost? | [18](docs/18-open-vs-closed-models.md), [19](docs/19-security-and-privacy.md) |

## 3. Scope

**In scope.** Text-primary foundation models and their multimodal extensions released or maintained by the model families listed in [section 6](#6-model-families-covered); benchmark methodology and its limitations; inference-time performance, cost, and energy; hardware and memory requirements for self-hosting; licensing, privacy, and data-retention terms as published; and a decision framework for model selection.

**Out of scope.** Image-only and video-only generative models; speech synthesis models; embedding and reranking models except where they appear in retrieval-augmented pipelines; fine-tuning recipes for specific downstream tasks; training-infrastructure engineering; commercial vendor negotiation; and any forecast of unreleased models.

**Boundary conditions.** The repository does not run new evaluations of proprietary models against paid APIs as part of continuous integration. The evaluation framework in [docs/evaluation/](docs/evaluation/internal-bakeoff.md) specifies a reproducible protocol that a reader may execute independently, with results contributed back as Grade A evidence.

## 4. Research cut-off date

The repository-wide research cut-off is **2026-07-22**.

Every file under [docs/model-profiles/](docs/model-profiles/), [docs/comparisons/](docs/comparisons/), and [docs/benchmarks/](docs/benchmarks/) carries its own cut-off line in a blockquote immediately below the title, because those files age at different rates. The file-level date takes precedence over the repository-level date. Dates are absolute and written as `YYYY-MM-DD`. Relative expressions such as "recently" or "the latest model" are prohibited by the style rules in [CONTRIBUTING.md](CONTRIBUTING.md).

## 5. Key findings

Each finding below answers a research question, rests on at least one Grade A or Grade B source, carries an absolute date, and is developed in exactly one chapter. Findings that would require ranking models are absent, because every benchmark result currently recorded has unstated evaluation conditions.

| # | Finding | RQ | Owned by |
|---|---|---|---|
| F1 | Inference optimisation changes energy use by a larger factor than model choice does. Fernandez and colleagues report reductions of up to 73 percent against an unoptimised baseline across hardware, serving frameworks, batching, and decoding strategies. Grade A. | RQ9 | [16](docs/16-energy-use.md) |
| F2 | Reasoning budget, not model size, dominates energy per query. Oviedo and colleagues estimate a median of 0.34 watt-hours for a representative frontier-scale query and 4.32 watt-hours at fifteen times the token use, roughly thirteen times higher. Grade A, analytical estimates rather than measurements of a named service. | RQ4, RQ9 | [16](docs/16-energy-use.md) |
| F3 | Advertised context capacity exceeds reliable capacity. Stanford's long-context evaluation states that support for long inputs does not imply long-context capability, and two independent benchmarks report degradation as context scales toward one million tokens. Grade A and Grade B. | RQ6 | [11](docs/11-long-context.md) |
| F4 | Agents approach but do not reach human performance on interactive benchmarks. The AI Index reports a best model result of 66.3 percent on OSWorld against a human baseline of 72.35 percent, and 74.3 percent on WebArena against 78.24 percent. Grade B. | RQ5 | [07](docs/07-agentic-ai.md) |
| F5 | Hallucination persists in hard domains even with web access. HalluHard reports that the strongest web-enabled configuration tested still hallucinated on about 30 percent of difficult multi-turn conversations. Grade B. | RQ3 | [10](docs/10-factuality-and-hallucination.md) |
| F6 | Output tokens dominate cost. Across every price schedule recorded here, the output rate is several times the input rate, and output is generated sequentially, so verbosity drives cost, latency, and energy at once. Grade B. | RQ8 | [15](docs/15-token-economics.md) |
| F7 | A per-token price is not comparable across providers without a token-count measurement. Anthropic states that the Claude Sonnet 5 tokenizer can produce about 30 percent more tokens for the same text than its predecessor. Grade B. | RQ7, RQ8 | [12](docs/12-tokenization.md) |
| F8 | No published benchmark result in this survey can be used for ranking. All nine recorded results are provider-reported with unstated harness, sampling policy, and tool permissions. Grade C, recorded and labelled. | RQ2 | [09](docs/09-benchmarking.md) |

Findings that would require energy, latency, or factuality datasets are not published, because those datasets are empty for the reasons given in [21. Research gaps](docs/21-research-gaps.md).

## 6. Model families covered

Sixteen profile files, one per family, each following the fixed template defined in [CONTRIBUTING.md](CONTRIBUTING.md#5-model-profile-template).

| Family | Profile | Weights |
|---|---|---|
| OpenAI | [openai.md](docs/model-profiles/openai.md) | Closed, with open-weight releases |
| Anthropic | [anthropic.md](docs/model-profiles/anthropic.md) | Closed |
| Google Gemini | [google-gemini.md](docs/model-profiles/google-gemini.md) | Closed, with open-weight Gemma line |
| Meta Llama | [meta-llama.md](docs/model-profiles/meta-llama.md) | Open weights, community licence |
| DeepSeek | [deepseek.md](docs/model-profiles/deepseek.md) | Open weights |
| Mistral | [mistral.md](docs/model-profiles/mistral.md) | Mixed open and closed |
| Qwen | [qwen.md](docs/model-profiles/qwen.md) | Open weights |
| xAI Grok | [xai-grok.md](docs/model-profiles/xai-grok.md) | Mixed |
| Microsoft Phi | [microsoft-phi.md](docs/model-profiles/microsoft-phi.md) | Open weights |
| Cohere Command | [cohere-command.md](docs/model-profiles/cohere-command.md) | Mixed |
| Amazon Nova | [amazon-nova.md](docs/model-profiles/amazon-nova.md) | Closed |
| AI21 Jamba | [ai21-jamba.md](docs/model-profiles/ai21-jamba.md) | Mixed |
| Moonshot Kimi | [moonshot-kimi.md](docs/model-profiles/moonshot-kimi.md) | Mixed |
| MiniMax | [minimax.md](docs/model-profiles/minimax.md) | Mixed |
| Zhipu GLM | [zhipu-glm.md](docs/model-profiles/zhipu-glm.md) | Mixed |
| Other families | [other-models.md](docs/model-profiles/other-models.md) | Mixed |

The `Weights` column above states the general posture of each organisation and is itself subject to verification during Phase 3. Per-model licence terms are recorded in `data/models.csv` with a source URL and are authoritative over this summary.

## 7. Benchmark categories covered

Nine benchmark files organised by construct rather than by vendor leaderboard.

| Category | File | Benchmarks documented |
|---|---|---|
| Overview and taxonomy | [benchmark-overview.md](docs/benchmarks/benchmark-overview.md) | Cross-cutting: HELM, MedHELM, Chatbot Arena, MT-Bench |
| Knowledge and reasoning | [knowledge-and-reasoning.md](docs/benchmarks/knowledge-and-reasoning.md) | MMLU, MMLU-Pro, GPQA Diamond, Humanity's Last Exam, ARC-AGI-1, ARC-AGI-2, ARC-AGI-3, FrontierMath, AIME, MATH, GSM8K |
| Coding | [coding.md](docs/benchmarks/coding.md) | SWE-Bench, SWE-Bench Verified, SWE-Bench Pro, Terminal-Bench, LiveCodeBench, HumanEval, MBPP |
| Agents and computer use | [agents-and-computer-use.md](docs/benchmarks/agents-and-computer-use.md) | BrowseComp, WebArena, OSWorld, GAIA, AgentBench, BFCL, ToolBench |
| Multimodal | [multimodal.md](docs/benchmarks/multimodal.md) | MMMU, MMMU-Pro, MathVista, DocVQA, ChartQA, VideoMME |
| Long context | [long-context.md](docs/benchmarks/long-context.md) | LongBench, LongCodeBench, RULER, MRCR, Needle-in-a-Haystack |
| Factuality | [factuality.md](docs/benchmarks/factuality.md) | FACTS, SimpleQA, TruthfulQA, HaluEval, HalluHard |
| Multilingual | [multilingual.md](docs/benchmarks/multilingual.md) | Multilingual coverage and tokenizer-induced score distortion |
| Limitations | [benchmark-limitations.md](docs/benchmarks/benchmark-limitations.md) | Contamination, saturation, prompt sensitivity, sampling policy |

Every benchmark entry documents nine fields: what it measures, task format, scoring method, known limitations, contamination risk, whether tools are permitted, whether multiple samples are used, whether human baselines are comparable, and whether scores are suitable for procurement decisions.

## 8. Methodology summary

The full protocol is in [research-methodology.md](research-methodology.md). In brief:

1. **Data first.** Machine-readable records in `data/*.csv` are the single source of truth. Markdown comparison tables are generated from those records by `scripts/generate_model_tables.py` and `scripts/generate_benchmark_tables.py`. A hand-edited comparison table without a corresponding CSV row is a defect and fails continuous integration.
2. **Source before claim.** Every row in `data/*.csv` carries a `source_id` that resolves to a record in `data/sources.csv`. `scripts/validate_sources.py` fails the build on an unresolved reference, a missing date, or a missing evidence grade.
3. **Grade before comparison.** Results are labelled with an evidence grade at the point of use. Results of different grades are never averaged or ranked against each other without an explicit warning in the surrounding text.
4. **Conditions before number.** A benchmark score is recorded with its evaluation harness, sampling policy, tool permissions, and date. A latency figure is recorded with its percentile, concurrency, and region. An energy figure is recorded with the eleven conditions listed in [docs/16-energy-use.md](docs/16-energy-use.md).
5. **Reproducibility.** All scripts are deterministic, take file paths as arguments, depend on no paid API, and write outputs that are diffable in version control.

## 9. Evidence-quality classification

Three grades apply throughout the repository. The assignment rules and edge cases are defined in [docs/appendices/source-quality-framework.md](docs/appendices/source-quality-framework.md).

| Grade | Name | Admits | Typical use |
|---|---|---|---|
| **A** | Independently verified | Peer-reviewed studies; standardised academic benchmarks; reproducible third-party evaluations; independently measured system performance; public datasets with disclosed methodology | Any comparative claim between model families |
| **B** | Institutional primary research | University research reports; technical reports; model cards; benchmark methodology pages; official architecture disclosures | Architecture, context window, licence, and specification claims |
| **C** | Provider-reported | Launch benchmark tables; vendor latency claims; vendor customer studies; self-reported energy claims; product documentation | Recorded and labelled, never used alone to rank one provider above another |

Grade C evidence is included because excluding it would leave large gaps, particularly on pricing and on models whose weights are not public. It is always labelled as provider-reported at the point of use, and comparison tables carry an `Evidence grade` column so that a reader can filter to Grade A rows.

## 10. Compact comparison table

This table is generated from `data/models.csv` and `data/pricing.csv` by `scripts/generate_model_tables.py --view compact`. It is deliberately short. Full per-benchmark results live in [docs/comparisons/](docs/comparisons/model-selection-matrix.md), and full pricing lives in [docs/15-token-economics.md](docs/15-token-economics.md).

<!-- BEGIN GENERATED: compact-comparison -->
| Provider | Model | Release date | Open weights | Context window | Input USD / 1M | Output USD / 1M | Evidence grade | Source date |
|---|---|---|---|---|---|---|---|---|
| Alibaba | Qwen 3.6 family | Not publicly disclosed | yes | 1000000 | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| Alibaba | Qwen 3.7 family | Not publicly disclosed | yes | 1000000 | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| Anthropic | Claude Fable 5 | Not publicly disclosed | no | 1000000 | 10.00 | 50.00 | B | 2026-07-22 |
| Anthropic | Claude Opus 4.8 | Not publicly disclosed | no | 1000000 | 5.00 | 25.00 | B | 2026-07-22 |
| Anthropic | Claude Sonnet 5 | Not publicly disclosed | no | 1000000 | 3.00 | 15.00 | B | 2026-07-22 |
| DeepSeek | DeepSeek V4 Flash | Not publicly disclosed | yes | 1000000 | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| DeepSeek | DeepSeek V4 Pro | Not publicly disclosed | yes | 1000000 | 0.435 | 0.87 | B | 2026-07-22 |
| Google | Gemini 3.1 Flash-Lite | Not publicly disclosed | no | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| Google | Gemini 3.1 Pro | Not publicly disclosed | no | 1000000 | Not publicly disclosed | Not publicly disclosed | C | 2026-07-22 |
| Meta | Llama 4 Maverick | Not publicly disclosed | yes | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| Meta | Llama 4 Scout | Not publicly disclosed | yes | Not publicly disclosed | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| Meta | Meta Muse Spark 1.1 | Not publicly disclosed | no | 1000000 | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| Mistral | Mistral Medium 3.5 | Not publicly disclosed | yes | 256000 | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| Mistral | Mistral Small 4 | Not publicly disclosed | yes | 256000 | Not publicly disclosed | Not publicly disclosed | B | 2026-07-22 |
| OpenAI | GPT-5.6 Luna | Not publicly disclosed | no | 1050000 | 1.00 | 6.00 | B | 2026-07-22 |
| OpenAI | GPT-5.6 Sol | Not publicly disclosed | no | 1050000 | 5.00 | 30.00 | B | 2026-07-22 |
| OpenAI | GPT-5.6 Terra | Not publicly disclosed | no | 1050000 | 2.50 | 15.00 | B | 2026-07-22 |
| xAI | Grok 4.5 | Not publicly disclosed | no | 500000 | 2.00 | 6.00 | B | 2026-07-22 |
<!-- END GENERATED: compact-comparison -->

The generator rewrites the content between the two markers and leaves the rest of this file untouched. Do not edit the region by hand.

## 11. Repository navigation

| Path | Contents |
|---|---|
| [docs/](docs/index.md) | The handbook. Chapters 01 to 21, model profiles, benchmarks, comparisons, evaluation protocol, appendices |
| [data/](data/) | Machine-readable source of truth: models, benchmarks, pricing, context windows, energy studies, sources, and JSON Schemas |
| [scripts/](scripts/) | Validation and table-generation scripts. All are runnable from the repository root |
| [notebooks/](notebooks/) | Analysis notebooks that read only from `data/` |
| [assets/](assets/) | Generated diagrams, charts, and table images |
| [docs/interactive/](docs/interactive/index.html) | The interactive companion page: a live cost-per-accepted-task calculator and four charts, each labelled with its evidence grade. Self-contained HTML, no build step, no external requests. Published at <https://ethical-tech-colab.github.io/AI-Models-Research/interactive/> |
| [research-methodology.md](research-methodology.md) | Search strategy, inclusion and exclusion criteria, extraction protocol, and quality control |
| [data-sources.md](data-sources.md) | The source register, the seed bibliography, and the outstanding verification queue |
| [glossary.md](glossary.md) | Terms and acronyms used across the repository |
| [limitations.md](limitations.md) | What this repository cannot establish, and why |
| [references.bib](references.bib) | BibTeX database backing all numbered footnotes |

Start at [docs/index.md](docs/index.md) or the full table of contents in [SUMMARY.md](SUMMARY.md).

## 12. Local installation

Python 3.11 or later is required.

On macOS and Linux:

```bash
git clone https://github.com/Ethical-Tech-CoLab/AI-Models-Research.git
cd AI-Models-Research
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, using PowerShell:

```powershell
git clone https://github.com/Ethical-Tech-CoLab/AI-Models-Research.git
cd AI-Models-Research
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the validation suite:

```bash
python scripts/validate_sources.py
python scripts/validate_tables.py
python scripts/validate_links.py
```

Each script exits with status `0` on success and `1` on any violation, and prints one line per violation in `path:line: message` form. No script fails silently.

## 13. Building the documentation

The site is built with MkDocs Material. Configuration is in [mkdocs.yml](mkdocs.yml).

```bash
mkdocs serve          # live preview at http://127.0.0.1:8000
mkdocs build --strict # fails on any broken internal link or navigation warning
```

On Windows, prefix with the activated virtual environment as shown in [section 12](#12-local-installation); the `mkdocs` commands are identical.

`mkdocs build --strict` runs in continuous integration through `build-docs.yml`. A warning is treated as a failure, so a chapter listed in the navigation but missing from disk, or present on disk but missing from the navigation, blocks the merge. The three workflows are currently parked in [.github/workflows-pending/](.github/workflows-pending/README.md) and are activated with one command; see that file for why.

## 14. Citing this repository

Machine-readable citation metadata is in [CITATION.cff](CITATION.cff). GitHub renders a formatted citation from that file in the sidebar.

Cite the repository, not an individual chapter, and include the commit hash and access date, because content changes:

```bibtex
@misc{etc_ai_models_research,
  author       = {{Ethical Tech CoLab}},
  title        = {{AI Models: Performance, Capabilities, Accuracy, Speed,
                   Energy Use, and Token Economics}},
  year         = {2026},
  howpublished = {\url{https://github.com/Ethical-Tech-CoLab/AI-Models-Research}},
  note         = {Commit <hash>. Accessed YYYY-MM-DD.}
}
```

When citing a finding, cite the underlying primary source recorded in `data/sources.csv` in preference to this repository. This repository is a survey and should not be used as the primary source for a result it did not produce.

## 15. Contribution rules

Full rules are in [CONTRIBUTING.md](CONTRIBUTING.md). The rules that cause the most rejected pull requests:

1. No numerical claim without a citation resolving to `data/sources.csv`.
2. No claim about a current model without an absolute date.
3. Provider-reported results must be labelled Grade C at the point of use.
4. No hand-edited generated table. Update the CSV and rerun the generator.
5. No em dashes in prose.
6. No repetition of an argument that another chapter already owns. Link to it.
7. No blog post cited for an academic finding where a paper exists, no AI-generated summaries, and no search-result snippets.
8. Benchmark scores obtained under different harnesses, sampling policies, or tool permissions are not placed in the same ranked column without a stated warning.

Use the issue templates for [benchmark updates](.github/ISSUE_TEMPLATE/benchmark-update.md), [model updates](.github/ISSUE_TEMPLATE/model-update.md), and [source corrections](.github/ISSUE_TEMPLATE/source-correction.md).

## 16. Limitations

Stated in full in [limitations.md](limitations.md). The principal constraints are that provider-reported evaluation conditions are frequently undisclosed and therefore unverifiable; that closed-weight models cannot be independently profiled for parameter count, memory footprint, or energy per token; that leaderboard and arena rankings are subject to prompt-selection and voting-population effects; that per-token energy figures are hardware-specific and cannot be generalised across serving stacks; and that this survey is not itself peer reviewed.

## 17. Disclaimer

Benchmark rankings, arena positions, API prices, rate limits, context windows, and model availability change without notice and frequently. Every such value in this repository is a historical record of what a named source stated on a named date, not a statement about the present. Verify against the provider's current documentation before making a procurement, budgeting, or deployment decision.

Nothing in this repository is legal, financial, or procurement advice. Licence summaries are research notes, not legal interpretations; read the licence text.

## 18. Repository status

| Phase | Contents | Status |
|---|---|---|
| 1 | Directory structure, configuration, schemas, methodology, source-quality framework, README, seed bibliography, validation scripts, continuous integration | Complete |
| 2 | Chapters 01 to 21 | Partial. Thirteen files written from registered sources: chapters 01, 02, 07, 09, 10, 11, 12, 14, 15, 16, 18, 20, 21, plus the bakeoff protocol and the benchmark glossary. The remainder carry a scope statement and a research checklist |
| 3 | Sixteen model-family profiles | Not started. Each file carries the fixed template and a research checklist |
| 4 | CSV population, validation, generated tables | Partial. 41 sources, 18 models, 8 pricing rows, 14 context-window rows, and 9 benchmark results are recorded; energy, latency, and factuality datasets are empty for stated reasons |
| 5 | Navigation completion, link and lint passes, citation validation, research completeness report, data-gap register | Partial. The full gate passes; the data-gap register is in chapter 21 |

Outstanding data gaps and unverified sources are tracked in [data-sources.md](data-sources.md#5-verification-queue).

## Licence

Documentation and data are licensed under Creative Commons Attribution 4.0 International. Source code under `scripts/` and `notebooks/` is licensed under the MIT Licence. See [LICENSE](LICENSE).

---

## Peer Review

The full independent academic peer review of this survey is in [PEER-REVIEW.md](PEER-REVIEW.md) (also available as [Word](peer-review/ai-models-research-Peer-Review.docx) under [`peer-review/`](peer-review/)).

**Recommendation:** Minor revisions — the methodology, `limitations.md`, and the evidence taxonomy are described in the review as the best in the CoLab portfolio; the gap is between that apparatus and how little data currently sits under it.

**What the review found:**

- **After the evidence rules are applied, almost nothing is left to compare.** `benchmarks.csv` holds nine rows, all Grade C, each individually marked "excluded from ranked comparison" — zero rows are eligible for the comparison the survey exists to support, so RQ2 is answered entirely in prose. The review's recommendation is to publish this as the finding it is: as of July 2026, no public benchmark evidence for frontier commercial models survives a reproducibility bar. That is a result about the field's disclosure practices, not a to-do item.
- **`energy-studies.csv` contains a header row and no data**, while energy is in the title and has its own chapter.
- **`Not publicly disclosed` is used where the provider does disclose.** On all three Anthropic pricing rows, `cached_input_price_per_1m`, `reasoning_token_billing`, and `batch_discount_percent` are recorded as undisclosed; all three are documented by that provider. This records a source-review gap as a provider-transparency finding — the exact distinction the taxonomy exists to preserve. Recommended fix: add a fourth value (`Not extracted`) and re-audit every such cell.
- **A blanket caveat that is false for a whole provider block** — every row carries "model_id is a normalised slug … replace with the exact string when the API reference is read", but the recorded Anthropic IDs *are* the exact API strings.
- **The low-cost tier of a major family is missing** — Claude Haiku 4.5 (200K context, $1/$5) is absent, so the selection framework cannot express a cheap-tier recommendation there, and the one in-family counterexample to "context has converged at 1M" is gone.
- Minor: the build-status line ("Phase 1 complete. Phases 2 to 5 are not yet written") contradicts the §18 table and the 21 chapters in the tree; sample sizes and grade distribution are stated nowhere a reader will see them; `release_date` is `Not publicly disclosed` for all 18 models; family-level Qwen rows sit in a per-model table.

**Verified against the data layer:** the Anthropic rows check out — Claude Fable 5 at $10/$50 per MTok, Opus 4.8 at $5/$25, Sonnet 5 at $3/$15 with the introductory rate noted, all at 1M context and 128K max output, and the Sonnet 5 tokenizer note is accurate. The reviewer verified only the Anthropic block; a per-provider audit of the rest is recommended before publication.
