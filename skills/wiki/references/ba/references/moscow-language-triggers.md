# MoSCoW Language Triggers and Override Rules

## Purpose
Use this reference during Step 4 (Prioritise) of ba-elicitation-synthesizer.
Apply language trigger matching first, then check override rules, then apply defaults.

---

## MoSCoW Definitions (Applied Consistently)

| Priority | Definition for this skill |
|----------|--------------------------|
| **Must Have** | Without this, the solution fails to meet its core purpose or violates a legal/contractual obligation. A go-live is blocked without Must Haves. |
| **Should Have** | Important and expected. Significant negative impact if absent, but the solution can operate without it temporarily. |
| **Could Have** | Desirable if effort/cost allows. Limited impact if omitted. Often deferred to a later release. |
| **Won't Have (this time)** | Explicitly out of scope for the current delivery. May be revisited in future. Not "never" — "not now." |

---

## Language Trigger Table

### Must Have Triggers
Apply **Must Have** when the stakeholder uses any of the following (in any tense or inflection):

| Trigger Pattern | Example |
|----------------|---------|
| must, must have, must be, must not | "It must allow export to CSV." |
| have to, has to, need to, needs to | "We have to comply with GDPR." |
| required, requirement, is required | "Password complexity is required by policy." |
| essential, critical, cannot function without | "This is critical for payroll to run." |
| legally required, regulatory, compliance | "HMRC requires a submission audit trail." |
| contractually obligated, SLA requires | "The SLA requires 99.9% uptime." |
| will not go live without | "We won't sign off without role-based access." |
| non-negotiable | "Non-negotiable — must have SSO." |

---

### Should Have Triggers
Apply **Should Have** when:

| Trigger Pattern | Example |
|----------------|---------|
| should, should have | "It should notify managers by email." |
| important, very important | "Real-time dashboard is very important to us." |
| expect, expected, expecting | "Users expect search to work across all fields." |
| normally, standard practice, best practice | "Standard practice is to send a confirmation." |
| strongly prefer, really want | "We really want mobile access at launch." |
| significant impact if missing | "Without this, the approval process is manual." |

---

### Could Have Triggers
Apply **Could Have** when:

| Trigger Pattern | Example |
|----------------|---------|
| nice to have, would be nice | "It would be nice to have dark mode." |
| could, could have | "We could add bulk import later." |
| low priority, not urgent | "Low priority, but dark mode would help." |
| would like, ideally | "Ideally the dashboard would be customisable." |
| if time allows, if budget allows | "If budget allows, add a mobile app." |
| minor improvement, convenience | "A keyboard shortcut would be convenient." |

---

### Won't Have Triggers
Apply **Won't Have** when:

| Trigger Pattern | Example |
|----------------|---------|
| out of scope, not in scope | "Native mobile app is out of scope for v1." |
| not this time, not for now | "We're not doing multi-currency for now." |
| explicitly deferred, phase 2, future release | "Phase 2 will handle integrations." |
| won't, will not (applied to a feature) | "We won't support IE11." |
| explicitly excluded by sponsor | Sponsor statement removing a feature |

---

## Override Rules (Apply After Trigger Match)

These rules take precedence over language triggers.

### Override 1 — Regulatory or Contractual Basis
If a requirement has a stated legal, regulatory, or contractual basis, it is **Must Have** regardless
of the language used.
> "It would be nice to have GDPR compliance" → Must Have (regulatory basis overrides "would be nice")
> Note: "GDPR basis override applied — language signal was Could Have."

### Override 2 — Sponsor Scope Declaration
If the project sponsor has explicitly stated a feature is out of scope (in any phrasing), it is
**Won't Have** regardless of other stakeholder requests for it.
> Note this conflict in the Issues Log as `[CONFLICT]` if another stakeholder has expressed it as Must/Should.

### Override 3 — Core Workflow Dependency
If a FR is the only mechanism enabling a Must Have FR to function, it is also **Must Have**, even
if stated weakly.
> "The login page would be a good starting point" — if login is required to access any Must Have
> functionality, it is Must Have.
> Note: "Core dependency elevation applied."

### Override 4 — Inferred (No Signal)
If no language trigger and no override rule applies, assign **Should Have** and append:
`Priority: Should Have (Inferred — no language signal; confirm with stakeholder)`

---

## Conflict Handling

When language signals from different stakeholders contradict:
1. Record both signals in the Issues Log as `[CONFLICT]`
2. Apply the higher-priority stakeholder's signal (Sponsor > Decision-Maker > SME > End User)
3. Flag: "Priority assigned per [Sponsor name] statement. [Other stakeholder] stated [other priority] — to be resolved in review."

---

## MoSCoW Application Checklist

Before completing Step 4:
- [ ] Every item has a MoSCoW value — no blanks
- [ ] Every "Inferred" item is flagged in the Notes column
- [ ] All regulatory/contractual overrides are noted with the basis
- [ ] Conflicts between stakeholder signals are in the Issues Log
- [ ] Won't Have items are still documented (they are scope decisions, not deletions)
