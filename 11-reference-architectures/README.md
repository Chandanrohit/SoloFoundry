# Reference architectures

**Maturity:** worked examples; none is a production-tested template.

Reference architectures are worked teaching examples, not production templates. They show how requirements connect to data flow, trust boundaries, delivery, operations, and business constraints. Change them when your users, risk, or service promise differs.

## Worked architecture

- [Repair-shop appointment and waitlist service](repair-shop-appointments/README.md): a fictional small multi-tenant SaaS with a modular monolith, PostgreSQL, tenant isolation, notifications, privacy boundaries, deployment, and operating measures.

## How to read or contribute an architecture

Check the scenario assumptions first. Then inspect the requirements, context diagram, data lifecycle, component responsibilities, failure modes, security controls, rollout and recovery path, cost drivers, and rejected alternatives. Use the [architecture decision record](../templates/ARCHITECTURE_DECISION_RECORD.md) to adapt a decision to your own constraints.

Examples are explicitly hypothetical. Cost figures are formulae and drivers rather than provider quotes; check current pricing and service limits before budgeting.
