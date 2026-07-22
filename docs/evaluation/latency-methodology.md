# Latency measurement methodology

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Specifies how a latency measurement in this repository is produced and reported: warm-up policy, request pattern, concurrency levels, prompt and output lengths, percentiles reported, region, client location, and clock methodology. A latency figure that does not carry these conditions is not admitted.

## Research checklist

- [ ] Specify the warm-up and cold-start policy and require it to be reported.
- [ ] Specify which percentiles are mandatory: p50, p90, p95, and p99.
- [ ] Specify how time to first token is measured under streaming, including where the clock starts and stops.
- [ ] Specify the minimum number of requests per configuration and the basis for that minimum.
- [ ] Specify how network path and client location are reported, since they are part of the measurement.

## Completion criteria

This file is complete when every checklist item above is closed and the quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
