# Gap Action Patterns and Roadmap Horizon Rules

## Purpose
Use during Step 5 (Derive Recommended Actions) and Step 7 (Build Roadmap View) of ba-gap-analysis.

---

## Action Pattern Library

Each pattern is a named, reusable recommended action type. Apply by matching root cause and severity.

### AP-01 — Document and Standardise
**Root cause:** PR | **Severity range:** 1–2
**When to apply:** A process exists informally or inconsistently but is not documented.
**Action:** Conduct a process mapping session, produce an SOP, and publish it to affected teams.
**Effort:** Low | **Impact:** Medium
**Horizon:** Quick Win

---

### AP-02 — Redesign Process
**Root cause:** PR | **Severity range:** 2–4
**When to apply:** The existing process is structurally flawed — rework loops, unclear handoffs,
excessive manual steps, or known failure points.
**Action:** Run a process redesign workshop (ba-workshop-facilitator: Process Mapping type),
produce AS-IS and TO-BE models, agree and implement the new process.
**Effort:** Medium | **Impact:** High
**Horizon:** Short-term initiative

---

### AP-03 — Configure Existing System
**Root cause:** T | **Severity range:** 1–2
**When to apply:** The required capability exists in a system already in use but is not enabled,
configured, or activated.
**Action:** Define configuration requirements, complete configuration in a test environment,
validate, and deploy.
**Effort:** Low | **Impact:** Medium–High
**Horizon:** Quick Win to Short-term

---

### AP-04 — Build System Integration
**Root cause:** T | **Severity range:** 2–3
**When to apply:** Two or more systems need to share data or trigger actions between them
and no integration currently exists.
**Action:** Define integration requirements (source, target, trigger, data mapping, frequency,
error handling), procure or build the integration, test, and deploy.
**Effort:** Medium–High | **Impact:** High
**Horizon:** Short-term to Long-term

---

### AP-05 — Procure or Build New System
**Root cause:** T | **Severity range:** 3–4
**When to apply:** No existing system can support the required capability. A new tool, platform,
or application must be acquired or built.
**Action:** Run an RFI/RFP process or build/buy analysis (ba-rfi-rfp-analyzer, ba-solution-assessment),
select, procure, implement, and transition.
**Effort:** High | **Impact:** High
**Horizon:** Long-term programme

---

### AP-06 — Train and Upskill
**Root cause:** P | **Severity range:** 1–2
**When to apply:** The skill gap is specific and addressable through a structured training
programme without organisational restructuring.
**Action:** Define the skill target, identify training options, deliver training, assess competency.
**Effort:** Low–Medium | **Impact:** Medium
**Horizon:** Quick Win to Short-term

---

### AP-07 — Define Role and Recruit
**Root cause:** P | **Severity range:** 3–4
**When to apply:** A required role does not exist in the organisation.
**Action:** Write a role description, obtain headcount approval, recruit or reassign internally,
onboard, and integrate into relevant RACI assignments.
**Effort:** Medium–High | **Impact:** High
**Horizon:** Short-term to Long-term

---

### AP-08 — Clarify Ownership and RACI
**Root cause:** P or G | **Severity range:** 1–3
**When to apply:** Accountability for a capability, process, or deliverable is unclear, disputed,
or absent — but the people exist.
**Action:** Facilitate an ownership alignment session, update RACI, publish and socialise.
**Effort:** Low | **Impact:** Medium–High
**Horizon:** Quick Win

---

### AP-09 — Draft and Approve Policy
**Root cause:** G | **Severity range:** 2–4
**When to apply:** A governing policy, standard, or procedure does not exist or is not fit for
purpose. Required for compliance, consistency, or decision-making authority.
**Action:** Draft policy with relevant stakeholders, obtain sign-off from the appropriate
authority, publish, communicate, and integrate into onboarding and operations.
**Effort:** Low–Medium | **Impact:** High
**Horizon:** Quick Win to Short-term

---

### AP-10 — Establish Governance Structure
**Root cause:** G | **Severity range:** 3–4
**When to apply:** No committee, forum, or oversight body exists to own a critical domain
(e.g. data governance, AI governance, change authority).
**Action:** Define the structure, mandate, and operating model; appoint members; run a pilot
cycle; embed into organisational governance calendar.
**Effort:** Medium | **Impact:** High
**Horizon:** Short-term initiative

---

### AP-11 — Improve Data Quality
**Root cause:** D | **Severity range:** 2–3
**When to apply:** Data exists but is inconsistent, incomplete, or unreliable for its intended use.
**Action:** Profile the data, identify the root causes of poor quality (source, process, input
validation), implement cleansing and prevention controls, define quality KPIs and monitoring.
**Effort:** Medium–High | **Impact:** High
**Horizon:** Short-term to Long-term

---

### AP-12 — Design Data Capture
**Root cause:** D | **Severity range:** 3–4
**When to apply:** Required data is not captured anywhere. The source process or system does
not record what is needed.
**Action:** Define the data requirement (entity, attributes, granularity, frequency), design the
capture point (form, system event, sensor, manual log), build and deploy the capture mechanism.
**Effort:** Medium–High | **Impact:** High
**Horizon:** Short-term to Long-term

---

### AP-13 — Accept and Monitor
**Root cause:** Any | **Severity range:** 1–2 with Low impact
**When to apply:** The gap exists but closing it provides insufficient value relative to effort,
or it is constrained by external factors outside the project's control.
**Action:** Document the gap and the rationale for acceptance. Define a monitoring trigger:
the condition under which this gap would be re-assessed and elevated. Assign an owner to monitor.
**Effort:** Low | **Impact:** Low
**Horizon:** Backlog (monitor only)

---

## Roadmap Horizon Rules

Apply these rules to assign every action to a horizon after effort/impact scoring.

| Effort | Impact | Horizon |
|--------|--------|---------|
| Low | High | Quick Win |
| Low | Medium | Quick Win |
| Low | Low | Accept / Monitor |
| Medium | High | Short-term initiative |
| Medium | Medium | Short-term initiative |
| Medium | Low | Accept / Monitor |
| High | High | Long-term programme |
| High | Medium | Long-term programme (consider deferral) |
| High | Low | Accept / Monitor — do not commit resources |

**Override:** Any gap with Severity 4 (Critical) is promoted to Short-term or Long-term
regardless of effort/impact scoring. Critical gaps blocking the TO-BE cannot be accepted.

**Quick Win definition:** Can be initiated and completed within 30 days by existing staff
without additional budget approval.

**Short-term initiative definition:** Requires a defined scope, a named owner, and budget
allocation. Completes within 90 days.

**Long-term programme definition:** Requires formal project initiation, governance approval,
and dedicated resourcing. Timeline 90 days to 12 months or beyond.
