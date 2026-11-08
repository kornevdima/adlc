---
type: concept
title: "Project Within a Larger System"
confidence: medium
created: 2026-11-08
updated: 2026-11-08
sources: ["[[backstage-system-model]]", "[[backstage-descriptor-format]]", "[[fowler-bounded-context]]", "[[contextmapper-context-map]]", "[[redhat-golden-paths]]"]
tags: [architecture, catalog, team-topologies, c4, ddd, golden-path]
---

# Project within a larger system

A project is placed among others by four records: a diagram of where it sits, a record of who it depends on and how, a catalog entry that names owner and system, and shared standards it inherits. Each can live as Markdown or YAML in the wiki and git, so an agent can read it.

## 1. Where it sits: C4

C4 (c4model.com) has system context and container diagrams per system, and a supplementary system landscape diagram. The landscape diagram is a context diagram with no single system as focus: it maps the people and systems in an enterprise, organisation or department, for technical and non-technical readers, and is recommended for larger organisations (Source: https://c4model.com/diagrams/system-landscape, undated, confidence medium). Use context to show neighbours of this project, container to show its deployable parts and data stores, landscape for the whole portfolio.

## 2. Dependencies between teams: Team Topologies

Three interaction modes: collaboration (joint work, short, for discovery), X-as-a-Service (consume an API or tool with minimal contact, once the boundary is stable), facilitating (an enabling team helps another adopt something, temporary). Modes should change over time, with exit criteria and timeframes; X-as-a-Service is judged by adoption, not API count (Source: teamtopologies.com newsletter, Feb 2025, seen in search results only, confidence medium). Record each dependency as a row: upstream, downstream, mode, expected end date.

SAFe's program board and dependency board record the same thing per planning increment. Not fetched; confidence low.

## 3. Catalog: who owns what

The Backstage model gives Component, API, Resource, System, Domain, plus Group and User (Source: [[backstage-system-model]]). Each entity is a small YAML descriptor with `apiVersion`, `kind` and `metadata.name`, kept in the repository, with the portal as the index (Source: [[backstage-descriptor-format]]).

Which kinds carry which fields (Source: [[backstage-descriptor-format]]):

- `owner` is required on Component, API, Resource, System and Domain. It is a reference to a Group or User, "the singular entity (commonly a team) that bears ultimate responsibility", and is for display, not authorization. Group and User have no owner.
- Component adds `system`, `providesApis`, `consumesApis`, `dependsOn` (Components or Resources) and `dependencyOf`, plus required `type` and `lifecycle` (experimental, production, deprecated).
- API and Resource may name a `system`. System may name a `domain`. Domain may name a parent with `subdomainOf`.
- Group carries `children`, `parent` and `members`; User carries `memberOf`. That is how teams hang under business units.

So the four facts a portfolio index needs, owner, system, APIs and dependencies, are all first-class fields. Confidence high for the format, as read from the primary page. Cross-repo documentation links then go through the catalog entry, not through copied paths. The vault side of this is [[Cross-Repo Wiki Access]].

## 4. Domain boundaries: bounded contexts

Record each service's bounded context and a context map of the relations between contexts (Source: [[fowler-bounded-context]]). Align a context with one team where possible, since language and culture set the boundary.

The relationship types for the map (Source: [[contextmapper-context-map]]):

- Symmetric: Partnership and Shared Kernel. No upstream or downstream.
- Upstream-Downstream: the upstream influences the downstream, never the reverse.
- Customer-Supplier: the same, but the downstream priorities factor into upstream planning.
- Upstream roles: Open Host Service and Published Language. Downstream roles: Conformist and Anticorruption Layer.

Add a relationship column to the dependency table from section 2: team mode says how the teams work together, the context-map type says who bends to whom. Confidence medium: the source names the roles but defines only the asymmetric forms. The definitions of Conformist, Anticorruption Layer and the rest are standard DDD vocabulary not yet sourced in the wiki.

## 5. Shared standards

A golden path is "an opinionated, well-documented, and supported way of building and deploying software". Platform engineers create and maintain it. It bundles templates, infrastructure modules, build and deploy pipelines, observability and security scans, and it should be optional so teams can leave it when they have reason (Source: [[redhat-golden-paths]]). It lives in an internal developer platform as self-service. A project inherits it by starting from the template, and records the departures.

This is the X-as-a-Service mode of section 2 applied to a platform team: the path is consumed with minimal contact and judged by adoption. The Backstage templates page describes scaffolding only (skeleton code, input variables, publishing to a code host) and never defines golden paths or names an owner, so the definition and the ownership claim rest on one vendor explainer. Confidence medium. Handbooks and architecture principles remain unsourced.

## For this plugin

Each project's wiki should carry: a context diagram, a dependency table with interaction mode and context-map relationship, a catalog descriptor naming owner and system, and a bounded-context note. The portfolio index sits one level above the projects. Standards arrive as a golden-path template the project starts from, and a note of where it departed.
