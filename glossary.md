# Glossary

> **Research cut-off date: 2026-07-22.**

Definitions of terms and acronyms used across this repository. Entries are definitional and deliberately free of quantities: any number belongs in a chapter with a citation, not in a glossary. Domain-specific glossaries for benchmarks and hardware are in [docs/appendices/benchmark-glossary.md](docs/appendices/benchmark-glossary.md) and [docs/appendices/hardware-glossary.md](docs/appendices/hardware-glossary.md).

Where a term has more than one meaning in common use, the meaning used in this repository is stated first and the alternative is noted.

## A

**Accelerator.** A processor specialised for the dense linear algebra of neural network training and inference, such as a GPU, TPU, or dedicated inference chip. Contrasted with the host CPU that schedules work onto it.

**Active parameters.** In a mixture-of-experts model, the number of parameters used to process a single token, which is smaller than the total parameter count. Determines inference compute per token; total parameters determine memory footprint.

**Agent.** A system in which a model iteratively selects actions, observes their results, and continues until a stopping condition. Distinguished from single-turn generation by the presence of a loop and of external effects.

**ALiBi.** Attention with Linear Biases. A positional method that applies a distance-dependent penalty to attention scores rather than adding positional embeddings.

**Attention.** The operation by which a token's representation is updated as a weighted sum over other tokens' representations, with weights computed from query and key projections.

**Autoregressive decoding.** Generating a sequence one token at a time, conditioning each token on all preceding tokens.

## B

**Batching.** Processing several requests together so that a single pass over the model weights serves all of them. Raises throughput and hardware utilisation; can raise latency for an individual request. See *continuous batching*.

**BPE.** Byte-pair encoding. A subword tokenization algorithm that iteratively merges the most frequent adjacent symbol pair, producing a vocabulary of variable-length units.

**Byte-level tokenization.** Tokenization over raw bytes rather than Unicode characters, which guarantees that any input is representable without an unknown-token symbol.

## C

**Cached tokens.** Input tokens whose intermediate representations were retained from a previous request and are reused rather than recomputed. Usually billed at a reduced rate. See *prefix caching*.

**Carbon intensity.** Mass of carbon dioxide equivalent emitted per unit of electrical energy consumed, specific to a grid, a location, and a time.

**Causal attention.** Attention masked so that a position may attend only to itself and to earlier positions, which is what permits autoregressive generation.

**Chain of thought.** Generation of intermediate reasoning steps before a final answer.

**Cold start.** The first request served by a newly initialised worker, which includes weight loading and cache warming and is therefore slower than subsequent requests.

**Compaction tokens.** Tokens consumed when a long conversation or agent trajectory is summarised to fit within a context window. A cost that recurs over a session and is frequently omitted from cost estimates.

**Concurrency.** The number of requests in flight simultaneously against a serving endpoint. A necessary condition on any latency or throughput measurement.

**Context window.** The maximum number of tokens a model may attend over in a single request, counting input and, depending on the provider's accounting, output. See *effective context* for the distinction between the advertised and the usable length.

**Continuous batching.** A serving policy in which new requests join a running batch as earlier requests complete, rather than waiting for a fixed batch to be assembled.

**Contamination.** Presence of benchmark test items, or close variants, in a model's training data, which inflates measured performance without a corresponding capability.

## D

**Decode phase.** The stage of inference that generates output tokens one at a time. Bound by memory bandwidth rather than by arithmetic throughput. Contrasted with *prefill*.

**Dense model.** A model in which every parameter participates in processing every token. Contrasted with *mixture of experts*.

**Distillation.** Training a smaller model to reproduce the behaviour of a larger one, using the larger model's outputs or internal signals as the training target.

**DPO.** Direct Preference Optimization. A preference-tuning method that optimises a model against preference pairs directly, without training a separate reward model or running a reinforcement learning loop.

## E

**Effective context.** The context length at which a model retains measurable retrieval and reasoning performance, as distinct from the advertised maximum. Established by evaluation, not by specification.

**Embodied emissions.** Emissions attributable to manufacturing, transporting, and disposing of hardware, as distinct from emissions from operating it.

**Evidence grade.** This repository's three-level classification of source reliability: A independently verified, B institutional primary research, C provider-reported. Defined in [research-methodology.md](research-methodology.md#4-evidence-grading).

**Expert routing.** The mechanism that selects which experts in a mixture-of-experts layer process a given token.

## F

**Few-shot prompting.** Supplying worked examples in the prompt to specify the task, without changing model weights.

**Fine-tuning.** Continued training of a pretrained model on a narrower dataset in order to adapt its behaviour.

**FLOP.** Floating-point operation. Used as the unit of training and inference compute.

## G

**GQA.** Grouped-query attention. An attention variant in which several query heads share one key and value head, reducing key-value cache size relative to multi-head attention.

**GRPO.** Group Relative Policy Optimization. A policy-gradient method that estimates advantage from the relative reward of a group of sampled responses, avoiding a separate learned value model.

**Grounding.** Constraining a model's output to information present in supplied source material, and evaluating whether the output is supported by it.

## H

**Hallucination.** Generation of content presented as factual that is not supported by the model's sources or by the world. In this repository, hallucination is always reported with the benchmark and grounding condition under which it was measured, because the term denotes several distinct measured phenomena.

**Host energy.** Energy consumed by the CPU, memory, storage, and networking of a serving node, excluding the accelerator.

**Hybrid architecture.** A model combining attention layers with layers of a different class, most commonly state-space or recurrent layers.

## I

**Inference.** Executing a trained model to produce outputs. Contrasted with training.

