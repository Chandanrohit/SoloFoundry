# Retail product discovery and design

**Maturity:** reviewed domain guide; example workflows and economics are not validated with retailers.

Retail work spans online and physical channels, seasonal demand, product catalogs, stock, fulfillment, payments, returns, and customer service. A useful tool should fit store operations and reconcile with existing systems; a dashboard alone does not make inventory accurate.

## Find the operational seam

Observe a specific task: reconciling stock after returns, finding catalog errors, preparing a replenishment order, or routing a support case. Identify the person who changes the record, the system of record, and when an update must reach point-of-sale, e-commerce, warehouse, or supplier systems. Ask how stores handle outages and late data.

For an initial product, use read-only exports and generate a review queue. Keep item IDs, unit conventions, timestamps, source locations, and human corrections. Do not autonomously change prices, place purchase orders, or promise availability until downstream effects and rollback are understood.

## Measure user and business outcomes

Potential measures include inventory discrepancy rate, time to resolve a stock exception, avoidable stockouts, overstock exposure, return handling time, catalog correction rate, and support contacts. Segment by store/channel/product and season. Calculate gross margin after discounts, returns, payment fees, and fulfillment costs; sales lift alone can hide margin erosion.

Protect customer and employee data, limit access to sales detail, and define retention. If payment card data is involved, use the current [PCI SSC standards and document library](https://www.pcisecuritystandards.org/document_library/) and confirm scope with the payment provider/acquirer. Product identity and exchange requirements may benefit from [GS1 standards](https://www.gs1.org/standards); confirm the particular identifier and implementation relevant to the supply chain.

## Failure modes to test

- Duplicate or delayed webhooks; retries that double-count stock or refunds.
- Different item IDs, bundles, variants, units, or store calendars.
- Offline sales and returns that arrive after a stock decision.
- Seasonal patterns that make historical averages misleading.
- A model-generated product description with unsupported claims or incorrect attributes.

Prefer deterministic ledgers and explicit reconciliation for inventory and money. AI may assist with catalog classification or support drafts only when users can inspect and correct output.
