---
type: concept
title: "Disciplines Bodies of Knowledge and Boundaries"
created: 2026-11-08
updated: 2026-11-08
tags: [concept, babok, architecture, quality-attributes, bodies-of-knowledge]
confidence: medium
sources: ["web search summaries only; the IIBA page was login-gated and the SEI report returned 403"]
---

# Disciplines, bodies of knowledge and boundaries

Each kind of input has a reference body of knowledge, and the useful boundary between neighbours is the requirement type. Evidence quality: the BABOK, SEI ADD and ISO 25010 facts below come from search summaries of primary sites, not fetched primary pages, so they are medium confidence. The mapping table is the author's synthesis, low to medium.

## Mapping (inputs to bodies of knowledge)

This table names the reference body for each input; only the first row and the architecture detail below were researched.

| Input | Reference body | Status |
|---|---|---|
| Product, business analysis | BABOK (IIBA) | Researched |
| Architecture | TOGAF (enterprise), ISO/IEC/IEEE 42010 (stakeholders, concerns, viewpoints), SEI ADD | ADD researched; TOGAF and 42010 unverified |
| Project management | PMBOK (PMI) | Unverified |
| Testing | ISTQB | Unverified |
| Engineering | SWEBOK | Unverified |
| Operations | DevOps handbook, SRE | Unverified |
| Design | Nielsen Norman and similar | Unverified |

## Business analysis ends where architecture begins

BABOK classifies requirements as business, stakeholder, solution and transition. Solution requirements split into functional (behavior and information the solution manages) and non-functional (how well it must perform, quality of service) (IIBA, via search summary; consistent across summaries, medium). Business analysis owns all four classes. A critique from an IIBA chapter workshop argues the functional/non-functional split matters mainly to designers (Regev, 2022, low, secondhand).

The architect takes the solution requirements and adds, per the SEI's Attribute-Driven Design: ADD's inputs are functional requirements, quality attribute requirements and design constraints (the SEI technical report on ADD, 2006, potentially stale but foundational, medium). The architect selects the architecture drivers, the top-priority mix of functional and quality requirements, restates each quality requirement as a system-specific quality attribute scenario, then chooses tactics and patterns to satisfy them. A Quality Attribute Workshop elicits the scenarios.

The vocabulary for quality is ISO/IEC 25010:2023, nine characteristics: functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility, safety (arc42 summary, medium). Older guides list eight, from the 2011 edition.

Rule of thumb: the analyst states what quality is needed and why; the architect makes it testable as a scenario, ranks it, records constraints, and records the decision that satisfies it. The hand-off is a non-functional requirement in; a scenario, a driver ranking and a decision out.

Gates: [[Gates as Checkpoints Without Documents]]. Handoffs: [[Software Lifecycle Inputs and Handoffs]].
