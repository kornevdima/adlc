---
type: source
title: "SEI Attribute-Driven Design method collection"
source_type: web
author: "Software Engineering Institute, Carnegie Mellon University (ADD version 2.0 by Wojcik, Bachmann, Bass, Clements, Merson, Nord, Wood)"
date_published: 2006-10-31
url: "https://www.sei.cmu.edu/library/attribute-driven-design-method-collection/"
created: 2026-11-08
updated: 2026-11-08
confidence: high
key_claims:
  - "ADD is a step-by-step method that bases an architecture on quality attribute requirements and decomposes the system recursively."
  - "ADD takes three inputs: functional requirements, quality attribute requirements and constraints."
  - "Functional requirements arrive as a feature list or use cases; quality attribute requirements arrive as quality attribute scenarios, for example from a Quality Attribute Workshop."
  - "Part 1 of the method picks an element, identifies candidate architectural drivers and chooses a design concept (tactics, patterns) that satisfies them."
  - "Part 2 instantiates elements, allocates responsibilities, defines interfaces, and turns refined requirements into constraints on each element."
tags: [source, architecture, add, quality-attributes]
---

# SEI Attribute-Driven Design method collection

The Software Engineering Institute's library page for Attribute-Driven Design (ADD) lists the method report, version 2.0 (October 2006), and related papers. This is the primary publisher's page. The full report text was not fetched; the page summarizes it. The collection page is dated 30 November 2012 and the earlier-tracked report URL returned a 403.

## What the page states

ADD designs the architecture of a software-intensive system from its quality attribute requirements. It decomposes the system recursively and picks tactics and architectural patterns at each level.

The inputs are three:

- functional requirements, written as a feature list or as use cases;
- quality attribute requirements, written as quality attribute scenarios such as those a Quality Attribute Workshop produces;
- constraints, which are design decisions forced from outside.

The steps, in two parts:

1. Using tactics to meet quality requirements: confirm the requirements information is sufficient, choose an element to decompose, identify candidate architectural drivers, choose a design concept that satisfies the drivers.
2. Documenting the decomposition: instantiate elements and allocate responsibilities, define interfaces, verify and refine requirements and turn them into constraints for each element, then repeat for the next element.

## What the page does not state

The page names architectural drivers as a step but does not define the term. It lists quality attribute scenarios as an input without describing their parts. The "top-priority mix of functional and quality requirements" definition of a driver therefore still rests on the secondary summaries already in the wiki.

## Use in the wiki

It backs the boundary in [[Disciplines Bodies of Knowledge and Boundaries]]: the analyst supplies requirements (including quality requirements), and the architect restates quality requirements as scenarios, picks drivers and records the constraints. Related: [[Gates as Checkpoints Without Documents]].
