# Table of contents

> **Research cut-off date: 2026-07-22.**

This file is the canonical table of contents for readers browsing the repository on GitHub. The rendered documentation site uses the navigation defined in [mkdocs.yml](mkdocs.yml). The two must agree; `mkdocs build --strict` fails if a file appears in one and not the other.

## Project documents

- [README](README.md)
- [Research methodology](research-methodology.md)
- [Data sources](data-sources.md)
- [Limitations](limitations.md)
- [Glossary](glossary.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [Citation metadata](CITATION.cff)
- [Bibliography](references.bib)

## Handbook

- [Index](docs/index.md)
- [01. Introduction](docs/01-introduction.md)
- [02. Foundation models](docs/02-foundation-models.md)
- [03. Transformer architecture](docs/03-transformer-architecture.md)
- [04. Training and post-training](docs/04-training-and-post-training.md)
- [05. Scaling laws](docs/05-scaling-laws.md)
- [06. Reasoning models](docs/06-reasoning-models.md)
- [07. Agentic AI](docs/07-agentic-ai.md)
- [08. Multimodal models](docs/08-multimodal-models.md)
- [09. Benchmarking](docs/09-benchmarking.md)
- [10. Factuality and hallucination](docs/10-factuality-and-hallucination.md)
- [11. Long context](docs/11-long-context.md)
- [12. Tokenization](docs/12-tokenization.md)
- [13. Inference](docs/13-inference.md)
- [14. Latency and throughput](docs/14-latency-and-throughput.md)
- [15. Token economics](docs/15-token-economics.md)
- [16. Energy use](docs/16-energy-use.md)
- [17. Hardware and memory](docs/17-hardware-and-memory.md)
- [18. Open versus closed models](docs/18-open-vs-closed-models.md)
- [19. Security and privacy](docs/19-security-and-privacy.md)
- [20. Model selection framework](docs/20-model-selection-framework.md)
- [21. Research gaps](docs/21-research-gaps.md)

## Model profiles

- [OpenAI](docs/model-profiles/openai.md)
- [Anthropic](docs/model-profiles/anthropic.md)
- [Google Gemini](docs/model-profiles/google-gemini.md)
- [Meta Llama](docs/model-profiles/meta-llama.md)
- [DeepSeek](docs/model-profiles/deepseek.md)
- [Mistral](docs/model-profiles/mistral.md)
- [Qwen](docs/model-profiles/qwen.md)
- [xAI Grok](docs/model-profiles/xai-grok.md)
- [Microsoft Phi](docs/model-profiles/microsoft-phi.md)
- [Cohere Command](docs/model-profiles/cohere-command.md)
- [Amazon Nova](docs/model-profiles/amazon-nova.md)
- [AI21 Jamba](docs/model-profiles/ai21-jamba.md)
- [Moonshot Kimi](docs/model-profiles/moonshot-kimi.md)
- [MiniMax](docs/model-profiles/minimax.md)
- [Zhipu GLM](docs/model-profiles/zhipu-glm.md)
- [Other families](docs/model-profiles/other-models.md)

## Benchmarks

- [Benchmark overview](docs/benchmarks/benchmark-overview.md)
- [Knowledge and reasoning](docs/benchmarks/knowledge-and-reasoning.md)
- [Coding](docs/benchmarks/coding.md)
- [Agents and computer use](docs/benchmarks/agents-and-computer-use.md)
- [Multimodal](docs/benchmarks/multimodal.md)
- [Long context](docs/benchmarks/long-context.md)
- [Factuality](docs/benchmarks/factuality.md)
- [Multilingual](docs/benchmarks/multilingual.md)
- [Benchmark limitations](docs/benchmarks/benchmark-limitations.md)

## Comparisons

- [Frontier models](docs/comparisons/frontier-models.md)
- [Open-weight models](docs/comparisons/open-weight-models.md)
- [Coding models](docs/comparisons/coding-models.md)
- [Reasoning models](docs/comparisons/reasoning-models.md)
- [Multimodal models](docs/comparisons/multimodal-models.md)
- [Long-context models](docs/comparisons/long-context-models.md)
- [Efficient models](docs/comparisons/efficient-models.md)
- [Model selection matrix](docs/comparisons/model-selection-matrix.md)

## Evaluation framework

- [Internal bakeoff](docs/evaluation/internal-bakeoff.md)
- [Quality metrics](docs/evaluation/quality-metrics.md)
- [Latency methodology](docs/evaluation/latency-methodology.md)
- [Token cost methodology](docs/evaluation/token-cost-methodology.md)
- [Energy methodology](docs/evaluation/energy-methodology.md)
- [Reproducibility](docs/evaluation/reproducibility.md)

## Appendices

- [Formulas](docs/appendices/formulas.md)
- [Benchmark glossary](docs/appendices/benchmark-glossary.md)
- [Hardware glossary](docs/appendices/hardware-glossary.md)
- [Model release timeline](docs/appendices/model-release-timeline.md)
- [Source quality framework](docs/appendices/source-quality-framework.md)

## Data

- [models.csv](data/models.csv)
- [benchmarks.csv](data/benchmarks.csv)
- [pricing.csv](data/pricing.csv)
- [context-windows.csv](data/context-windows.csv)
- [energy-studies.csv](data/energy-studies.csv)
- [sources.csv](data/sources.csv)
- [Schemas](data/schema/)

## Scripts

- [validate_sources.py](scripts/validate_sources.py)
- [validate_links.py](scripts/validate_links.py)
- [validate_tables.py](scripts/validate_tables.py)
- [generate_model_tables.py](scripts/generate_model_tables.py)
- [generate_benchmark_tables.py](scripts/generate_benchmark_tables.py)
- [calculate_token_costs.py](scripts/calculate_token_costs.py)
- [estimate_memory.py](scripts/estimate_memory.py)
- [build_release_timeline.py](scripts/build_release_timeline.py)

## Notebooks

- [benchmark-comparison.ipynb](notebooks/benchmark-comparison.ipynb)
- [token-cost-analysis.ipynb](notebooks/token-cost-analysis.ipynb)
- [latency-analysis.ipynb](notebooks/latency-analysis.ipynb)
- [energy-analysis.ipynb](notebooks/energy-analysis.ipynb)
