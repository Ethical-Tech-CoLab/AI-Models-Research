# Limitations

> **Research cut-off date: 2026-07-22.**

This document states what this repository cannot establish. It is placed at the top level rather than in an appendix because a reader who skips it will misread the comparison tables.

The limitations are grouped into five classes: limits of the evidence base, limits of benchmark measurement, limits of cost and performance measurement, limits of environmental measurement, and limits of this survey as an artefact. Each entry states the limitation, its consequence for interpretation, and any mitigation applied.

## 1. Limits of the evidence base

### 1.1 Verification asymmetry between open and closed weights

Open-weight models can be downloaded, instrumented, and measured by any party with sufficient hardware. Memory footprint, throughput, quantization behaviour, and energy per token are therefore directly observable. Closed-weight models cannot be measured in any of these respects; the caller observes only latency and price at the API boundary.

*Consequence.* Grade A evidence is systematically more available for open-weight models. Any aggregate statement of the form "open-weight models are better characterised on dimension X" reflects data availability, not model behaviour. Comparisons of evidence quantity between the two categories are meaningless.

*Mitigation.* Comparison tables carry an `Evidence grade` column so a reader can see which cells rest on independent measurement. No aggregate score is computed across cells of different grades.

### 1.2 Provider-selected evaluation conditions

Grade C results are produced by the party that benefits from a favourable outcome, typically after the outcome is known. Prompt formatting, sampling policy, number of attempts, tool permissions, and the choice of which benchmarks to report are all selected by the provider, and the selection is rarely disclosed.

*Consequence.* Provider-reported results establish an upper bound on what a provider is willing to claim. They do not establish a model's performance under a reader's conditions and are not comparable to another provider's self-reported figure.

*Mitigation.* Grade C results are recorded rather than excluded, because exclusion would leave the survey silent on most commercial models. They are labelled at the point of use and are never ranked against Grade A results in the same column.

### 1.3 Undisclosed training data

Training-corpus composition is not published for most commercial models and is incompletely published for most open-weight models.

*Consequence.* Benchmark contamination cannot be excluded for any such model. A high score on a public benchmark is consistent with both genuine capability and memorisation, and this survey cannot distinguish them.

*Mitigation.* Contamination risk is documented per benchmark in [docs/benchmarks/](docs/benchmarks/benchmark-limitations.md). Benchmarks with a contamination-resistant design, such as those drawing problems published after a model's training cut-off, are identified as such.

### 1.4 Availability sampling

The survey covers organisations that publish enough documentation to be documented. Providers with minimal public disclosure are under-represented regardless of the capability of their models.

*Consequence.* The set of profiled families is a sample selected by disclosure practice, not a census of capable models.

### 1.5 Undisclosed model versioning

Commercial API endpoints are sometimes updated without a change to the model identifier, and versioned identifiers are sometimes retired without notice.

*Consequence.* A result recorded against a model identifier on one date may not reproduce against the same identifier on a later date, even in the absence of any announcement.

*Mitigation.* Every result row carries the date on which it was reported and, where available, a dated model identifier. Results are treated as historical records rather than as current properties of an endpoint.

## 2. Limits of benchmark measurement

### 2.1 Construct validity

A benchmark measures performance on the benchmark. Whether that performance transfers to a deployment task is an empirical question that most benchmarks do not address, and that this survey cannot resolve for a reader's specific task.

*Consequence.* No ranking in this repository should be read as a ranking of usefulness. The model-selection framework in [docs/20-model-selection-framework.md](docs/20-model-selection-framework.md) is a procedure for a reader to run their own evaluation, not a substitute for one.

### 2.2 Saturation and ceiling effects

Where scores on a benchmark cluster near its maximum, differences between models fall within the range attributable to prompt formatting, parser behaviour, and answer-extraction heuristics.

*Consequence.* Small differences on saturated benchmarks carry no information. This survey does not report a rank ordering derived from differences within the noise range of a saturated benchmark.

### 2.3 Incomparable evaluation settings

Scores on the same benchmark are frequently produced under different harnesses, prompt templates, sampling policies, and tool permissions. Reported figures for a single model on a single benchmark can vary substantially across evaluators for these reasons alone.

*Consequence.* A table that places such figures side by side implies a comparison that the underlying measurements do not support.

