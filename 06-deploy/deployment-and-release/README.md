# Deployment and release for independent builders

**Maturity:** reviewed method guide; no provider deployment was executed.

Pick the smallest hosting model that meets data, latency, availability, and growth needs. Every additional platform is an operating surface: identity, network, patching, monitoring, backup, and billing.

## Choose a deployment shape

| Shape | Fits | Costs and risks to account for |
|---|---|---|
| Static hosting + managed APIs | Static sites, lightweight client apps | API limits, secrets must stay server-side, separate data services |
| Managed application platform / PaaS | Most early web products and APIs | Provider constraints, platform-specific config, service limits |
| Serverless functions | Event-driven or bursty work with short tasks | Cold starts, execution limits, distributed logs, retry/idempotency needs |
| Virtual machine | Custom runtime or persistent process | OS patching, firewall, process supervision, backup and recovery ownership |
| Containers on a managed service | Reproducible runtime or multiple services | Image patching, registry credentials, network and orchestration complexity |
| Kubernetes / self-managed cluster | Many workloads or a team with platform capacity | High operational burden; rarely a solo starting point |

Before choosing, write down where user data may reside, who patches the runtime, how backups work, how to roll back, what the monthly spend cap is, and which provider limits could block launch. See [stack comparisons](../../templates/STACK_COMPARISON.md).

## A safe release path

```text
change → review and automated checks → immutable build artifact
      → staging smoke check → database compatibility check
      → limited production rollout → verify → monitor or roll back
```

Keep the first pipeline understandable. Protect the default branch; grant CI only required permissions; store deploy credentials as secrets; pin or review third-party actions; never execute untrusted pull-request code with production secrets. GitHub's [secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) documents relevant risks.

### Database and state changes

Use additive migrations first: add nullable fields/tables, deploy code that supports old and new shape, backfill in bounded batches, then remove old fields only after all readers are updated. Take a backup before destructive changes and verify restoration separately. Application rollback does not reverse every data migration; write down the recovery action before release.

### Rollout checklist

- Build artifact is immutable and tied to a source revision.
- Required checks pass; credentials and logs are reviewed for leakage.
- Configuration and migrations are compatible with current production.
- Backup and restore path are understood for affected state.
- Smoke check covers sign-in, core user task, and one failure path.
- Errors, latency, spend, and provider health have a visible dashboard or alert.
- Rollback or feature-disable path is available and tested in a safe environment.

## Learn by doing

Deploy a tiny sample service with no real user data. Add a health endpoint, environment-specific configuration, CI build, staging deploy, and manual production approval. Make a harmless release, observe it, then practice rollback. Capture the exact steps in a runbook before deploying a customer product.

## References and tools

- [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use): permissions, secrets, untrusted code, and third-party actions.
- [SLSA getting started](https://slsa.dev/how-to/get-started) and [build provenance](https://github.com/slsa-framework/slsa/blob/main/spec/build-provenance.md): understand how to establish where an artifact came from; adopt controls that match risk.
- Infrastructure as code can make environments repeatable, but state files and plans can contain secrets. Protect state access and review destructive plans.

Next: [reliability and recovery](../../07-operate/reliability-and-recovery/README.md), [security](../../05-secure/secure-product-engineering/README.md), and [architecture decision records](../../templates/ARCHITECTURE_DECISION_RECORD.md).
