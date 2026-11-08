---
type: source
source_type: article
title: "Bounded Context (Martin Fowler bliki)"
author: Martin Fowler
date_published: 2014-01-15
url: https://martinfowler.com/bliki/BoundedContext.html
confidence: high
key_claims:
  - "Large models are divided into bounded contexts, each with one internally consistent model."
  - "Total unification of a large system's domain model is not feasible or cost-effective."
  - "Relationships between contexts should be drawn on a context map."
  - "Language and human culture are the dominant factor in where a boundary falls."
tags: [ddd, bounded-context, context-map]
---

# Bounded context (Fowler, 2014)

Foundational, so its age is not a staleness concern, but it is over 3 years old and gives only a short treatment of context maps. Confidence is high for the definitions, low for map notation (not covered).

A bounded context is the boundary inside which one model and one vocabulary hold. The same word (customer, product) can mean different things in two contexts, so integration needs an explicit mapping. Fowler recommends a context map to show those relationships and ties boundaries to teams and language more than to technology. For relationship patterns (partnership, customer-supplier, anticorruption layer) he points to Evans and Vernon.

See [[Project Within a Larger System]].
