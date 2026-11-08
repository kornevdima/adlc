---
type: source
source_type: documentation
title: "Backstage System Model"
author: Backstage project (Spotify, CNCF)
date_published: undated (footer 2026)
url: https://backstage.io/docs/features/software-catalog/system-model
confidence: medium
key_claims:
  - "The catalog models software as Component, API, Resource, System and Domain, plus Group and User for people."
  - "A System is an optional grouping of components and resources that exposes public APIs and hides the rest."
  - "A Domain is an optional grouping of systems that share terminology, models or business purpose."
  - "Components implement and consume APIs and depend on other components and resources."
tags: [catalog, ownership, system-model]
---

# Backstage system model

Primary documentation, undated, so confidence is medium. The fetched page does not describe the `owner` field, `spec.system` or `dependsOn` by name. Those come from the next documentation page (YAML file format) and from third-party write-ups that were not fetched.

## What it says

- Component: one piece of software (web site, backend service, data pipeline).
- API: the boundary between components; the main way to discover what a component offers.
- Resource: runtime infrastructure such as a database, topic or bucket.
- System: optional grouping of components and resources that exposes public APIs; its internals stay hidden from consumers.
- Domain: optional grouping of systems.
- Group and User: the organizational entities (teams, business units, people).

## Why it matters here

A catalog answers "who owns this, what is it part of, what does it depend on" in one place, one descriptor per component kept next to the code. That is the index across projects. See [[Project Within a Larger System]].
