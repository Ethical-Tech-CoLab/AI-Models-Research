# Research methodology

> **Research cut-off date: 2026-07-22.**

This document defines how evidence enters the repository, how it is graded, how it is extracted into machine-readable form, and what must pass before a chapter is considered complete. It is binding on all contributions. Where this document and any other file disagree, this document governs.

## 1. Design

The repository is a **structured research survey with a reproducible data layer**. It follows the logic of a systematic review in three respects: a declared search strategy, declared inclusion and exclusion criteria, and a declared extraction schema. It departs from a formal systematic review in two respects that a reader must understand.

First, the object of study changes faster than the review cycle. A frozen literature search would be stale before publication, so the search is continuous and every record carries an access date rather than a single search date.

Second, a large share of the relevant evidence is not peer reviewed and never will be. Model cards, provider technical reports, and pricing pages are primary sources for facts about commercial products that no independent party can otherwise establish. Excluding them would not raise quality; it would leave the survey silent on most of its subject matter. The evidence-grading system in section 4 exists to admit these sources while keeping them separable from independently verified results.

## 2. Search strategy

### 2.1 Priority tiers

Sources are sought in the following order. A lower tier is used only when no higher tier addresses the claim.

**Tier 1. Peer-reviewed and archival venues.** ACL Anthology; NeurIPS; ICML; ICLR; EMNLP; USENIX; ACM Digital Library; IEEE Xplore; journals indexed in Google Scholar.

**Tier 2. Institutional research.** Stanford (including the Institute for Human-Centered AI and the Center for Research on Foundation Models), MIT, Harvard, NYU, Princeton, Carnegie Mellon, UC Berkeley, Oxford, Cambridge; Google DeepMind; Microsoft Research; Meta AI; Anthropic; OpenAI; Mistral; Hugging Face; the International Energy Agency.

**Tier 3. Preprints.** arXiv, used when no peer-reviewed version exists. Where a paper has both a preprint and a published version, the published version is cited and the preprint identifier is retained in the `notes` field of `data/sources.csv`.

**Tier 4. Official product documentation.** Provider model cards, API reference pages, pricing pages, licence texts, and official repositories on GitHub and Hugging Face. These are authoritative for commercial terms and product behaviour and for nothing else.

### 2.2 Standing sources

The following are checked on a recurring basis because they aggregate evidence across the field: the Stanford AI Index; Stanford CRFM HELM and MedHELM; the Stanford Foundation Model Transparency Index; Google DeepMind FACTS; the International Energy Agency electricity and data-centre reporting; and official provider changelogs for each of the sixteen model families.

### 2.3 Excluded source types

The following are never cited as the primary support for a claim: AI-generated summaries of any kind; search-engine result snippets; secondary reporting of a paper where the paper is accessible; marketing blog posts where a technical report or model card exists; social-media posts; undated web pages; and any page whose content cannot be retrieved at the recorded URL.

A blog post may be cited when it is itself the primary artefact, for example a provider announcing a price change that appears in no other document. In that case it is Grade C and is labelled as provider-reported.

## 3. Inclusion and exclusion criteria

### 3.1 Model inclusion

A model is profiled when all of the following hold:

1. It is a general-purpose foundation model whose primary interface accepts natural-language input.
2. It is generally available, in public preview, or formally deprecated with documentation still accessible. Announced but unreleased models are excluded.
3. At least one Grade A or Grade B source documents either its architecture or its evaluated performance.
4. Either its weights are downloadable under a stated licence, or it is served through a documented commercial API with published pricing.

### 3.2 Benchmark inclusion

A benchmark is documented when it has a published construction methodology, a defined scoring procedure, and either a peer-reviewed description or a maintained public methodology page. Leaderboards without a documented methodology are described as leaderboards and are not treated as benchmarks.

### 3.3 Result inclusion

A benchmark result is recorded only with all of: model name and version identifier; benchmark name and version; score and metric; evaluation harness or "unstated"; sampling policy (single sample, best-of-n, majority vote at n, or unstated); tool permissions (none, retrieval, code execution, browsing, or unstated); the reporting organisation; the publication date; and the evidence grade.

