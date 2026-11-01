# Tool-using workflows

**Maturity:** reviewed method guide; no agent implementation has been tested.

Give a model tools only when a deterministic workflow or a user-mediated action cannot meet the need. Start from a [bounded workflow](../model-backed-product-patterns/README.md); do not begin with an open-ended autonomous agent.

## Workflow or agent?

| Prefer a fixed workflow when… | Consider an agent when… |
|---|---|
| Steps and branches are known | The next step depends on varied context |
| Actions are sensitive or irreversible | The task is low impact and actions are reversible |
| You need predictable completion | You can bound tool calls, time, spend, and uncertainty |
| A user can choose the next action | You can inspect and audit each action |

If you cannot explain how to stop it, recover from a partial action, and identify who authorized each action, do not grant tools yet.

## Design each tool as an API boundary

For every tool document: purpose, input schema, output schema, caller identity, allowed resources, side effects, failure modes, idempotency behavior, timeout, and audit fields. Validate arguments in application code. The model may propose an action; ordinary authorization code decides whether it is allowed. Use narrow, task-specific credentials and scopes. Never expose general shell, raw SQL, unrestricted filesystem, or broad admin access to a model in a user-facing product.

Separate read-only tools from writes. For high-impact writes, show a human-readable preview and require confirmation immediately before execution. Bind confirmation to the exact action and arguments so an altered request cannot reuse approval. Use idempotency keys for retried writes, and represent partial completion explicitly.

## Bound the loop

- Set maximum turns, tool calls, wall time, output size, and spend.
- Validate tool output as untrusted input; limit bytes and strip secrets.
- Use allowlists for destinations and actions; deny by default.
- Stop on repeated errors, policy conflicts, or uncertain identity.
- Provide a cancel path and preserve enough state to resume safely.
- Keep a human-readable event record: user, request, model/version, proposed action, policy decision, confirmation, result, and correlation ID. Avoid retaining raw private prompts unless needed and disclosed.

## Resist prompt injection and confused-deputy behavior

Treat user text, retrieved pages, documents, email, and tool output as data that may contain hostile instructions. Delimit and label sources, but do not assume delimiters make the model immune. Enforce security with tool permissions and deterministic checks. Never let an instruction found in retrieved content silently expand permissions, export data, or send messages. Test direct and indirect injection, cross-tenant data, secret exfiltration, unexpected URLs, malformed tool arguments, retries, and revoked access.

Review the [OWASP GenAI Security Project](https://genai.owasp.org/) and its [agentic AI security work](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/); use threat lists as test prompts, not proof of safety.

## Practical rollout

1. Make the workflow read-only and run on synthetic/public data.
2. Log proposed actions without executing them; review false positives and missed actions.
3. Enable one narrow reversible action for an internal user group.
4. Add per-action confirmation for consequential writes.
5. Measure completion, correction, refusal, escalation, duplicate action, latency, and spend.
6. Add a kill switch and documented manual fallback before expanding access.

Cross-check the [threat model template](../../templates/THREAT_MODEL.md), [AI evaluation plan](../../templates/AI_EVALUATION_PLAN.md), and [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework). For AI operations, see [evaluation and production operations](../evaluation-and-production-operations/README.md).
