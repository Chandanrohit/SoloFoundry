# Product brief and scope

> **Status:** reviewed decision guide. The template is a planning aid; it does not prove desirability, feasibility, or viability.

## Start with the outcome

Write a short brief that lets a builder decide what to learn or deliver next. Carry forward evidence from discovery and preserve its limitations. Name the user and situation, the task or progress they need, what happens today, the evidence behind the need, and the result that would matter to them. Distinguish users from buyers, approvers, operators, support staff, and people affected by the product.

Use [the product brief template](../../templates/PRODUCT_BRIEF.md). Keep research evidence linked or summarized without publishing private participant information.

## Write a testable product hypothesis

A useful hypothesis connects a specific group and context to a user outcome, a proposed intervention, and a way to observe whether the outcome improved. It should expose assumptions rather than hide them inside solution language. For example:

> For [specific users] in [context], [change] may help them [observable outcome]. We will learn whether it works by observing [measure or behavior] over [time/context].

Avoid claiming causation from before-and-after metrics alone if other changes could explain the difference. Define a baseline and relevant comparison where practical.

## Set boundaries and sequence work

Document the smallest end-to-end scope that can deliver or test the outcome. Add explicit non-goals, dependencies, constraints, risks, and deferred needs. Include operational and failure states: accessibility, privacy, permissions, errors, empty data, cancellation, support, recovery, and data export or deletion where relevant.

Prioritize by user impact, evidence, risk, learning value, effort, and dependencies. Do not use a single numeric score as an automatic decision. Keep a short rationale for what is out of scope and what evidence or event would bring it back.

## Define acceptance around user behavior

Turn scope into observable outcomes and examples. State what the user can accomplish and how success, partial completion, error, and recovery will be checked. Implementation details can follow when they reduce ambiguity for the people building and testing the work. In regulated, safety-sensitive, or high-impact settings, include domain review and documented risk controls before testing with affected people.

## Keep the brief alive

Review the brief when new research, a production failure, a changed constraint, or an operational burden changes the premise. Record decisions and dates. A product brief should remain short enough to guide action; detailed technical choices belong in a linked architecture decision record.

### References

- [GOV.UK Service Manual: understand user needs](https://www.gov.uk/service-manual/service-standard/point-1-understand-user-needs): public-sector guidance to understand the wider problem, use research, and prototype hypotheses early.
- [GOV.UK: define user needs](https://www.gov.uk/guidance/define-user-needs): emphasizes evidence-based needs and the users affected by technology choices, including support and operations.
- [SoloFoundry opportunity assessment](../../templates/OPPORTUNITY_ASSESSMENT.md): carries discovery evidence and uncertainty into product decisions.

