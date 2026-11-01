# Product engineering

> **Status:** reviewed learning path and method guides. The examples are conceptual; no reference implementation or production system is tested here.

Engineering turns a product brief into software that can be changed and operated. Begin with the user and operational needs from [product design](../02-design/README.md), then choose boundaries, data, interfaces, and verification methods that fit the real constraints.

## A practical learning path

1. [Architecture and modular design](architecture-and-modular-design/README.md): choose boundaries and architecture based on quality needs and team capacity.
2. [Application and API design](application-and-api-design/README.md): define frontend/backend responsibilities, API contracts, identity boundaries, and external integrations.
3. [Data modeling and schema changes](data-modeling-and-migrations/README.md): select storage based on access and consistency needs; evolve data safely.
4. [Testing and software quality](testing-and-software-quality/README.md): build a risk-based verification strategy and keep software changeable.
5. [Billing and service integrations](billing-and-service-integrations/README.md): model payment-provider boundaries, event delivery, retries, and entitlement state.

Use the [architecture decision record](../templates/ARCHITECTURE_DECISION_RECORD.md) when a choice has meaningful long-term consequences, and the [stack comparison](../templates/STACK_COMPARISON.md) when comparing whole-system options.

## Engineering principles

- Prefer the simplest architecture that meets written user, security, reliability, and operating requirements.
- Keep domain rules explicit and testable; isolate infrastructure details behind clear boundaries when that reduces coupling.
- Treat data, APIs, migrations, and integrations as contracts with failure modes and compatibility expectations.
- Verify important behavior at the boundary where it can actually fail. A test count or coverage percentage is not proof of product quality.
- Include performance and accessibility in product requirements; measure before optimizing.
- Authentication, authorization, secure data handling, production deployment, and incident response need deeper treatment in [Security](../05-secure/README.md), [Deployment](../06-deploy/README.md), and [Operations](../07-operate/README.md).

