# Traceability Matrix Template

## Purpose
Defines the column structure, link types, and coverage rules for the Requirements Traceability
Matrix (RTM) produced by ba-requirements-lifecycle in Trace mode. Read this file before
building or updating any RTM.

---

## RTM Structure

The RTM is a single Excel sheet with one row per requirement. Columns are grouped into four
link-level zones. Add or remove zone columns based on what artefacts exist in the project.

### Zone A: Requirement identity (always present)
| Column | Content | Example |
|--------|---------|---------|
| Requirement ID | From the requirements register | CRM-FR-007 |
| Type | FR / NFR / AS / CO / DE / RI | FR |
| MoSCoW | From the register | Must Have |
| Status | From the register | Approved |
| Domain | Business cluster label | User Management |

### Zone B: Business need origin (include when available)
| Column | Content | Example |
|--------|---------|---------|
| Business Objective ID | Strategic objective, OKR, or regulation reference | OKR-2.3 |
| Business Objective Description | Short label | Reduce onboarding time by 40% |
| Origin Source | Where the requirement came from | Workshop 2026-04-15 / Interview: Head of Ops |

### Zone C: Solution decomposition (include when backlog exists)
| Column | Content | Example |
|--------|---------|---------|
| Epic ID | Epic that addresses this requirement | EPIC-002 |
| Story ID(s) | One or more Story IDs; comma-separate multiple | PAY-002-001, PAY-002-002 |
| Story count | Number of stories linked | 2 |
| Decomposition status | Fully decomposed / Partially decomposed / Not yet decomposed | Fully decomposed |

### Zone D: Test coverage (include when test register exists)
| Column | Content | Example |
|--------|---------|---------|
| Test Case ID(s) | Linked test case IDs | TC-PAY-002-HP-001, TC-PAY-002-NP-001 |
| Test type coverage | HP / NP / BC / EC — which types are covered | HP, NP |
| Test coverage status | Fully covered / Partially covered / Not tested | Fully covered |

### Zone E: Flags (always present)
| Column | Content | Trigger |
|--------|---------|---------|
| Traceability flag | UNTRACEABLE / ORPHAN / OK | See rules below |
| Notes | Free text for any anomaly | |

---

## Flag Definitions

| Flag | Meaning | Where it appears |
|------|---------|-----------------|
| `[UNTRACEABLE]` | Requirement has no downstream story or test case linked | Zone C story count = 0 AND Zone D test count = 0 |
| `[ORPHAN]` | A story or test case exists with no upstream requirement | In the backlog or test register, not in the RTM |
| `[PARTIAL TRACE]` | Requirement has a story but no test case, or vice versa | Zone C populated but Zone D empty, or reverse |
| `[STALE LINK]` | A linked story or test case ID no longer exists in the current register | Detected during maintain pass |
| `[OK]` | All populated link levels are consistent and complete | Default when no flag applies |

---

## Link Types

Use these labels in notes when a relationship is not a direct decomposition:

| Link Type | Definition | Example |
|-----------|-----------|---------|
| Derives | This requirement is derived from another requirement | CRM-FR-010 derives from CRM-FR-003 |
| Conflicts | This requirement is in conflict with another (from Issues Log) | CRM-FR-007 conflicts with CRM-CO-002 |
| Supersedes | This requirement replaces a prior version | CRM-FR-007 v2 supersedes CRM-FR-007 v1 |
| Satisfies | This story or test fully satisfies the requirement | PAY-002-001 satisfies CRM-FR-007 |
| Partially satisfies | This story or test covers part of the requirement | PAY-002-001 partially satisfies CRM-FR-007 (condition A only) |

---

## Coverage Rules

Apply these rules during the coverage report step:

| Coverage check | Pass threshold | Fail action |
|---------------|---------------|------------|
| Must Have FRs with at least one linked story | 100% | Flag each failing item; block story sprint-ready sign-off |
| Must Have FRs with at least one linked test case | 100% | Flag; raise as impediment in ba-scrum-events-pack |
| Should Have FRs with at least one linked story | ≥ 80% | Report gap; no block |
| NFRs with at least one linked test case | 100% | Flag `[NO TEST]`; NFRs without tests are invisible in QA |
| Orphan stories (no upstream requirement) | 0 allowed | Flag; trace back to a requirement or raise a new one |

---

## Coverage Report Format

Produce this summary table at the bottom of the RTM sheet and in the inline summary:

| Metric | Value |
|--------|-------|
| Total requirements | N |
| Fully traced (all populated zones consistent) | N (%) |
| Untraceable (no downstream links) | N |
| Partial trace (story but no test, or vice versa) | N |
| Stale links | N |
| Orphan stories (no upstream requirement) | N |
| Must Have FRs: all linked to at least one story | Pass / Fail |
| Must Have FRs: all linked to at least one test case | Pass / Fail |
| NFRs: all linked to at least one test case | Pass / Fail |
