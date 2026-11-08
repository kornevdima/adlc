---
type: source
title: "Atlassian: view and understand the control chart"
source_type: documentation
author: "Atlassian"
date_published: 2026-01-01
url: "https://support.atlassian.com/jira-software-cloud/docs/view-and-understand-the-control-chart/"
confidence: high
status: reviewed
created: 2026-11-08
updated: 2026-11-08
tags: [source, jira, cycle-time, lead-time]
key_claims:
  - "Cycle time is the time spent working on a work item, from when work begins to when it completes."
  - "Lead time starts when the work item is logged and ends when work is completed."
  - "The clock follows the statuses the team selects as columns; Jira tries to preselect them."
  - "The rolling average spans 20% of displayed items, an odd number, minimum 5."
---

# Atlassian: view and understand the control chart

Jira's control chart defines the two times its users see. The page carries no date; the date above is a placeholder for "current documentation". (confidence: high for definitions)

- Cycle time: time spent working on an item, usually from when work begins until it completes.
- Lead time: from when the item is logged until work completes.
- Clock boundaries are not fixed transitions. They depend on the space's workflow, and the team chooses which statuses count (for example In Progress and In Review for cycle time). Each dot sits at the moment the item last left a selected status.
- The blue line is a work-based rolling average over 20% of displayed items (odd, at least 5); the shaded band is the standard deviation, and a narrow band means future cycle times are likely close to the average.

Consequence: a cycle time is only comparable across teams if they select the same statuses, so the selection belongs in the record.

Used in [[Delivery Metrics and Their Data Sources]].
