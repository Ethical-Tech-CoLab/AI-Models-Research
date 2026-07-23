# Changelog

All substantive changes to this repository are recorded here. A substantive change is one that alters a number, an evidence grade, a conclusion, or a source. Typographic corrections are not logged.

Dates are absolute and written `YYYY-MM-DD`. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) with one addition: an `Evidence` section records changes to the source register, because in a research repository a change of source is more consequential than a change of code.

## [0.2.0] Phase 2 partial, 2026-07-22

### Added

- Thirteen chapters written from registered sources: 01 Introduction, 02 Foundation models, 07 Agentic AI, 09 Benchmarking, 10 Factuality and hallucination, 11 Long context, 12 Tokenization, 14 Latency and throughput, 15 Token economics, 16 Energy use, 18 Open versus closed models, 20 Model selection framework, 21 Research gaps.
- The internal bakeoff protocol and the benchmark glossary.
- Eight key findings in the README, each tied to a research question, a source of Grade A or Grade B, and the single chapter that owns it.
- An interactive companion page at `docs/interactive/`, published to GitHub Pages alongside the handbook.

### Evidence

- `data/sources.csv` populated with 41 unique sources behind the 60 footnotes of the July 2026 comparative review, each with all fourteen fields and an access date of 2026-07-22.
- `references.bib` extended with a matching entry per registered source. The duplicate seed entry for the holistic evaluation preprint was removed in favour of the registered key.
- `data/models.csv`: 18 models. `data/pricing.csv`: 8 schedules. `data/context-windows.csv`: 14 records. `data/benchmarks.csv`: 9 provider-reported results.
- All generated comparison tables regenerated from the populated data layer.
- Six figures from the source review archived under `assets/charts/`.

### Deliberately empty

- `data/energy-studies.csv`. The two Grade A inference-energy studies do not restate all eleven required conditions in a transcribable form, so their findings appear in chapter 16 prose with assumptions attached rather than as dataset rows the comparison rules would then forbid anyone from using.
- Latency rows. The two provider throughput figures state no percentile, concurrency, region, or prompt length.
- Factuality rows. Reported rates do not state the grounding condition per model.

All three absences are registered in chapter 21 with the specific evidence that would close them.

### Fixed

- `validate_tables.py` coerced CSV cells by their textual shape rather than by their schema type, so a benchmark version of `2.1` was read as a number and rejected. Coercion is now driven by the declared type, including through `anyOf` branches.
- The comparability check fired on definitional tables whose entries carry digits in their names, such as `ARC-AGI-2`. It now requires a body cell that is entirely a measurement.

### Known gaps

- No model release dates are disclosed by the sources used, so the release timeline diagram is empty and the contamination argument has no time axis.
- Model profiles remain unwritten.
- Every bibliography entry is still pending verification against the published record.

## [Unreleased]

### Planned

- Phase 2: chapters 01 to 21.
- Phase 3: sixteen model-family profiles.
- Phase 4: population of `data/*.csv`, validation, and generated comparison tables.
- Phase 5: navigation completion, link and lint passes, citation validation, research completeness report, and the data-gap register.

## [0.1.0] Phase 1 foundation, 2026-07-22

### Added

- Repository structure: `docs/`, `data/`, `scripts/`, `notebooks/`, `assets/`, and `.github/`.
- `README.md` with purpose, eleven research questions, scope, research cut-off date, model families, benchmark categories, methodology summary, evidence-quality classification, navigation, installation and build instructions, citation instructions, contribution rules, limitations, and disclaimer.
- `research-methodology.md`: search strategy, inclusion and exclusion criteria, evidence grading, extraction protocol, comparison rules, writing standards, quality control, and known methodological limitations.
- `data-sources.md`: the source register specification, source priority tiers, dataset map, seed bibliography description, and the verification queue.
- `limitations.md`: five classes of limitation with consequences and mitigations.
- `glossary.md`: definitional entries covering architecture, training, inference, cost, latency, and energy terminology.
- `CONTRIBUTING.md`: evidence rules, writing style, the model profile template, the benchmark documentation template, and the review process.
- `references.bib`: Phase 1 seed bibliography of foundational and methodological literature, in twelve sections. All entries are unverified at this date.
- `CITATION.cff`, `LICENSE`, `.gitignore`, `requirements.txt`, `pyproject.toml`, `mkdocs.yml`.
- JSON Schemas for models, benchmarks, and sources under `data/schema/`.
- Header-only CSV files under `data/`.
- Eight Python scripts under `scripts/`: three validators, three generators, and two calculators.
- Four analysis notebooks under `notebooks/`.
- GitHub Actions workflows for link checking, Markdown linting with validation, and documentation build.
- Three issue templates and a pull request template.
- Scope statements and research checklists for all sixty-five files under `docs/`.

### Evidence

- No evidence records exist at this release. `data/sources.csv` contains headers only, and every entry in `references.bib` is pending verification per [data-sources.md](data-sources.md#5-verification-queue).
- No benchmark result, price, parameter count, context window, or energy figure appears anywhere in the repository at this release. This is deliberate: the data layer and its validation must precede the claims that depend on it.

### Known gaps

- Twenty-eight outstanding source acquisitions are listed in [data-sources.md](data-sources.md#52-outstanding-source-acquisitions).
- Five gaps expected to remain unresolvable are listed in [data-sources.md](data-sources.md#53-known-gaps-that-verification-will-not-close).
