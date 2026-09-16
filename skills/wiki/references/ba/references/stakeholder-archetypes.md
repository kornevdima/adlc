# Stakeholder Archetypes — Engagement Patterns and Concern Profiles

## Purpose
Use this reference during Step 1 (Classify Archetypes) and Step 5 (Write Concern Narratives)
of ba-stakeholder-analyzer. Apply the archetype profile to seed the concern narrative;
supplement with any actual input provided about the stakeholder.

---

## Archetype 1 — Sponsor

**Typical titles:** CEO, CXO, VP, Programme Director, Business Owner, Divisional Director
**Typical Power score:** 4–5 | **Typical Interest score:** 3–4

**What they care about:**
- Business outcomes and measurable value (not features or technical details)
- Budget adherence and delivery within committed timelines
- Organisational reputation and strategic alignment
- Not being surprised by problems — early warning over late escalation

**What makes them resist or disengage:**
- Meetings that do not respect their time
- Status reports that lead with activities instead of decisions needed
- Scope changes that arrive without a business case
- Being excluded from key decisions that land back on their desk

**Best framing for this stakeholder:**
Lead with outcomes and impact. Use financial language. Keep asks crisp: "I need a decision on X
by [date] to protect [outcome]." Never use jargon without a translation.

**Bad outcome from their perspective:**
Budget overrun, delivery failure attributed to poor requirements, or strategic misalignment
surfacing late in the programme.

**Preferred channel:** Executive briefing (face-to-face or VC, 30 min max), one-page summary email
**Cadence:** Milestone-driven; do not contact weekly unless specifically requested

---

## Archetype 2 — Decision-Maker

**Typical titles:** Department Head, Product Owner, Director, Programme Manager, Business Lead
**Typical Power score:** 3–4 | **Typical Interest score:** 4–5

**What they care about:**
- Making well-informed decisions without having to do the underlying analysis themselves
- Protecting their team and their operational domain from disruption
- Being seen as a credible sponsor to their own stakeholders
- Having clear, documented agreements so decisions do not get revisited

**What makes them resist or disengage:**
- Ambiguous options presented without a recommended position
- Being asked to decide on incomplete information under time pressure
- Decisions being made around them rather than with them
- Documentation that does not clearly reflect what was agreed

**Best framing:**
Present options with a recommended option clearly stated. Be explicit about trade-offs.
Always confirm decisions in writing immediately after discussion.

**Bad outcome:** A project outcome that creates operational problems for their team; being held
accountable for something they were not properly consulted on.

**Preferred channel:** Structured review meeting, follow-up email confirming decisions
**Cadence:** Weekly or bi-weekly; always before key deliverable sign-offs

---

## Archetype 3 — Subject Matter Expert (SME)

**Typical titles:** Senior Analyst, Technical Lead, Process Owner, Operations Manager, Domain Expert
**Typical Power score:** 2–3 | **Typical Interest score:** 4–5

**What they care about:**
- Being consulted, not just informed — they want their expertise acknowledged
- Accuracy: requirements that reflect how things actually work, not how people assume they work
- Not having their processes broken by a solution designed without understanding them
- Credit and acknowledgement for their contribution to the solution

**What makes them resist or disengage:**
- Being brought in too late, after decisions are already made
- Requirements that contradict their domain knowledge and are not explained
- Findings attributed to "the BA" without naming their input
- Workshops that run over time due to poor facilitation

**Best framing:**
Consult explicitly and early. Name them as the source of key domain knowledge in documents.
Validate findings with them before presenting to Decision-Makers.

**Bad outcome:** A solution deployed into their domain that breaks key processes they warned about.

**Preferred channel:** Structured one-to-one interview, small working group session, document review
**Cadence:** Intensive during discovery/analysis; review-cycle during definition and testing

---

## Archetype 4 — End User

**Typical titles:** Staff, Operator, Coordinator, Customer-facing Role, Frontline Worker
**Typical Power score:** 1–2 | **Typical Interest score:** 5

**What they care about:**
- That their day-to-day work becomes easier, not harder
- Not being forced to learn a completely new way of working without support
- Their feedback being acted on, not just collected and forgotten
- Job security if the project involves automation

**What makes them resist or disengage:**
- Not being consulted at all — only finding out about changes at training
- Requirements that do not reflect how they actually work (shadow processes)
- A gap between how the system was demoed and how it works in practice
- Change being imposed without explanation of why

**Best framing:**
Be transparent about what is changing and why. Acknowledge what will be harder before go-live.
Show that their input shaped the solution. Avoid jargon entirely.

