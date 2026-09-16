# Financial Model Formulas — NPV, ROI, Payback, Sensitivity, and Cost Categories

## Purpose
Use during Step 4 (Build Financial Model) and Step 5 (Sensitivity Analysis) of ba-business-case-builder.
Section 1: NPV formula and discount rates. Section 2: ROI formula. Section 3: Payback period.
Section 4: Discount factors table. Section 5: Sensitivity analysis design. Section 6: Standard cost and benefit categories.

---

## Section 1 — Net Present Value (NPV)

```
NPV = Sum of (Net Benefit_t / (1 + r)^t) for t = 0 to n

Where:
  Net Benefit_t = Total Benefits in year t minus Total Costs in year t
  r = discount rate (default 8% unless specified)
  t = year number (0 = current year / investment year)
  n = model horizon (3 or 5 years)
```

**Interpretation:**
- NPV > 0: The initiative creates value in present-value terms → supports investment
- NPV < 0: The initiative destroys value in present-value terms → requires non-financial justification
- NPV = 0: Break-even at the discount rate

**Default discount rates by context:**

| Context | Default Rate |
|---------|-------------|
| General commercial | 8% |
| Public sector (UK/EU) | 3.5% (HM Treasury Green Book) |
| High-risk technology | 12–15% |
| Stated WACC provided | Use stated WACC |

**Rule:** Always state the discount rate used. Never present an NPV figure without the rate it was calculated at. If the reader uses a different rate, the NPV changes — this must be visible.

---

## Section 2 — Return on Investment (ROI %)

```
ROI % = (Total Net Benefits over horizon / Total Costs over horizon) × 100

Where:
  Total Net Benefits = Sum of all benefit values over the model horizon
  Total Costs = Sum of all cost values over the model horizon (not discounted)
```

**Important distinction:** ROI as defined here is undiscounted. It should always be presented alongside NPV, not instead of it. NPV is the more rigorous measure; ROI is included because it is the metric most decision-makers instinctively understand and ask for.

**Worked example:**
```
Year 0 costs: £120,000
Year 1–3 annual costs (support + licence): £20,000/year → £60,000 total
Total costs over 3 years: £180,000

Year 1 benefits: £60,000
Year 2 benefits: £90,000
Year 3 benefits: £90,000
Total benefits over 3 years: £240,000

ROI % = (£240,000 / £180,000) × 100 = 133%
```

---

## Section 3 — Payback Period

```
Payback Period = The first year (or part-year) at which Cumulative Net Benefit ≥ 0

Part-year calculation:
  Payback = Last year with negative cumulative + (|Last negative cumulative| / Net benefit in next year)
```

**Worked example:**
```
Year 0: Net benefit = -£120,000  |  Cumulative = -£120,000
Year 1: Net benefit = +£40,000   |  Cumulative = -£80,000
Year 2: Net benefit = +£70,000   |  Cumulative = -£10,000
Year 3: Net benefit = +£70,000   |  Cumulative = +£60,000

Payback = 2 + (10,000 / 70,000) = 2.14 years ≈ 2 years 2 months
```

**Presenting payback period:** Always express in years and months, not as a decimal. "2.14 years" is harder to act on than "2 years and 2 months."

---

## Section 4 — Discount Factors Table (8% default)

Use these multipliers to convert future net benefits into present value.

| Year | Discount Factor (8%) |
|------|---------------------|
| 0 | 1.0000 |
| 1 | 0.9259 |
| 2 | 0.8573 |
| 3 | 0.7938 |
| 4 | 0.7350 |
| 5 | 0.6806 |

For any other rate r: `Factor_t = 1 / (1 + r)^t`

**Example for 3.5% (public sector rate):**
| Year | Discount Factor (3.5%) |
|------|----------------------|
| 0 | 1.0000 |
| 1 | 0.9662 |
| 2 | 0.9335 |
| 3 | 0.9019 |

---

## Section 5 — Sensitivity Analysis Design

