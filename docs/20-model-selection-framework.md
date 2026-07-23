# Model selection framework

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

This chapter converts the handbook into a procedure. Given a task specification, a quality bar, a latency budget, a cost ceiling, and a deployment constraint, it produces a shortlist and an evaluation plan. It does not produce a recommendation, because construct validity cannot be established on a reader's behalf.

Developed elsewhere: running the evaluation in [internal bakeoff](evaluation/internal-bakeoff.md); cost arithmetic in [15. Token economics](15-token-economics.md); the generated matrix in [model selection matrix](comparisons/model-selection-matrix.md).

## 1. Start from failure cost

The control posture is set by what a wrong answer costs, before any model is considered.

| Risk tier | Examples | Minimum control posture |
|---|---|---|
| Low | Drafting, brainstorming, rewriting | Fast low-cost model, light validation |
| Moderate | Internal summarisation, extraction, analytics assistance | Schema validation, citations, sampled human review |
| High | Public research, financial analysis, legal support, code deployment | Strong model, source verification, tests, approvals |
| Critical | Clinical decisions, autonomous transactions, safety systems | Narrow validated system, expert oversight, formal governance |

## 2. The cascade

Constraints first, capability second, cost third. Each stage eliminates candidates; none of them ranks survivors.

1. **Eliminate on constraints.** Privacy, data residency, licence, deployment mode, and modality support. A model that cannot legally or technically be used is not a candidate at any price.
2. **Eliminate on capability floor.** Does the shortlist clear the quality bar on your own evaluation set? Not on a published benchmark, on yours.
3. **Order on cost per accepted task.** Only among survivors, and only with the acceptance criterion stated.
4. **Check latency at the required percentile** under expected concurrency, not at the default.
5. **Re-evaluate on a schedule**, because endpoints and prices change.

## 3. Weighted criteria

Where a formal scoring model is required, these weights are a starting point to be argued rather than adopted.

| Criterion | Typical weight | Measurement |
|---|---|---|
| Verified task quality | 25 to 40 percent | Local golden set, end-to-end success, expert review |
| Factual reliability | 10 to 25 percent | Claim support, calibration, abstention, citation accuracy |
| Latency | 5 to 20 percent | p50 and p95 time to first token and completion time |
| Token and tool cost | 5 to 20 percent | Cost per accepted task |
| Energy efficiency | 5 to 15 percent | Joules per accepted task, or a declared proxy |
| Privacy and security | 10 to 25 percent | Retention, region, access controls, prompt injection resistance |
| Deployment control | 5 to 20 percent | Open weights, fine-tuning, version pinning, observability |

## 4. Architecture patterns

The right system is frequently not one model.

| Pattern | Design | Best fit |
|---|---|---|
| Cascade | A small model handles easy cases; a frontier model handles escalations | High-volume mixed-difficulty workloads |
| Router | A classifier selects model, tools, and reasoning budget | Multiple task types under a cost constraint |
| Generator and verifier | One model produces, another checks claims or execution | High error cost with verifiable outputs |
| Retrieval-grounded | The model answers only from a controlled evidence set | Research, policy, legal, enterprise knowledge |
| Human in the loop | A person approves uncertain or consequential actions | High-stakes decisions and transactions |
| Local plus cloud | A private local model handles sensitive data; a cloud model handles de-identified hard tasks | Sovereignty and privacy constraints |

An adaptive system that varies model size, reasoning budget, context, and tool use by difficulty can improve quality per unit of cost and energy. It also creates an evaluation problem: the object being evaluated becomes a dynamic policy rather than a model, and the resource budget must be reported in full, including hidden reasoning, retries, verification, and tool calls.

## 5. The rule this chapter exists to enforce

No model is selected on a published benchmark. The benchmark narrows the candidate set; a local evaluation selects. The handbook can tell you what has been measured, under what conditions, and by whom. It cannot tell you whether that transfers to your task, and any document that claims otherwise is selling something.

## 6. Open research questions

- What sample size distinguishes two models at a stated effect size on a typical procurement task?
- Do weighted scoring models produce more defensible selections than a constraint cascade, or only more auditable ones?
- How should an adaptive routing policy be evaluated when its behaviour depends on traffic composition?
