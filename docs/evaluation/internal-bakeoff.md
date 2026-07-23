# Internal bakeoff protocol

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

A protocol for comparing models under production-like conditions. This repository runs no paid evaluations, so this protocol is the route by which Grade A evidence for closed-weight models can enter it: a reader executes it, records the conditions, and contributes the result.

## 1. Why a local evaluation is not optional

Published benchmarks narrow a candidate set. They do not establish that performance transfers to your task, your prompts, your documents, your languages, or your acceptance criterion. Every ranking in this handbook is conditioned on evaluation settings that are not yours.

## 2. Protocol

| Element | Requirement |
|---|---|
| Dataset | At least 200 representative cases for a moderate-risk workflow, stratified by difficulty, language, input length, and source quality |
| Models | Pin exact model identifiers and dates. Record region, service tier, reasoning level, temperature, and maximum output |
| Prompts | One frozen production prompt per task, plus a small prompt-robustness set |
| Tools | Identical retrieval, browser, code, and database capability across models, or the differences reported explicitly |
| Trials | At least three trials for stochastic tasks, more for high-variance agents |
| Quality | Deterministic checks where possible, blinded expert review for open-ended output |
| Factuality | Decompose responses into claims and verify support, not overall impression |
| Latency | Record time to first token, generation time, tool time, and end-to-end time at p50 and p95 |
| Cost | Record uncached input, cached input, output, reasoning, tool fees, retries, and human review time |
| Energy | For self-hosted systems measure wall power or accelerator plus host power. For APIs use provider disclosure or a clearly labelled proxy |
| Acceptance | Define the pass threshold before testing. Report cost and energy only after dividing by accepted outputs |
| Governance | Log prompts, outputs, tools, model version, reviewer decision, and the reason for each failure |

## 3. Procedure

1. **Define the task contract.** Inputs, allowed tools, required output, prohibited behaviour, latency target, and error tolerance.
2. **Build the evaluation set.** Common cases, difficult cases, long inputs, multilingual cases, adversarial inputs, and known historical failures.
3. **Run controlled comparisons.** Hold prompts, tools, reasoning budget, sampling, and validation constant, or report what differed.
4. **Measure end-to-end outcomes.** Success, unsupported claims, tokens, cost, latency, retries, tool calls, and human correction time.
5. **Test reliability.** Repeat across runs and prompt variants. Inspect variance, not only the mean.
6. **Evaluate safety and governance.** Data leakage, prompt injection, permission boundaries, refusal behaviour, and audit logs.
7. **Pilot with monitoring.** Limited traffic, canary versions, rollback, and a clear escalation path.
8. **Re-evaluate continuously.** Pin versions and rerun the suite before any upgrade.

## 4. Contributing a result

A contributed result enters `data/benchmarks.csv` only with harness, sampling policy, tool permissions, evaluation date, and reporting party. A result missing those is recorded with them marked unstated, and is thereby excluded from ranked comparison. Use the [benchmark update issue template](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/.github/ISSUE_TEMPLATE/benchmark-update.md).

## 5. Open research questions

- What sample size distinguishes two models at a stated effect size for a typical procurement task?
- What inter-rater agreement is achievable on blinded expert review of open-ended output?
- How should the acceptance criterion be specified so that two teams applying it to identical outputs agree?
