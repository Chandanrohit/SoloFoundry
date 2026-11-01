# Accessible content and design systems

> **Status:** reviewed baseline guidance. This guide is not an accessibility audit or legal-compliance determination.

## Treat accessibility as part of product quality

Accessibility affects whether people can perceive, understand, navigate, and operate a product. Bring it into product requirements and prototypes, not only a final checklist. Ask which users, technologies, environments, languages, and support needs matter. Test with people who use assistive technologies when the product and access needs warrant it; no automated scan or checklist covers every barrier.

## Use standards carefully

[WCAG 2.2](https://www.w3.org/TR/WCAG22/) is the W3C Recommendation for web content accessibility. Select a conformance target with the people responsible for the product and applicable obligations. WCAG conformance is assessed against all relevant criteria at a stated level and scope; citing the standard or passing a scan alone does not prove conformance. Legal requirements vary by jurisdiction, product, and service.

For design and implementation, check semantic structure and names, keyboard operation and visible focus, zoom and reflow, color contrast, text alternatives, captions, form labels and errors, target size, motion preferences, authentication, and accessible recovery. Test manually with keyboard and relevant assistive technologies as well as automated tools.

## Write content for the task

Use the words people use for their goal. Put the main action and requirements where they are needed; explain unfamiliar terms; make headings descriptive; use link text that works out of context; and state consequences, costs, data use, and next steps plainly. Error messages should say what happened, how to fix it, and what happens to entered information. Do not rely on color, icons, or tone alone to convey meaning.

Plain language does not mean removing necessary precision. Get subject-matter review for technical, legal, health, or financial content. Localize for language and culture instead of assuming a translation alone makes an experience usable.

## Reuse patterns with evidence

A design system can improve consistency and reduce repeated implementation work. Choose components that fit the user's task and technical environment. Check component behavior, accessibility support, maintenance state, and customization cost. Document design tokens, interaction states, content guidance, and versioning; test the assembled service because accessible components do not guarantee an accessible whole.

### References

- [W3C Recommendation: Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/): normative web-content accessibility criteria and conformance model.
- [W3C WAI: What's new in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/): summary of the changes and added criteria.
- [GOV.UK Design System: accessibility](https://design-system.service.gov.uk/accessibility/): guidance for teams using GOV.UK components; applicability depends on a service's context.
- [GOV.UK content and publishing guidance: understand content design](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/): explains starting from user needs and keeping content findable and current; used as a practical reference rather than a universal style rule.

