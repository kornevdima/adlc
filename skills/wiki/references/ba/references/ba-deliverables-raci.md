# BA Deliverables RACI — Default Assignments by Archetype

## Purpose
Use this reference during Step 4 (Build RACI Matrix) of ba-stakeholder-analyzer.
Apply archetype defaults first, then adjust based on project-specific context.
Identify the closest matching stakeholder for each archetype column present in the project.

---

## RACI Key
| Symbol | Role | Obligation |
|--------|------|-----------|
| R | Responsible | Does the work or produces the output |
| A | Accountable | Single owner; approves and signs off; cannot be shared |
| C | Consulted | Provides input before the deliverable is finalised; two-way |
| I | Informed | Receives the output; no input required |
| — | Not involved | No action required for this deliverable |

**Rule:** Every deliverable must have exactly one **A**. If the project has no stakeholder matching
the default A archetype, the BA must explicitly decide who takes that role and note it.

---

## Standard BA Deliverable Set

### D01 — Project Charter / Initiation Brief
| Archetype | Default |
|-----------|---------|
| Sponsor | **A** |
| Decision-Maker | C |
| SME | — |
| End User | — |
| Regulator / Compliance | C |
| Technical Gatekeeper | C |
| Influencer | — |
| BA | R |

---

### D02 — Stakeholder Register and Analysis
| Archetype | Default |
|-----------|---------|
| Sponsor | I |
| Decision-Maker | C |
| SME | — |
| End User | — |
| Regulator / Compliance | — |
| Technical Gatekeeper | — |
| Influencer | — |
| BA | **A**, R |

---

### D03 — Elicitation Plan (workshop schedule, interview plan)
| Archetype | Default |
|-----------|---------|
| Sponsor | I |
| Decision-Maker | **A** |
| SME | C |
| End User | C |
| Regulator / Compliance | I |
| Technical Gatekeeper | I |
| Influencer | — |
| BA | R |

---

### D04 — Business Requirements Document (BRD)
| Archetype | Default |
|-----------|---------|
| Sponsor | **A** |
| Decision-Maker | C |
| SME | C |
| End User | C |
| Regulator / Compliance | C |
| Technical Gatekeeper | C |
| Influencer | — |
| BA | R |

---

### D05 — Requirements Register (living document)
| Archetype | Default |
|-----------|---------|
| Sponsor | I |
| Decision-Maker | **A** |
| SME | C |
| End User | — |
| Regulator / Compliance | C (for compliance-tagged items) |
| Technical Gatekeeper | C (for NFR items) |
| Influencer | — |
| BA | R |

---

### D06 — Process Models (AS-IS and TO-BE)
| Archetype | Default |
|-----------|---------|
| Sponsor | I |
| Decision-Maker | **A** |
| SME | R, C |
| End User | C |
| Regulator / Compliance | C (for regulated processes) |
| Technical Gatekeeper | I |
| Influencer | — |
| BA | R |

---

### D07 — Gap Analysis
| Archetype | Default |
|-----------|---------|
| Sponsor | **A** |
| Decision-Maker | C |
| SME | C |
| End User | — |
| Regulator / Compliance | C |
| Technical Gatekeeper | C |
| Influencer | — |
| BA | R |

---

### D08 — User Stories and Acceptance Criteria
| Archetype | Default |
|-----------|---------|
| Sponsor | I |
| Decision-Maker | **A** |
| SME | C |
| End User | C |
| Regulator / Compliance | C (for compliance stories) |
| Technical Gatekeeper | C (for NFR stories) |
| Influencer | — |
| BA | R |

---

### D09 — Business Case
| Archetype | Default |
|-----------|---------|
| Sponsor | **A** |
| Decision-Maker | C |
| SME | C |
| End User | I |
| Regulator / Compliance | C |
| Technical Gatekeeper | C |
| Influencer | C |
| BA | R |

---

### D10 — Solution Assessment / Options Analysis
| Archetype | Default |
|-----------|---------|
| Sponsor | **A** |
| Decision-Maker | C |
| SME | C |
| End User | I |
| Regulator / Compliance | C |
| Technical Gatekeeper | C |
| Influencer | C |
| BA | R |

---

### D11 — UAT Test Cases and Script
| Archetype | Default |
|-----------|---------|
| Sponsor | I |
| Decision-Maker | **A** |
| SME | C |
| End User | R, C |
| Regulator / Compliance | C (for compliance scope) |
| Technical Gatekeeper | I |
| Influencer | — |
| BA | R |

---

### D12 — Scrum Event Inputs (Product Backlog, Sprint inputs)
| Archetype | Default |
|-----------|---------|
| Sponsor | I |
| Decision-Maker | **A** |
| SME | C |
| End User | C |
| Regulator / Compliance | I |
| Technical Gatekeeper | C |
| Influencer | — |
| BA | R |

---

## RACI Adjustment Rules

### Rule 1 — No Matching Archetype
If a deliverable's default A archetype is not present in the project, assign A to the
next-highest Power stakeholder and note: "Default A archetype (Sponsor) not available;
A assigned to [Name] as highest-authority stakeholder present."

### Rule 2 — Single Person Covering Multiple Archetypes
When one person covers Sponsor and Decision-Maker (common in small projects), they hold all
RACI assignments from both archetypes. Combine into one row; no duplication.

### Rule 3 — BA as Accountable
The BA is only ever A on stakeholder analysis (D02). On all other deliverables, the BA is R.
The business always owns the decision; the BA produces the artefact.

### Rule 4 — Compliance Stakeholder Involvement
Add Regulator/Compliance as C on any deliverable that touches regulated data, legal obligations,
or audit-relevant processes, regardless of default. Mark the C with an asterisk (C*) and note
the compliance basis.

### Rule 5 — RACI Gaps
If any deliverable has no A after applying all rules, it is a critical gap.
Flag it in the Issues section as: `[RACI GAP: D0X has no Accountable owner — resolve before
deliverable work begins]`
