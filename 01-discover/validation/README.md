# Validation

> **Status:** reviewed experiment-design overview. The table is a starting point; outcomes depend on test design and context.

Validation is a sequence of tests that reduce uncertainty. Choose an experiment based on the riskiest assumption, not on what is easiest to build.

| Experiment | Useful when | Evidence to capture |
|---|---|---|
| Problem interview | Problem and workflow uncertain | Recent behavior, frequency, cost, workaround |
| Landing page | Message and segment uncertain | Qualified visits, conversion, source/channel |
| Prototype test | Workflow/usability uncertain | Task completion, errors, observed confusion |
| Concierge pilot | Outcome and willingness to pay uncertain | Usage, manual effort, renewal/payment behavior |
| Pre-order / paid pilot | Commercial commitment uncertain | Actual commitment, objections, delivery cost |

Define hypothesis, target cohort, method, success threshold, duration, ethical considerations and decision before running the experiment. Avoid moving thresholds after seeing results.

## Write a test card

State one assumption in a falsifiable way, the participants or system under test, the intervention, the observable outcome, the threshold that changes the decision, the duration and stop condition. Choose the smallest safe test that can produce relevant evidence. A clickable prototype is suitable for task comprehension; it cannot establish repeat purchase. An email signup shows interest in that message and channel; it is not a purchase. A deposit or paid pilot can signal commitment, but may still be atypical or non-repeatable.

Keep a denominator and report exclusions, missing data, recruitment channel, incentives, and any deviations from the plan. For small samples, report counts and qualitative context instead of implying statistical precision. For experiments involving live users, protect privacy and provide a way to stop or opt out where appropriate. Do not use deceptive pricing, collect unnecessary sensitive data, or expose users to unreviewed high-impact decisions.

## Select methods by uncertainty

| Uncertainty | Possible first test | What it can teach | What it cannot establish alone |
|---|---|---|---|
| Is the workflow real and painful? | Recent-event interview; observation with consent | Steps, context, workarounds, variation | Market prevalence or payment |
| Can the user complete the workflow? | Moderated prototype task | Comprehension, friction, errors | Sustained use or business viability |
| Can the team deliver the outcome? | Concierge or manual pilot | Delivery steps, operational effort, outcome | Scalable unit economics |
| Is there actionable interest? | Landing page with qualified traffic source | Response to a specific message/channel | Product-market fit or representative demand |
| Will a buyer commit? | Paid pilot, deposit, or procurement step | Commitment under stated terms | Retention, repeatability, margin, broad demand |

### References

- [Strategyzer Experiment Library](https://www.strategyzer.com/library/experiment-library): experiment types described in terms of risk, cost, timing, and evidence strength; practitioner resource.
- [Strategyzer, business hypothesis evidence](https://www.strategyzer.com/library/business-testing-is-your-hypothesis-really-validated): discusses limits of interviews and landing-page interest relative to real-world action and commitment.

