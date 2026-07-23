# Energy use

> **Research cut-off date: 2026-07-22.**
> **Status: written.** Every figure below carries its source, its evidence grade, and the conditions under which it was produced. No universal per-model energy value appears anywhere in this chapter, because no such value exists.

## Scope

This chapter establishes what may and may not be said about the energy cost of AI models. It defines the accounting boundary, distinguishes training from inference, sets out the conditions any energy figure must carry, and fixes the reporting unit. It answers research question RQ9.

Developed elsewhere: the measurement protocol in [energy methodology](evaluation/energy-methodology.md); the formulas in the [appendix of formulas](appendices/formulas.md); hardware characteristics in [17. Hardware and memory](17-hardware-and-memory.md); rebound effects and system-level demand in the [limitations document](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/limitations.md).

## 1. Training and inference are separate accounting problems

Training energy is a large, episodic expenditure covering pretraining, post-training, data processing, experimentation, and failed runs. Inference energy is distributed across every production request. A heavily used model can accumulate more inference energy over its service life than its training run consumed, but the crossover point depends on model size, traffic, hardware, utilisation, and service lifetime. None of those are published for commercial endpoints, so the crossover cannot be located for any specific model in this survey.

Neither quantity is interpretable without a stated system boundary.

| Boundary term | What it covers |
|---|---|
| Direct accelerator energy | GPU, TPU, or other accelerator power during model execution |
| Host and network energy | CPU, memory, storage, networking, and interconnect on the serving node |
| Facility overhead | Cooling, power conversion, and distribution, summarised in part by power usage effectiveness |
| Embodied impacts | Manufacture, transport, and replacement of chips, servers, cooling plant, and buildings |
| Water and grid effects | Cooling water, the generation mix, and the time and place of consumption |

Two correctly computed figures for the same workload can differ by a large factor because they draw this boundary differently. A comparison without a stated boundary is not a comparison.

## 2. What the peer-reviewed evidence establishes

### 2.1 Optimisation dominates model choice

Fernandez and colleagues evaluated inference across workloads, hardware, serving frameworks, batching strategies, decoding strategies, and parallelism. They report that estimates derived from floating-point operation counts understate real energy use, and that the benefit of any given optimisation depends on the geometry of the workload. Appropriate combinations of optimisations reduced energy by as much as 73 percent against an unoptimised baseline.[^fernandez2025energy]

That is the strongest argument against attaching a single energy number to a model name. The same weights, on the same hardware, under two serving configurations, are two different energy propositions.

### 2.2 Reasoning budget dominates per-query energy

Oviedo and colleagues built a bottom-up estimate for frontier-scale inference. Under stated H100 utilisation and power usage effectiveness assumptions, the median estimate was 0.34 watt-hours for a representative query, with an interquartile range of 0.18 to 0.67 watt-hours; raising token use by a factor of 15 to model test-time scaling raised the median to 4.32 watt-hours, roughly 13 times higher, and combined model, serving, and hardware improvements were estimated to offer an 8 to 20 times efficiency opportunity.[^oviedo2026energy]

These are analytical estimates, not measurements of a named commercial service. They are Grade A because the methodology is disclosed and the work is peer reviewed, not because a meter was attached to a production endpoint. No such reading is public for any commercial API in this survey.

The [interactive companion](interactive/index.html) presents both scenarios. It toggles between them rather than sliding, because the source states two points and the values between them are not sourced.

The direction of that finding is corroborated by work on the energy cost of test-time compute, which reports that extended reasoning raises consumption substantially.[^jin2025energy]

### 2.3 Sector totals do not divide into per-query figures

The International Energy Agency projects global data-centre electricity consumption reaching about 945 terawatt-hours in 2030 in its base case, roughly double the 2024 level.[^iea2025energy] It reports that data-centre electricity demand grew 17 percent in 2025, with AI-focused facilities growing faster.[^iea2026keyquestions]

That aggregate covers every data-centre workload, not AI queries alone, and utilisation patterns differ across them. Dividing it by a presumed query count produces a figure with no defensible denominator. This handbook does not perform that division and treats any number derived that way as unsupported.

## 3. Why energy per token varies

| Driver | Mechanism |
|---|---|
| Architecture | Dense against mixture-of-experts, active parameter count, attention sparsity, key-value cache design |
| Precision | Full, half, and reduced-precision formats, and mixed-precision kernels |
| Input length | Long prefill raises compute and memory traffic |
| Output length | Decoding re-executes the model for every generated token |
| Batch and concurrency | Higher utilisation can lower energy per token while raising per-request latency |
| Hardware generation | Newer accelerators change throughput per watt and memory bandwidth |
| Serving software | Kernel fusion, speculative decoding, continuous batching, quantization, caching |
| Reasoning policy | More reasoning and self-consistency sampling produce more tokens |
| Acceptance rate | Rejected outputs and retries consume energy without producing useful work |

The last row is the one most often omitted. Energy spent on an output that fails a quality check is energy spent for nothing, which is why the reporting unit this handbook prefers is energy per accepted task rather than energy per token.

