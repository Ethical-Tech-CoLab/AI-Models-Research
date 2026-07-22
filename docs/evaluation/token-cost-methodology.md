# Token cost methodology

> **Research cut-off date: 2026-07-22.**
> **Status: Phase 2, not yet written.** This file states the scope of the work, the arguments it owns, and the research required to complete it. It contains no findings, because none have been sourced. See [the changelog](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/CHANGELOG.md) for phase status.


## Scope

Specifies how token volumes are measured and how costs are computed from them: which token classes are counted, how cached tokens are identified, how reasoning tokens are obtained when they are hidden, how tool tokens are attributed, and how the acceptance rate is established. The reference implementation is `scripts/calculate_token_costs.py`.

## Research checklist

- [ ] Specify the source of each token count: provider usage response, local tokenizer, or estimate, and require the source to be recorded.
- [ ] Specify how to handle providers that do not report reasoning token counts.
- [ ] Specify the acceptance rate measurement procedure and its sample size.
- [ ] Verify every formula against the script and state that a discrepancy is a defect in the document, not in the script.

## Completion criteria

This file is complete when every checklist item above is closed and the quality-control checklist in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#8-quality-control) passes.
