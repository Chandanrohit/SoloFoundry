# Billing and service integrations

> **Status:** reviewed conceptual guide. This is not payment-provider implementation advice, financial advice, or a substitute for jurisdiction-specific review.

## Model product state separately from provider state

Treat checkout, payment, invoice, subscription, refund, dispute, and product entitlement as related but distinct concepts. Define the states the product needs to represent and the user-visible effect of each transition. A successful redirect or browser callback is not durable proof that a payment settled; confirm state with the provider's server-side API or verified event flow.

Choose a provider by supported countries, payment methods, currencies, settlement, fees, taxes, fraud controls, subscription features, accessibility, data handling, and failure support. Check contractual terms and local legal/tax requirements before launch. Prefer provider-hosted payment capture or tokenized components when appropriate so the product does not unnecessarily handle raw payment credentials; this does not eliminate security or compliance responsibilities.

## Design for retries and event delivery

Network outcomes can be ambiguous: a request may succeed remotely even when your service times out before receiving its response. Use a provider-supported idempotency mechanism for retried write operations and bind the key to one logical action. Do not create a fresh key for each retry of that same action.

For provider events, validate the provider's signature using its current instructions, persist event identity, tolerate duplicates and reordering, and make handlers safe to retry. Acknowledge only after the event is durably accepted. Move slow work to a durable queue if needed, with replay, dead-letter handling, and visibility into failed events. Periodically reconcile provider records with local state so a dropped event does not leave access or billing permanently wrong.

## Test real lifecycle edges

Use the provider's test environment and synthetic events. Cover delayed or failed payment, authentication requirements, duplicate and out-of-order events, cancellation, failed renewal, refund, dispute, stale webhook, and the effect on entitlements. Test that users receive accurate status and a recovery path; do not promise access or charge state before it is confirmed.

Keep provider secrets server-side. Restrict permissions and rotate credentials according to provider guidance. Log correlation IDs and state transitions without recording card data, secret keys, or unnecessary personal data. For operational ownership and incident handling, see [Operations](../../07-operate/README.md); for threat modeling and data protection, see [Security](../../05-secure/README.md).

### References

- [IETF RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html): defines method idempotency semantics; application-level retry protection still needs an explicit design.
- [OWASP Webhook Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Webhook_Security_Cheat_Sheet.html): security risks and mitigation patterns for webhook consumers and publishers.
- [Stripe documentation: testing integrations](https://docs.stripe.com/automated-testing): provider-specific example of testing payment lifecycle outcomes with controlled responses; not a recommendation to choose Stripe.
- [Stripe documentation: receive events with webhooks](https://docs.stripe.com/webhooks): provider-specific event delivery and signature behavior; check the current documentation for whichever provider you use.

