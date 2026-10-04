---
type: research-plan
title: "Plan: Research Change Data Capture Tools"
created: 2026-09-20
updated: 2026-09-20
tags: [research, plan]
status: active
---

# Plan: Research Change Data Capture Tools

Statuses: `[ ]` not started | `[→]` in progress | `[✓]` done | `[!]` blocked

- [✓] Q1: What is change data capture and how does log-based CDC differ from query-based CDC?
- [ ] Q2: How do Debezium, AWS DMS and Maxwell compare for CDC from MySQL and PostgreSQL?
- [ ] Q3: What are the common operational pitfalls of running CDC in production?

## Notes
- Q1: filed [[cdc-overview]]; log-based CDC reads the database's transaction log, query-based CDC polls with timestamps.
