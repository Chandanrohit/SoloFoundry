<div align="center">
  <img src="assets/brand/solofoundry-logo.png" alt="SoloFoundry — anvil struck by a hammer, creating sparks" width="720">
  <h1>SoloFoundry</h1>
  <p><strong>Build with knowledge. Craft with purpose.</strong></p>
  <p>An open-source workshop for independent builders.</p>
</div>

---

## What is SoloFoundry?

SoloFoundry is a documentation-first, open-source knowledge system for people who want to take a product from an observed problem to a useful, secure, sustainable product. It connects product discovery, market evidence, design, software and AI engineering, security, deployment, operations, distribution, and business fundamentals.

It is not a boilerplate, a tool directory, or a promise that one person should become an expert in every discipline. It helps an independent builder make informed decisions, use tools effectively, recognize risks, and know when specialist help is necessary.

## The product-building journey

```mermaid
flowchart LR
  A[Observe a problem] --> B[Research users and market]
  B --> C{Evidence strong enough?}
  C -- No --> D[Run another experiment]
  D --> B
  C -- Yes --> E[Define product and UX]
  E --> F[Choose architecture and stack]
  F --> G[Build and test]
  G --> H[Secure and deploy]
  H --> I[Operate and support]
  I --> J[Distribute and grow]
  J --> K[Measure, learn, improve]
  K --> B
```

## Explore the workshop

| Area | What it helps you do |
|---|---|
| [00 · Foundations](00-foundations/) | Learn the independent-builder mindset and decision principles. |
| [01 · Discover](01-discover/) | Find painful problems, understand users, assess markets, validate demand. |
| [02 · Design](02-design/) | Turn evidence into product scope, workflows, UX and accessible interfaces. |
| [03 · Engineer](03-engineer/) | Build frontend, backend, APIs, data systems and architectures. |
| [04 · AI](04-ai/) | Design LLM, RAG, agent, evaluation and inference systems responsibly. |
| [05 · Secure](05-secure/) | Threat-model and protect products, data, identities and supply chains. |
| [06 · Deploy](06-deploy/) | Ship through cloud, containers, CI/CD, networking and infrastructure as code. |
| [07 · Operate](07-operate/) | Monitor, support, back up, respond to incidents and improve reliability. |
| [08 · Grow](08-grow/) | Position, distribute, market, measure acquisition and retain users. |
| [09 · Business](09-business/) | Understand pricing, billing, finance, legal basics and business models. |
| [10 · Industry playbooks](10-industry-playbooks/) | Apply the lifecycle to real industry problem spaces. |
| [11 · Reference architectures](11-reference-architectures/) | Study end-to-end architectures with explicit trade-offs. |
| [12 · Stack combinations](12-stack-combinations/) | Compare coherent technology combinations for specific constraints. |
| [Templates](templates/) | Reusable canvases, checklists, experiment logs and decision records. |
| [Resources](resources/) | Curated docs, standards, research, courses and repositories. |

## How SoloFoundry is different

A link collection tells you what exists. SoloFoundry aims to explain **how to decide, why a choice fits, what it connects to, and what can go wrong**.

Every substantial guide should connect: problem → requirements → architecture → components → implementation → security → deployment → operations → cost → product and business outcomes.

## Guide quality standard

Each guide should answer, where relevant:

1. What problem does this solve, and for whom?
2. When should you use it—and when should you avoid it?
3. What concepts and prerequisites matter?
4. How do the components interact? Include a diagram where useful.
5. What are the viable approaches, tools and alternatives?
6. What assumptions, trade-offs, costs and maintenance burdens apply?
7. What security, privacy, accessibility and reliability concerns apply?
8. How can a builder implement and test it?
9. What can fail in production, and how is it diagnosed?
10. What evidence, official documentation, standards, repositories or research support the guide?
11. What checklist or decision record should the reader leave with?

Use the [guide template](templates/GUIDE_TEMPLATE.md). Mark maturity honestly: `draft`, `reviewed`, or `tested`. Never label an example production-ready without evidence.

## Principles

- **Craft over shortcuts:** explain mechanisms, not just recipes.
- **Evidence over hype:** prefer primary sources, standards and reproducible examples.
- **Independence over dependency:** teach decision-making, not blind tool adoption.
- **Simplicity over complexity:** choose the least complex system that meets real requirements.
- **Depth over link volume:** curated references must have context and a reason to exist.
- **Practice over theory:** connect concepts to experiments, implementation and verification.
- **Safety by design:** security, privacy, accessibility and reliability are not afterthoughts.
- **Honest uncertainty:** distinguish facts, assumptions, recommendations and experience.

## Start here

If you have an idea, begin with [Problem Discovery](01-discover/problem-discovery/README.md), then use the [Opportunity Assessment](templates/OPPORTUNITY_ASSESSMENT.md) and [Experiment Log](templates/EXPERIMENT_LOG.md). Do not start by selecting a framework.

If you already have a product, start with the relevant engineering, security, deployment or operations guide and work backwards to identify missing evidence.

### Learning paths

- **I have an idea:** follow [the opportunity discovery path](01-discover/README.md), from problem signals to a build, pivot, pause, or reject decision.
- **I am shaping a product:** start with [Product Design](02-design/README.md), then work through engineering, security, deployment, and operations.
- **I already have a product:** use the relevant lifecycle area as an audit path; check its status in [Content Status](CONTENT_STATUS.md) before treating an outline as a complete guide.

SoloFoundry is being built in reviewable phases. A folder or planned topic is not evidence that a guide exists. The current phase and remaining lifecycle coverage are tracked in [the roadmap](ROADMAP.md) and [content status](CONTENT_STATUS.md).

## Contributing

Contributions are welcome: corrections, tested examples, architecture diagrams, industry research, reference updates and better learning paths. Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [source evaluation policy](resources/SOURCE_EVALUATION.md) first.

## Status and roadmap

This is an evolving knowledge base. The initial repository foundation defines its information architecture, templates, editorial rules and first discovery workflows. See [ROADMAP.md](ROADMAP.md) for staged delivery and [CONTENT_STATUS.md](CONTENT_STATUS.md) for coverage tracking.

## License

Original educational documentation and diagrams use **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Original code examples and software use the **MIT License** in [LICENSE](LICENSE). Third-party material remains under its own license; see [LICENSES.md](LICENSES.md).

---

<div align="center"><sub>SoloFoundry · Learn the craft. Understand the systems. Build independently.</sub></div>

