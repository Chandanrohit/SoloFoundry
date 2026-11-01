# AI engineering

Treat AI as a probabilistic component in a product system—not as a substitute for product thinking or deterministic software.

## Domains
- Model selection: hosted vs open-weight, quality, latency, privacy, context, licensing and cost.
- LLM applications: prompts, structured outputs, tool use, context engineering and fallback paths.
- Retrieval: ingestion, parsing, chunking, embeddings, hybrid retrieval, reranking, citations and freshness.
- Agents: workflow vs agent decisions, tool permissions, state, memory, human approval and bounded execution.
- Evaluation: task datasets, rubrics, deterministic assertions, human review, regression tests and online monitoring.
- Inference: batching, caching, quantization, routing, GPU sizing and serving.
- AI security: prompt injection, data leakage, unsafe tool execution, model supply chain and abuse.

Every AI guide must discuss failure modes, evaluation, privacy, cost and a non-AI or simpler alternative.

## Learning path

1. [Model-backed product patterns](model-backed-product-patterns/README.md): decide whether AI belongs, compare hosting routes, and set product boundaries.
2. [Retrieval and grounded knowledge](retrieval-and-grounded-knowledge/README.md): build a data-to-answer path with authorization, freshness, and citation checks.
3. [Tool-using workflows](tool-using-workflows/README.md): bound model-proposed actions and preserve deterministic authorization.
4. [Evaluation and production operations](evaluation-and-production-operations/README.md): test quality and safety, monitor, roll out, and recover.
5. Complete the [RAG evaluation lab](labs/RAG_EVALUATION_LAB.md) and record a plan with the [AI evaluation template](../templates/AI_EVALUATION_PLAN.md).

These are reviewed method guides, not tested implementations. Check linked sources for current versions and terms before choosing a provider or adopting a control.
