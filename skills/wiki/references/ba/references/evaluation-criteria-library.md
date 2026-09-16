# Evaluation Criteria Library

## Purpose
Use during Step 2 (Select Criteria) and Step 4 (Sensitivity Analysis) of ba-solution-assessment.

---

## Section 1 — Default Criteria Sets by Decision Type

### Vendor / COTS Solution Selection

| Cluster | Criterion | Default Weight | Notes |
|---------|-----------|---------------|-------|
| Functional Fit (30%) | Core feature coverage | 15% | Does it do what we need? |
| | Integration capability | 10% | APIs, connectors, data formats |
| | Configurability / extensibility | 5% | Can it adapt without custom code? |
| Technical Fit (20%) | Architecture alignment | 8% | Cloud, on-prem, hybrid; compatibility with estate |
| | Security posture | 7% | Certifications, data handling, access controls |
| | Performance and scalability | 5% | Handles our volume and growth |
| Vendor Maturity (15%) | Track record and references | 8% | Customers in our sector, tenure, case studies |
| | Financial stability | 4% | Not likely to disappear post-contract |
| | Product roadmap | 3% | Direction of travel aligns with our needs |
| Commercial (15%) | Total cost of ownership (3yr) | 10% | Licences, implementation, support, maintenance |
| | Pricing model suitability | 5% | Per user, per transaction, flat — fits our model |
| Support and Service (15%) | SLA and support hours | 7% | Matches our operational requirements |
| | Onboarding and implementation support | 5% | Availability of implementation partner ecosystem |
| | Documentation and training | 3% | Quality and accessibility of learning resources |
| Compliance (5%) | Regulatory certifications | 5% | GDPR, ISO 27001, sector-specific |

---

### Build vs Buy Decision

| Cluster | Criterion | Default Weight | Notes |
|---------|-----------|---------------|-------|
| Total Cost of Ownership (25%) | 3-year total cost | 15% | Build: internal + external dev; Buy: licences + implementation |
| | Hidden / ongoing costs | 10% | Maintenance, upgrades, licence escalation |
| Time to Value (20%) | Time to first usable capability | 12% | How quickly does the organisation benefit? |
| | Time to full capability | 8% | When is the full scope delivered? |
| Strategic Fit (20%) | Competitive differentiation | 10% | Does owning this capability create strategic advantage? |
| | Alignment with technology strategy | 10% | Build: is internal capability a strategic goal? Buy: vendor lock-in risk |
| Risk (20%) | Delivery risk | 10% | Build: team capability and delivery track record; Buy: vendor and integration risk |
| | Operational risk | 10% | Build: ongoing maintenance burden; Buy: dependency on vendor continuity |
| Team Capability (15%) | Internal skills available | 8% | Can the team build AND maintain it? |
| | Capacity | 7% | Is the team available without compromising other priorities? |

---

### Architecture Option Appraisal

| Cluster | Criterion | Default Weight | Notes |
|---------|-----------|---------------|-------|
| Technical Soundness (30%) | Alignment with target architecture | 12% | Fits the enterprise architecture direction |
| | Technical risk | 10% | Known unknowns, technology maturity |
| | Supportability and maintainability | 8% | Can the team support it post-delivery? |
| Scalability and Fit (25%) | Meets NFRs (performance, availability) | 15% | Core quality attributes satisfied |
| | Growth and evolution headroom | 10% | Handles future scale and change |
| Cost and Effort (25%) | Implementation effort | 15% | Story points or FTE estimate |
| | Operational cost | 10% | Ongoing infrastructure, licencing, support |
| Risk (20%) | Delivery risk | 10% | Confidence in delivery within constraints |
| | Reversibility | 10% | Cost/effort to undo this decision if wrong |

---

### Initiative Prioritisation (Backlog or Portfolio Level)

