# Architecture and modular design

> **Status:** reviewed decision guide. Architecture examples are patterns, not prescriptions or tested implementations.

## Begin with constraints and quality needs

Architecture is a set of boundaries and choices that shape how a system can change, scale, fail, and be operated. Write down the user capabilities the system must support and its important quality needs: data sensitivity, availability, response time, peak load, recovery, portability, team skill, budget, and expected change. Use measurable targets where the product can define them.

Turn those needs into constraints on the design. “Fast” or “scalable” alone is not a requirement. A measurable response-time target for a named operation and workload can guide a decision; an unbounded expectation cannot.

## Choose boundaries before deployment units

Group code around cohesive capabilities and business rules. Give each module a clear responsibility, owned data, and narrow interface. Keep dependencies visible and avoid making every module reach into another module's tables or internal implementation. Start with a modular monolith when one deployable unit meets delivery, scale, and isolation needs. It keeps local calls and deployment simpler while preserving boundaries that can be tested.

Consider separate services when a real constraint justifies the added network, deployment, monitoring, data-consistency, and coordination work: independent release needs, fault or security isolation, distinct scaling profiles, or ownership boundaries that cannot be served well inside one process. Service extraction adds distributed-system failure modes; it does not remove the need for clear module boundaries.

| Approach | Often fits | Costs and risks to account for |
|---|---|---|
| Modular monolith | One product team, shared data needs, fast iteration | A single release and scaling unit; boundaries can erode without discipline |
| Separate services | Independent scaling, release, ownership, or isolation requirements | Network failures, observability, deployment, data ownership, retries, and eventual consistency |
| Event-driven components | Work can proceed asynchronously, producers and consumers need loose coupling | Duplicate/out-of-order delivery, replay, schema evolution, debugging, and operational tooling |
| Serverless functions/services | Bursty or event-oriented workloads where managed execution reduces operations | Runtime limits, cold starts, provider-specific behavior, local development, and cost under sustained use |

These categories can be combined. Do not select microservices, event streams, containers, or orchestration because they appear on a popular stack diagram.

## Make data ownership and failure behavior explicit

For each component, identify what it owns, what it calls, and what happens when a dependency is slow, unavailable, or returns invalid data. Define timeout, retry, duplicate handling, and degraded behavior at the boundary. Avoid retrying non-idempotent work without a deduplication or idempotency design. Keep security trust boundaries visible and carry them into threat modeling.

## Record decisions and revisit triggers

Use an [architecture decision record](../../templates/ARCHITECTURE_DECISION_RECORD.md) for consequential or difficult-to-reverse choices. Include alternatives, a simpler option, assumptions, operational consequences, and a specific trigger for review. Architecture can evolve; planned changes should be driven by evidence such as load tests, incidents, recurring coordination cost, or new isolation requirements.

### References

- [GOV.UK guidance: define user needs](https://www.gov.uk/guidance/define-user-needs): include operational, support, integration, and affected-user needs when making technology choices.
- [IETF RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html): authoritative semantics for HTTP methods, representations, status codes, and request/response behavior.
- [SoloFoundry architecture decision record template](../../templates/ARCHITECTURE_DECISION_RECORD.md): a reusable record for context, drivers, options, consequences, and review triggers.