A result missing the harness, sampling policy, or tool permissions is still recorded, with those fields set to `unstated`, and is thereby disqualified from any ranked comparison under the rule in section 6.3.

## 4. Evidence grading

### 4.1 Definitions

**Grade A, independently verified.** The result was produced or reproduced by a party with no commercial interest in the outcome, under a disclosed methodology. Admits peer-reviewed studies; standardised academic benchmarks run by their maintainers; reproducible third-party evaluations; independently measured system performance; and public datasets with clear methodology.

**Grade B, institutional primary research.** The result or specification comes from the originating institution under a documented methodology, without independent replication. Admits university research reports; technical reports; model cards; benchmark methodology pages; and official architecture disclosures.

**Grade C, provider-reported.** The claim originates with the commercial party that benefits from it, under conditions that are typically incomplete. Admits launch benchmark tables; vendor latency claims; vendor customer studies; self-reported energy claims; and product documentation.

### 4.2 Assignment rules

1. Grade the *evidence*, not the *organisation*. A peer-reviewed paper authored at a frontier laboratory and evaluated on a third-party benchmark is Grade A. A press release from a university is Grade C for any claim about a commercial product it did not measure.
2. When a source restates another source, grade the original and cite the original.
3. When a claim is supported by several sources of different grades, record the highest grade and list the additional source identifiers in the `notes` field.
4. When two sources of equal grade conflict, record both rows, mark the conflict in `notes`, and state the disagreement in prose. Do not average them and do not silently prefer one.
5. Pricing, licence terms, rate limits, and data-retention policies are Grade B when taken from official documentation, because the provider is the definitive authority on its own commercial terms. Provider claims about *performance* are Grade C.

The full decision procedure and worked edge cases are in [docs/appendices/source-quality-framework.md](docs/appendices/source-quality-framework.md).

## 5. Extraction protocol

### 5.1 Order of operations

1. Locate the source and confirm it resolves at the recorded URL.
2. Create the record in `data/sources.csv` with all fourteen required fields.
3. Add the BibTeX entry to `references.bib` using the same `source_id` as the citation key.
4. Extract the data points into the appropriate dataset: `data/models.csv`, `data/benchmarks.csv`, `data/pricing.csv`, `data/context-windows.csv`, or `data/energy-studies.csv`.
5. Run `python scripts/validate_sources.py` and `python scripts/validate_tables.py`.
6. Write or amend the prose, citing with a numbered Markdown footnote whose key matches the `source_id`.
7. Regenerate any affected table with the relevant script in `scripts/`.

Prose is never written before the data record exists. This ordering is what makes the numeric claim and its citation impossible to separate.

### 5.2 Field conventions

| Convention | Rule |
|---|---|
| Dates | `YYYY-MM-DD`. Where a source gives only a month, use the first day of the month and note the imprecision in `notes`. |
| Unknown values | `Not publicly disclosed` where the provider has not stated the value; `Insufficient independent evidence` where a value is claimed but unverified; `unstated` for missing evaluation conditions. Empty cells are a validation error. |
| Currency | United States dollars, per one million tokens, exclusive of tax and of committed-use discounts. |
| Units | SI. Energy in joules or watt-hours with the unit named in the column header. Memory in gibibytes, written `GiB`. |
| Model identifiers | The provider's exact API model string where one exists, recorded verbatim including any date suffix. |
| Uncertainty | Recorded explicitly as a range or an interval with its basis stated. A point estimate presented without a basis is a validation error for energy rows. |

## 6. Comparison rules

### 6.1 Data before Markdown

Comparison tables in `docs/` are generated from `data/*.csv`. Hand-editing a generated region is a defect. Generated regions are delimited by `<!-- BEGIN GENERATED: <name> -->` and `<!-- END GENERATED: <name> -->` and are rewritten wholesale by the generator.

### 6.2 Mandatory columns

Every comparison table includes, at minimum, the compared quantity, the `Evidence grade`, the `Source date`, and a resolvable `Source` reference. Tables comparing benchmark scores additionally include the sampling policy and tool permissions, because a score without them is not comparable.

