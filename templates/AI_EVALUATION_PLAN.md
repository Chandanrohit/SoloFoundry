# AI evaluation plan

Copy this file for one feature. Do not include personal or confidential data unless processing is authorized and necessary.

## Feature and intended outcome

- Feature / owner:
- User task and expected benefit:
- Non-AI baseline:
- In-scope users, languages, data, and excluded uses:
- Material failure and recovery path:

## System and data

- Model/provider and pinned version (or “not selected”):
- Prompt/retrieval/tool version:
- Data sent, purpose, sensitivity, retention, deletion path:
- Authorization and tenant boundary:
- Known limitations:

## Evaluation cases

| Case ID / slice | Input source (safe/minimized) | Expected behavior / evidence | Safety label | Result / reviewer |
|---|---|---|---|---|

Include ordinary, edge, ambiguous, no-answer, abuse, and access-boundary cases where relevant. Record the rubric and keep a held-back regression subset.

## Measures and thresholds

| Measure | Definition | Release threshold | Result by slice |
|---|---|---|---|

Track task success, unsupported claims, citation correctness, refusal/abstention, safety failures, latency, errors, and spend as applicable. State denominators and sample size. Do not hide safety failures in an average.

## Rollout and operations

- Pre-release regression and human review:
- Canary scope and observation period:
- Rate/spend limits:
- Alerts and responder/action:
- Fallback and rollback switch:
- User feedback/report route:
- Logging minimization and retention:

## Decision record

- Decision: ship / limited rollout / revise / reject
- Evidence and unresolved uncertainty:
- Failure cases and retest plan:
- Reviewer and date:
- Next review trigger (model, data, prompt, provider, user population, or policy change):
