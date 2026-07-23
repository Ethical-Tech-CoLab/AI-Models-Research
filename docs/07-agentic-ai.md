# Agentic AI

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

This chapter covers models used inside action loops, and the measurement problem that follows from it: a published agent result is a property of a model-and-scaffold pair, not of a model. It answers research question RQ5.

Developed elsewhere: benchmark construction in [agent and computer-use benchmarks](benchmarks/agents-and-computer-use.md); context exhaustion in [11. Long context](11-long-context.md); tool-call token cost in [15. Token economics](15-token-economics.md).

## 1. The scaffold problem

An agent plans, calls a tool, observes the result, updates state, and continues until a stopping condition. The scaffold that manages tools, context, retries, and termination is doing a substantial share of the work, and it is rarely described in enough detail to reproduce.

The consequence for evidence is direct: a result attributed to a model was produced by a system, and two evaluations of the same model under different scaffolds are not comparable. Every agent result recorded in `data/benchmarks.csv` therefore carries the reporting party in its own column, and rows without a scaffold description are marked unstated.

## 2. Where agents stand against human performance

The Stanford AI Index reports best model results against human baselines on interactive benchmarks. On OSWorld, which tests computer use in realistic desktop environments, the best reported model result was 66.3 percent against a human baseline of 72.35 percent. On WebArena, which tests web navigation and task completion, the best reported result was 74.3 percent against a human baseline of 78.24 percent. Terminal-Bench 2.0 reached 77.3 percent, and Vibe Code Bench, which measures end-to-end application construction, reached about 57.6 percent.[^stanford2026aiindex]

Two readings follow. Agents approach human performance on these benchmarks without consistently exceeding it. And the ordering across benchmarks shows that building a functioning application remains materially harder than completing an isolated task, which is what a long-horizon workload actually requires.

Human scores are frequently measured under different time, tool, and incentive conditions than model scores, so the gap is indicative rather than exact. That caveat is owned by the AI Index itself and is restated here because the numbers are meaningless without it.

The [interactive companion](interactive/index.html) presents this comparison with the human baselines marked.

## 3. Why small error rates compound

Production systems fail through sequences of small errors rather than single wrong answers. An agent that is reliable per step can still fail end to end, because per-step accuracy multiplies across a trajectory. That is why a few percentage points on a long-horizon benchmark matter more than the same gap on a single-answer test, and why per-step accuracy is the wrong thing to optimise on its own.

The failure surface for computer-use agents specifically includes visual misperception, stale page state, hidden confirmation steps, prompt injection, permission errors, and irreversible actions.

## 4. Controls for consequential actions

High-impact actions require confirmation, scoped credentials, transaction limits, logging, and a recovery path. These are architecture decisions rather than model decisions, and no model choice substitutes for them.

## 5. Open research questions

- What is the relationship between per-step accuracy and end-to-end success as step count grows?
- Does any Grade A evidence link agent benchmark performance to deployed reliability?
- How much of the variation between reported agent results is scaffold rather than model?
- How should a benchmark represent recovery from a failed action, which production systems depend on and current scoring largely ignores?

## Sources

[^stanford2026aiindex]: Stanford Institute for Human-Centered Artificial Intelligence (2026). AI Index Report 2026, Technical Performance chapter. Grade B, institutional compilation. Values are snapshots, not permanent rankings. Accessed 2026-07-22.
