# Legal, privacy, contracts, and customer support basics

**Maturity:** reviewed orientation guide; not legal advice, and no jurisdiction-specific review has been performed.

An independent builder remains responsible for understanding the business obligations attached to the product. The exact rules depend on where you operate, where customers are, what data/product you handle, and how you sell. Treat this guide as an issue-spotting map, then verify primary local sources or consult qualified counsel/accounting support for consequential decisions.

## Make an obligations map

Record:

- Business location, legal entity/owner, and markets served.
- Product category, customer type (consumer/business/child/regulated entity), and sales channels.
- Personal/sensitive data collected, purpose, processors, transfers, retention, deletion, and rights requests.
- Billing model, currencies, taxes, auto-renewal/cancellation, refunds, and chargeback handling.
- Third-party assets/code/data, open-source licenses, customer content, and ownership/assignment terms.
- Required registrations, licenses, insurance, accessibility requirements, and breach/reporting contacts.

Use the [threat model](../../templates/THREAT_MODEL.md) for data/security risk and the [vendor review](../../06-deploy/deployment-and-release/README.md) for provider boundaries.

## Privacy information and data handling

For each data field, say why it is needed, whether it is optional, who can access it, where it is sent, how long it is retained, and how the user can request correction or deletion. Make public notices match actual behavior; a privacy policy that describes a plan the product does not follow can mislead users. Minimize collection and retention. Keep analytics and marketing preferences separate from product-critical processing where required.

The EU's [Your Europe GDPR business guide](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm) describes GDPR obligations for relevant EU contexts, including transparency and data protection by default. It does not decide whether GDPR applies to a particular product or replace advice. U.S. state, federal, and other national rules differ and change; assess target markets individually.

## Terms, contracts, and intellectual property

Have qualified counsel review terms appropriate to the product and customer. Issues to discuss include scope/service availability, acceptable use, account closure, payment/refunds, support, data processing, security responsibilities, intellectual property, warranties, liability limits, dispute venue, and change notice. Consumer protection rules may limit what contract language can validly waive.

For business customers, determine whether a data-processing addendum, security exhibit, accessibility representation, insurance, or procurement terms are requested. Do not accept commitments that operations cannot meet. Keep signed agreements, versions, renewal dates, and notice windows in a controlled record.

Maintain a license and provenance record for dependencies, fonts, images, datasets, and contributions. Open-source usage does not remove license obligations; check the exact license, attribution, notice, source-offer, and trademark requirements. See repository [license inventory](../../LICENSES.md).

## Customer support as a product capability

Provide a visible contact route and state expected response windows honestly. Collect only information needed to diagnose an issue; never ask users to email passwords, payment card numbers, or access tokens. Classify requests by account/security, billing, data rights, product defect, and general question. Define how to acknowledge, investigate, escalate, resolve, and close each category.

Use support contacts as evidence: tag the user task, impact, workaround, and recurrence. Remove personal data before adding a case to an issue tracker or analytics. Publish incident updates when users are materially affected and keep status claims factual. For operations procedures, see [reliability and recovery](../../07-operate/reliability-and-recovery/README.md).

## Marketing and email

Keep claims evidence-based and testimonials authentic. Disclose material relationships, paid endorsements, affiliate links, and incentives according to the rules where the audience lives. Commercial email rules differ by country. The [FTC CAN-SPAM guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) covers U.S. commercial email, including identification and opt-out duties; it is not a global checklist.

## When to seek professional help

Get jurisdiction-specific advice before selecting an entity for liability/tax reasons, storing sensitive or children's data, selling into new markets, making regulated claims, signing enterprise data/security terms, hiring, raising funds, or handling an actual legal demand or breach. Keep a dated record of the question, source, decision, and review trigger.
