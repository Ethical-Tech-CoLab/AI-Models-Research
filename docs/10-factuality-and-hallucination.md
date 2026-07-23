# Factuality and hallucination

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

This chapter separates the distinct phenomena that the word hallucination is used for, explains how each is measured, and states why a single hallucination rate for a model is not a well-defined quantity. It answers research question RQ3.

Developed elsewhere: benchmark construction in [factuality benchmarks](benchmarks/factuality.md); retrieval as a mitigation in [13. Inference](13-inference.md); the effect on selection in [20. Model selection framework](20-model-selection-framework.md).

## 1. Four different accuracy problems

| Type | Question | How it is evaluated |
|---|---|---|
| Parametric factuality | Is the answer correct from internal model knowledge? | Closed-book factual question answering |
| Groundedness | Does every material claim follow from the supplied sources? | Claim-level entailment against provided evidence |
| Procedural correctness | Did the model follow the required method and constraints? | Schema validation, unit tests, workflow checks |
| Epistemic behaviour | Does the model recognise when evidence is insufficient? | Calibration, selective accuracy, abstention |

Google DeepMind's factuality programme separates grounding, parametric knowledge, search, and multimodal evidence rather than reporting one rate.[^deepmind2024facts] [^deepmind2025factssuite] That separation is the right default, because a model can fail differently in each setting: search reduces stale-knowledge errors while introducing source selection, citation, and synthesis errors, and retrieval improves grounding while still failing when evidence is contradictory or dispersed.

## 2. Evidence from hard domains

HalluHard evaluates 950 difficult multi-turn conversations in legal, research, medical, and coding settings, and checks whether cited material actually supports the generated claims. The strongest web-enabled configuration tested still hallucinated on about 30 percent of conversations, and rates without web access were substantially higher.[^fan2026halluhard] The same work reports that early errors can cascade as a conversation lengthens, which makes multi-turn reliability a property of the system rather than of a single answer.

Software generation carries a distinct and concrete risk. Research at NYU's OSIRIS Lab on package hallucination, in which a model recommends dependencies that do not exist, found invented package names in roughly 4.6 to 6.1 percent of tested package suggestions across frontier systems, with some fabricated names recurring across models.[^osiris2026package] That is a supply-chain exposure rather than a quality nuisance: a name that several models hallucinate can be registered by an attacker and then installed by automation.

## 3. Calibration and abstention

Fluency is not calibration. Confidence can be expressed through verbal hedging, an explicit probability, token log-probabilities, agreement across samples, or a separate verifier, and these signals do not always agree with one another.[^bowman2023eight] Uncertainty estimators can correlate weakly with actual hallucination depending on the error type and the model, so a production system should validate its uncertainty signal against its own domain rather than assume a confident model is right or an uncertain one is wrong.

## 4. Reliability is a system property

No model choice removes the need for the following controls, and they matter more than the choice itself.

| Control | Implementation objective |
|---|---|
| Retrieval with provenance | Retrieve a small evidence set, preserve source identifiers, require claim-level citation |
| Constrained generation | Schemas, grammars, enumerated values, and deterministic validators wherever possible |
| Verification | Run the calculation, the code, the query, or the citation check against the first output |
| Selective escalation | Route low-confidence, high-risk, or contradictory cases to a stronger model or a human |
| Abstention policy | Define when the system must say the evidence is insufficient, and what would resolve it |
| Version control | Pin model snapshots and rerun regression evaluations before an upgrade |
| Adversarial evaluation | Test prompt injection, conflicting documents, missing evidence, and long-context distractors |

## 5. What this repository records

`data/benchmarks.csv` holds no factuality results at this revision. The generated table in [factuality benchmarks](benchmarks/factuality.md) is therefore empty, and states that rather than presenting a blank table as an absence of failures.

The reason is the grounding condition. A grounded and a closed-book measurement answer different questions, and the sources used for this revision report rates without stating the condition in a form that could be recorded per model. Recording them anyway would create exactly the single hallucination rate this chapter argues does not exist.

## 6. Open research questions

- Are grounded and closed-book hallucination rates for the same model ever reported under compatible conditions?
- Do any providers publish an abstention or calibration measurement for their own models?
- What is the current package hallucination rate under a fixed prompt set, and is it falling?
- Does claim-level citation checking reduce measured hallucination, or move it into citation selection?

## Sources

[^deepmind2024facts]: Google DeepMind (2024). FACTS Grounding: a benchmark for evaluating factuality. Grade B, benchmark methodology from the maintaining organisation. Accessed 2026-07-22.

[^deepmind2025factssuite]: Google DeepMind (2025). FACTS Benchmark Suite. Grade B, benchmark methodology. Accessed 2026-07-22.

[^fan2026halluhard]: Fan, D., Delsad, S., Flammarion, N., and Andriushchenko, M. (2026). HalluHard: a hard multi-turn hallucination benchmark. Preprint. Grade B. Accessed 2026-07-22.

[^osiris2026package]: NYU OSIRIS Lab (2026). LLM package hallucination research. New York University. Grade B, institutional. The specific replication study should be cited directly once located; see the verification queue. Accessed 2026-07-22.

[^bowman2023eight]: Bowman, S. R. (2023). Eight things to know about large language models. New York University. Grade B. Accessed 2026-07-22.