## 4. Reporting standard

A growing body of systems research argues that energy per token, rather than a single model-level figure, should be the unit of sustainable inference reporting.[^wilhelm2025beyond] [^liu2026position] Benchmark work in the same direction proposes standardised energy-aware evaluation.[^kao2026watt] This handbook adopts that position.

| Metric | Use |
|---|---|
| Joules per input token | Prefill energy divided by input tokens |
| Joules per output token | Decode energy divided by generated tokens |
| Joules per accepted task | Total system energy divided by outputs that pass the quality check |
| Tokens per kilowatt-hour | Throughput-oriented efficiency under a defined workload |
| Facility-adjusted energy | Energy delivered to computing equipment multiplied by power usage effectiveness |
| Carbon per accepted task | Energy multiplied by time-specific and location-specific grid intensity |
| Water per accepted task | Direct cooling and generation-related water under a declared method |

Each is defined once in the [appendix of formulas](appendices/formulas.md).

### 4.1 The eleven conditions

No energy figure is published in this repository without all eleven of the following. `scripts/validate_tables.py --check-energy` enforces their presence on every row of `data/energy-studies.csv` and rejects a row whose condition is recorded as unstated.

1. Hardware
2. Model version
3. Numerical precision
4. Prompt length
5. Output length
6. Batch size
7. Utilisation
8. Serving framework
9. Power usage effectiveness
10. Measurement or estimation method
11. Uncertainty

## 5. Recorded measurements

`data/energy-studies.csv` is empty at this revision, and that is a finding rather than an omission.

The two Grade A studies above are the strongest inference-energy evidence located for this survey, and neither restates all eleven conditions in a form this survey could transcribe without reading the full papers. Recording them with conditions marked absent would place figures in a machine-readable dataset that the handbook's own comparison rules would then forbid anyone from using. The findings therefore appear in prose above, with their assumptions attached, and the dataset row waits until the primary papers are read and the conditions extracted.

This is registered as an open data gap in [21. Research gaps](21-research-gaps.md).

## 6. What cannot be established

1. **Per-token energy for any commercial API.** The caller cannot observe serving hardware, batch composition, or utilisation, and no provider in this survey publishes them. Estimates can bound the quantity; they cannot measure it.
2. **Model-specific disclosure.** No provider covered here publishes measured joules per token under a standardised workload, alongside utilisation, power usage effectiveness, embodied emissions, or water consumption.
3. **Water and embodied emissions per query.** Neither is reported at a granularity permitting attribution to a model or a request. Both are recorded as `Insufficient independent evidence`.
4. **Training energy for most models.** Published for almost none of the families profiled here.

## 7. Open research questions

- Do any two independent parties measure the same open-weight model under the same eleven conditions, so that a reproducibility claim can be made at all?
- What is the ratio of lifetime inference energy to training energy for a served model, and is any provider willing to publish the request volume that would let it be computed?
- How much of the efficiency opportunity identified by Oviedo and colleagues has been realised in deployed systems, and how would an outside party verify it?[^oviedo2026energy]
- Does energy per accepted task, rather than energy per token, reverse the ordering between a small model with retries and a large model without them?

## Sources

[^fernandez2025energy]: Fernandez, J., Na, C., Tiwari, V., Bisk, Y., Luccioni, S., and Strubell, E. (2025). Energy considerations of large language model inference and efficiency optimizations. *Proceedings of ACL 2025*. Grade A, peer reviewed. Accessed 2026-07-22.

[^oviedo2026energy]: Oviedo, F., Kazhamiaka, F., Choukse, E., Kim, A., Luers, A., Nakagawa, M., Bianchini, R., and Lavista Ferres, J. M. (2026). Energy use of AI inference: efficiency pathways and test-time compute. *Joule*. Grade A, peer reviewed. Analytical estimates, not measurements of a named commercial service. Accessed 2026-07-22.

[^jin2025energy]: Jin, Y., Wei, G.-Y., and Brooks, D. (2025). The energy cost of reasoning: analyzing energy usage in LLMs with test-time compute. Preprint. Grade B. Accessed 2026-07-22.

[^iea2025energy]: International Energy Agency (2025). *Energy and AI: energy demand from AI*. Grade B, institutional. Accessed 2026-07-22.

[^iea2026keyquestions]: International Energy Agency (2026). *Key questions on energy and AI*. Grade B, institutional. Accessed 2026-07-22.

[^wilhelm2025beyond]: Wilhelm, P., Wittkopp, T., and Kao, O. (2025). Beyond test-time compute strategies: advocating energy-per-token in LLM inference. *EuroMLSys 2025*. Grade A, peer reviewed. Accessed 2026-07-22.

[^liu2026position]: Liu, X., and others (2026). Position: LLM inference should be evaluated as energy-to-token production. Preprint. Grade B. Accessed 2026-07-22.

[^kao2026watt]: Kao, O., and others (2026). Watt Counts: energy-aware benchmark for sustainable LLM inference. Preprint. Grade B. Accessed 2026-07-22.
