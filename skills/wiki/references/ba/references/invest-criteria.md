# INVEST Criteria — Definitions, Failure Modes, and Repair Patterns

## Purpose
Use during Step 4 (Apply INVEST Test) of ba-user-story-factory.
Test every story against all 6 criteria. Record any failure and apply the repair pattern.

---

## I — Independent

**Definition:** The story can be developed, tested, and delivered without requiring another
story to be completed first. Stories that are tightly coupled to each other create scheduling
constraints that reduce Sprint flexibility.

**Passes if:** The story provides value on its own OR can be demoed independently even if other
stories are also in flight.

**Fails if:** The story only makes sense when another specific story is also Done; or it is a
pure prerequisite with no standalone testable value.

**Common failure modes:**
- "Step 1 of 3" stories — no value without Step 2 and Step 3
- UI story that only works if a specific API story is done
- Stories split by technical layer (front-end story + back-end story for the same feature)

**Repair patterns:**
- Vertical slice: include all layers needed to deliver end-to-end value in one story
- Combine steps 1–3 into one story if they have no independent value
- Accept the dependency if unavoidable; tag it in the Dependency Map rather than failing the story

---

## N — Negotiable

**Definition:** The story is not a contract — it describes the goal and value, leaving room for
the Development Team and Product Owner to negotiate how it is implemented. Details emerge
during Sprint events.

**Passes if:** The "I want" clause describes an outcome, not a specific UI component or
technical solution.

**Fails if:** The story prescribes implementation ("the button must be blue and positioned
top-right"), specific technical architecture, or exact screen layouts.

**Common failure modes:**
- "As a user I want a dropdown menu with these 14 options..."
- "The API must use REST/JSON with this exact endpoint structure"
- "There must be a table with these exact columns in this exact order"

**Repair patterns:**
- Rewrite to describe the outcome: "As a user I want to filter results by status so that I can
  find relevant items quickly" — implementation is left to the team
- Move implementation constraints to a separate technical note or Spike story
- If specific UI is required by a client contractual obligation, flag it as a constraint in
  the Notes column and accept the failure

---

## V — Valuable

**Definition:** The story delivers value to a specific user or the business. Every story
must answer the question: why does this matter?

**Passes if:** The "So that" clause describes a concrete, verifiable benefit to a real user
or a measurable business outcome.

**Fails if:** The "So that" is absent, vague, purely internal ("so that the developer has
something to build"), or purely technical ("so that the database is normalised").

**Common failure modes:**
- "As a developer I want to refactor the authentication module" — no user value stated
- "As a user I want this functionality so that things work better" — unmeasurable
- Stories written for technical cleanup without connecting to a user outcome

**Repair patterns:**
- Always complete the "So that": ask "why does the user need this? what happens if they
  don't have it?"
- For technical enabler stories, frame value as: "so that [story X] can be delivered" and
  link to the story that has user value
- Spike stories: "so that the team can make an informed decision about [approach]"

---

## E — Estimable

**Definition:** The Development Team can form a reasonable estimate of the effort required.
If a story cannot be estimated, it is either too large, too ambiguous, or requires a Spike first.

**Passes if:** The team understands what Done looks like well enough to size the story,
even roughly.

**Fails if:** The story contains significant unknown technical risk; acceptance criteria
are missing or unmeasurable; scope is unbounded.

**Common failure modes:**
- "Implement AI-based recommendations" — no bounded scope
- Story with no acceptance criteria — team does not know what Done means
- Story dependent on a third-party decision not yet made

**Repair patterns:**
- Add Gherkin acceptance criteria — the main repair for estimability failures
- Create a Spike first: "Investigate X and produce a recommendation" — time-boxed,
  produces knowledge, not software
- Add constraints: "limited to [scope boundary] in this iteration"

---

## S — Small

**Definition:** The story can be completed within a single Sprint. If it cannot, it must
be split further.

**Passes if:** The effort indicator is XS, S, or M (up to approximately 5 developer-days).

**Fails if:** The effort indicator is L (more than 5 developer-days) or the story covers
multiple workflow steps, multiple user roles, or multiple screen flows.

**Common failure modes:**
- Stories covering an entire feature ("manage users" — covers create, read, update, delete)
- Stories with 8+ acceptance criteria scenarios — indicates too broad a scope
- Stories that span multiple user roles

**Repair patterns:**
- Apply story splitting patterns (see story-splitting-patterns.md)
- Flag with `[NEEDS SPLITTING]` and leave for Product Backlog Refinement
- For first-pass decomposition, L-size stories are acceptable as a placeholder —
  they must be split before Sprint Planning

---

## T — Testable

**Definition:** There is a clear, objective way to verify that the story is Done. The acceptance
criteria must be checkable by a tester who was not present when the story was written.

**Passes if:** Every acceptance criterion can be verified as pass/fail without subjective
judgement. Gherkin scenarios are present and specific.

**Fails if:** Acceptance criteria are vague ("the system should be easy to use"), subjective
("the UI should look professional"), or absent entirely.

**Common failure modes:**
- "The system should perform well" — no threshold
- "The user experience should be intuitive" — not testable
- "Error handling should work" — no specific error conditions defined

**Repair patterns:**
- Replace subjective criteria with measurable thresholds:
  "performs well" → "responds in ≤ 2 seconds for 95% of requests under 500 concurrent users"
- Write explicit Gherkin scenarios for every boundary condition and exception
- For usability criteria, define a testable proxy: "passes accessibility scan with zero Level AA violations"
