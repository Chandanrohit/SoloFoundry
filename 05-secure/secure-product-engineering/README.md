# Secure product engineering for a small team

**Maturity:** reviewed method guide; no product security assessment has been performed.

Security work is choosing what to protect, reducing the ways it can be reached, and preparing to notice and recover from failures. A solo builder cannot eliminate every risk; prioritize controls by data sensitivity, exposure, impact, and realistic capacity. Use the [threat model template](../../templates/THREAT_MODEL.md) as a working record.

## A practical threat-model loop

1. Draw the system and trust boundaries: browser, API, database, background jobs, providers, admin tools, backups, and CI.
2. List assets and obligations: accounts, customer content, credentials, payment state, private business data, availability, and deletion requests.
3. Identify actors and abuse cases: account takeover, tenant-crossing reads, forged webhooks, malicious uploads, dependency compromise, accidental exposure, and denial of service.
4. Rank by likelihood, impact, exposure, and detectability. Record uncertainty; a score is a prioritization aid, not a prediction.
5. Choose controls with a named owner and verification step. Prefer removing unnecessary data or capability over adding complex controls.
6. Revisit after new integrations, sensitive data, public endpoints, AI features, or major architecture changes.

## Secure defaults that pay off early

- Enforce authorization on every server-side resource request; authentication only establishes identity.
- Scope database queries by tenant and user; test a cross-account request explicitly.
- Store secrets in a managed secret store or deployment environment, rotate exposed credentials, and keep them out of source, logs, and client bundles.
- Validate input at boundaries; encode output for its context; use parameterized queries and established authentication libraries.
- Restrict dependency and CI permissions; pin or review third-party build actions; protect release credentials.
- Rate-limit expensive/public operations and bound file size, request time, and background retries.
- Collect the minimum personal data needed; document purpose, access, retention, deletion, and backup expiry.
- Use secure transport and managed encryption where available, while protecting keys and access paths.

For AI features, add prompt injection, sensitive-data disclosure, tool misuse, model/provider retention, and retrieval tenant boundaries to the model. See [AI workflow security](../../04-ai/tool-using-workflows/README.md).

## Use standards proportionately

- [OWASP ASVS](https://asvs.owasp.org/) provides testable application security requirements. Select relevant requirements for your architecture; it is not a substitute for testing or a certification claim.
- [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) organizes secure development practices across the software lifecycle. Check NIST for revisions before adopting in policy.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) gives a risk-management vocabulary useful for prioritization, not a checklist that makes a small product compliant.
- Legal, privacy, breach-notification, and sector obligations depend on jurisdiction, customer, and data. Verify primary local guidance and get qualified advice for consequential decisions.

## A 90-minute first pass

Draw one data flow, identify the three highest-impact assets, and write five plausible abuse stories. For each, choose one preventive control and one way to verify it. Fix exposed credentials and authorization gaps before polishing low-impact headers. Record accepted risks and the condition that would make you revisit them.

Then connect controls to the [deployment guide](../../06-deploy/deployment-and-release/README.md), [reliability and recovery guide](../../07-operate/reliability-and-recovery/README.md), and [threat model template](../../templates/THREAT_MODEL.md).
