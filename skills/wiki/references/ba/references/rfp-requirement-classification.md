# RFP Requirement Classification — Taxonomy, Document Structure, and Scoring Defaults

## Section 1 — Requirement Category Taxonomy

### F — Functional
**Definition:** A capability, behaviour, or function the solution must provide.
**Signals:** "The system shall...", "The solution must enable...", "Users must be able to..."
**Examples:** "The system shall support multi-currency transactions", "The solution must integrate
with Salesforce CRM", "Users must be able to export data in CSV and Excel formats"

---

### T — Technical / Non-Functional
**Definition:** Quality attributes of the solution (performance, security, availability, scalability,
architecture constraints).
**Signals:** Uptime percentages, response time targets, security certifications, hosting requirements,
API standards, data residency.
**Examples:** "The solution must achieve 99.9% uptime", "All data must be encrypted at rest using
AES-256", "The solution must be deployable on AWS or Azure"

---

### C — Commercial
**Definition:** Pricing structure, payment terms, licensing model, and commercial obligations.
**Signals:** "The vendor must provide...", "Pricing must be...", "The contract must include..."
**Examples:** "The vendor must provide a fixed-price quote", "Licence fees must be per named user,
not per concurrent user", "The contract must include a 30-day termination for convenience clause"

---

### L — Legal / Contractual
**Definition:** Contract terms, IP ownership, liability caps, indemnification, audit rights.
**Signals:** IP assignment, liability, indemnity, governing law, dispute resolution, audit.
**Examples:** "IP developed under this contract shall vest in the buyer", "Liability cap: 2×
annual contract value", "The vendor grants the buyer audit rights on request"

---

### CO — Compliance / Regulatory
**Definition:** Requirements arising from law, regulation, industry standard, or certification.
**Signals:** GDPR, ISO, SOC2, FCA, HIPAA, PCI-DSS, specific regulatory references.
**Examples:** "The solution must be GDPR-compliant for EU data subjects", "The vendor must hold
ISO 27001 certification", "The solution must comply with PCI-DSS Level 1"

---

### SL — Service Level / SLA
**Definition:** Performance commitments that are contractually measurable and may attract
service credits.
**Signals:** Response times, resolution times, uptime SLA, support hours, escalation paths.
**Examples:** "Priority 1 incidents must be acknowledged within 15 minutes", "The vendor must
provide 24/7 support coverage", "Planned downtime must not exceed 4 hours per calendar month"

---

### S — Submission / Process
**Definition:** Requirements about the response itself — format, deadline, attachments, page limits.
These are knockout criteria: non-compliance invalidates the submission.
**Signals:** Deadline, file format, page limit, required sections, required signatories.
**Examples:** "Responses must be submitted by 17:00 GMT on [date]", "Responses must not exceed
50 pages excluding appendices", "The response must include a signed declaration of compliance"

---

## Section 2 — Common RFP Document Structure Patterns

Most enterprise RFPs follow one of these structures. Use this map to locate requirement sections quickly.

### Pattern A — Classic Public Sector / Government
1. Introduction and background
2. Scope of requirement
3. Mandatory criteria (pass/fail)
4. Scored criteria (weighted)
5. Pricing schedule
6. Terms and conditions
7. Response instructions and deadline

*Requirements concentrated in sections 2–4. Mandatory criteria in section 3 are knockout.*

### Pattern B — Commercial Enterprise
1. Executive overview
2. Functional requirements
3. Technical and integration requirements
4. Security and compliance requirements
5. Support and service requirements
6. Commercial terms
7. Vendor information and references
8. Submission instructions

*Requirements spread across sections 2–6. Mandatory vs. scored distinction often implicit.*

### Pattern C — RFI (Information Only)
1. Background and context
2. Areas of interest / questions for vendors
3. Response format
4. No formal scoring or commitment to proceed

*No compliance matrix needed for RFI. Extract questions; treat each as a capability inquiry.*

---

## Section 3 — Evaluation Criteria Default Weights (Evaluate Mode)

Apply these weights when the RFP does not specify weights. Adjust proportionally if the
RFP assigns different emphasis to specific areas.

| Criterion Cluster | Default Weight |
|------------------|---------------|
| Functional fit (solution meets requirements) | 30% |
| Technical fit and architecture | 20% |
| Vendor capability and track record | 15% |
| Service level and support model | 15% |
| Commercial and pricing | 15% |
| Compliance and security posture | 5% |
| **Total** | **100%** |

---

## Section 4 — Mandatory vs. Scored Distinction

A requirement is **Mandatory (Knockout)** if any of the following apply:
- The document explicitly labels it as mandatory, essential, or pass/fail
- It contains regulatory or legal language ("must", "required by law", "ISO certification required")
- It specifies a minimum threshold that is non-negotiable (e.g. "must hold Public Liability
  Insurance of at least £5 million")
- The submission instructions state that non-compliance disqualifies the response

A vendor that fails any Mandatory requirement is excluded from the scored evaluation entirely.
Do not include failed mandatory vendors in scoring comparisons — it creates a misleading comparison.

---

## Section 5 — Response Stub Quality Standards

When writing response stubs in Respond mode, apply these standards:

**Do:**
- State compliance status in the first sentence: "We are fully compliant with this requirement."
- Reference a specific capability, feature, or certification by name
- Quantify wherever possible: SLAs, performance metrics, certification numbers
- Be honest about partial compliance: "Our standard configuration supports X; Y requires
  a configuration option that we can enable as part of implementation."

**Do not:**
- Use marketing language ("industry-leading", "best-in-class", "world-class")
- Make claims that cannot be evidenced in the proposal
- Avoid addressing Non-Compliant items — state non-compliance clearly and offer an alternative or roadmap
- Copy the requirement text back as the response
