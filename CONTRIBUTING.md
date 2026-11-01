# Contributing to SoloFoundry

Thank you for helping make independent product building more understandable and responsible.

## What we value

- Accuracy, clarity, practical usefulness and intellectual honesty.
- Primary sources and reproducible claims.
- Vendor-neutral reasoning where possible.
- Explicit assumptions, alternatives, trade-offs and failure modes.
- Security, privacy, accessibility and maintainability.

## Before opening a pull request

1. Search for an existing guide to avoid duplication.
2. Identify the reader, problem and intended outcome.
3. Use `templates/GUIDE_TEMPLATE.md` for substantial guides.
4. Verify links and version-sensitive claims.
5. Include source title, publisher/author, URL, access or publication date, and why it is useful.
6. Mark claims as fact, recommendation, assumption or personal observation where ambiguity matters.
7. Do not copy third-party prose, diagrams, screenshots or code without permission and compatible licensing. Summarize in your own words and cite the original.
8. Never include secrets, private customer data or credentials.
9. Update `CONTENT_STATUS.md` and source freshness entries when a guide changes maturity or relies on time-sensitive material.
10. For a local preview, install `requirements-docs.txt` and run `mkdocs serve`. The documentation workflow checks local links, source metadata, and a strict site build.

## Maturity labels

- `draft`: incomplete or not independently checked.
- `reviewed`: checked for clarity, source quality and internal consistency.
- `tested`: implementation or workflow has been executed under documented conditions.

## Pull request checklist

- [ ] Scope and audience are clear.
- [ ] Claims are sourced or labeled as recommendations/assumptions.
- [ ] Alternatives and trade-offs are discussed.
- [ ] Security/privacy/accessibility concerns are considered.
- [ ] Links and code examples are checked.
- [ ] No third-party content has been copied improperly.
- [ ] Related index and `CONTENT_STATUS.md` are updated.
- [ ] Source register last-checked dates and recheck triggers are current.
- [ ] Examples state whether they are fictional, planned, or actually executed.

## Review and maintenance

Substantial guides should receive an editorial review before being described as `reviewed`. A `tested` label requires an executed walkthrough with environment, version, data boundary, steps, and observed result recorded. When a source, standard, provider API, legal rule, or market claim may change, add a dated source and a clear recheck trigger in `resources/SOURCE_REGISTER.json`.

Use the repository [pull request template](https://github.com/Chandanrohit/SoloFoundry/blob/main/.github/PULL_REQUEST_TEMPLATE.md). Please keep one coherent reader outcome per contribution; splitting unrelated changes makes technical and editorial review easier.

The project aims to reply when maintainers are available; it has no service-level response promise. See [SUPPORT.md](SUPPORT.md), [SECURITY.md](SECURITY.md), and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Documentation site

The site is built from the Markdown already in the repository using Material for MkDocs. Preview locally with:

```powershell
python -m pip install -r requirements-docs.txt
mkdocs serve
```

The Actions workflow builds and publishes on updates to `main`. For the first deployment, a repository maintainer must open **Settings → Pages** and set the publishing source to **GitHub Actions**. The site URL is `https://chandanrohit.github.io/SoloFoundry/` after Pages is enabled and the deployment succeeds. A passing workflow build alone does not prove the Pages setting or live deployment is complete.
