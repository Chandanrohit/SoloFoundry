# Reliability and recovery for a solo-operated product

**Maturity:** reviewed method guide; no service has been operated or recovery-tested.

Operations is the work that keeps a shipped product trustworthy: seeing failures, responding, restoring data, communicating with users, and learning. Start with the service's user promise; do not set an availability target that you cannot measure or sustain.

## Pick user-centered service indicators

Choose a small set tied to actual tasks, such as successful sign-in, completed checkout, API success, or time to load a core view. Define numerator, denominator, window, exclusions, and data source. A server returning HTTP 200 does not prove the user task succeeded.

An SLO is a target over a time window. Example only: if 99.5% of 10,000 monthly core-task attempts should succeed, the allowed unsuccessful attempts are 50. The target is meaningful only if events are measured consistently and the product's business promise supports it. A solo builder can begin with a service objective and a monthly review rather than complex error-budget automation.

## Observe enough to act

- **Logs:** event details for diagnosis; redact tokens, personal content, and secrets.
- **Metrics:** rates, counts, latency percentiles, queue depth, and spend trends.
- **Traces:** a request's path through dependencies when distributed behavior makes debugging hard.
- **User reports:** errors, confusing outcomes, and lost work that telemetry may miss.

Correlate with a request ID, use consistent timestamps, and restrict access. OpenTelemetry's [observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) explains signals and context. Use the simplest dashboard that helps answer: what failed, who was affected, since when, and what action is available?

Alert only when someone can take a defined action. For a one-person service, use a small set of high-signal alerts and a clear quiet-hours/maintenance policy. Avoid alerts for every transient dependency blip.

## Incident response with limited capacity

Prepare a one-page runbook with service/dependency map, dashboard, provider status links, credential rotation path, backup location, user communication channel, and escalation contact. During an incident:

1. Confirm impact and start a timestamped incident note.
2. Stabilize: disable a feature, shed load, or roll back if that is safer than debugging live.
3. Protect data and preserve useful evidence; avoid destructive “fixes” before understanding scope.
4. Communicate a short factual update to affected users when appropriate.
5. Restore service, then verify the core user task and data integrity.
6. Record cause, contributing conditions, what detection missed, and one or two owned follow-ups.

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integrates incident response with broader cybersecurity risk management. Use it for vocabulary and planning; adapt its organizational scope to a small product.

## Backups are not recovery until restored

Define:

- **RPO:** maximum acceptable data loss, expressed as time.
- **RTO:** target time to restore the service.
- What is backed up: database, uploads, configuration, encryption keys/secret recovery, and infrastructure definitions.
- Who can access backups, where they are stored, retention, and how deletion obligations apply.

Run a restore drill into an isolated environment. Verify schema, files, access controls, and a representative user task. Record duration and surprises; then update the RTO/RPO assumptions. A backup with inaccessible keys or an undocumented restore command is not a usable recovery plan.

## Solo-friendly operating cadence

- After each release: smoke-test the core task and check errors/latency.
- Weekly: review high-severity alerts, user reports, cost, backup completion, and dependency notices.
- Monthly: sample a restore, review access and secrets, examine SLO trends, and prune unused data.
- After incidents: close only the most valuable corrective actions and verify that they changed the failure path.

For build and release controls, see [deployment and release](../../06-deploy/deployment-and-release/README.md). For risk prioritization, see [secure product engineering](../../05-secure/secure-product-engineering/README.md).
