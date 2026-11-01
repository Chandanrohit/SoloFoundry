# Retrieval and grounded knowledge

**Maturity:** reviewed method guide; no reference implementation has been tested.

Retrieval-augmented generation (RAG) retrieves relevant source material at request time and gives it to a model to answer. Retrieval can improve access to a private or changing corpus, but it does not guarantee that the answer is correct. Start with [model-backed product patterns](../model-backed-product-patterns/README.md) and ask whether ordinary search already solves the user's task.

## The end-to-end path

```text
authorized sources → parse and normalize → split and label → index
user question → authenticate and scope → retrieve → optional rerank
retrieved passages + instructions → generate → validate and cite → user feedback
```

Keep source identity, owner, timestamps, access labels, and deletion state attached through every stage. A document index is a copy of data: it needs the same access policy, retention, and deletion behavior as the original.

## Build a first retrieval system

1. **Choose a small permitted corpus.** Record where each file came from, who may access it, and whether it may be processed by the selected embedding/model provider.
2. **Parse for meaning.** Preserve headings, tables, code blocks, page numbers, URLs, and version metadata where they matter. Test parsing on representative files; silent extraction loss is common.
3. **Split with context.** Start with sections or paragraphs, carry the title and parent heading into each chunk, and avoid splitting tables or instructions mid-step. Compare a few chunk sizes rather than treating a token count as a universal answer.
4. **Index and retrieve.** Begin with keyword/full-text search or embeddings according to the corpus and query vocabulary. Hybrid search can help when exact names and semantic paraphrases both matter. Add reranking only if measured retrieval errors justify its cost and latency.
5. **Generate with boundaries.** Tell the model to answer only from supplied evidence, distinguish missing evidence, and return source identifiers. Treat retrieved text as untrusted data, not instructions.
6. **Render verifiable citations.** Link to the source and section/page. Check that cited identifiers were actually retrieved and exist. A citation can be real while failing to support the claim, so evaluate support separately.
7. **Handle updates and deletion.** Make ingestion repeatable; detect changed documents; remove deleted or newly unauthorized chunks and associated caches. Test this path.

## Security and privacy boundaries

Authenticate first, then apply tenant/user/document access filters before retrieval. Filtering after retrieval can leak snippets through generation, logs, traces, caches, or timing. Never rely on a prompt to enforce authorization. Protect vector stores and backups, isolate tenants, and test with a user who should not see a document. Treat prompt injection inside source documents as an expected threat; do not permit retrieved content to override system policy or authorize tools.

Minimize sensitive fields before embedding. Embeddings can reveal information and are not anonymization. Define retention and deletion for source files, chunks, embeddings, prompts, outputs, and provider logs. Tell users what is processed and why.

## Evaluate retrieval separately from answers

Create 20–30 questions grounded in the corpus, with expected source passages and an answerable/unanswerable label. Include exact lookup, paraphrase, multiple-source synthesis, stale content, conflicting versions, no-answer, and access-boundary cases. For each query inspect:

- **Retrieval:** did the expected evidence appear in the top results? Record rank and relevant passages; compare methods on the same query set.
- **Answer support:** are material claims supported by the retrieved text?
- **Citation validity:** do cited links resolve to the right passage, and does it support the claim?
- **Abstention:** does the system admit when the corpus has no answer?
- **Safety:** did private or unauthorized material appear?

Use the hands-on [RAG evaluation lab](../labs/RAG_EVALUATION_LAB.md). Keep a small fixed regression set, and add failures only after removing secrets and confirming data-use permission. Do not treat an LLM judge as ground truth; calibrate it against human review and report disagreement.

## Common failures

| Symptom | Likely cause | First investigation |
|---|---|---|
| Answer misses an obvious passage | Parser, chunking, filters, or query mismatch | Inspect extracted text and top-k results before changing prompts |
| Correct source, wrong claim | Generation overstates weak evidence | Require claim-level support; shorten context; test abstention |
| Old policy appears | Stale index or cache | Trace source version and deletion/update propagation |
| Private snippet leaks | Authorization applied too late or tenant mixing | Review every retrieval, cache, log, and fallback boundary |
| Cost/latency grows | Too many chunks, reranking, retries, or large context | Measure stages; cap context and retries; test simpler search |

## References

- Lewis et al., [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), the original RAG paper; its benchmarks do not establish quality for your corpus.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) for organizing risk work.
- [OWASP GenAI Security Project](https://genai.owasp.org/) for current prompt injection and data-handling threat material; check versions.
