# Formulas

> **Research cut-off date: 2026-07-22.**

Canonical definitions of every formula used in this handbook. Each formula is defined once here and referenced elsewhere. Where a formula has a reference implementation in `scripts/`, the script is named; if a script and this page disagree, the defect is in this page and the script is authoritative, because the script is the artefact that is executed and tested.

These are definitions and arithmetic. They contain no measured values, so they carry no citations. Every quantity substituted into them must carry its own source, date, and evidence grade.

## Notation

| Symbol | Quantity |
|---|---|
| \(T_{\text{in}}\) | Uncached input tokens per task |
| \(T_{\text{cache}}\) | Cached input tokens per task |
| \(T_{\text{out}}\) | Visible output tokens per task |
| \(T_{\text{reason}}\) | Reasoning tokens per task, billed or not |
| \(T_{\text{tool}}\) | Tokens consumed by tool definitions and tool results |
| \(P_{\text{in}}, P_{\text{cache}}, P_{\text{out}}\) | Prices in USD per one million tokens |
| \(a\) | Acceptance rate, the fraction of attempts whose output is accepted, \(0 < a \le 1\) |
| \(N\) | Total parameter count |
| \(L\) | Transformer layers |
| \(H_{kv}\) | Key and value heads per layer, after any grouping |
| \(d_{\text{head}}\) | Head dimension |
| \(S\) | Sequence length in tokens |
| \(B\) | Concurrent sequences |
| \(b\) | Bytes per element at a stated precision |
| \(E\) | Energy, in joules unless stated |
| \(\text{PUE}\) | Power usage effectiveness of the facility |
| \(I\) | Grid carbon intensity, in grams of carbon dioxide equivalent per kilowatt hour |

## 1. Token economics

Reference implementation: `scripts/calculate_token_costs.py`.

### 1.1 Effective tokens per task

Every token class a task consumes, whether or not the provider bills it. The distinction matters because a class that is not billed still consumes context and latency.

\[
T_{\text{eff}} = T_{\text{in}} + T_{\text{cache}} + T_{\text{out}} + T_{\text{reason}} + T_{\text{tool}}
\]

### 1.2 Total API cost

Tool tokens are billed at the input price, because tool definitions and tool results enter the context as input. Reasoning tokens are billed at the output price where the provider bills them at all; where a provider does not bill them, set \(T_{\text{reason}} = 0\) in this formula and retain the count in \(T_{\text{eff}}\).

\[
C = \frac{(T_{\text{in}} + T_{\text{tool}})\,P_{\text{in}} + T_{\text{cache}}\,P_{\text{cache}} + (T_{\text{out}} + T_{\text{reason}})\,P_{\text{out}}}{10^{6}}
\]

Under a batch discount \(d\), expressed as a fraction:

\[
C_{\text{batch}} = C\,(1 - d)
\]

### 1.3 Cost per accepted task

The quantity that matters for a budget. A model that is cheap per call and frequently rejected is not cheap.

\[
C_{\text{task}} = \frac{C}{a}
\]

The acceptance criterion must be stated wherever \(a\) is used. Two teams applying different acceptance criteria to the same outputs will compute different costs from identical prices, and the difference will be attributed to the model unless the criterion is visible.

### 1.4 Cache savings

Savings relative to paying the uncached input price for every input token.

\[
S = \frac{T_{\text{cache}}\,(P_{\text{in}} - P_{\text{cache}})}{10^{6}}
\]

Savings are realised only for the fraction of requests that hit the cache. Over a workload with hit rate \(h\):

\[
S_{\text{workload}} = h \cdot \frac{(T_{\text{in}} + T_{\text{cache}})\,(P_{\text{in}} - P_{\text{cache}})}{10^{6}}
\]

### 1.5 Reasoning overhead

Reported both as a token ratio and as a share of cost, because the two differ whenever reasoning tokens are billed at a different rate from visible output.

\[
R_{\text{tokens}} = \frac{T_{\text{reason}}}{T_{\text{out}}}
\qquad
R_{\text{cost}} = \frac{T_{\text{reason}}\,P_{\text{out}}}{10^{6}\,C}
\]

## 2. Latency

Reference chapter: [14. Latency and throughput](../14-latency-and-throughput.md).

### 2.1 Decomposition

\[
t_{\text{total}} = t_{\text{queue}} + t_{\text{prefill}} + t_{\text{decode}} + t_{\text{tool}}
\]

Time to first token is the part of that sum a user perceives before any output appears:

\[
\text{TTFT} = t_{\text{queue}} + t_{\text{prefill}}
\]

Decode time is the count of output tokens multiplied by the mean time per output token:

\[
t_{\text{decode}} = (T_{\text{out}} + T_{\text{reason}}) \cdot \text{TPOT}
\]

Reasoning tokens appear in decode time whether or not they are visible to the caller, which is why a reasoning model can be slow without appearing to produce more output.

### 2.2 Prefill

Prefill time grows with input length. For a system whose prefill is bound by arithmetic throughput:

\[
t_{\text{prefill}} \approx \frac{2\,N_{\text{active}}\,T_{\text{in}}}{\Phi\,u}
\]

where \(N_{\text{active}}\) is active parameters, \(\Phi\) is the accelerator's floating-point throughput at the serving precision, and \(u\) is achieved utilisation. The factor of two counts a multiply and an add per parameter per token. This is an order-of-magnitude relationship, not a prediction: it ignores attention cost, which grows faster than linearly in input length.

### 2.3 Throughput and concurrency

For a system serving \(B\) concurrent sequences at a mean time per output token:

