---
type: concept
title: "Project Within a Larger System"
confidence: medium
sources: ["[[backstage-system-model]]", "[[fowler-bounded-context]]"]
tags: [architecture, catalog, team-topologies, c4, ddd]
---

# Project within a larger system

A project is placed among others by four records: a diagram of where it sits, a record of who it depends on and how, a catalog entry that names owner and system, and shared standards it inherits. Each can live as Markdown or YAML in the wiki and git, so an agent can read it.

## 1. Where it sits: C4

C4 (c4model.com) has system context and container diagrams per system, and a supplementary system landscape diagram. The landscape diagram is a context diagram with no single system as focus: it maps the people and systems in an enterprise, organisation or department, for technical and non-technical readers, and is recommended for larger organisations (Source: https://c4model.com/diagrams/system-landscape, undated, confidence medium). Use context to show neighbours of this project, container to show its deployable parts and data stores, landscape for the whole portfolio.

## 2. Dependencies between teams: Team Topologies

Three interaction modes: collaboration (joint work, short, for discovery), X-as-a-Service (consume an API or tool with minimal contact, once the boundary is stable), facilitating (an enabling team helps another adopt something, temporary). Modes should change over time, with exit criteria and timeframes; X-as-a-Service is judged by adoption, not API count (Source: teamtopologies.com newsletter, Feb 2025, seen in search results only, confidence medium). Record each dependency as a row: upstream, downstream, mode, expected end date.

SAFe's program board and dependency board record the same thing per planning increment. Not fetched; confidence low.

## 3. Catalog: who owns what

The Backstage model gives Component, API, Resource, System, Domain, plus Group and User (Source: [[backstage-system-model]]). The useful fields are owner, system membership and dependencies, kept in a descriptor in each repository, with the portal as the index. Those fields come from third-party summaries, not the fetched page (confidence low). Cross-repo documentation links then go through the catalog entry, not through copied paths. The vault side of this is [[Cross-Repo Wiki Access]].

## 4. Domain boundaries: bounded contexts

Record each service's bounded context and a context map of the relations between contexts (Source: [[fowler-bounded-context]]). Align a context with one team where possible, since language and culture set the boundary.

## 5. Shared standards

Handbooks, architecture principles, golden paths and platform teams were not fetched in this pass. The platform-team pattern is the X-as-a-Service mode above. Confidence low.

## For this plugin

Each project's wiki should carry: a context diagram, a dependency table with interaction modes, a catalog descriptor naming owner and system, and a bounded-context note. The portfolio index sits one level above the projects.
