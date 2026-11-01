# Tabletop: a release exposes another customer's data

**Purpose:** rehearse decisions and communication without touching production. Scenario details are fictional.

## Scenario card

After a release, one customer reports seeing a record that appears to belong to another account. The report includes a screenshot with a record identifier. Logs show a rise in 403 responses but no clear data export event. The database is healthy. You are the sole maintainer, and another release is scheduled in two hours.

## Round 1: first 15 minutes

Write your actions before reading ahead:

- Who is potentially affected, and how will you establish scope without broadening exposure?
- What feature or access path can you disable safely?
- Which logs/evidence should be preserved and who can access them?
- What do you tell the reporter now? What do you avoid claiming?
- What credentials, sessions, or links might need revocation?

### Facilitator prompts

Contain access first; preserve evidence; do not copy sensitive records into public issues or chats. Do not assume a 403 means no data was disclosed. Pause the planned release. Follow the incident and privacy reporting obligations for the relevant jurisdiction/customer contract; do not guess at deadlines.

## Round 2: scope and recovery

New information: a tenant filter was omitted in one export endpoint. The database contains records from 14 accounts, and one account made three export requests. A backup is available but restoring the entire database would erase newer writes.

- How do you determine which requests returned data and to whom?
- Can the affected endpoint be disabled while other product functions remain available?
- What targeted fix/test would prevent cross-tenant access on all endpoints?
- How will you preserve evidence and coordinate with the customer before notifying others?
- What criteria allow a safe fix rollout? How do you monitor for recurrence?

## Round 3: user communication and follow-up

Draft a short holding update with known facts, current containment, next update time, and a contact route. Do not disclose another customer's data or speculate about cause until verified. Consult counsel/contract obligations for notifications.

After containment, record timeline, impact, contributing conditions, detection gap, and no more than three prioritized corrective actions. Include owner, due date, verification test, and affected data deletion/retention follow-up.

## Debrief scorecard

| Area | Ready / gap | Evidence or next step |
|---|---|---|
| Containment and rollback | | |
| Tenant-isolation tests | | |
| Evidence preservation and access | | |
| Customer communication owner | | |
| Legal/contract notification decision path | | |
| Backup and targeted recovery understanding | | |
| Alert/runbook discoverability | | |
| Follow-up ownership and verification | | |

This exercise is not a legal determination or proof of incident readiness. Connect it to the [threat model](../../templates/THREAT_MODEL.md) and [reliability and recovery guide](../reliability-and-recovery/README.md).
