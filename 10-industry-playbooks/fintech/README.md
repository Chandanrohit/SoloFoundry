# FinTech product discovery and design

**Maturity:** reviewed domain guide; no financial product or compliance approach has been validated.

FinTech users may be consumers, finance teams, institutions, or service providers. The person using a workflow may not be the account owner or buyer. Start with a specific task such as reconciliation, cash-flow visibility, financial research, or evidence collection—not “make finance smarter.”

## Map the workflow and evidence

Trace a transaction or financial fact from its source, through normalization and calculation, to a review or decision. Record source timestamp, currency, account/owner, transformation, correction history, and whether the source permits reuse. Distinguish pending, posted, adjusted, estimated, and missing values. Never imply a feed is complete or real-time unless measured.

For an early reconciliation tool, a safe first slice could import user-selected CSV rows, flag unmatched items with deterministic rules, and let a finance user resolve them. Keep source rows and edits auditable. Avoid scraping credentials or automatically initiating transfers in a first version.

## Design for error impact

- Separate data collection, normalization, deterministic calculations, explanation, and user approval.
- Use decimal-safe arithmetic, explicit rounding/currency rules, and reproducible calculations.
- Show source, as-of time, assumptions, and uncertainty beside each material number.
- Require explicit authorization for account connections and isolate each customer’s data.
- Provide correction, export, deletion, incident, and reconciliation paths.
- Treat AI as an optional explanation/search layer; never let it invent numbers or silently move money.

Measure reconciliation precision/recall against labeled cases, stale/missing-source rate, correction rate, time to resolve, and support burden. For high impact, require a qualified human review and a process for disputed results.

## Constraints to verify

Financial-services obligations depend on product function, funds flow, role, customer, and jurisdiction. Before launch, map whether the product touches custody, advice, credit decisions, payments, identity verification, or regulated data; get qualified regulatory review. If cardholder data is in scope, use the [PCI Security Standards Council document library](https://www.pcisecuritystandards.org/document_library/) and ask the acquirer/payment provider which validation path applies. Do not assume outsourcing payments eliminates every merchant obligation.

The [CFPB personal financial data rights resource](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/personal-financial-data-rights/) is U.S.-specific and its rule/status can change; check its current notice before relying on it. Prefer a provider’s documented API and permissions over credential collection.

## Useful validation questions

1. Show me the last time this task happened; what was its source of truth?
2. What happens when two sources disagree, or a transaction changes later?
3. Who may view, correct, export, or approve the record?
4. Which error would cause financial loss, reporting risk, or a missed obligation?
5. What would make you trust or reject a system-generated finding?

Build from the [discovery path](../../01-discover/README.md), then use the [threat model](../../templates/THREAT_MODEL.md) before handling real account data.
