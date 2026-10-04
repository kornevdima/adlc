---
type: source
title: "cdc-overview"
created: 2026-09-01
updated: 2026-09-01
tags:
  - source
  - cdc
status: current
related: []
source_type: article
confidence: medium
key_claims:
  - "Log-based CDC reads the transaction log"
  - "Query-based CDC misses hard deletes"
---

# cdc-overview

Change data capture streams row-level changes out of a database. Log-based CDC tails the transaction log (binlog, WAL); query-based CDC polls tables by an updated-at column and misses deletes.
