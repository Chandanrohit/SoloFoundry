# Healthcare product discovery and design

**Maturity:** reviewed domain guide; no clinical or regulated healthcare product has been assessed.

Healthcare software has multiple users and consequences: a patient, clinician, administrator, payer, and provider organization can have different needs and authority. Begin with a workflow such as scheduling, document routing, claims reconciliation, or clinician-reviewed reference lookup. Do not begin with autonomous diagnosis.

## Separate administrative from clinical function

Map who enters, reviews, changes, and acts on information. Identify the source of truth, handoffs, downtime procedure, and how corrections reach downstream records. A scheduling reminder has different risk from a recommendation that changes diagnosis or treatment. Intended use and actual claims matter; seek regulatory and clinical review before crossing into clinical decision support or medical-device territory.

For a low-risk administrative pilot, use synthetic or de-identified test data where appropriate, measure task completion and handoff errors, and keep a manual fallback. Do not claim that de-identification removes every privacy risk without a proper method and assessment.

## Safety and privacy requirements

- Preserve patient identity and record provenance; prevent mix-ups across individuals and organizations.
- Use role-based access, minimum necessary data, audit trails, secure messaging, and time-bounded access.
- Show missing, stale, and conflicting values rather than silently resolving them.
- Validate with clinicians and affected users; test accessibility and language needs.
- Define downtime, escalation, correction, incident communication, and retention procedures.
- Do not send patient data to analytics, models, or vendors until the purpose, terms, and obligations are reviewed.

Measure unsafe handoff rate, correction and escalation rate, completion time, accessibility issues, and user-reported burden. Engagement alone is not evidence of learning or clinical benefit.

## Standards and specialist review

For U.S. contexts, [HHS HIPAA cloud guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html) explains why a provider that creates, receives, maintains, or transmits electronic protected health information on behalf of a covered entity may be a business associate and require an appropriate agreement. This is not a determination that HIPAA applies to a particular product; confirm roles, contracts, and current rules with counsel. Other countries have separate health privacy regimes.

Clinical validity, interoperability, procurement/security review, and the possibility of medical-device regulation require people with domain expertise. See [incident/recovery planning](../../07-operate/reliability-and-recovery/README.md) before running any workflow that affects care.
