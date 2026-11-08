---
type: source
source_type: documentation
title: "Context Mapper: Context Map"
author: Context Mapper project
date_published: undated (fetched 2026-11-08)
url: https://contextmapper.org/docs/context-map/
confidence: medium
key_claims:
  - "Context map relationships are symmetric (Partnership, Shared Kernel) or asymmetric (Upstream-Downstream, Customer-Supplier)."
  - "In upstream-downstream the upstream influences the downstream but not the reverse."
  - "In Customer-Supplier the downstream priorities factor into upstream planning."
  - "Open Host Service and Published Language are upstream roles; Conformist and Anticorruption Layer are downstream roles."
tags: [ddd, context-map, relationships]
---

# Context Mapper: context map

Tool documentation for a DDD modelling language. The extracted page gave short definitions only for the two asymmetric relationships; the rest are named with their roles, not defined, so confidence is medium. Pair with [[fowler-bounded-context]].

## Relationship types

- Symmetric: Partnership (P) and Shared Kernel (SK). Neither side is upstream or downstream.
- Upstream-Downstream (U, D): the upstream influences the downstream; the downstream has no influence on the upstream.
- Customer-Supplier (C/S): a special upstream-downstream form where the downstream priorities factor into upstream planning.

## Roles an asymmetric relationship can carry

- Upstream: Open Host Service (OHS) and Published Language (PL).
- Downstream: Conformist (CF) and Anticorruption Layer (ACL).

Separate Ways and Big Ball of Mud are not on this page.

## Why it matters here

The relationship type is the context-level counterpart of a team interaction mode: it says who bends to whom. Record it in the dependency table. See [[Project Within a Larger System]].
