---
type: concept
title: "CQRS"
created: 2026-09-01
updated: 2026-09-01
tags:
  - concept
  - architecture
status: developing
related:
  - "[[Event Sourcing]]"
  - "[[cqrs-journey]]"
---

# CQRS

Command Query Responsibility Segregation splits the model that handles writes (commands) from the models that serve reads (queries).

## Relationship to event sourcing

CQRS does **not** require [[Event Sourcing]]. The write side can persist plain current state in a relational table and project read models from it. The two are often combined because an event log makes read-model projection natural, but each is usable alone ([[cqrs-journey]]).

## Trade-offs

- Read models are eventually consistent with the write model.
- Two models to maintain; worth it only where read and write shapes differ a lot.
