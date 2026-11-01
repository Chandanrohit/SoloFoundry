# Industry playbooks

**Maturity:** decision guides; scenarios are examples, not market research or compliance advice.

Industry context changes product requirements. Start with a problem and user workflow, then map buyer, data, integrations, risk, adoption, procurement, and economics. An industry label alone is not proof of a market opportunity.

## How to use a playbook

1. Choose a narrow role and repeated task; interview users and observe the current workaround.
2. Identify the payer, operator, affected people, and any gatekeeper. They may be different.
3. Trace data from source to user-visible outcome. Record provenance, rights, sensitivity, retention, and correction path.
4. Name domain-specific failure costs and obligations. Verify current primary law/standards for the actual jurisdictions and role.
5. Prefer a reversible workflow with human review where errors carry material risk. Use deterministic rules for money, permissions, safety limits, and records.
6. Test a thin vertical slice with representative users and non-production data before claiming fit.
7. Connect the resulting requirements to the [reference architecture](../11-reference-architectures/repair-shop-appointments/README.md), [stack comparisons](../12-stack-combinations/README.md), and lifecycle [content status](../CONTENT_STATUS.md).

## Starter domains

| Domain | First guide | Risks to examine early |
|---|---|---|
| Financial technology | [FinTech](fintech/README.md) | Data rights, financial accuracy, fraud, auditability, payment-card scope |
| Healthcare | [Healthcare](healthcare/README.md) | Patient safety, protected information, clinical validation, provider workflow |
| Legal technology | [LegalTech](legaltech/README.md) | Confidentiality, privilege, citation integrity, professional rules |
| Manufacturing | [Manufacturing](manufacturing/README.md) | OT boundaries, worker safety, uptime, legacy systems |
| Retail | [Retail](retail/README.md) | Inventory truth, payment scope, seasonality, customer privacy |
| Education | [Education](education/README.md) | Student privacy, age-appropriate design, accessibility, learning outcomes |

## Scope discipline

These guides are discovery and design aids. They do not establish demand, replace domain experts, determine whether a law applies, or certify a system. Avoid storing regulated data or making consequential decisions until the obligation, provider terms, and operational controls have been reviewed by qualified people.
