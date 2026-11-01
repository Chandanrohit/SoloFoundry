# Manufacturing product discovery and design

**Maturity:** reviewed domain guide; no operational technology system has been assessed.

Manufacturing combines IT systems with operational technology (OT) that can monitor or change physical processes. A builder should first target an observational, advisory, or administrative workflow—such as maintenance logs, quality evidence, inventory visibility, or shift handoff—before considering any control path.

## Map people, equipment, and downtime

Identify operator, maintenance lead, quality engineer, plant IT/OT, safety owner, buyer, and vendor. Trace data from a sensor, machine, spreadsheet, or MES/ERP system to a decision. Record units, calibration, timestamps, asset identity, network path, and what happens when the source is unavailable or wrong.

Choose a pilot area with a bounded machine and a human decision. Do not connect a prototype to a PLC or production control network. Simulate or read copied data first, then work with the plant's OT/security team on a formally approved test boundary.

## Reliability and safety before novelty

- Keep IT and OT trust boundaries explicit; restrict inbound/outbound paths and remote access.
- Do not send control commands from a web application or model-generated workflow.
- Design offline/degraded behavior, time synchronization, local buffering, and safe manual procedures.
- Preserve operator override and change approval; test fail-safe behavior with qualified engineers.
- Measure false alarms, missed defects, maintenance time, downtime, and operator workload.
- Document data ownership and access; production schedules and process parameters may be sensitive.

For security context use [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final), which addresses OT's performance, reliability, and safety needs. NIST noted a Revision 4 draft in September 2026; verify the publication status before adopting any edition as policy. This guide is not an OT risk assessment.

## A practical first vertical slice

Read a daily maintenance log export, normalize asset IDs and timestamps, surface records that lack a completed inspection, and let a maintenance lead verify them. Keep an export of source rows and a manual fallback. Only after users demonstrate value should the builder explore live connectors, predictive analytics, or controlled integration.

Related: [deployment and release](../../06-deploy/deployment-and-release/README.md), [incident recovery](../../07-operate/reliability-and-recovery/README.md), and [problem discovery](../../01-discover/README.md).
