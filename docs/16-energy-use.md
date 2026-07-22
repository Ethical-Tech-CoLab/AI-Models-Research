# Energy use

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.

## Scope

Establishes what may and may not be said about the energy cost of AI models. Defines the accounting boundary explicitly, covering direct accelerator energy, host energy, networking, storage, cooling and power usage effectiveness, grid carbon intensity, embodied emissions, and water consumption. Distinguishes training energy from inference energy and per-token from per-query and per-accepted-task measures. Answers research question RQ9. Publishes no universal per-model energy value.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The accounting boundary definition used throughout the repository.
- The eleven conditions required of any energy figure.
- The energy and carbon formulas.
- The argument that boundary selection, not model choice, dominates differences between published figures.

## Developed elsewhere

- Measurement protocol: [evaluation/energy-methodology.md](evaluation/energy-methodology.md)
- Hardware characteristics: [17-hardware-and-memory.md](17-hardware-and-memory.md)
- Rebound effects and system-level demand: [https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/limitations.md](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/limitations.md)

## Research checklist

- [ ] Cite the training-energy and inference-energy literature separately; do not generalise a training figure to inference.
- [ ] Populate data/energy-studies.csv with every published measurement that states all eleven conditions; exclude those that do not and record the exclusion.
- [ ] Source grid carbon intensity per region from the International Energy Agency or a national grid operator, with the measurement period.
- [ ] State the water-consumption evidence position explicitly, including where it is 'Insufficient independent evidence'.
- [ ] Add the Mermaid diagram of the energy accounting boundary.
- [ ] Verify the formulas against the appendix and confirm no figure in the chapter lacks its conditions.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