**Input tokens.** Tokens supplied to the model, comprising the system prompt, conversation history, retrieved context, tool definitions, and the user message.

**Instruction tuning.** Supervised fine-tuning on instruction-and-response pairs to make a pretrained model follow directions.

## K

**KV cache.** The stored key and value tensors for tokens already processed, retained so that generating each new token does not require recomputing them. Its size grows with sequence length, batch size, and the number of key and value heads, and it is frequently the binding memory constraint during serving.

## L

**Latency.** Elapsed time to serve a request. Decomposed in this repository into queueing time, prefill time, time to first token, and time per output token.

**Long context.** Operation at input lengths substantially beyond those typical of single-turn use. Treated here as a measured capability rather than a specification.

## M

**Mixture of experts.** An architecture in which each layer contains multiple expert subnetworks and a router activates a subset per token, decoupling total parameter count from per-token compute.

**Model card.** A structured disclosure document describing a model's intended use, training, evaluation, and limitations. Grade B evidence in this repository.

**MQA.** Multi-query attention. An attention variant in which all query heads share a single key and value head. A limiting case of grouped-query attention.

**Multimodal.** Accepting or producing more than one modality, most commonly text with images, audio, or video.

## O

**Open weights.** Model parameters that are downloadable. Distinct from open source: a licence may restrict use, redistribution, or fields of application, and training data and code are usually not released.

**Outcome supervision.** Training a reward signal on the correctness of a final answer only. Contrasted with *process supervision*.

**Output tokens.** Tokens generated by the model, including reasoning tokens where the provider bills them.

## P

**Percentile latency.** Latency at a stated quantile of the request distribution, written p50, p90, p95, or p99. A mean latency without a percentile distribution conceals tail behaviour.

**Prefill phase.** The stage of inference that processes the input prompt and populates the KV cache. Bound by arithmetic throughput and roughly proportional to input length. Contrasted with *decode*.

**Prefix caching.** Reuse of the KV cache for a shared prompt prefix across requests, avoiding recomputation of unchanged leading tokens.

**Process supervision.** Training a reward signal on the correctness of each intermediate reasoning step rather than on the final answer alone.

**PUE.** Power usage effectiveness. Total facility energy divided by energy delivered to computing equipment. A multiplier applied to compute energy to account for cooling and distribution overhead.

## Q

**Quantization.** Representing weights, activations, or KV cache at reduced numerical precision to lower memory footprint and raise throughput, at some cost in accuracy that must be measured rather than assumed.

## R

**RAG.** Retrieval-augmented generation. Retrieving documents at inference time and supplying them in the context so that generation is conditioned on them.

**Reasoning tokens.** Tokens generated as intermediate reasoning before a final answer. May be billed, may be hidden from the caller, and materially change both cost and latency. Whether they are visible and whether they are billed differs by provider and must be recorded per model.

**Rebound effect.** An increase in total consumption that follows an improvement in per-unit efficiency, because the improvement lowers the cost of use and thereby raises demand.

**RLAIF.** Reinforcement learning from AI feedback. Preference training in which the preference labels are generated by a model rather than by human annotators.

**RLHF.** Reinforcement learning from human feedback. Preference training in which a reward model trained on human comparisons supplies the training signal.

**RLVR.** Reinforcement learning with verifiable rewards. Reinforcement learning in which the reward comes from an automatic checker, such as a unit test or a symbolic verifier, rather than from a learned reward model.

**RoPE.** Rotary position embedding. A positional method that encodes position by rotating query and key vectors as a function of their index.

## S

**Sampling policy.** The procedure by which a reported score was obtained: a single sample, best of n, majority vote at n, or unstated. A necessary condition on any comparison of benchmark scores.

**Sliding-window attention.** Attention restricted to a fixed-size window of nearby positions, reducing cost from quadratic to linear in sequence length at the cost of direct long-range access.

**Sparse attention.** Any attention pattern that computes a subset of the full position-pair matrix.

**Speculative decoding.** Generating candidate tokens with a cheaper draft model and verifying them in a single pass of the target model, accepting the longest verified prefix.

**SSM.** State-space model. A sequence model that maintains a recurrent state with linear-time updates, rather than attending over all prior positions.

**Supervised fine-tuning.** Fine-tuning on labelled input-and-output pairs. Abbreviated SFT.

**Synthetic data.** Training data generated by a model rather than collected from human-authored sources.

## T

**Test-time compute.** Computation expended during inference to improve output quality, for example by generating longer reasoning or sampling and selecting among multiple candidates. Trades cost and latency for accuracy.

**Throughput.** Tokens or requests served per unit time by a system at a stated concurrency. A system property, not a model property.

**Time to first token.** Elapsed time from request submission to receipt of the first output token. Abbreviated TTFT. Dominated by queueing and prefill.

**Time per output token.** Mean elapsed time between successive output tokens during decoding. Abbreviated TPOT. Determines perceived streaming speed.

**Token.** The unit into which text is segmented for model processing. Not a word and not a character; token counts for the same text differ by tokenizer.

**Tokenizer.** The algorithm and vocabulary that map text to tokens and back.

**Tool call.** A structured request emitted by a model for an external function to be executed, together with the arguments for it. Both the tool definitions and the returned results consume tokens.

## U

**Utilisation.** The fraction of an accelerator's theoretical throughput actually achieved by a workload. A necessary condition on any energy-per-token figure.

## W

**Warm start.** A request served by a worker whose weights are already resident and whose caches are populated. Contrasted with *cold start*.

**Water consumption.** Water withdrawn or evaporated for data-centre cooling and for electricity generation. Reported separately for on-site and off-site consumption where the distinction is available.
