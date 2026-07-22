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

**No findings are published at Phase 1.** Publishing summary findings before the underlying chapters and datasets exist would produce exactly the unsourced ranking claims this repository is designed to displace.

A finding is admitted to this section only when all five conditions hold:

1. It answers one of the research questions in [section 2](#2-research-questions).
2. It is supported by at least one Grade A or Grade B source recorded in `data/sources.csv`.
3. Where it compares models, the compared results were produced under stated and compatible evaluation conditions, or the incompatibility is stated in the finding itself.
4. It carries an absolute date and a named evaluation setting.
5. It is not restated elsewhere in the repository; the finding links to the single chapter that owns the argument.

Findings are added during Phase 5 and recorded in [CHANGELOG.md](CHANGELOG.md) with the commit that introduced the supporting evidence.

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
| _No rows. Populate the source dataset in data/ and rerun scripts/generate_model_tables.py_ | | | | | | | | |
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
| [web/](web/) | Source of the interactive companion page: a live cost-per-accepted-task calculator and four charts, each labelled with its evidence grade. Self-contained HTML, no build step, no external requests |
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
| 2 | Chapters 01 to 21 | Not started. Each chapter file currently carries a scope statement and a research checklist |
| 3 | Sixteen model-family profiles | Not started. Each file carries the fixed template and a research checklist |
| 4 | CSV population, validation, generated tables | Not started. CSV files contain validated headers only |
| 5 | Navigation completion, link and lint passes, citation validation, research completeness report, data-gap register | Not started |

Outstanding data gaps and unverified sources are tracked in [data-sources.md](data-sources.md#5-verification-queue).

## Licence

Documentation and data are licensed under Creative Commons Attribution 4.0 International. Source code under `scripts/` and `notebooks/` is licensed under the MIT Licence. See [LICENSE](LICENSE).