| Cluster | Criterion | Default Weight | Notes |
|---------|-----------|---------------|-------|
| Strategic Impact (30%) | Alignment to strategic objective | 15% | How directly does this advance the strategy? |
| | User / customer value | 15% | Does this meaningfully improve the experience? |
| Urgency (20%) | Cost of delay | 12% | What is lost for every sprint this is not done? |
| | Regulatory or contractual deadline | 8% | External forcing function |
| Feasibility (25%) | Team capability | 12% | Does the team have the skills to deliver this? |
| | Dependencies resolved | 8% | Can this be started without blocking work? |
| | Estimability | 5% | Is this well-understood enough to plan? |
| Risk (25%) | Delivery risk | 12% | Likelihood of successful delivery |
| | Business risk if not done | 13% | Consequence of not delivering this |

---

## Section 2 — Scoring Rubric Details

### Functional Fit — Detailed Rubric

| Score | Criteria | Evidence |
|-------|---------|---------|
| 5 | Solution meets the requirement completely, out of the box, with no customisation | Live demo, documented feature |
| 4 | Solution meets the requirement with minor configuration only | Configuration documentation or confirmed by vendor |
| 3 | Solution meets the core of the requirement; edge cases need customisation | Vendor confirms with development estimate |
| 2 | Solution partially meets the requirement; a workaround exists but is not ideal | Vendor confirms workaround |
| 1 | Requirement is not met; vendor cannot confirm a roadmap item | Vendor confirms gap |

### Total Cost of Ownership — Calculation Approach

Calculate over a 3-year horizon:
- Year 0: Implementation cost (consultancy, internal staff time, data migration, testing)
- Year 1–3: Licence/subscription fees + ongoing support + internal maintenance FTE allocation
- Include: training, change management, integration maintenance

Compare on total 3-year cost, not Year 0 only. Build options often look cheaper on Year 0
but more expensive on 3-year TCO.

### Vendor Track Record — Scoring Guide

| Score | Criteria |
|-------|---------|
| 5 | 3+ reference customers in the same sector with similar scope; available to speak |
| 4 | Reference customers available; some sector alignment |
| 3 | References available but different sector or smaller scale |
| 2 | Limited references; case studies only, no live customers willing to speak |
| 1 | No references; product is new or early-stage |

---

## Section 3 — Sensitivity Analysis Design

Run exactly three scenarios. Design each to test a realistic alternative weighting
perspective, not an extreme outlier.

### Scenario 1 — Sponsor Priority
**Rationale:** The sponsor's most important criterion may differ from the balanced default weights.
**Adjustment:** Identify the criterion the sponsor has explicitly prioritised (or infer from their
role archetype). Increase its weight by 20 percentage points. Reduce all other criteria weights
proportionally to maintain 100% total.
**Question it answers:** "If the sponsor's top priority is weighted more heavily, does the
recommendation hold?"

### Scenario 2 — Risk Emphasis
**Rationale:** Projects that fail often fail on risk, not on feature fit. Decision-makers often
underweight risk in scoring models.
**Adjustment:** Set the implementation risk criterion to 25%. Reduce all other criteria proportionally.
**Question it answers:** "If we weight risk more heavily than typical, does the recommendation hold?"

### Scenario 3 — Cost Emphasis
**Rationale:** Budgets are constrained. The commercially cheapest option may be acceptable
if the scoring gap on other criteria is small.
**Adjustment:** Set the commercial / TCO criterion cluster to 30%. Reduce all other clusters proportionally.
**Question it answers:** "If cost is the primary driver, does the recommendation hold?"

### Stability Assessment

After running all three scenarios, assess:

| Outcome | Statement |
|---------|-----------|
| Ranking unchanged across all 3 | "The recommendation is robust across all sensitivity scenarios." |
| Ranking changes in 1 scenario | "The recommendation holds in most scenarios. Under [scenario name], [Option B] would be preferable if [condition]. Decision-makers who prioritise [criterion] should note this." |
| Ranking changes in 2+ scenarios | "The decision is sensitive to weighting assumptions. The recommendation of [Option A] depends on [criteria cluster] being weighted at [X%] or above. Decision-makers should validate the agreed weights with stakeholders before proceeding." |
