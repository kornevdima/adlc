# Definition of Ready and Definition of Done

## Purpose
Use during Sprint Planning support and Sprint Review support in ba-scrum-events-pack.
Section 1: Default DoR with BA responsibility per criterion.
Section 2: Default DoD with BA responsibility per criterion.
Section 3: Customisation rules.

---

## Section 1 — Definition of Ready (DoR)

**What it is:** A shared understanding of the criteria a Product Backlog Item must meet before
the Developers will accept it into a Sprint. The DoR is not in the Scrum Guide 2020 — it is a
widely adopted practice. It serves as a quality gate at Sprint Planning.

**The BA's responsibility:** Ensuring PBIs meet the DoR before Sprint Planning begins.
Items that fail DoR at Sprint Planning waste event time and erode trust.

### Default DoR Criteria

| Criterion | Definition | BA Responsibility |
|-----------|-----------|-------------------|
| User story written in standard form | "As a [specific role], I want [specific action], so that [specific value]" | BA writes or reviews |
| Acceptance criteria present and in Gherkin format | At minimum: one happy path, one negative path | BA writes and confirms |
| INVEST test applied | Story is Independent, Negotiable, Valuable, Estimable, Small, Testable | BA validates |
| No compound requirement | Story contains no AND in the "I want" clause | BA validates |
| Dependencies identified | All dependencies documented; blocking dependencies resolved or a plan exists | BA identifies and tracks |
| NFR tagged | Any applicable non-functional requirements referenced on the story | BA tags from NFR register |
| Mockup or wireframe linked (if UI change) | If the story changes a UI, a design reference is linked | BA coordinates with designer |
| Business rules documented | Any business rules governing the story's behaviour are stated | BA writes |
| Estimation attempted | Developers have had an opportunity to size the story (even roughly) | BA supports by providing clarity |
| Stakeholder SME confirmed available | If the story requires SME input during the Sprint, SME availability is confirmed | BA confirms |

**DoR check format for Sprint Planning input:**
| Story ID | Story Title | DoR Criterion | Status | Notes |
|----------|-------------|---------------|--------|-------|
| | | [criterion] | Pass / Fail / Partial | If Fail: what is needed to resolve |

---

## Section 2 — Definition of Done (DoD)

**What it is:** A formal description of the state of the Increment when it meets the quality
measures required. It creates transparency and shared understanding of the work needed to
create an Increment.

**Scrum Guide 2020 requirement:** The DoD is not optional. If a PBI does not meet the DoD,
it cannot be presented at the Sprint Review or counted as part of the Increment.

**The BA's responsibility:** Verifying that acceptance criteria are met (the functional
component of Done). The BA does not own the full DoD — the Developers own it. The BA
owns the acceptance criteria verification step.

### Default DoD Criteria

| Criterion | Definition | Primary Owner |
|-----------|-----------|---------------|
| Acceptance criteria met | All Gherkin scenarios pass as verified against the deployed code | BA verifies |
| Code reviewed | Peer code review completed | Developers |
| Unit tests passing | All unit tests pass with no failures | Developers |
| Integration tests passing | Tests covering integration points for this story pass | Developers |
| No known Critical or High defects | All Critical and High priority defects are resolved | Developers + QA |
| Deployed to the agreed environment | The Increment is available in the Sprint Review environment | Developers |
| Documentation updated | Any user-facing documentation affected by the change is updated | BA / technical writer |
| Accessibility check passed | The change does not introduce accessibility regressions | Developers + BA |
| Product Owner accepts the Increment | The Product Owner confirms the story meets intent | Product Owner (after BA verification) |

**DoD check format for Sprint Review:**
| Story ID | DoD Criterion | Status | Evidence | Notes |
|----------|---------------|--------|---------|-------|
| | Acceptance criteria met | Pass / Fail | TC-XXX-HP-001: Pass | |
| | Code reviewed | Pass / Fail | PR #{number} | |

---

## Section 3 — Customisation Rules

### Adding Criteria
Teams may add criteria to both DoR and DoD that reflect their specific context:
- DoR: "Performance baseline established for stories touching the search service"
- DoD: "OWASP top 10 security check passed for any story touching authentication"
- DoD: "Database migration script reviewed and tested in staging"

**Rule for adding:** Any criterion added must be verifiable (pass/fail determinable) and must
be achievable by the team within the Sprint. Do not add aspirational criteria that the team
cannot consistently meet.

### Removing Criteria
Never remove a DoD criterion without explicit agreement from the entire Scrum Team and the
Product Owner. Removing DoD criteria increases technical debt and reduces increment quality.

A DoD criterion may be suspended (not removed) for a specific Sprint only if:
- An explicit exception is agreed before the Sprint starts
- The exception is documented and a plan to address the gap is in the next Sprint Backlog

### Scaling DoR/DoD
For large-scale Scrum (LeSS, SAFe, Nexus), DoD may have additional layers:
- Team DoD: what each team must achieve for their part of the Increment
- Integration DoD: what the combined Increment must achieve
- Release DoD: additional criteria for a version to be released to production

The BA's verification responsibility applies at the Team DoD level.

---

## Section 4 — DoR vs. DoD — Common Confusion

| Question | Answer |
|---------|--------|
| Is DoR in the Scrum Guide 2020? | No. It is a widely adopted practice, not a Scrum requirement. |
| Is DoD in the Scrum Guide 2020? | Yes. It is mandatory. |
| Who owns DoR? | Typically the Product Owner and BA together — the Product Owner decides what enters Sprints. |
| Who owns DoD? | The Scrum Team collectively; the Developers define it. |
| Can a story be Done without meeting the DoD? | No. The Scrum Guide is explicit: if a PBI does not meet the DoD, it is not Done. |
| Can the DoD change during a Sprint? | No. The DoD for a Sprint is fixed at Sprint Planning. It may be updated for future Sprints. |
| What happens to a story that fails DoD at Sprint Review? | It returns to the Product Backlog. It is not presented as delivered. |
