# Contributing

> **Research cut-off date: 2026-07-22.**

Thank you for contributing. This repository is a research artefact, so contributions are reviewed against evidentiary standards rather than only against style. Read [research-methodology.md](research-methodology.md) before your first substantive pull request.

## 1. Ways to contribute

| Contribution | Route |
|---|---|
| A benchmark result is missing, outdated, or wrong | [Benchmark update issue](.github/ISSUE_TEMPLATE/benchmark-update.md) |
| A model specification, price, licence, or availability has changed | [Model update issue](.github/ISSUE_TEMPLATE/model-update.md) |
| A citation is wrong, a URL is dead, or a grade is misassigned | [Source correction issue](.github/ISSUE_TEMPLATE/source-correction.md) |
| Prose, structure, scripts, or tooling | Pull request |

Open an issue before a large prose contribution so that chapter ownership can be confirmed. The repository prohibits duplicated argumentation, so two contributors writing the same argument in two chapters produces work that cannot be merged.

## 2. Development setup

Python 3.11 or later.

```bash
git clone https://github.com/Ethical-Tech-CoLab/AI-Models-Research.git
cd AI-Models-Research
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Before every push:

```bash
python scripts/validate_sources.py
python scripts/validate_tables.py
python scripts/validate_links.py
mkdocs build --strict
```

All four must exit `0`. Continuous integration runs the same commands.

## 3. Evidence rules

These are the rules that cause contributions to be rejected. They are not negotiable.

### 3.1 Every number has a citation

A numerical claim in prose carries a numbered Markdown footnote whose key is a `source_id` present in `data/sources.csv`. `scripts/validate_sources.py --check-citations` fails on an unresolved key.

### 3.2 Every current-model claim has an absolute date

Write `as of 2026-03-14`, not `currently`, `recently`, `at the time of writing`, or `the latest`. Relative time expressions are rejected.

### 3.3 Data before prose

Add the source to `data/sources.csv`, add the BibTeX entry to `references.bib`, add the data row to the relevant `data/*.csv`, and only then write the prose. A prose number with no CSV row behind it is a defect even when it is correct.

### 3.4 Never hand-edit a generated table

Regions delimited by `<!-- BEGIN GENERATED: name -->` and `<!-- END GENERATED: name -->` are rewritten by the scripts in `scripts/`. Change the CSV and rerun the generator:

```bash
python scripts/generate_model_tables.py
python scripts/generate_benchmark_tables.py
```

### 3.5 Label provider claims at the point of use

A provider-reported figure is marked Grade C in the table cell or in the sentence that carries it, not only in a footnote. Write "provider-reported" explicitly.

### 3.6 Do not rank incomparable results

Benchmark scores produced under different harnesses, sampling policies, or tool permissions do not go in the same ranked column unless a warning immediately adjacent to the table states the difference. Results with `unstated` conditions are never ranked against results with known conditions.

### 3.7 Do not invent

Never write a benchmark result, model specification, price, parameter count, context window, architecture detail, or citation that you have not read in a source. Where the value is unavailable, write `Not publicly disclosed` or `Insufficient independent evidence`. An honest gap is a contribution; a plausible guess is a defect that is expensive to detect later.

### 3.8 Source hierarchy

Prefer peer-reviewed work, then institutional research, then preprints, then official product documentation. Do not cite a blog post for an academic finding when the paper exists. Never cite an AI-generated summary or a search-result snippet.

## 4. Writing style

1. Formal academic English. First person plural for methodological statements; no first person singular.
2. **No em dashes.** Use a comma, a semicolon, a colon, or parentheses. This is checked automatically.
3. One argument, one chapter. Link to the chapter that owns an argument rather than restating it.
4. No unqualified comparatives. Name the benchmark, the metric, the conditions, and the date.
5. Mark uncertainty in the sentence that carries the claim.
6. Define an acronym at first use in each chapter and add it to [glossary.md](glossary.md).
7. Sentence case for headings. American or British spelling is acceptable, consistently within a file.
8. Tables: header row, alignment row, one row per record. Wide tables belong in a generated region driven by a CSV.

## 5. Model profile template

Every file in `docs/model-profiles/` uses this structure exactly, in this order. Do not add, remove, or reorder headings. Do not leave a section empty: write `Not publicly disclosed` or `Insufficient independent evidence` where the evidence does not exist.

```markdown
# Model Family Name

> Research cut-off: YYYY-MM-DD

## Overview
## Organization
## Current model lineup
## Architecture
## Total parameters
## Active parameters
## Dense or mixture-of-experts
## Training and post-training
## Modalities
## Context window
## Maximum output
## Tokenizer
## Reasoning modes
## Tool use
## Agent capabilities
## Coding performance
## Scientific reasoning
## Long-context performance
## Multimodal performance
## Factuality and hallucination
## Latency
## Throughput
## Token pricing
## Caching
## Batch pricing
## Hardware requirements
## Quantization
## Memory footprint
## Energy evidence
## Privacy and data retention
## Licensing
## Strengths
## Limitations
## Best use cases
## Inappropriate use cases
## Independent evidence
## Provider-reported evidence
## Open research questions
## Sources
```

Section-specific requirements:

- **Current model lineup.** One row per model identifier, with release date and status (`generally available`, `preview`, `deprecated`, `retired`).
- **Total parameters** and **Active parameters.** `Not publicly disclosed` for most closed-weight models. Do not estimate from benchmark behaviour.
- **Context window** and **Maximum output.** Advertised values with a source, plus any independently measured effective context, clearly distinguished.
- **Latency** and **Throughput.** Include percentile, concurrency, region, and date, or state that the source omitted them.
- **Token pricing**, **Caching**, **Batch pricing.** USD per million tokens with an effective date. Cross-reference the row in `data/pricing.csv`.
- **Energy evidence.** All eleven conditions per [research-methodology.md](research-methodology.md#64-energy-claims), or `Insufficient independent evidence`.
- **Independent evidence** and **Provider-reported evidence.** These two sections separate Grade A and Grade B material from Grade C material. Do not mix them.
- **Sources.** Numbered footnote definitions, each resolving to a `source_id`.

`scripts/validate_tables.py --check-profiles` verifies that every profile file contains all thirty-nine headings in order and that no section is empty.

## 6. Benchmark documentation template

Every benchmark documented in `docs/benchmarks/` answers all nine questions, under these headings:

1. What it measures
2. Task format
3. Scoring method
4. Known limitations
5. Contamination risk
6. Tool permissions
7. Sampling policy
8. Human baseline comparability
9. Suitability for procurement

The ninth is a judgement and must be argued, not asserted.

## 7. Adding a source

1. Retrieve the source and confirm the URL resolves.
2. Add a row to `data/sources.csv` with all fourteen fields. See [data-sources.md](data-sources.md#11-required-fields).
3. Add the BibTeX entry to [references.bib](references.bib) with the citation key equal to `source_id`.
4. Assign the evidence grade per [docs/appendices/source-quality-framework.md](docs/appendices/source-quality-framework.md).
5. Run `python scripts/validate_sources.py`.

Author lists are taken from the published record. Do not expand `and others` from memory.

## 8. Pull request checklist

The full checklist is in [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) and is reproduced from [research-methodology.md](research-methodology.md#8-quality-control). A pull request that leaves items unchecked without explanation is not reviewed.

Commits are small and scoped to one chapter or one dataset where possible. Commit messages state what changed and, for evidence changes, which source drove the change.

## 9. Review

Reviewers check, in order: whether the evidence rules in section 3 hold; whether the argument is owned by this chapter and not duplicated; whether comparisons are legitimate under the incomparable-settings rule; and only then style and prose.

A reviewer who cannot locate the claim in the cited source will request the specific page, section, or table. Contributors should include that locator in the `notes` field of the source row when the source is long.

## 10. Conduct

Contributors are expected to engage respectfully and in good faith. Disagreements about evidence are resolved by returning to the source, not by seniority. A contributor who identifies an error in their own merged work and reports it is doing the most valuable thing available in a repository of this kind.

## 11. Licence of contributions

By contributing you agree that your documentation and data contributions are licensed under Creative Commons Attribution 4.0 International, and your code contributions under the MIT Licence, as stated in [LICENSE](LICENSE).
