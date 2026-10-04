---
type: concept
title: "Saga Pattern"
created: 2026-09-01
updated: 2026-09-01
tags:
  - concept
  - architecture
status: developing
related:
  - "[[Event Sourcing]]"
---

# Saga Pattern

A saga coordinates a business transaction across services as a sequence of local transactions, each with a compensating action that undoes it on failure.

Two styles: orchestration (a coordinator tells each service what to do) and choreography (services react to each other's events). See [[Event Sourcing]] for one way to publish those events.
