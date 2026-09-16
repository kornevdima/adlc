# Gap Severity Rubric and Root Cause Classification

## Purpose
Use during Step 3 (Score Gap Severity) and Step 4 (Classify Root Cause) of ba-gap-analysis.

---

## Severity Scoring Guide

Apply the criteria below to determine the correct severity score for each element.
When two scores seem equally applicable, apply the higher one and note the uncertainty.

### Score 0 — None
**Criteria:**
- The current state fully satisfies the target requirement or TO-BE description
- No action is required
- The element may be used as a positive reference point

**Example indicators:** "We already do this", "System supports this out of the box",
"Policy exists and is enforced", "Team has the required skill and capacity"

---

### Score 1 — Minor
**Criteria:**
- Current state partially meets the target; a small, well-defined shortfall exists
- Addressable within current operational budget and resourcing without a formal project
- No dependency on external decisions or major technology change

**Example indicators:** "Mostly covered but one edge case is missing",
"Process exists but lacks a documented procedure", "Tool supports it but configuration is needed",
"Team has the skill but needs a refresher"

**Typical actions:** Update documentation, apply configuration change, run a short training session

---

### Score 2 — Moderate
**Criteria:**
- Current state partially meets the target but a meaningful, structured improvement is needed
- Requires a defined improvement action, dedicated effort, and likely a budget line
- Will not resolve itself through routine operations

**Example indicators:** "Process exists but frequently fails or has known workarounds",
"System has partial capability but requires integration or customisation",
"Role exists but has no clear accountability for this area",
"Data is available but quality is inconsistent"

**Typical actions:** Process redesign, system configuration project, role and RACI clarification,
data quality improvement initiative

---

### Score 3 — Significant
**Criteria:**
- Current state has a major shortfall relative to the target
- Requires a structured initiative with defined scope, timeline, and ownership
- May require investment decision, procurement, or organisational change

**Example indicators:** "Process is ad-hoc with no consistency", "System cannot support this
without significant development", "Role does not exist", "Data is not collected or captured",
"Governance structure would need to be redesigned"

**Typical actions:** Programme or project initiation, technology procurement or build,
new role or team creation, governance framework design

---

### Score 4 — Critical
**Criteria:**
- Current state is entirely absent or fundamentally incompatible with the target
- Without closing this gap, the TO-BE cannot be achieved
- Blocks delivery of related requirements, capabilities, or processes

**Example indicators:** "No current capability exists in this area",
"Legacy system is technically incompatible", "Regulatory requirement is not met at all",
"Critical data does not exist anywhere in the organisation",
"Structural impediment prevents the target state from being reached"

**Special rule:** If a target requirement has no corresponding current state element at all
(a net-new capability), it is Critical by default unless explicitly overridden with rationale.

---

## Root Cause Classification Guide

### P — People
**Definition:** The gap is primarily caused by a shortfall in human capacity: missing skills,
insufficient headcount, unclear roles, or lack of accountability.

**Signals in input:**
- "Nobody knows how to...", "We don't have anyone who can..."
- "It's unclear who owns this", "The team doesn't have capacity"
- "Training hasn't been done", "High turnover in this area"

**Typical remedies:** Training programme, recruitment, role definition, coaching, RACI clarification

---

### PR — Process
**Definition:** The gap is caused by a missing, broken, undocumented, or inefficient workflow.
The people and tools may exist but the process is not fit for purpose.

**Signals in input:**
- "We do it differently each time", "There's no standard procedure"
- "Things fall through the cracks at handoff", "It takes too long because of manual steps"
- "Nobody follows the current process", "The SOP is out of date"

**Typical remedies:** Process redesign, SOP documentation, automation, workflow tooling

---

### T — Technology
**Definition:** The gap is caused by a missing, inadequate, or technically incompatible system,
tool, integration, or infrastructure component.

**Signals in input:**
- "The system doesn't support this", "We're using spreadsheets because the tool can't do it"
- "No integration exists between X and Y", "The platform is end-of-life"
- "We'd need to build something", "The current tool is too slow / doesn't scale"

**Typical remedies:** System procurement, development project, integration build, upgrade, migration

---

### D — Data
**Definition:** The gap is caused by missing, poor quality, inaccessible, or ungoverned data.
The process and technology may exist but the data needed to execute is not available or reliable.

**Signals in input:**
- "We don't capture that data", "The data is in multiple systems and inconsistent"
- "Reports are unreliable", "We can't trust the numbers", "No single source of truth"
- "GDPR means we can't use that data for this purpose"

**Typical remedies:** Data collection design, data quality programme, master data management,
data governance policy, analytics platform

---

### G — Governance
**Definition:** The gap is caused by the absence of a policy, decision right, standard,
accountability structure, or oversight mechanism.

**Signals in input:**
- "Nobody has authority to make this decision", "There's no policy covering this"
- "Different teams do it their own way with no standard", "Compliance hasn't signed off"
- "The committee that should own this doesn't exist yet"

**Typical remedies:** Policy drafting, committee or forum establishment, decision rights
framework, standards definition, audit and assurance mechanism

---

## Severity + Root Cause Combinations — Common Patterns

| Pattern | Severity | Root Cause | Typical Horizon |
|---------|----------|-----------|----------------|
| Missing policy in regulated area | 3–4 | G | Quick Win (governance fix) |
| Undocumented but functioning process | 1–2 | PR | Quick Win (document it) |
| Legacy system blocking new capability | 3–4 | T | Long-term programme |
| Skill gap in an existing team | 2–3 | P | Short-term initiative |
| No data collection for a key metric | 3–4 | D | Short-term to Long-term |
| Ad-hoc process with high failure rate | 3 | PR | Short-term initiative |
| Net-new role needed | 3–4 | P | Short-term to Long-term |
| Integration missing between two systems | 2–3 | T | Short-term initiative |
