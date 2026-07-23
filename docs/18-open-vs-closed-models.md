# Open versus closed models

> **Research cut-off date: 2026-07-22.**
> **Status: written.**

## Scope

This chapter examines what separates downloadable weights from API-only access along the dimensions that matter for research and deployment. It answers research question RQ11.

Developed elsewhere: the effect on evidence availability in the [limitations document](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/limitations.md); privacy and retention in [19. Security and privacy](19-security-and-privacy.md); selection consequences in [20. Model selection framework](20-model-selection-framework.md).

## 1. Openness is a spectrum of separable artefacts

Weights, training data, training code, evaluation code, and licence terms are released independently of one another. Open weights and open source are different claims: parameters can be downloadable under a licence that restricts use, redistribution, or field of application, while training data and code remain unpublished.

`data/models.csv` records the licence name and a link to the licence text where the source stated them. For several open-weight families in this survey the licence name was not extracted and is recorded as not publicly disclosed, which is a gap in this revision rather than in the provider's disclosure.

## 2. The strategic case for open weights

Open-weight families support local deployment, privacy, fine-tuning, and hardware-level optimisation. Their advantage depends less on benchmark parity than on the ability to optimise the whole stack: quantization, retrieval, domain fine-tuning, caching, and hardware. Research on local inference treats that stack as the object of study rather than the model alone.[^bench3602025local] Work on edge deployment reaches a similar conclusion about where the constraints actually sit.[^seas2025edge]

Deployment targets recorded in this survey are concrete. Mistral Medium 3.5 is described as self-hostable on as few as four GPUs, without a stated GPU model or precision.[^mistral2026medium] Llama 4 Scout is described with an INT4 deployment target of a single H100, and Llama 4 Maverick with a single-host H100 target.[^meta2025llama] Those are provider statements about their own products and are Grade B; neither has been independently reproduced for this survey.

## 3. The verification asymmetry

Open-weight models can be downloaded, instrumented, and measured. Memory footprint, throughput, quantization behaviour, and energy per token are directly observable. Closed-weight models cannot be measured in any of those respects; the caller observes latency and price at the API boundary and nothing else.

Grade A evidence is therefore systematically more available for open-weight models. Any aggregate statement that open-weight models are better characterised reflects data availability rather than model behaviour. That asymmetry is developed in the limitations document and is not restated here.

## 4. What closed access buys

Hosted frontier models retain advantages in integrated tools, rapid updates, and breadth of capability. What they cost the buyer is version stability and auditability: an endpoint can change without notice, and no independent party can profile the model. Buyers who need reproducibility should demand version pinning and change notification as contractual terms rather than assume them.

## 5. Open research questions

- Which providers publish a deprecation and retirement policy, and how much notice do they give?
- Does any independent evaluation of an open-weight model reproduce the provider's own hardware claims?
- What licence restrictions in the open-weight families actually bind a research or commercial use, as opposed to appearing to?
- How should a survey compare a downloadable artefact with a served endpoint without the comparison being dominated by data availability?

## Sources

[^bench3602025local]: Bench360 authors (2025). Bench360: benchmarking local LLM inference from 360 degrees. Preprint. Grade B. Accessed 2026-07-22.

[^seas2025edge]: Harvard John A. Paulson School of Engineering and Applied Sciences (2025). Generative AI at the edge: challenges and opportunities. Grade B, institutional. Accessed 2026-07-22.

[^mistral2026medium]: Mistral AI (2026). Mistral Medium 3.5 and remote agents. Grade B, official documentation. Accessed 2026-07-22.

[^meta2025llama]: Meta (2025). The Llama 4 herd: natively multimodal open-weight models. Grade B, official technical report. Accessed 2026-07-22.
