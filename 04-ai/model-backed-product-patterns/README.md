# Model-backed product patterns

**Maturity:** reviewed method guide; no model or product implementation has been tested.

AI belongs in a product when it improves a user outcome enough to justify probabilistic output, data handling, latency, operating cost, and ongoing evaluation. Begin with the [product brief](../../templates/PRODUCT_BRIEF.md), [problem evidence](../../01-discover/assumptions-and-evidence/README.md), and a non-AI baseline.

## Decide whether a model belongs

Write down the user task, current workaround, acceptable error, and how a user can recover. Prefer ordinary code, search, rules, or a human workflow when the task has a stable specification and mistakes are costly. A model is a candidate when inputs are varied or unstructured and useful output can be checked or corrected.

| Pattern | Good fit | Main burden |
|---|---|---|
| Deterministic software | Exact rules, billing, permissions, calculations | Modeling edge cases |
| Model as classifier/extractor | Unstructured input with reviewable fields | Calibration, false positives/negatives |
| Model as drafting assistant | First drafts where user retains control | Factuality, attribution, editing cost |
| Retrieval plus model | Answers constrained to a changing document set | Ingestion, access controls, retrieval quality |
| Tool-using workflow | Multi-step task with bounded, auditable actions | Tool authorization and action safety |

Do not use a model as the authority for access control, money movement, safety-critical advice, or irreversible actions. Keep those decisions in deterministic, testable code and require explicit user review where appropriate.

## Choose a hosting and model route

| Route | Consider when | Check before choosing |
|---|---|---|
| Hosted API | Fastest path to a prototype; variable traffic | Data terms, retention, region, quotas, versioning, outage behavior, exportability |
| Managed model platform | Need deployment controls or a cloud boundary | Identity model, network boundary, logging, model availability, portability |
| Open weights hosted by a provider | Need more control over model choice or serving | License, provider access, patching, hardware, model provenance |
| Self-hosted open weights | Strong residency/control need and operational capacity | GPU/CPU memory, throughput, patching, abuse controls, on-call and total cost |

Open weights do not automatically mean open training data, unrestricted commercial use, or low cost. Read the exact model license and model card, pin a revision, and record source, checksum, quantization, and known limitations. Hugging Face explains [model cards](https://huggingface.co/docs/hub/en/model-cards) and [loading model architectures/checkpoints](https://huggingface.co/docs/transformers/main/models).

## Select by task, not leaderboard rank

Create a small representative test set before a vendor comparison. Include normal inputs, confusing inputs, empty or malformed inputs, abuse attempts, and cases that should be refused or escalated. Compare candidate models on task quality, citation/support quality (if relevant), latency at realistic load, privacy terms, availability, and total workflow cost. Use the [AI evaluation plan](../../templates/AI_EVALUATION_PLAN.md) and [evaluation lab](../labs/RAG_EVALUATION_LAB.md).

Estimate recurring model spend as:

`requests per month × (average input tokens × input price + average output tokens × output price)`

Then include retries, embeddings, reranking, storage, observability, human review, and engineering time. Prices change; use provider calculators/current pricing only when making a dated decision. Put a budget cap, per-user rate limit, and graceful fallback in the product before launch.

## Design the user experience around uncertainty

- Label generated content and show sources when users need to verify it.
- Make editing, retrying, reporting, and reaching a human straightforward.
- Say when the system lacks enough information; do not fill gaps with confident invention.
- Preserve user work when a request times out; avoid duplicate submissions on retry.
- Do not send sensitive content to a model until the user-facing purpose and data terms justify it.
- Keep provider prompts and outputs out of logs by default; redact and retain only what debugging needs.

## A solo-builder implementation sequence

1. Write a one-sentence outcome and a non-AI baseline.
2. Identify data sent to the model, its sensitivity, retention, and deletion path.
3. Build a representative evaluation set from permitted, minimized data.
4. Prototype one narrow task behind a feature flag and explicit usage limit.
5. Measure quality, latency, failures, and cost against the baseline.
6. Add fallback, user correction, abuse handling, and a rollback switch.
7. Review changes to prompts, model versions, and retrieval as product changes; rerun evaluations.

## Study and tooling

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [Generative AI Profile (NIST AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence): use to structure risks and controls, not as a product certification.
- [OWASP GenAI Security Project](https://genai.owasp.org/): threat-oriented security references; verify the publication date/version of any list you adopt.
- Model cards above: inspect license, intended use, limitations, evaluation, and provenance.

Next: [retrieval and grounded knowledge](../retrieval-and-grounded-knowledge/README.md), [tool-using workflows](../tool-using-workflows/README.md), and [evaluation and production operations](../evaluation-and-production-operations/README.md).
