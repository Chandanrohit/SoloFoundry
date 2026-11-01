# Legal technology product discovery and design

**Maturity:** reviewed domain guide; no legal product, jurisdiction, or professional workflow has been validated.

Legal work depends on authority, jurisdiction, deadlines, confidentiality, and context. A tool that helps organize documents is different from one that recommends a legal position. Identify who the user is (lawyer, client, legal operations, court staff), who owns the matter, and who is authorized to see each record.

## Choose a narrow support task

Good initial scopes may include matter intake routing, document inventory, clause comparison against an approved playbook, deadline reminders with human verification, or search over a firm's own approved material. Keep the original document, source location, version, extraction, and reviewer edits. For generated summaries, cite exact source passages and make missing evidence visible.

Do not market a general model as a lawyer, guarantee legal outcomes, or let generated text reach a court, opposing party, or client without qualified review. Deadline calculations need jurisdiction-specific rules, calendar handling, and a verified human check.

## Confidentiality and accuracy controls

- Treat client information as highly sensitive even when it is publicly filed; representation context can remain confidential.
- Use matter-level access boundaries, secure deletion, retention controls, audit logs, and vendor agreements.
- Do not train on client content or send it to a model provider without informed authorization and legal review.
- Preserve citations, versions, and source-of-truth links; show conflicts and uncertainty.
- Test hallucinations, stale law, incorrect jurisdiction, missed clauses, prompt injection in documents, and cross-matter leakage.

The [ABA Model Rule 1.6](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_6_confidentiality_of_information/) is a U.S. model rule; states adopt and modify professional rules differently. It is a reference for issue-spotting, not a universal law or a substitute for local professional advice. Unauthorized practice, privilege, records, and bar requirements must be assessed locally.

## Evaluate with qualified reviewers

Build a test set from authorized, minimized examples with attorney-verified expected passages and outcomes. Measure citation support, missed material clauses, false alerts, reviewer correction time, and confidentiality failures. Preserve human responsibility; a disclaimer does not make an unsafe workflow safe.

Related: [RAG security boundaries](../../04-ai/retrieval-and-grounded-knowledge/README.md), [privacy/contract basics](../../09-business/legal-privacy-contracts-and-support/README.md), and the [threat model](../../templates/THREAT_MODEL.md).
