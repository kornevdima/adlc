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

A saga coordinates a business transaction across services as a sequence of local transactions, each with a [[Compensating Transaction]] that undoes it on failure.

Two styles: orchestration and choreography. See [[Event Sourcing]] for one way to publish the events.
