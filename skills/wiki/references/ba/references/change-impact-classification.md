# Change Impact Classification — Rules, Scoring, and Approval Routing

## Purpose
Use during Assess Change mode (BABOK 5.4) of ba-requirements-lifecycle. Defines how to
classify a change request, score its impact, and route it to the correct approval authority.

---

## Change Request Classification

### Primary classification

| Class | Definition | Key indicators |
|-------|-----------|----------------|
| Minor | Wording or formatting only; functional intent unchanged | No new actor, no new condition, no new integration, no change to MoSCoW |
| Moderate | Functional scope change within already-agreed boundaries | New condition on existing FR, adjusted NFR threshold, requirement split or merge |
| Major | Adds a new capability, removes a previously agreed capability, or has material budget or timeline impact | New Epic required, new integration point, story count change > 20%, delay of ≥ 1 Sprint |
| Critical | Changes baseline assumptions, alters contractual commitments, or redefines the project's strategic scope | Business case assumptions invalidated, sponsor-committed deliverables changed, regulatory requirements altered |

When in doubt between two adjacent classes, apply the higher class.

---

## Impact Scoring

Score each change request on four impact dimensions. Each dimension is rated 0–3.

### Dimension 1: Functional scope impact
| Score | Meaning |
|-------|---------|
| 0 | No functional change — wording only |
| 1 | Clarifies an existing function without adding or removing behaviour |
| 2 | Modifies the behaviour of an existing function |
| 3 | Adds a new function or removes an existing one |

### Dimension 2: Downstream artefact impact
| Score | Meaning |
|-------|---------|
| 0 | No downstream artefacts need to change |
| 1 | 1–3 stories or test cases need to be updated |
| 2 | 4–10 stories or test cases need to be updated, or an epic is affected |
| 3 | More than 10 artefacts affected, or the product backlog structure changes |

### Dimension 3: Schedule and cost impact
| Score | Meaning |
|-------|---------|
| 0 | No schedule or cost impact |
| 1 | Minor: absorbed within existing Sprint or budget contingency |
| 2 | Moderate: requires re-planning within the current release |
| 3 | Significant: delays a milestone, extends the project, or requires additional budget approval |

### Dimension 4: Stakeholder impact
| Score | Meaning |
|-------|---------|
| 0 | No stakeholder notification required |
| 1 | Inform only — Manage Closely stakeholders should be briefed |
| 2 | Consult required — at least one stakeholder needs to approve the change before it proceeds |
| 3 | Escalation required — change affects sponsor commitments or cross-team agreements |

### Composite impact score
Sum the four dimension scores. Use this total to guide (but not override) the classification.

| Total score | Indicative classification |
|------------|--------------------------|
| 0–2 | Minor |
| 3–5 | Moderate |
| 6–9 | Major |
| 10–12 | Critical |

The classification takes precedence if a single dimension score of 3 exists, regardless of total.

---

## Approval Routing

### Standard routing by classification

| Classification | Approval required from | Turnaround expectation |
|---------------|----------------------|----------------------|
| Minor | BA lead only | Same day |
| Moderate | BA lead + Product Owner or Sponsor representative | 2–3 working days |
| Major | Sponsor + Technical Gatekeeper (if technical impact) + Product Owner | Formal change control board — 5 working days |
| Critical | Programme Director or CXO + all Manage Closely stakeholders | Escalation meeting required — timeline to be agreed |

### Escalation triggers (automatic upgrade to next class)
Apply regardless of composite score:
- Change affects a Must Have requirement that is already Approved: upgrade to at least Major
- Change was previously rejected and is being re-submitted in modified form: upgrade to Major
- Change originates from a regulatory body or external audit finding: upgrade to Critical
- Change was not submitted through the defined change control process: flag as `[UNCONTROLLED CHANGE]` and require retrospective approval before proceeding

---

## Change Log Schema

One row per change request in the running change impact register.

| Column | Content |
|--------|---------|
| CR ID | CR-{NNN} sequential |
| Date raised | Date the change request was submitted |
| Raised by | Name and role |
| Requirement ID(s) | Comma-separated list |
| Change description | One sentence: what is being proposed |
| Reason | Business driver or stakeholder instruction |
| Classification | Minor / Moderate / Major / Critical |
| Dimension scores | D1 / D2 / D3 / D4 as four separate columns |
| Composite score | Sum |
| Downstream artefacts affected | Story IDs and Test Case IDs |
| Approval required from | Named role(s) |
| Decision | Approved / Rejected / Deferred / Descoped |
| Decision date | Date the decision was made |
| Decision maker | Name and role |
| Implementation notes | Which stories and test cases were updated as a result |
| Status | Open / Approved / Rejected / Closed |

---

## Escalation Procedure

When a change request reaches Critical classification or triggers an automatic escalation:

1. Freeze downstream artefacts: notify ba-user-story-factory and ba-test-case-generator
   operators not to work on affected items until the CR is resolved.
2. Prepare a one-page change impact summary (not the full CR record) for the escalation audience.
   The summary must contain: the change in one sentence, the business driver, the options
   (proceed / reject / defer / alternative), the financial impact estimate, and the recommendation.
3. Record the escalation in the change log with status "Escalated — awaiting decision".
4. On resolution, update the requirements register version, the change log, and notify all
   downstream skill operators to resume work.

---

## Version Control Conventions

When a requirement is modified following an approved change request:
- Increment the minor version of the requirements register (e.g., v1.2 becomes v1.3)
- Add a note to the requirement row: `[Modified per CR-{NNN} — {date} — approved by {role}]`
- Retain the original requirement text in a "Previous version" column (hidden by default; visible on request)
- Major changes that affect the project baseline increment the major version (v1.x becomes v2.0)
  and require a new sponsor sign-off of the full register

A version history table must appear on the change log sheet of every versioned requirements register:

| Version | Date | Changed by | Summary of changes | CR reference |
|---------|------|-----------|-------------------|-------------|
| v1.0 | | | Initial baseline | — |
| v1.1 | | | | |
