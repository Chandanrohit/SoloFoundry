# Source freshness register

This register tracks time-sensitive primary references used in SoloFoundry's security, industry, business, and search guidance. It is a review queue, not a claim that every statement in every guide has been independently audited.

Each entry includes scope and a trigger for rechecking. `last_checked` means the page was opened on that date; it does not mean the policy will remain unchanged. Update the machine-readable [source register](SOURCE_REGISTER.json) when a key link changes and cite the page-specific source in the guide itself.

| Key | Source | Scope | Last checked | Recheck trigger |
|---|---|---|---|---|
| nist-ai-rmf | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | Risk management; no certification | 2026-11-01 | NIST revision or control-specific advice |
| nist-genai-profile | [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Cross-sector GenAI risk guidance | 2026-11-01 | NIST RMF/profile revision |
| owasp-genai | [OWASP GenAI Security Project](https://genai.owasp.org/) | Threat guidance; check edition/date | 2026-11-01 | New OWASP list or threat update |
| owasp-asvs | [OWASP ASVS](https://asvs.owasp.org/) | App security requirements | 2026-11-01 | New version or requirement-level citation |
| nist-ssdf | [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) | Secure development | 2026-11-01 | NIST revision |
| nist-ot-security | [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | OT; Rev. 4 draft noted Sep 2026 | 2026-11-01 | New draft/final or policy use |
| hhs-hipaa-cloud | [HHS HIPAA cloud guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html) | U.S. HIPAA contexts only | 2026-11-01 | HHS update or provider obligation claim |
| cfpb-data-rights | [CFPB financial data rights](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/personal-financial-data-rights/) | U.S.-specific; rule status can change | 2026-11-01 | CFPB/court status update |
| pci-ssc-library | [PCI SSC document library](https://www.pcisecuritystandards.org/document_library/) | Payment card environment dependent | 2026-11-01 | Before in-scope implementation advice |
| aba-rule-1-6 | [ABA Model Rule 1.6](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_6_confidentiality_of_information/) | U.S. model rule, locally adopted differently | 2026-11-01 | Rule revision or local legal claim |
| us-ed-student-privacy | [U.S. Department of Education privacy resources](https://studentprivacy.ed.gov/resources) | U.S. FERPA guidance | 2026-11-01 | Department update or real student data |
| eu-gdpr-business | [Your Europe GDPR business guide](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm) | EU overview; applicability must be assessed | 2026-11-01 | EU law/guidance change or new market |
| ftc-advertising | [FTC advertising and marketing](https://www.ftc.gov/business-guidance/advertising-marketing) | U.S. advertising claims and endorsements | 2026-11-01 | FTC rule/guidance update |
| google-search-essentials | [Google Search Essentials](https://developers.google.com/search/docs/essentials) | Google Search; no ranking guarantee | 2026-11-01 | Search policy update |
| google-ai-search | [Google generative AI search guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Google-specific; no universal GEO standard | 2026-11-01 | Guide or search feature update |
| sba-plan-business | [SBA plan your business](https://www.sba.gov/counseling/plan-your-business/) | U.S. business planning | 2026-11-01 | SBA resource moves/updates |
| sba-manage-business | [SBA manage your business](https://www.sba.gov/counseling/manage-your-business/) | U.S. business finance | 2026-11-01 | SBA resource moves/updates |

## Review cadence

Recheck sources when editing a linked recommendation, when an official publisher announces a revision, or at least annually for laws, standards, and provider-dependent advice. Remove or replace dead references; do not silently preserve a claim after its source changes. See the [source evaluation policy](SOURCE_EVALUATION.md).
