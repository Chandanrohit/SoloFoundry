# Evaluation and production operations for AI features

**Maturity:** reviewed method guide; operational examples are illustrative, not tested.

An AI feature needs a repeatable way to notice regressions because output can change with models, prompts, data, and dependencies. Evaluation is a product feedback loop, not a one-time launch gate.

## Build an evaluation set

Start with user outcomes and failure costs. Store each case with input, expected behavior, relevant context, safety labels, and rationale. Include common cases and the long tail: ambiguous, malformed, adversarial, unanswerable, multilingual (if supported), and accessibility-sensitive inputs. Use synthetic or consented/minimized records; do not copy customer conversations into a third-party evaluation service without checking policy and consent.

Version the dataset and label rubric. Split development examples from a held-back regression set to reduce overfitting. Record evaluator identity and disagreement. For open-ended responses, combine exact checks (schema, citation ID, refusal requirements), human review, and model-based grading. Validate model graders against humans; their scores can drift or reward fluent but unsupported output.

Track quality by slice, not only aggregate score. A stable average can conceal a failure on one language, customer type, or safety case. The [evaluation plan template](../../templates/AI_EVALUATION_PLAN.md) helps record owner, cases, thresholds, and rollout criteria.

## Monitor without collecting too much

Useful operational measures include request count, error/timeout rate, p50/p95 latency, input/output tokens, cost, rate-limit events, fallback rate, and tool/action outcomes. Product-quality signals may include user edits, retries, reports, successful task completion, and support contacts. Define what each measure means before alerting on it.

Avoid logging raw prompts and outputs by default. Prefer redacted metadata, sampled/consented debugging records with short retention, and access controls. Keep secrets and personal data out of traces. Give users a report/feedback path and review it on a defined schedule.

Use [OpenTelemetry's observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) for the general signals model. Its concepts are useful even if a solo project chooses a simpler platform-specific dashboard.

## Release and recover

Pin model and prompt versions where possible. Before a change: run the fixed regression suite, compare cost and latency, review changed safety failures, then canary for a small cohort. Keep a rollback switch and note which versions generated affected outputs. Feature flags should allow disabling the model while the core product remains usable where possible.

Budget for provider outages and limits: queue only work that can safely wait, make retries bounded with backoff, prevent duplicate writes, and provide a clear fallback. Set rate and spend limits per user and globally. Document who receives an alert and the next action; a solo operator needs fewer actionable alerts, not a stream of noisy notifications.

## Lightweight operating review

Weekly or after a material change, inspect a sample of failures and user corrections, top cost/latency drivers, provider/model changes, safety reports, and open data deletion requests. Record the decision: keep, adjust, roll back, or retire. Revisit the evaluation set as users and content change.

For framework context, see [NIST's Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) and [OWASP GenAI security resources](https://genai.owasp.org/). For a practical exercise, complete the [RAG evaluation lab](../labs/RAG_EVALUATION_LAB.md).
