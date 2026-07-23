# Benchmark glossary

> **Research cut-off date: 2026-07-22.**
> **Status: written.** Definitional entries only. No scores appear here; results live in `data/benchmarks.csv` with their evaluation conditions attached.

| Benchmark | What it tests | Primary use |
|---|---|---|
| GPQA Diamond | Graduate-level, expert-written science questions | Scientific knowledge and reasoning |
| Humanity's Last Exam | Difficult multidisciplinary academic questions | Broad frontier reasoning |
| ARC-AGI-2 and ARC-AGI-3 | Abstract reasoning puzzles designed to resist memorisation | Novel abstraction and adaptation |
| SWE-Bench Verified | Repository issues with human-validated test conditions | Software repair |
| SWE-Bench Pro | Harder and more diverse repository tasks | Agentic coding |
| Terminal-Bench | Tasks executed in a terminal environment | Tool use, coding, systems work |
| BrowseComp | Difficult information retrieval and browsing | Search planning and synthesis |
| OSWorld | Realistic computer interaction | Desktop computer use |
| WebArena | Tasks on realistic websites | Web navigation and action |
| Vibe Code Bench | End-to-end application construction | Building a working product rather than a snippet |
| MMMU-Pro | Multidisciplinary multimodal questions | Visual and textual reasoning |
| FACTS Suite | Grounding, parametric, search, and multimodal factuality | Factual reliability |
| SimpleQA Verified | Short factual questions with verified answers | Parametric factual accuracy |
| HalluHard | Difficult multi-turn conversations with citation checking | Multi-turn hallucination under hard domains |
| MRCR | Multi-round coreference and long-context retrieval | Long-context recall and tracking |
| LongCodeBench | Real code tasks at very long context | Effective long-context coding |
| LongProc | Long procedural generation with structured output | Instruction retention and long-form coherence |
| HELM | Holistic evaluation framework | Multi-metric model comparison |
| MedHELM | Clinical and medical tasks organised by workflow | Health-domain applicability |

## Reading these names

Several entries differ from similarly named benchmarks in ways that matter. ARC-AGI is not the AI2 Reasoning Challenge. SWE-Bench Verified and SWE-Bench Pro are distinct constructions from the original SWE-Bench, and a score against one is not a score against another. A benchmark version must be recorded with every result, because these constructions are revised.

Full documentation for each, under the nine required headings, is in the [benchmarks section](../benchmarks/benchmark-overview.md). An entry appears in that section only after its construction methodology has been located and registered.