*Mitigation.* The incompatible-settings rule in [research-methodology.md](research-methodology.md#63-incompatible-settings-rule) prohibits ranking results whose conditions differ or are unstated, unless the difference is stated adjacent to the table.

### 2.4 Preference leaderboards

Arena-style rankings aggregate human preference votes over user-submitted prompts. The prompt distribution is determined by the voting population, and preference is influenced by response formatting and length as well as by correctness.

*Consequence.* An arena rank measures aggregate preference on that platform's prompt distribution at that time. It is not an accuracy measurement and does not transfer to a different prompt distribution.

*Mitigation.* Arena positions are recorded with the date and are documented in [docs/benchmarks/benchmark-overview.md](docs/benchmarks/benchmark-overview.md) as a distinct construct from accuracy benchmarks.

### 2.5 Single-run reporting

Many published results report a single evaluation run without variance. Where a benchmark permits multiple samples, the sampling policy materially changes the score.

*Consequence.* Differences between reported figures cannot be attributed to model capability without knowing the sampling policy and the run-to-run variance, neither of which is usually published.

## 3. Limits of cost and performance measurement

### 3.1 Price per token is not cost per task

Advertised price per million tokens omits the token volume a task actually consumes. Reasoning tokens, retries, tool-call overhead, system prompts, cached prefixes, and context compaction all change the effective cost, and they change it by different factors for different models.

*Consequence.* Ranking models by advertised price is not a ranking by cost. This survey computes cost per accepted task where the inputs are available, and states when they are not.

*Mitigation.* Cost formulas and their required inputs are defined in [docs/15-token-economics.md](docs/15-token-economics.md) and implemented in `scripts/calculate_token_costs.py`.

### 3.2 Latency is not a property of a model

Measured latency depends on the serving stack, the region, concurrency, batch policy, the prompt and output lengths, and network path. The same model weights served by two providers can differ substantially in time to first token and tokens per second.

*Consequence.* A latency figure without its measurement conditions is uninterpretable, and a latency comparison across providers measures the serving infrastructure at least as much as the model.

*Mitigation.* Latency rows record percentile, concurrency, region, prompt and output length, and date, per [docs/evaluation/latency-methodology.md](docs/evaluation/latency-methodology.md).

### 3.3 Price volatility

API prices, cached-input discounts, batch discounts, and rate limits change without notice and are frequently reduced.

*Consequence.* Every price in this repository is a dated historical record. It is not a statement about the current price and must not be used for budgeting without re-verification.

### 3.4 No paid evaluation in continuous integration

The validation and generation scripts depend on no paid API. This repository therefore does not itself produce new measurements of commercial models.

*Consequence.* Grade A evidence for closed-weight models depends entirely on third parties choosing to publish reproducible measurements.

*Mitigation.* [docs/evaluation/internal-bakeoff.md](docs/evaluation/internal-bakeoff.md) specifies a protocol a reader can execute at their own cost, with results contributable back to the repository.

## 4. Limits of environmental measurement

### 4.1 No universal energy figure exists

Energy per token depends on hardware generation, numerical precision, batch size, sequence length, utilisation, and serving framework. A single number attached to a model name is not a measurement of anything.

*Consequence.* This repository publishes no universal per-model energy value. Every energy figure is bound to the eleven conditions listed in [research-methodology.md](research-methodology.md#64-energy-claims), and figures whose conditions differ are not compared.

### 4.2 Inference energy for commercial APIs is unobservable

The caller of a commercial API cannot observe the serving hardware, the batch composition, or the utilisation at the time of the call, and providers do not publish them.

*Consequence.* Per-token energy for commercial APIs can be bounded by assumption but not measured. Any published figure of this kind is an estimate resting on assumptions that should be stated and are usually not.

*Mitigation.* Estimates are recorded as estimates, with their assumptions in the row, and are graded no higher than the disclosure they rest on.

### 4.3 Boundary selection dominates the result

Whether a figure counts accelerator energy alone, or adds host energy, networking, storage, cooling, and embodied emissions, changes the result by a large factor. Power usage effectiveness and grid carbon intensity vary by facility and by hour.

*Consequence.* Two correctly computed figures for the same workload can differ substantially because they draw the accounting boundary differently. Comparison requires that the boundary be stated.

*Mitigation.* The accounting boundary is defined explicitly in [docs/16-energy-use.md](docs/16-energy-use.md) and recorded per row in `data/energy-studies.csv`.

### 4.4 Water and embodied emissions are poorly disclosed

Water consumption for cooling and embodied emissions from manufacturing are rarely reported at a granularity that permits attribution to a model or a query.

*Consequence.* Statements about water or embodied cost per query are, at present, estimates with wide and often unquantified uncertainty. Where the evidence does not support a figure, this repository records `Insufficient independent evidence`.

### 4.5 Rebound effects are out of scope

Efficiency improvements per token do not straightforwardly reduce total consumption, because they alter demand. This survey measures per-unit quantities and does not model system-level demand response.

## 5. Limits of this survey as an artefact

### 5.1 Not peer reviewed

This repository is a maintained survey, not a peer-reviewed publication. It has no external review process beyond pull-request review by its maintainers.

*Consequence.* Cite the primary sources recorded in `data/sources.csv` in preference to citing this repository. Where this repository is cited, cite the commit hash and the access date.

### 5.2 Single-reviewer extraction

Records are extracted by one contributor and checked at review, rather than double-extracted by independent coders as a formal systematic review requires.

*Consequence.* Extraction error is possible and is mitigated only by the automated validation layer and the source-correction process.

### 5.3 Recency decay

Every model profile, comparison table, and price begins to age on the day it is written. The repository states a cut-off date at file level precisely because different files decay at different rates.

*Consequence.* A file whose cut-off date is distant from the reader's date should be treated as a historical record. Check [CHANGELOG.md](CHANGELOG.md) for the date of the last substantive revision.

### 5.4 Scope exclusions

Image-only and video-only generative models, speech synthesis, embedding and reranking models outside retrieval pipelines, fine-tuning recipes, training-infrastructure engineering, and commercial negotiation are all out of scope. Conclusions drawn here do not extend to them.

### 5.5 Language and regional coverage

Benchmark coverage in the published literature is concentrated in English and, to a lesser degree, in a small set of high-resource languages. Tokenizer efficiency and evaluation coverage are both worse for low-resource languages.

*Consequence.* Statements about capability and about cost per task generalise least well to the languages that are least represented in the evidence base, which is the opposite of what an equitable survey would achieve. This is a property of the available literature that this survey documents in [docs/benchmarks/multilingual.md](docs/benchmarks/multilingual.md) rather than one it can correct.
