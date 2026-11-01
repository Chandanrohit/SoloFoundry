# Lab: prepare and rehearse a first deployment

**Purpose:** turn the deployment method guide into a provider-neutral runbook. No cloud account or production system is required; do not use real user data in a practice environment.

## Choose a sample

Use a tiny service you own or a tutorial app with an explicit license. Record runtime, dependencies, required environment variables, data stores, and health check. If you have no service, write a deployment plan against a hypothetical service and mark execution “not run.”

## Walkthrough

1. Choose a hosting shape from [deployment and release](../deployment-and-release/README.md); explain why a simpler option does not fit.
2. Draw local, staging, and production boundaries. Identify secrets and verify no secret is placed in source control or client-side configuration.
3. Describe the build artifact and how it maps to a source revision. Identify CI permissions and the credential used for deployment.
4. Define a health check and a smoke test for sign-in (if applicable), the core task, and a controlled failure.
5. Write the rollout sequence, migration order, observation window, and rollback/feature-disable action.
6. If using a real sandbox: deploy to staging, execute smoke tests, deploy a harmless change, then practice a rollback. Capture command/console steps and observed errors without exposing credentials.
7. Review the runbook with the [release checklist](../deployment-and-release/README.md#rollout-checklist) and the security guide. Note what was actually executed.

## Completion record

| Item | Decision/evidence |
|---|---|
| Provider and plan / costs checked on date | |
| Data location and service limits | |
| CI identity and least permissions | |
| Build artifact/revision | |
| Smoke checks and results | |
| Migration and rollback path | |
| Backup/restore dependency | |
| Steps run vs planned | |
| Follow-up / owner | |

“Deployed once” does not establish availability, security, or successful disaster recovery. Do a separate restore exercise using [reliability and recovery](../../07-operate/reliability-and-recovery/README.md).
