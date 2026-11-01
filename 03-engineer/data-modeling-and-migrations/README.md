# Data modeling and schema changes

> **Status:** reviewed method guide. Storage trade-offs depend on workload and operational constraints; examples are not benchmark results.

## Start from data access and invariants

List the entities or records the product needs, how they relate, how they are read and changed, which facts must remain consistent, and who may access them. Include growth, retention, export, deletion, recovery, reporting, and data quality needs. Let those requirements drive the data model and storage choice.

| Storage family | Often fits | Trade-offs to investigate |
|---|---|---|
| Relational | Related structured data, joins, constraints, and multi-record transactions | Schema evolution, query/index tuning, and operational capacity |
| Document | Records commonly read and updated as cohesive aggregates with flexible fields | Duplication, cross-record consistency, and query constraints |
| Key-value | Direct lookup by a stable key and simple access patterns | Limited query flexibility, key design, expiry, and consistency behavior |
| Time-series/analytical store | High-volume observations or analytical scans | Ingestion and retention design, query shape, and separation from transactional workflows |

These families overlap and vary by product. A familiar relational database is often a sensible starting point for business data, but measure the actual access pattern and constraints rather than treating any default as universal.

## Make correctness explicit

Use database constraints for invariants the database can enforce, and transactions for changes that must succeed or fail together. Define how concurrent updates behave and what a caller sees when a conflict occurs. Understand the chosen database's transaction isolation model; isolation names can have engine-specific behavior. Index for observed queries, accounting for extra storage and slower writes. Measure query plans and real workloads before adding caches or specialized stores.

## Change schemas safely

Treat a migration as a deployed change that may run while old and new application versions coexist. For a risky change, use an expand-and-contract sequence:

1. Add a compatible field or structure while old code still works.
2. Deploy code that can read both forms and writes the new form.
3. Backfill in bounded, observable batches; make the job resumable and safe to repeat.
4. Verify counts, constraints, and application behavior.
5. Switch reads fully to the new form, then remove old code and data only after the rollback window closes.

Not every migration needs every step. Estimate lock time, table size, write load, storage, rollback options, and the effect on live traffic before applying a change. A database rollback may not safely reverse already transformed data; sometimes a forward repair is safer.

## Protect data throughout its lifecycle

Classify data, minimize collection, define access and retention, and plan export or deletion. Use synthetic or properly de-identified test data where possible. Backups and restoration belong to operations planning; a schema change should remain compatible with the available backup and recovery strategy.

### References

- [PostgreSQL documentation: transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html): database-specific explanation of concurrent visibility and isolation behavior; consult the chosen engine's equivalent documentation.
- [PostgreSQL documentation: modifying tables](https://www.postgresql.org/docs/current/ddl-alter.html): examples of altering populated tables and the effects of schema changes.
- [GOV.UK: define user needs](https://www.gov.uk/guidance/define-user-needs): includes operational, support, integration, and affected-user needs in technology decisions.

