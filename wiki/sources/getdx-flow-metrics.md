---
type: source
title: "Flow metrics (DX blog, after Kersten's Flow Framework)"
source_type: article
author: "DX (getdx.com), summarizing Mik Kersten"
date_published: 2025-09-09
url: "https://getdx.com/blog/flow-metrics/"
confidence: medium
status: reviewed
created: 2026-11-08
updated: 2026-11-08
tags: [source, flow-metrics, flow-framework, cycle-time]
key_claims:
  - "Flow time runs from approval (entry to the development backlog) to production, including waiting and active states."
  - "Flow velocity is the count of flow items completed per period, regardless of size."
  - "Flow efficiency is active time divided by total flow time, times 100."
  - "Flow load is the count of items in progress."
  - "Flow distribution is the mix of features, defects, risks and debt."
---

# Flow metrics (DX blog)

A vendor article, last updated 2025-09-09, original date not stated. It credits the metrics to Mik Kersten's Flow Framework, which I did not read directly (confidence: medium). The article names five metrics and gives no required data fields; the data needs below are inferred from the definitions.

- Flow time: start and end timestamps per item.
- Flow velocity: completion date per item.
- Flow efficiency: a timestamp for each state change, so active and waiting time can be split. The article does not say how to decide what counts as active.
- Flow load: items in an in-progress state at a point in time.
- Flow distribution: an item type per item.

It also says start and end points must be defined the same way for every work type, and that the best flow load must be found by trial.

Related search findings (low to medium confidence, vendor docs): throughput history feeds Monte Carlo forecasts of "how many by a date" and "when will N items finish"; a cycle time scatterplot forecasts a single item; Little's Law ties cycle time, throughput and WIP. NoEstimates is framed as replacing story points and velocity with throughput and cycle time.

Used in [[Delivery Metrics and Their Data Sources]].