### 6.3 Incompatible-settings rule

Two results are placed in the same ranked column only when their harness, sampling policy, and tool permissions match, or when the difference is stated in a warning adjacent to the table. A result whose conditions are `unstated` is never ranked against a result whose conditions are known. This rule has no exceptions and is the single most common cause of a rejected contribution.

### 6.4 Energy claims

No universal energy value is published for any model. Every energy figure states hardware, model version, numerical precision, prompt length, output length, batch size, utilisation, serving framework, power usage effectiveness, measurement or estimation method, and uncertainty. A figure missing any of these eleven conditions is not published. `scripts/validate_tables.py` enforces the presence of all eleven columns on every row of `data/energy-studies.csv`.

## 7. Writing standards

1. Formal academic English. First person plural is acceptable for methodological statements; first person singular is not.
2. No em dashes. Use commas, semicolons, colons, or parentheses. Enforced by `markdownlint` configuration and by `scripts/validate_tables.py --check-style`.
3. One argument, one owner. Each argument is developed in exactly one chapter; other chapters link to it. Duplicated argumentation is a defect, not redundancy for the reader's convenience.
4. No unqualified comparatives. "Model X outperforms model Y" is incomplete. State the benchmark, the metric, the evaluation conditions, and the date.
5. Uncertainty is marked in the sentence that carries the claim, not deferred to a general caveat at the end of the chapter.
6. Provider claims carry the label "provider-reported" in the sentence or the table cell where they appear, not only in a footnote.

## 8. Quality control

A chapter is complete only when every item below passes. This checklist is reproduced in [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) and is verified at review.

| # | Check | Automated by |
|---|---|---|
| 1 | Every numerical claim carries a citation | `validate_sources.py --check-citations` |
| 2 | Every claim about a current model carries an absolute date | `validate_sources.py --check-dates` |
| 3 | Provider claims are labelled at the point of use | Manual review |
| 4 | No benchmark scores compared under incompatible settings without a warning | `validate_tables.py --check-comparability`, plus manual review |
| 5 | No argument duplicated from another chapter | Manual review |
| 6 | No em dashes | `validate_tables.py --check-style` |
| 7 | All links resolve | `validate_links.py`, `.github/workflows/links.yml` |
| 8 | Tables are consistent with their source CSV | `validate_tables.py` |
| 9 | Filenames match the MkDocs navigation | `mkdocs build --strict` |
| 10 | All validation scripts pass | `.github/workflows/markdown-lint.yml` |
| 11 | Documentation builds without warnings | `.github/workflows/build-docs.yml` |
| 12 | The page renders correctly on GitHub | Manual review |

## 9. Revision and versioning

Substantive changes are recorded in [CHANGELOG.md](CHANGELOG.md) under the date of the change. A substantive change is one that alters a number, a grade, a conclusion, or a source. Typographic corrections are not logged.

When a source is superseded, for example when a provider changes a price, the previous row is retained in the CSV with its original `access_date` and a `superseded_by` reference in `notes`. History is preserved rather than overwritten, because a claim about a past date remains true.

## 10. Known methodological limitations

These limitations are inherent to the design and are not defects to be fixed. They are restated in context in [limitations.md](limitations.md).

1. **Verification asymmetry.** Open-weight models can be independently measured for memory, throughput, and energy. Closed-weight models cannot. Grade A evidence is therefore systematically more available for open-weight models, and any aggregate comparison of the two categories is biased by data availability rather than by capability.
2. **Provider-selected conditions.** Grade C results are typically produced under conditions selected by the provider after seeing the outcome. They are recorded because the alternative is silence, not because they are reliable.
3. **Benchmark contamination.** Public benchmarks may appear in training corpora. Contamination cannot be excluded for any model whose training data is undisclosed, which is most of them.
4. **Sampling by availability.** The survey covers models that publish enough to be documented. Models with minimal public documentation are under-represented independent of their capability.
5. **Single-reviewer extraction.** Records are extracted by one contributor and checked at review, not double-extracted by independent coders as a formal systematic review would require. Extraction error is therefore possible and is mitigated only by the automated validation layer and the source-correction issue template.