Run exactly three scenarios for the recommended option. Do not run them for non-recommended options — it creates unnecessary complexity and does not change the recommendation.

| Scenario | What changes | How to calculate |
|----------|-------------|-----------------|
| Base case | Nothing — figures as estimated | Reference model |
| Benefits -20% | All benefit rows × 0.80 | Recalculate NPV, ROI, Payback |
| Costs +20% | All cost rows × 1.20 | Recalculate NPV, ROI, Payback |
| Both adverse | Benefits × 0.80 AND Costs × 1.20 simultaneously | Recalculate NPV, ROI, Payback |

**Sensitivity interpretation:**

| Result | Statement in the document |
|--------|--------------------------|
| NPV positive in all four scenarios | "The case is robust. Even under combined adverse assumptions, the initiative remains NPV-positive." |
| NPV positive in base + one adverse, negative in both adverse | "The case is moderately sensitive. It depends on benefits being realised within 20% of estimates." |
| Recommendation changes in any single adverse scenario | "The case is fragile. Flag explicitly: the recommendation depends on [specific assumption] holding." |
| Payback extends beyond model horizon in any adverse scenario | "A risk: delayed payback under adverse conditions. Mitigation: [state mitigation]." |

**The sensitivity analysis is mandatory.** A business case without it cannot tell the reader how confident to be in the recommendation. A single point estimate presented without a range is not analysis — it is a guess with formatting.

---

## Section 6 — Standard Cost and Benefit Categories

Use these categories unless the project warrants different ones. Adapting the categories for the specific project is acceptable; omitting entire categories without explanation is not.

### Cost Categories

| Category | What to include | Timing |
|---------|----------------|--------|
| Implementation | External consultancy, development, integration, data migration | Year 0 (mostly) |
| Licences | Software licence fees (per user, per year, or flat) | Year 1 onwards |
| Infrastructure | Hosting, cloud services, hardware, network changes | Year 0 + annual |
| Internal staff time | FTE cost of staff dedicated to the project (% of burdened salary × months) | Year 0 + ongoing |
| Training | Design, delivery, materials, lost productivity during training | Year 0–1 |
| Change management | Communications, adoption support, process documentation | Year 0–1 |
| Contingency | 10–15% of total for well-defined scope; 20–25% for uncertain scope | Year 0 |
| Ongoing support and maintenance | Internal resource and external support contracts | Year 1 onwards |

**Contingency rule:** Contingency is not a fudge factor. It is an explicit acknowledgement that estimates are uncertain. State the contingency percentage and the basis for selecting it. A zero-contingency estimate signals that either the scope is perfectly defined (rare) or that contingency has been hidden elsewhere (common).

### Benefit Categories

| Category | How to quantify | What to avoid |
|---------|----------------|--------------|
| Cost avoidance | Hours saved × burdened hourly rate | Claiming 100% of a person's time — partial FTE avoidance is realistic |
| Efficiency gain | Output increase per FTE, converted to £ value per unit | Vague statements like "improved efficiency" without a number |
| Revenue uplift | Additional revenue directly enabled by this capability, with attribution fraction stated | Claiming all revenue growth; state the fraction attributed to this initiative |
| Risk reduction | Probability of risk event × financial impact of that event | Over-claiming intangible risks without a basis |
| Compliance value | Fine or remediation cost avoided, with regulatory reference | Claiming maximum possible fine as certain — use expected value |
| Productivity gain | Time freed × burdened cost, where freed time is used for value-creating activities | Claiming paper savings — only count if headcount or overtime is actually reduced |

**Benefit realisation timing:** Benefits rarely land in full in Year 1. Ramp the benefit values realistically:
- Year 1: 30–50% of steady-state benefit (adoption lag, change management)
- Year 2: 70–90% of steady-state benefit
- Year 3+: Full steady-state benefit

State the ramp assumption explicitly. An optimistic ramp weakens the credibility of the case; a conservative ramp that the initiative then beats strengthens it.
