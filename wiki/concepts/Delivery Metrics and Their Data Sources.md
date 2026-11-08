---
type: concept
title: "Delivery Metrics and Their Data Sources"
confidence: medium
sources: ["[[dora-metrics-guide]]", "[[getdx-flow-metrics]]"]
tags: [metrics, dora, space, flow, estimation, frontmatter]
---

# Delivery metrics and their data sources

Git gives the end of the clock (when code landed and shipped); the work item gives the start of the clock and the meaning (what the change was for, how big, which release). Keep both and link them by item id in commit messages and tags. (Source: [[dora-metrics-guide]], [[getdx-flow-metrics]]; the split itself is this page's synthesis, confidence: medium.)

## What each metric needs

The table lists each metric, its raw data, and where that data comes from.

| Metric | Raw data | From git | From the work item |
|---|---|---|---|
| Change lead time (DORA) | commit time, production deploy time | commit timestamp; deploy tag or release tag timestamp | none, if tags are the deploy record |
| Deployment frequency (DORA) | deploy events | tag or release timestamps | none |
| Failed deployment recovery time | failed deploy, restore time | revert or fix commit, next good tag | incident link helps; git alone cannot tell a failure from a normal fix |
| Change fail rate | deploys needing rollback or hotfix | revert commits, hotfix-named branches | a "caused by release X" field is more reliable than guessing |
| Deployment rework rate | unplanned deploys from incidents | partly (hotfix tags) | item type = incident or hotfix |
| Flow time (approval to production) | approval time, production time | production tag | approval or "ready" timestamp |
| Cycle time (start of work to done) | start time, done time | first commit on the branch, merge time | status-change timestamps are the true start |
| Flow velocity / throughput | items done per period | merges per period (proxy only) | done date per item |
| Flow efficiency | active vs waiting time | no | every status transition timestamp |
| Flow load (WIP) | items in progress now | open branches (proxy only) | status |
| Flow distribution | item type counts | no | type field |
| Estimation accuracy | estimate vs actual | no | size estimate plus cycle time |

## Definitions and tiers

DORA has five measures: change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate (Source: [[dora-metrics-guide]], high). The 2025 report adds reliability as a further outcome (low; not read directly). 2024 tiers, from secondary summaries (medium): elite deploys on demand with lead time under a day and recovery under an hour; low deploys less than monthly. Cutoffs for low and for failure rate vary by source.

Flow metrics: flow time, flow velocity, flow efficiency, flow load, flow distribution (Source: [[getdx-flow-metrics]], medium). Cycle time is conventionally start of work to done; flow time starts earlier, at approval.

SPACE (Forsgren, Storey and colleagues, ACM Queue 19(1), 2021; older than 3 years but foundational) has five dimensions: satisfaction and well-being, performance, activity, communication and collaboration, efficiency and flow. Guidance: use at least three dimensions, report in aggregate for teams, and treat activity counts as the most misused. This run could not fetch the article (HTTP 403), so this rests on search summaries (confidence: medium). Only activity and part of efficiency come from git; satisfaction needs a survey.

## Estimation

Story points and t-shirt sizes are team-relative guesses stored on the item; they are not derivable from git. NoEstimates and flow forecasting replace them with throughput history and cycle time distributions, run through Monte Carlo ("how many by a date", "when will N be done") and Little's Law (confidence: low to medium, vendor docs). Practical consequence: record a coarse size anyway, because it costs one field and lets a later vault compare both methods.

## Fields a story or epic must carry

So lead time, cycle time and throughput can be computed later, each record needs:

- `id`, `type` (feature, defect, risk, debt, incident), `parent` (epic id)
- `created`, `ready` (approval, starts flow time), `started`, `done` dates
- a status history: one dated line per transition, because efficiency and WIP need it
- `size` (t-shirt or points, optional)
- `release` (tag name), set when shipped
- `caused_by` (release or item id) on defects and incidents, for change fail rate
- commits carry the item id, so git history joins to the record

An epic needs the same dates plus its child ids; its times are derived from children, not entered by hand.

## Gaps

Tier thresholds for 2025 and the reliability definition need the primary report; SPACE needs the ACM text; Atlassian's own control-chart documentation was not reached.
