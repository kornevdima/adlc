# Requirement Types — Classification Taxonomy

## Purpose
Use this reference during Step 2 (Classify) of ba-elicitation-synthesizer.
Apply the decision tree first; use the per-type examples to validate your classification.

---

## Decision Tree

```
Does the statement describe what the SYSTEM must DO or PROVIDE?
├── Yes → FR (Functional Requirement)
└── No
    ├── Does it describe HOW WELL the system must do it?
    │   ├── Yes → NFR (Non-Functional Requirement)
    │   └── No
    │       ├── Is it stated as TRUE without verification (believed, not proven)?
    │       │   ├── Yes → AS (Assumption)
    │       │   └── No
    │       │       ├── Does it RESTRICT what the solution can be or use?
    │       │       │   ├── Yes → CO (Constraint)
    │       │       │   └── No
    │       │       │       ├── Does it reference ANOTHER system, decision, or delivery that must happen first?
    │       │       │       │   ├── Yes → DE (Dependency)
    │       │       │       │   └── No
    │       │       │       │       ├── Does it describe something that MIGHT go wrong or be uncertain?
    │       │       │       │       │   ├── Yes → RI (Risk Indicator)
    │       │       │       │       │   └── No → OQ (Open Question) — something needs clarification
```

---

## Type Definitions and Examples

### FR — Functional Requirement
**Definition:** A capability, behaviour, or function the system must provide or support.
The actor (user, system, role) must be explicit in the rewritten form.

**Standard form:** "The system shall [action verb] [object] [qualifying condition]."
Or persona form: "When [actor] [action], the system shall [respond/enable/prevent]."

**Positive examples:**
- "Users need to be able to reset their password via email link." → `The system shall enable registered users to reset their password via a one-time email link.`
- "We have to send confirmation emails." → `The system shall send an order confirmation email to the customer within 60 seconds of a successful transaction.`
- "Managers should approve timesheets." → `The system shall provide line managers with a timesheet approval workflow, including approve, reject, and return-for-correction actions.`

**Boundary — not FR:**
- "It should be fast" → NFR (performance)
- "We assume users have internet access" → AS
- "It must run on our existing Azure subscription" → CO

---

### NFR — Non-Functional Requirement
**Definition:** A quality attribute of the system — how well it performs a function, not what it does.

**Sub-types:**
| Sub-type | Trigger words | Example metric |
|----------|--------------|----------------|
| Performance | fast, responsive, real-time, concurrent users | Response time ≤ 2s at 500 concurrent users |
| Availability | uptime, always on, 24/7, no downtime | 99.9% uptime excluding scheduled maintenance |
| Scalability | grow, expand, more users, volume increase | Support 10x current transaction volume with no architecture change |
| Security | secure, encrypted, access control, GDPR, ISO 27001 | All PII encrypted at rest using AES-256 |
| Usability | easy to use, intuitive, training, accessibility | WCAG 2.1 AA compliance for all UI components |
| Maintainability | support, patch, upgrade, change easily | New report type deployable with no code change |
| Portability | run on, browser, mobile, cloud | Operational on Chrome, Edge, Safari (latest two versions) |
| Compliance | must comply, regulation, standard, audit | Compliant with GDPR Article 17 (right to erasure) |
| Recoverability | backup, restore, disaster recovery, RTO, RPO | RTO ≤ 4h, RPO ≤ 1h for Tier-1 services |

**Quality gate:** Every NFR must have a **measurable threshold**. If the source statement has none,
rewrite it with a `[NO MEASURE]` flag: "NFR-012 [NO MEASURE]: The system shall respond quickly to
search queries — threshold not defined; confirm with stakeholder."

---

### AS — Assumption
**Definition:** A statement accepted as true for planning purposes, without confirmed evidence.
If proven false, the requirement or scope may change.

**Standard form:** "It is assumed that [statement]."

**Examples:**
- "Users will have existing Active Directory accounts." → `It is assumed that all system users will have active accounts in the organisation's Azure AD tenant prior to go-live.`
- "The third-party API will be available." → `It is assumed that the payment gateway API will maintain its current interface specification for the project duration.`

