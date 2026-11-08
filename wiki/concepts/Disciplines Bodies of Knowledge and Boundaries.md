---
type: concept
title: "Disciplines Bodies of Knowledge and Boundaries"
created: 2026-11-08
updated: 2026-11-08
tags: [concept, babok, architecture, quality-attributes, bodies-of-knowledge]
confidence: medium
sources: ["[[sei-attribute-driven-design-method-collection]]"]
---

# Disciplines, bodies of knowledge and boundaries

Each kind of input has a reference body of knowledge, and the useful boundary between neighbours is the requirement type. Evidence quality: the ADD inputs and steps are backed by the SEI's own method page (high; see [[sei-attribute-driven-design-method-collection]]). The BABOK, TOGAF and ISO 25010 facts come from search summaries and secondary guides, because the IIBA and Open Group sites are login-gated, so they stay medium. The mapping table is the author's synthesis, low to medium.

## Mapping (inputs to bodies of knowledge)

This table names the reference body for each input; only the first row and the architecture detail below were researched.

| Input | Reference body | Status |
|---|---|---|
| Product, business analysis | BABOK (IIBA) | Researched |
| Architecture | TOGAF (enterprise), ISO/IEC/IEEE 42010 (stakeholders, concerns, viewpoints), SEI ADD | ADD researched, primary backed (high); TOGAF researched, secondary only (medium); 42010 unverified |
| Project management | PMBOK (PMI) | Unverified |
| Testing | ISTQB | Unverified |
| Engineering | SWEBOK | Unverified |
| Operations | DevOps handbook, SRE | Unverified |
| Design | Nielsen Norman and similar | Unverified |

## Business analysis ends where architecture begins

BABOK classifies requirements as business, stakeholder, solution and transition. Solution requirements split into functional (behavior and information the solution manages) and non-functional (how well it must perform, quality of service) (IIBA, via several study guides that agree; the IIBA text is gated, medium. Some cite BABOK version 2, where transition requirements sat beside solution requirements; later versions nest the split as described here.). Business analysis owns all four classes. A critique from an IIBA chapter workshop argues the functional/non-functional split matters mainly to designers (Regev, 2022, low, secondhand).

The architect takes the solution requirements and adds, per the SEI's Attribute-Driven Design: ADD's inputs are functional requirements, quality attribute requirements and design constraints (SEI method page listing the 2006 report, high for the inputs and steps: [[sei-attribute-driven-design-method-collection]]). The SEI page names selecting architectural drivers as a step but does not define the term, so the following definition is from secondary summaries (medium). The architect selects the architecture drivers, the top-priority mix of functional and quality requirements, restates each quality requirement as a system-specific quality attribute scenario, then chooses tactics and patterns to satisfy them. A Quality Attribute Workshop elicits the scenarios.

The vocabulary for quality is ISO/IEC 25010:2023, nine characteristics: functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility, safety (arc42 summary, medium). Older guides list eight, from the 2011 edition.

TOGAF places the same split at enterprise scale. Its Architecture Development Method has a preliminary phase and phases A to H, and Requirements Management sits in the centre, running across all phases rather than as one step: requirements are identified, stored, fed into and out of each phase, and a change triggers an impact assessment naming which phases to revisit; the method does not mandate a phase order (Open Group pocket guide, via search summary because the site redirects to a login; medium). The business requirements stay with the business analyst's input and the architecture phases consume them, which matches the boundary below.

Rule of thumb: the analyst states what quality is needed and why; the architect makes it testable as a scenario, ranks it, records constraints, and records the decision that satisfies it. The hand-off is a non-functional requirement in; a scenario, a driver ranking and a decision out.

The boundary rule is the author's synthesis of the three bodies above (medium): BABOK defines the requirement classes the analyst owns, ADD defines what the architect adds to them, and TOGAF shows requirements managed as a continuous thread rather than a hand-off.

Gates: [[Gates as Checkpoints Without Documents]]. Handoffs: [[Software Lifecycle Inputs and Handoffs]].
