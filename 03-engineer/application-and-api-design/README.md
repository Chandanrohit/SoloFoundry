# Application and API design

> **Status:** reviewed method guide. API conventions need to be documented and tested for each product; no particular framework is assumed.

## Separate presentation, domain rules, and external concerns

The frontend should represent user intent and show the server's current state. The backend should enforce domain rules and validate every request at the trust boundary. Data access and third-party calls should be explicit dependencies rather than hidden in presentation code. These boundaries help keep behavior testable without requiring a large multi-service architecture.

Validate inputs on the server even when the browser also validates them. Return user-facing validation that explains how to recover without exposing stack traces, secrets, or internal implementation details. Keep authorization checks close to the operation and the resource being accessed; authentication (who is acting) does not establish authorization (what they may do).

## Design an API as a long-lived contract

For each operation, specify resource identity, method, request and response shape, status codes, permissions, pagination, filtering, sorting, concurrency behavior, error cases, and compatibility expectations. Use standard HTTP semantics consistently. Choose an error format clients can handle; [RFC 9457 Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html) defines a machine-readable format for HTTP API errors. Avoid returning internal exception text or sensitive details in public errors.

Think about retries and repeat requests. HTTP methods have defined semantics; where a command must not apply twice, give it an explicit idempotency strategy and define the key scope, retention, conflict behavior, and response on replay. For concurrent edits, decide whether stale writes are rejected, merged, or deliberately allowed. Document deprecation and migration paths before breaking clients.

## Treat integrations as unreliable boundaries

Every remote dependency can time out, rate-limit, change a schema, return partial data, or fail while your process is waiting. Set timeouts; use bounded retries with backoff only when retries are safe; limit concurrency; and give users or operators a useful state when the dependency is unavailable. Avoid retry storms and indefinite queues. Persist enough context to diagnose a failure without storing credentials or unnecessary personal data.

For webhooks, verify authenticity before processing, tolerate duplicate and out-of-order events, persist an event identifier or deduplication key, and separate acknowledging receipt from slower follow-up work where appropriate. Provide a safe replay or reconciliation path. Provider-specific delivery guarantees and signature procedures must be checked against that provider's current documentation.

## Keep versioning proportionate

An internal single-client API may evolve in lockstep with its caller. Public or independently deployed clients need an explicit compatibility policy. Additive changes are usually easier to deploy than renames, removals, or changed meanings. Test old and new clients during a migration window; version only when compatibility needs justify the ongoing support cost.

### References

- [IETF RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html): normative HTTP method and status semantics, including idempotent methods.
- [IETF RFC 9457: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html): standard shape for machine-readable HTTP error details.
- [OWASP API Security Project](https://owasp.org/www-project-api-security/): security risks and guidance for API developers; use alongside the dedicated SoloFoundry security material.
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html): distinguishes authentication design from application-specific authorization decisions.