**Handling:** Flag assumptions that are high-risk (i.e. if false, significant rework results) with `[HIGH-RISK AS]`.

---

### CO — Constraint
**Definition:** A restriction on the solution space imposed by business, technical, legal, or organisational factors.
Not a wish — a hard boundary.

**Standard form:** "The solution is constrained to [restriction]."

**Examples:**
- "We can only use AWS." → `The solution is constrained to deployment on the organisation's existing AWS tenancy; no additional cloud accounts may be provisioned.`
- "Budget is £200k." → `The solution is constrained to a total implementation budget of £200,000 including all third-party licences.`
- "Must go live by Q2." → `The solution is constrained to a go-live date no later than 30 June 2026.`

**Constraint vs. Assumption:** A constraint is imposed externally or by policy. An assumption is believed to be true. "Users have internet access" = AS. "The solution must not use the internet" = CO.

---

### DE — Dependency
**Definition:** A condition, decision, delivery, or external system that must exist or complete before this requirement can be implemented or verified.

**Standard form:** "This requirement depends on [dependency statement]."

**Examples:**
- "We need the SSO system to be live first." → `This requirement depends on the organisation's SSO platform being operational and accessible from the solution environment prior to UAT.`
- "This needs the API from the finance team." → `This requirement depends on Finance delivering the Accounts API (version ≥ 2.0) with defined endpoints for balance retrieval and transaction history.`

**Handling:** Always link the dependency back to at least one FR or NFR by ID.

---

### RI — Risk Indicator
**Definition:** A statement indicating a potential threat to delivery, adoption, quality, or value.
Not a confirmed problem — a signal for the risk register.

**Standard form:** "There is a risk that [event/condition] may [impact]."

**Examples:**
- "I'm not sure the data will be clean enough." → `There is a risk that source data quality is insufficient to support automated migration, which may delay go-live or require a manual cleansing workstream.`
- "Users might not adopt it." → `There is a risk that low user adoption post-go-live may reduce realised benefit, particularly if training is insufficient or the UI deviates significantly from current tooling.`

**Handling:** RI items are not requirements. Do not assign MoSCoW. Log them in the Issues Log with
a note to escalate to the project risk register.

---

### OQ — Open Question
**Definition:** A statement that reveals a gap in understanding and requires a specific answer before
the related requirement can be confirmed, written, or prioritised.

**Standard form:** Rewrite as a direct, answerable question. Do not leave as a vague note.

**Examples:**
- "We need to figure out permissions." → `OQ-003: What permission model applies — role-based, attribute-based, or a combination? Who defines and maintains roles? (Owner: Product Owner)`
- "Not sure about the mobile requirement." → `OQ-007: Is mobile access required at go-live, or is it a post-launch phase? If required, does "mobile" mean responsive web or a native application? (Owner: Sponsor)`

**Handling:** Every OQ must have a nominated owner (derive from context or leave as "TBC"). It must
also reference the FR or topic it blocks.

---

## Section 5 — Domain-Specific NFR Defaults

When a domain tag is provided, apply these baseline NFRs automatically if not already present in the input.
Flag them as `[DOMAIN DEFAULT — confirm applicability]`.

### Healthcare
- Data at rest encrypted (HIPAA / local equivalent)
- Audit log for all access to patient records
- Availability ≥ 99.9% for clinical systems

### Financial Services
- PCI-DSS compliance for payment data
- Transaction audit trail, immutable, 7-year retention
- Fraud detection response time ≤ 500ms

### Public Sector
- Accessibility: WCAG 2.1 AA minimum
- Data residency: data must not leave the defined jurisdiction
- GDPR compliance where EU data subjects involved

### Retail / E-Commerce
- Peak load: system must sustain 3x average traffic during promotional events
- Cart and session persistence: minimum 30 minutes
- Payment gateway failover: secondary provider within 10 seconds

### Technology / SaaS
- API response time ≤ 200ms at p95
- Zero-downtime deployment
- Tenant data isolation (multi-tenancy)
