# Testing and software quality

> **Status:** reviewed method guide. The suggested portfolio is a starting point; choose checks according to risk, architecture, and change cost.

## Test risks and behavior, not implementation trivia

Start with what could harm users, corrupt or expose data, break a core workflow, violate a contract, or become costly to change. Write examples that show observable behavior and failure handling. Tests should make the system safer to change; tests coupled to private implementation details can make even safe refactoring expensive.

## Use multiple verification boundaries

| Check | Best for | Limits |
|---|---|---|
| Unit | Deterministic domain rules, parsing, calculations, and edge cases | Does not prove real database, network, or UI behavior |
| Component/integration | A module working with a real database, queue, filesystem, or service boundary | Slower and may need managed test environments or careful fixtures |
| Contract | Compatibility between independently changed producers and consumers | Only covers the contract cases and versions included |
| End-to-end | A small number of critical user workflows across the assembled system | Slower, harder to diagnose, and prone to environmental flakiness |
| Exploratory/manual | Novel flows, usability, content, and behavior difficult to encode | Findings need a clear record and follow-up; not repeatable by themselves |

The “test pyramid” is a metaphor, not a required ratio. Some products gain more confidence from integration tests; prototype work may need fast user tests more than a large automation suite. Choose the smallest set of checks that catches consequential failures quickly and reliably.

## Make tests trustworthy

Keep tests deterministic where possible: control time, randomness, and external services; isolate test data; clean up resources; and avoid relying on shared mutable environments. When a test flakes, diagnose whether the problem is the product, test design, or environment before rerunning it until it passes. Track slow or unstable tests because they can hide real failures and discourage use of the suite.

Test invalid input, permissions, boundary values, duplicate requests, dependency failures, migrations, and recovery paths where those risks apply. Use real integration tests for critical behavior that mocks cannot prove. Do not use production secrets or identifiable user data in test fixtures.

## Measure performance and maintainability

Define a user-relevant performance question before profiling. Measure representative operations and realistic data sizes; identify whether time is spent in the browser, database, network, or dependency. Optimize the measured bottleneck and recheck the outcome. Premature caches and asynchronous work can add consistency and recovery problems without improving the user's experience.

Make code understandable through clear names, cohesive modules, explicit dependencies, small reviewable changes, and useful tests. Refactor when evidence shows that duplication, coupling, or unclear behavior is slowing delivery or causing defects. Record unusual complexity and migration cost instead of treating every code-quality preference as a rewrite mandate.

### References

- [Martin Fowler: The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html): practitioner discussion of test scope, feedback speed, integration boundaries, and end-to-end test costs. The model is a heuristic, not a universal test-count rule.
- [GOV.UK Service Manual: test your service regularly](https://www.gov.uk/service-manual/technology/quality-assurance-testing-your-service-regularly): public-sector guidance to test usability, technical behavior, and unusual operating conditions.

