---
type: concept
title: "Event Sourcing"
created: 2026-09-01
updated: 2026-09-01
tags:
  - concept
  - architecture
status: developing
related:
  - "[[CQRS]]"
---

# Event Sourcing

Event sourcing stores every state change as an immutable event; current state is rebuilt by replaying the log.

It pairs well with [[CQRS]] (events feed the read-model projections) but does not depend on it.

## Trade-offs

- Full audit history and temporal queries.
- Schema evolution of old events is the main long-term cost.
