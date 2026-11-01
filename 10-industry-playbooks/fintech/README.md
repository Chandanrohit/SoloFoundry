# FinTech playbook

Potential problem spaces: reconciliation, financial research, reporting workflows, fraud operations, compliance evidence and cash-flow visibility.

Key constraints: financial accuracy, provenance, auditability, authorization, sensitive data, data licensing, explainability, human review and jurisdiction-specific regulation.

Example architecture pattern: licensed/source data ingestion → validation and normalization → durable relational store → deterministic calculation/domain services → optional retrieval or LLM explanation layer → human approval and audit trail → monitored API/UI. Do not let an LLM silently invent or execute financial calculations.
