# Security and privacy

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Covers the security and privacy properties that bear on model selection: data retention and training-use terms for commercial APIs, regional processing and residency, prompt injection and tool-use exposure in agent deployments, training-data extraction and memorisation, and the deployment options that change the threat model. Records commercial terms as dated snapshots, since they change without notice.

## Arguments this chapter owns

Other files link here rather than restating these. Duplicated argumentation is a defect under the writing standards, not redundancy for the reader's convenience.

- The threat model for model-mediated systems as it bears on selection.
- The distinction between provider policy, contractual commitment, and technical control.
- Dated records of data retention and training-use terms per provider.

## Developed elsewhere

- Agent scaffold failure modes: [07-agentic-ai.md](07-agentic-ai.md)
- Deployment options: [18-open-vs-closed-models.md](18-open-vs-closed-models.md)

## Research checklist

- [ ] Record data retention period, training-use default, and opt-out mechanism per provider, each with a URL and an access date.
- [ ] Cite the memorisation and extraction literature rather than describing the risk generically.
- [ ] Record regional processing and residency options per provider where documented.
- [ ] State explicitly that these terms are dated snapshots and must be re-verified before any procurement decision.

## Completion criteria

This chapter is complete when every checklist item above is closed, when every numerical claim carries a footnote resolving to `data/sources.csv`, when every claim about a current model carries an absolute date, and when the twelve-point quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
