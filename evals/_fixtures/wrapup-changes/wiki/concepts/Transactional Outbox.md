---
type: concept
title: "Transactional Outbox"
created: 2026-10-01
updated: 2026-10-01
tags:
  - concept
  - architecture
status: developing
related:
  - "[[Saga Pattern]]"
---

# Transactional Outbox

Write the outgoing message into an outbox table in the same local transaction as the business change; a relay publishes it afterwards. Gives at-least-once delivery, so consumers must be idempotent. Used by choreographed [[Saga Pattern]] steps.
