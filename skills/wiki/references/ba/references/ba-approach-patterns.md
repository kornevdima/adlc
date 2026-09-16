# BA Approach Patterns — Selection Criteria and Technique Defaults

## Purpose
Use during Plan Approach mode (BABOK 3.1) of ba-planning-monitor. Provides approach
archetypes, selection criteria, default technique sets, and risk flags for each approach type.

---

## Approach Archetypes

### Archetype 1: Waterfall / Predictive

**Select when:**
- Requirements are stable and well-understood upfront
- Regulatory or contractual constraints require a defined scope before work begins
- The project involves physical construction, infrastructure, or compliance delivery
- Stakeholder approval cycles are long and sequential (formal sign-off at each phase gate)
- The organisation has limited appetite for iterative delivery

**BA technique defaults:**

| Phase | Primary techniques |
|-------|-------------------|
| Initiation | Business case (ba-business-case-builder), stakeholder analysis (ba-stakeholder-analyzer) |
| Requirements | Structured interviews, workshops (ba-workshop-facilitator), elicitation synthesis (ba-elicitation-synthesizer), requirements register |
| Analysis | Process modelling (ba-process-modeler), gap analysis (ba-gap-analysis) |
| Design | Use cases, data modelling, interface analysis |
| Testing | Test case register (ba-test-case-generator), UAT script, traceability matrix (ba-requirements-lifecycle) |
| Closure | Solution assessment (ba-solution-assessment), BA performance review (ba-planning-monitor, mode 5) |

**Governance overhead:** High. All artefacts are formally signed off before the next phase begins.
**Risk flags:**
- Requirements changes are expensive: every change requires a formal change request (ba-requirements-lifecycle, Assess Change mode)
- Stakeholder engagement must be front-loaded: missed stakeholders in discovery compound throughout
- Late testing is high risk: ensure test cases trace to every Must Have FR

---

### Archetype 2: Agile (Scrum-based)

**Select when:**
- Requirements are expected to evolve throughout delivery
- The team is using Scrum and delivering in Sprints
- The organisation accepts iterative delivery and incremental value
- Stakeholders are available for regular refinement and review sessions

**BA technique defaults:**

| Scrum event / activity | Primary techniques |
|-----------------------|-------------------|
| Sprint 0 / Kickoff | Stakeholder analysis, BA approach, process modelling (AS-IS) |
| Product backlog creation | Elicitation synthesis, user story factory (ba-user-story-factory) |
| Backlog refinement | Requirements lifecycle — Prioritize mode, story splitting |
| Sprint Planning | ba-scrum-events-pack |
| Sprint execution | ba-requirements-lifecycle — Maintain and Trace modes (ongoing) |
| Sprint Review | ba-scrum-events-pack, ba-test-case-generator coverage check |
| Sprint Retrospective | ba-scrum-events-pack, ba-planning-monitor performance improvement |

**Governance overhead:** Low-to-medium. Formal sign-off at backlog level (Definition of Ready) and
increment level (Definition of Done). Change requests are handled via Product Backlog refinement,
not a formal change control board (unless the organisation mandates one).

**Risk flags:**
- Scope creep: without a Requirements Baseline, it is difficult to track what was originally committed
  and what was added. Use ba-requirements-lifecycle Maintain mode to version the backlog at Sprint 0.
- NFR neglect: non-functional requirements are easy to defer in agile; they must be tracked as
  explicit Product Backlog Items or as team-level acceptance criteria (DoD entries).
- Stakeholder drift: if the Product Owner becomes unavailable, requirements decisions stall.
  Ensure the engagement plan (ba-planning-monitor, mode 2) names a deputy decision-maker.

---

### Archetype 3: Hybrid

**Select when:**
- The project has a large upfront phase (business case, architecture, procurement) followed by
  agile delivery sprints
- A programme has multiple workstreams at different lifecycle stages simultaneously
- The organisation requires formal phase-gate approvals but iterative delivery within each phase
- The engagement involves both BA and architecture work at the programme level

**BA technique defaults:**
Run Waterfall techniques for phases 1–2 (initiation, design/procurement). Switch to Agile
techniques from delivery Sprint 1 onwards.

**Governance overhead:** High during initiation and design; Medium during agile delivery.
Apply formal change control for any change that affects the approved scope or business case.
Within-sprint backlog changes follow agile governance (Product Owner decision).

**Risk flags:**
- Transition friction: the shift from waterfall to agile governance is the highest-risk moment.
  Define explicitly in the governance plan (ba-planning-monitor, mode 3) where each governance
  model applies and who arbitrates boundary disputes.
- Artefact duplication: waterfall BRDs and agile backlogs can conflict. Use ba-requirements-lifecycle
  Trace mode to link BRD requirements to Product Backlog Items.

---

### Archetype 4: Iterative / Research-Led

**Select when:**
- The project involves design research, prototyping, or exploratory analysis where the destination
  is not yet known
- Requirements emerge from user research or experimental testing rather than stakeholder interviews
- The engagement is a discovery, feasibility study, or proof of concept — not a delivery project

**BA technique defaults:**

| Activity | Technique |
|----------|-----------|
| Problem framing | Workshop (ba-workshop-facilitator, Design Sprint type) |
| Current state understanding | Process modelling AS-IS, stakeholder analysis |
| Hypothesis generation | Gap analysis, business case (feasibility variant) |
| Prototype testing | Solution assessment (ba-solution-assessment) |
| Findings documentation | Elicitation synthesis (treat research findings as elicitation input) |

**Governance overhead:** Low. Artefacts are working documents, not formal deliverables.
Final outputs (business case, feasibility report) are signed off once, at the end.

**Risk flags:**
- Scope expansion: iterative exploration can drift indefinitely without a defined exit criterion.
  State in the BA approach what outcome marks the end of the discovery phase.
- Stakeholder fatigue: frequent workshops without visible progress erode engagement. Agree a
  research cadence and a "synthesis moment" schedule in the engagement plan.

---

## Technique Selection Reference

When the approach is defined, use this table to confirm the default techniques are appropriate.
Override any default if the project context warrants it, and note the reason in the BA approach document.

| BABOK technique | Waterfall default | Agile default | Hybrid default | Iterative default |
|----------------|------------------|--------------|----------------|------------------|
| Workshops | Formal, scheduled | Lightweight, frequent | Both, phase-dependent | Heavy — core activity |
| Interviews | Structured, recorded | Informal, just-in-time | Structured in initiation | Exploratory |
| Process modelling | Full AS-IS and TO-BE | AS-IS at Sprint 0 only | Full in design phase | AS-IS |
| Gap analysis | Full multi-dimension | Quick Win focus | Full in design phase | High-level only |
| Business case | Full financial model | Story-level value statements | Full before procurement | Feasibility variant |
| User stories | Not primary | Core delivery format | Core in delivery phase | Hypotheses |
| Test cases | Full RTM, formal UAT | Gherkin BDD, Sprint Review | Both | Not primary |
| Traceability | Full RTM mandatory | RTM at increment level | Full in design, increment in delivery | Lightweight |

---

## Methodology Change Triggers

State these in every BA approach document. If any trigger occurs mid-project, revisit the approach:

- Project scope increases by more than 30%
- A new regulatory requirement is imposed with a fixed deadline
- The delivery team switches methodologies (e.g., moves from Scrum to Kanban)
- A key decision-maker changes and the new stakeholder has different governance preferences
- Three or more change requests of Major or Critical classification are raised within a single Sprint