**Bad outcome:** A deployed solution that slows down their work, forcing workarounds or creating
anxiety about job displacement.

**Preferred channel:** Focus group, survey, walkthrough session
**Cadence:** Elicitation: early and intensive. Then inform at milestones (design, UAT, launch).

---

## Archetype 5 — Regulator / Compliance

**Typical titles:** Legal Counsel, Risk Manager, Data Protection Officer, Audit Lead, Compliance Officer
**Typical Power score:** 4–5 | **Typical Interest score:** 2–3

**What they care about:**
- That the organisation does not expose itself to legal or regulatory risk
- Having documented evidence of due diligence
- Being consulted before commitments are made, not after
- Precise language in requirements — wording matters

**What makes them resist or disengage:**
- Being presented with a fait accompli and asked to rubber-stamp
- Vague requirements in regulated areas ("we'll sort out GDPR later")
- Delivery speed being used to justify skipping compliance reviews
- Outputs that are not suitable as audit evidence

**Best framing:**
Lead with risk reduction. Use precise, legal-grade language for compliance-related requirements.
Always document that they have been consulted and what they confirmed.

**Bad outcome:** A deployed solution that creates a regulatory breach, audit finding, or legal liability.

**Preferred channel:** Formal review meeting with documented minutes; written sign-off
**Cadence:** At key gateways: requirements sign-off, design review, pre-UAT, pre-go-live

---

## Archetype 6 — Technical Gatekeeper

**Typical titles:** Enterprise Architect, Chief Technology Officer, Security Officer, Infrastructure Lead
**Typical Power score:** 3–4 | **Typical Interest score:** 3–4

**What they care about:**
- Architectural integrity and strategic alignment with the technology estate
- Security posture and not creating new attack surfaces
- Avoiding technical debt and unsupported components
- Standards compliance (API design, data models, cloud governance)

**What makes them resist or disengage:**
- Solutions designed in isolation from the enterprise architecture
- NFRs that have not been defined or are unmeasurable
- Being presented with a design that has already been sold to the business
- Fast delivery used to justify bypassing architecture review

**Best framing:**
Engage early with a technology context summary. Frame requirements in terms of system quality
and integration points. Never present a solution without asking for architectural guidance first.

**Bad outcome:** A deployed solution that creates security vulnerabilities, duplicates existing
capability, or violates platform governance policies.

**Preferred channel:** Technical review session; architecture review board
**Cadence:** Early in discovery (constraints input); design phase (review); pre-go-live (sign-off)

---

## Archetype 7 — Influencer

**Typical titles:** External Advisor, Key Account Customer, Industry Body Representative, Board Observer
**Typical Power score:** 2–3 | **Typical Interest score:** 2–4

**What they care about:**
- Their external perspective being taken seriously
- Outcomes that align with industry standards or their own stakeholder interests
- Not being overloaded with internal project detail

**What makes them resist or disengage:**
- Feeling their input is tokenistic
- Being asked to review documents that are too internal or technical
- Slow or no response to their feedback

**Best framing:**
Frame communication around outcomes and market/sector relevance, not internal mechanics.
Keep materials concise and polished — they will not tolerate rough drafts.

**Preferred channel:** Executive summary, brief advisory call
**Cadence:** Milestone-driven; 2–3 touchpoints across the project

---

## Archetype 8 — Blocker

**Typical titles:** Any role — identified by stated opposition, non-response, or active resistance
**Typical Power score:** Varies | **Typical Interest score:** Varies

**Characteristics:**
A Blocker is not defined by title but by behaviour. May be a former system owner, someone who
proposed an alternative approach, or someone whose team is most disrupted.

**What drives blocking behaviour:**
- Loss of control, authority, or budget
- A previous project that failed and left them holding the consequences
- Genuine concern about the solution that has not been addressed
- Political alignment with an opposing initiative

**Handling approach:**
1. Identify the underlying concern — a Blocker almost always has a legitimate point buried in the resistance
2. Create a private bilateral channel: do not confront blocking behaviour in group settings
3. Involve them meaningfully in a specific deliverable where their expertise is real
4. Document their objections formally — unacknowledged concerns often escalate
5. Escalate to Sponsor only if blocking is impeding delivery and bilateral resolution has been attempted

**Do not:** Dismiss, avoid, or publicly challenge a Blocker.

**Preferred channel:** Private one-to-one; direct and honest
**Cadence:** Immediate engagement; ongoing until resistance is resolved or formally escalated