\[
\text{throughput} = \frac{B}{\text{TPOT}}
\]

Raising \(B\) raises throughput and raises TPOT. Reporting either without the other describes half the system.

### 2.4 Percentiles

Latency is reported at p50, p90, p95, and p99, never as a mean alone. For \(n\) sorted observations, the \(p\)-th percentile is the observation at index \(\lceil p\,n / 100 \rceil\). A mean conceals the tail, and the tail is what a user experiences as unreliability.

## 3. Memory

Reference implementation: `scripts/estimate_memory.py`.

### 3.1 Bytes per element

| Precision | \(b\) |
|---|---|
| fp32, tf32 | 4 |
| bf16, fp16 | 2 |
| fp8, int8 | 1 |
| int4 | 0.5 |

### 3.2 Weight memory

\[
M_{w} = N \cdot b_{w}
\]

For a mixture-of-experts model, \(N\) is the total parameter count, not the active count: every expert must be resident even though only some are used per token. Active parameters determine compute per token, not memory.

### 3.3 KV cache memory

Per sequence, at sequence length \(S\):

\[
M_{kv} = 2\,L\,H_{kv}\,d_{\text{head}}\,S\,b_{kv}
\]

The factor of two counts keys and values. \(H_{kv}\) is the key and value head count after grouping: it equals the query head count under multi-head attention, is smaller under grouped-query attention, and is one under multi-query attention. This term is why grouped-query and multi-query attention were adopted, and why long context is expensive independent of parameter count.

### 3.4 Total requirement

\[
M = (M_{w} + B\,M_{kv})\,(1 + \omega)
\]

where \(\omega\) is the activation and framework overhead fraction. Accelerator count for a device of capacity \(M_{\text{acc}}\):

\[
n_{\text{acc}} = \left\lceil \frac{M}{M_{\text{acc}}} \right\rceil
\]

This is a plausibility check, not a deployment specification. Real memory use depends on the serving framework, the attention kernel, and fragmentation, and tensor or pipeline parallelism imposes its own constraints on how the total may be divided.

## 4. Energy and carbon

Reference chapter: [16. Energy use](../16-energy-use.md). No figure computed with these formulas may be published without the eleven conditions listed in the [research methodology](https://github.com/Ethical-Tech-CoLab/AI-Models-Research/blob/main/research-methodology.md#64-energy-claims).

### 4.1 Energy per token

Measured over a workload rather than derived from a specification:

\[
E_{\text{token}} = \frac{E_{\text{accelerator}} + E_{\text{host}}}{T_{\text{out}} + T_{\text{reason}}}
\]

The denominator counts generated tokens. Prefill energy is attributed to the request rather than to a token, because it is a function of input length and does not divide sensibly by output tokens. Where a per-token figure must cover both, state that prefill is included and state the input length it assumed.

### 4.2 Facility-adjusted energy

\[
E_{\text{facility}} = E_{\text{IT}} \cdot \text{PUE}
\]

\(E_{\text{IT}}\) is energy delivered to computing equipment. Power usage effectiveness covers cooling and distribution. It varies by facility, by season, and by hour, so a figure computed with an assumed value states the assumption.

### 4.3 Energy per query and per accepted task

\[
E_{\text{query}} = E_{\text{facility per request}}
\qquad
E_{\text{task}} = \frac{E_{\text{query}}}{a}
\]

Energy per accepted task is the analogue of cost per accepted task, and it is the figure that supports a comparison between a model that answers correctly at once and a model that must be retried.

### 4.4 Carbon per task

\[
\text{CO}_{2}\text{e}_{\text{task}} = \frac{E_{\text{task}}\,[\text{kWh}] \cdot I}{1}
\]

with \(I\) in grams of carbon dioxide equivalent per kilowatt hour for the grid region and period in which the work was served. A marginal intensity and an average intensity answer different questions; state which is used. Embodied emissions from hardware manufacture are not included in this expression and are accounted separately, because attributing them to a query requires an assumed hardware lifetime and utilisation that must be stated.

### 4.5 Accounting boundary

Any energy figure states which of these terms it includes:

\[
E_{\text{total}} = E_{\text{accelerator}} + E_{\text{host}} + E_{\text{network}} + E_{\text{storage}} + E_{\text{cooling}} + E_{\text{embodied}}
\]

Two correctly computed figures for the same workload can differ by a large factor because they draw this boundary differently. Comparison without a stated boundary is not comparison.

## 5. Scaling

Reference chapter: [05. Scaling laws](../05-scaling-laws.md).

### 5.1 Training compute

The standard approximation for a dense transformer, counting forward and backward passes:

\[
C_{\text{train}} \approx 6\,N\,D
\]

for \(N\) parameters trained on \(D\) tokens. For a mixture-of-experts model, substitute active parameters per token, and state that the substitution was made.

### 5.2 Inference compute

\[
C_{\text{infer}} \approx 2\,N_{\text{active}}\,(T_{\text{in}} + T_{\text{out}} + T_{\text{reason}})
\]

The ratio of these two expressions over a model's deployed lifetime is the quantity that determines whether training or inference dominates its total energy cost. That ratio depends on request volume, which is disclosed for almost no commercial model.

### 5.3 Power-law form

Scaling results are reported in the form

\[
\mathcal{L}(X) = \left(\frac{X_{c}}{X}\right)^{\alpha_{X}}
\]

for a resource \(X\) among parameters, data, or compute, with fitted constants \(X_{c}\) and \(\alpha_{X}\). Fitted constants are specific to the model family, data distribution, and training procedure under which they were fitted. Transferring them to another setting is an extrapolation and is marked as one.
