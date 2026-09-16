# BA Governance Templates — Governance Plan Structure, Information Management Schema, and Performance Review Rubric

## Purpose
Use during Plan Governance (mode 3), Plan Information Management (mode 4), and Identify BA
Performance Improvements (mode 5) of ba-planning-monitor. Provides the structural templates
and scoring rubrics for each.

---

## Part 1 — Governance Plan Structure

### Document header fields (mandatory)
Every BA governance plan must begin with these fields:

| Field | Content |
|-------|---------|
| Project name | |
| BA lead | Name + email |
| Sponsor | Name + role |
| Document version | v1.0 at initiation |
| Date | Creation date |
| Review date | Date when this plan will be reviewed (recommend: at end of first sprint or phase) |

---

### Section 1: Approval authority matrix template

Reproduce this table for every project, populated with named roles.

| Deliverable | Produces | Approves (A) | Reviews (C) | Notified (I) | Approval deadline |
|-------------|----------|-------------|------------|-------------|------------------|
| BA approach document | BA Lead | Sponsor | PM, Technical Gatekeeper | Project team | Before any BA activity begins |
| Stakeholder analysis | BA Lead | Sponsor | PM | All stakeholders | Before first workshop |
| Requirements register (baseline) | BA Lead | Sponsor | SMEs, Technical Gatekeeper, Compliance | End users | Before sprint 1 or design phase |
| BRD | BA Lead | Sponsor | Compliance, PM | All stakeholders | Before story writing or solution design |
| Process models | BA Lead | Process Owner | Technical Gatekeeper | End users | Before gap analysis |
| Gap analysis report | BA Lead | Sponsor | Technical Gatekeeper | PM, SMEs | Before business case or design phase |
| Business case | BA Lead | Board / CXO | Finance, PM, Legal | All Manage Closely stakeholders | Before procurement or budget release |
| Product backlog (baseline) | BA Lead | Product Owner | Development lead | Scrum team | Before Sprint 1 Planning |
| Test cases | BA Lead | QA Lead | Product Owner | Development team | Before UAT |
| Sprint Planning pack | Scrum Master | Product Owner | BA Lead | Scrum team | At Sprint Planning |
| Sprint Review report | BA Lead | Product Owner | Sponsor | All stakeholders | Within 24h of Sprint Review |

Adapt this table for the specific project — add or remove rows as needed.

---

### Section 2: Change control summary template

| Topic | Decision |
|-------|---------|
| How to submit a change request | [e.g., email to BA Lead with subject line "Change Request: {project}"] |
| Who classifies the change | BA Lead applies the classification rubric from ba-requirements-lifecycle |
| Turnaround time: Minor | Same working day |
| Turnaround time: Moderate | 2–3 working days |
| Turnaround time: Major | 5 working days — change control board meeting required |
| Turnaround time: Critical | Escalation meeting — timeline to be agreed |
| Where decisions are recorded | ba-requirements-lifecycle change impact register |
| Who can approve Minor changes | BA Lead only |
| Who can approve Moderate changes | BA Lead + Product Owner |
| Who can approve Major changes | Sponsor + Technical Gatekeeper + Product Owner |
| Who can approve Critical changes | Programme Director + all Manage Closely stakeholders |

---

### Section 3: Issue escalation path template

State this as a chain with contact details filled in:

1. Issue first raised with: BA Lead
2. If unresolved in 2 working days: Product Owner
3. If unresolved in a further 2 working days: Sponsor
4. If unresolved at Sponsor level or if the issue affects the business case: Programme Director / CXO
5. If the issue involves a regulatory commitment: escalate in parallel to Compliance officer

For workshop conflicts or stakeholder disputes: BA Lead mediates first. If unresolvable,
Sponsor makes the final decision. Record the decision in the Issues Log.

---

## Part 2 — Information Management Schema

### Artefact inventory columns

Every artefact produced on the engagement should appear in this inventory. Maintain it as a
sheet in the project management workbook.

| Column | Content |
|--------|---------|
| Artefact name | Human-readable label (e.g., "Requirements Register") |
| Filename pattern | As defined in CLAUDE.md naming conventions (e.g., `{prefix}_requirements_register.xlsx`) |
| Producing skill | Which suite skill produces it |
| Owner role | Role responsible for keeping it current |
| Storage location | Full path or URL |
| Access level | Open / Project team only / BA team only / Restricted (PII or commercial) |
| Version control method | Manual versioning (`v1.0`, `v1.1`) / Git / SharePoint versioning |
| Retention period | How long the artefact is kept after project close (e.g., "3 years per document policy") |
| Status | Not started / Draft / Under review / Approved / Archived |

---

### Repository folder structure template

Use this as the default. Adapt folder names to match the organisation's conventions.

```
{PROJECT-CODE}/
  00-governance/
    ba-approach/
    engagement-plan/
    governance-plan/
    information-management-plan/
  01-discovery/
    stakeholder-analysis/
    workshop-materials/
      {workshop_type}_{date}_facilitator_guide.docx
      {workshop_type}_{date}_workshop_deck.pptx
      {workshop_type}_{date}_pre_read.docx
      {workshop_type}_{date}_synthesis_export.docx
  02-requirements/
    requirements-register/
    BRD/
    requirements-traceability/
    change-requests/
  03-analysis/
    process-models/
      as-is/
      to-be/
    gap-analysis/
  04-definition/
    product-backlog/
    story-specs/
    business-case/
    financial-models/
    rfi-rfp/
  05-validation/
    test-cases/
    bdd-specs/
    uat-scripts/
    solution-assessment/
  06-delivery/
    sprint-packs/
    impediment-logs/
    acceptance-evidence/
    retro-actions/
  99-archive/
    superseded/
```

