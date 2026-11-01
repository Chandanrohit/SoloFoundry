# Stack combinations for independent builders

**Maturity:** decision guide; no stack is production-tested by SoloFoundry.

A stack is a set of interacting choices, not a popularity contest. Select the smallest combination that meets validated requirements and that you can operate. Service names and prices change; treat these as patterns, not endorsements or current quotes.

Use the [stack comparison template](../templates/STACK_COMPARISON.md) and compare the workload, data boundary, deployment, backups, support, cost drivers, lock-in, and exit path. No combination below is production-tested by SoloFoundry.

## Four useful starting profiles

| Profile | Concrete starting combination | Fits | Avoid when |
|---|---|---|---|
| Managed web monolith | Node.js active LTS + TypeScript in one server-rendered web application; managed PostgreSQL; hosted identity, transactional email, and object storage; GitHub Actions | Small SaaS, forms, dashboards, booking, internal workflows | You require offline-first behavior, custom networking, or cannot accept the host's runtime limits |
| Python API product | FastAPI + SQLAlchemy 2 + Alembic + PostgreSQL; a single web client; one managed app/container platform; OpenTelemetry-compatible logs/metrics | Data-heavy integrations, Python libraries, background jobs, or a clear API boundary | You do not need a separate API/client, cannot maintain Python dependencies, or need a one-language minimal setup |
| Managed event processing | Managed functions + durable queue + object storage + managed relational database; idempotent handlers; scheduled reconciliation | Webhooks, imports, bursts, and work that can safely retry | Long-running work, tight latency budgets, difficult local debugging, or portability is a primary requirement |
| Self-managed compact stack | Linux LTS VM + Docker Compose + Caddy + PostgreSQL + encrypted off-site backups + hosted email | Learning, sovereignty constraints, or a maintainer comfortable patching and restoring a server | You lack time for OS patching/on-call or cannot rehearse recovery |

## Decision matrix

Score each requirement 1–5 and weight the top three more heavily. Include the operating cost of your own time.

| Criterion | Questions |
|---|---|
| Time to first useful release | How many independent services and credentials must be configured? |
| Data risk | Who stores identity, uploads, logs, backups, and keys? Can tenants be isolated? |
| Reliability | How do health checks, retries, queueing, rollback, and restore work? |
| Cost | Which baseline fees and variable volumes apply? What triggers a surprise bill? |
| Portability | Can you export data and move workloads? Which APIs or managed features create lock-in? |
| Solo operability | Can one person update, alert, restore, and explain each component? |
| Growth path | What concrete bottleneck would trigger the next component? |

Do not compare only monthly hosting. Include database backups, email/SMS, model/provider calls, payment fees, observability, support work, compliance reviews, and migration effort. Recheck provider prices and region availability at decision time.

## A sensible adoption sequence

1. Start with a modular monolith and one relational database for most early SaaS products.
2. Use managed identity, payments, email, and storage where the service meaningfully reduces work; review data terms and exit options.
3. Add a queue only when asynchronous work needs retries/durability or its latency should not block a user request.
4. Add a cache only after measuring repeated expensive reads and defining invalidation behavior.
5. Split a service only for team ownership, security isolation, scaling, or independent release needs supported by evidence.
6. Revisit architecture when incidents, cost, or product requirements provide data—not because a diagram looks more impressive.

## Learning resources

- [Node.js release schedule](https://nodejs.org/en/about/previous-releases): select a currently supported LTS line at implementation time; do not pin a new project to an EOL runtime.
- [PostgreSQL documentation](https://www.postgresql.org/docs/): relational modeling, transactions, constraints, indexes, backup, and operations.
- [Docker Compose documentation](https://docs.docker.com/compose/): local multi-service development and its boundaries relative to production orchestration.
- [FastAPI documentation](https://fastapi.tiangolo.com/): Python API option; check its dependency and security guidance before adoption.
- [SQLAlchemy 2 documentation](https://docs.sqlalchemy.org/en/20/intro.html) and [Alembic](https://alembic.sqlalchemy.org/en/latest/): ORM/data access and database migration tooling; neither removes the need to inspect generated SQL or test migration recovery.
- [Caddy automatic HTTPS](https://caddyserver.com/docs/automatic-https): an option for a self-managed reverse proxy; certificates do not replace host patching, firewall rules, or application security.
- [GitHub Actions documentation](https://docs.github.com/en/actions): CI workflows and security practices; keep permissions narrow.
- [OpenTelemetry documentation](https://opentelemetry.io/docs/): portable instrumentation concepts; choose a backend based on data and retention needs.

## Estimate cost without false precision

For each candidate, build a monthly low/base/high estimate from current vendor calculators and your expected use: compute hours/requests, database baseline and storage, backups/egress, email/SMS, observability, identity MAU, support time, and paid integrations. Record date, region, free-tier assumptions, and the event that moves you into the next pricing tier. Compare an expected month and a peak/burst month. A free tier is a temporary constraint set, not a unit-economics model.

## Migration and exit checks

Before adopting a managed service, test whether you can export users/data, replace the provider, restore a backup elsewhere, and remove secrets/identifiers from logs. Keep business rules in application code where feasible. Document any proprietary API or data format that would make an exit expensive.

Use the [repair-shop reference architecture](../11-reference-architectures/repair-shop-appointments/README.md) to see one modest profile end to end.