---

### Access level definitions

| Level | Who has access | Typical artefacts |
|-------|---------------|------------------|
| Open | All project stakeholders | Workshop pre-reads, sprint overviews, public-facing communications |
| Project team only | Named project team members + sponsor | Requirements register, BRD, process models, gap analysis, backlog |
| BA team only | BA Lead + named BA team members | Working drafts, issues logs, internal notes |
| Restricted | BA Lead + named approvers only | Commercially sensitive cost estimates, PII in stakeholder analysis, legal constraints |

PII handling note: any artefact containing personal data (names, contact details, employment
information) must be classified as Restricted and stored in compliance with the organisation's
data protection policy. Do not include personal data in artefacts classified as Open.

---

## Part 3 — BA Performance Review Scoring Rubric

Use during Identify BA Performance Improvements mode (BABOK 3.5).

### Dimension scoring guide

Score each dimension 1–5 using these criteria.

**Dimension 1: Requirements quality**

| Score | Evidence |
|-------|---------|
| 5 | All FRs had explicit actors and measurable conditions; NFR thresholds were all defined; zero requirements required rework after sprint starts |
| 4 | Fewer than 10% of FRs required rework; NFRs mostly measurable; minor ambiguity issues resolved quickly |
| 3 | 10–25% of FRs required rework; some NFRs lacked thresholds; conflicts surfaced late |
| 2 | More than 25% of FRs required rework; frequent ambiguity; NFRs were largely unmeasured |
| 1 | Requirements were unclear throughout; caused repeated sprint replanning or significant rework |

**Dimension 2: Stakeholder engagement**

| Score | Evidence |
|-------|---------|
| 5 | All Manage Closely stakeholders were engaged at agreed cadence; no missed approvals; no surprises at Sprint Review |
| 4 | Engagement plan followed with minor exceptions; one missed approval cycle recovered quickly |
| 3 | Engagement inconsistent for at least one key stakeholder; approval delays occurred |
| 2 | Stakeholders disengaged mid-project; multiple approval cycles missed; key decisions delayed |
| 1 | Stakeholder engagement broke down significantly; project direction challenged by uninformed stakeholders |

**Dimension 3: Traceability**

| Score | Evidence |
|-------|---------|
| 5 | Full RTM maintained throughout; zero orphan stories; 100% Must Have FRs linked to stories and tests |
| 4 | RTM maintained with minor gaps; orphan count below 5; all Must Have FRs traceable |
| 3 | RTM created but not maintained; some orphan stories; traceability gaps found at UAT |
| 2 | RTM created but rarely used; significant traceability gaps; test coverage unclear |
| 1 | No traceability maintained; unable to determine requirement-to-test coverage at project close |

**Dimension 4: Change management**

| Score | Evidence |
|-------|---------|
| 5 | All changes submitted through defined process; zero uncontrolled changes; decisions made within turnaround times |
| 4 | Change process followed with minor exceptions; turnaround times met in >80% of cases |
| 3 | Change process used inconsistently; some uncontrolled changes; turnaround targets missed in several cases |
| 2 | Change process used in minority of cases; frequent uncontrolled scope additions; schedule impacted |
| 1 | No change control in practice; scope changed without record; significant rework and missed commitments |

**Dimension 5: Documentation**

| Score | Evidence |
|-------|---------|
| 5 | All artefacts produced on schedule, stored in agreed repository, versioned, and accessible to all intended recipients |
| 4 | Minor gaps in documentation (1–2 artefacts delayed or misplaced); recoverable without project impact |
| 3 | Several artefacts delayed; version control inconsistent; some stakeholders could not find required documents |
| 2 | Documentation frequently late or missing; no consistent version control; artefact ownership unclear |
| 1 | BA documentation not maintained; artefacts unavailable at project close; significant information loss |

**Dimension 6: Delivery alignment**

| Score | Evidence |
|-------|---------|
| 5 | All approved Must Have FRs delivered and tested; sprint velocity stable; acceptance criteria met without rework |
| 4 | >95% of Must Have FRs delivered; minor acceptance criteria issues resolved at Sprint Review |
| 3 | 80–95% of Must Have FRs delivered; acceptance criteria gaps found at Sprint Review on multiple sprints |
| 2 | 60–80% of Must Have FRs delivered; acceptance criteria frequently contested; significant rework |
| 1 | Less than 60% of Must Have FRs delivered; BA outputs and delivery outcomes poorly aligned |

---

### Performance score interpretation

| Total score (sum of all 6 dimensions) | Assessment |
|--------------------------------------|-----------|
| 27–30 | Excellent: BA practice was highly effective. Capture and replicate |
| 21–26 | Good: Strong performance with targeted improvements needed |
| 15–20 | Acceptable: BA practice functioning but inconsistently applied |
| 9–14 | At risk: BA practice needs structural improvements before the next engagement |
| 6–8 | Critical: Fundamental issues with BA practice. Team-level improvement programme required |

---

### Improvement action template

| Action ID | Dimension | Finding (what went wrong) | Root cause | Improvement action | Success measure | Owner | Apply from |
|----------|-----------|--------------------------|-----------|-------------------|----------------|-------|-----------|
| IA-001 | | | | | | | |

Root cause shorthand: P (People), PR (Process), T (Tool or technique), G (Governance), K (Knowledge gap)

Success measure: a single observable outcome that confirms the improvement has worked on the next project
(e.g., "RTM coverage above 95% at UAT start", "zero uncontrolled changes in the change log").
