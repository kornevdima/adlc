---
type: source
source_type: documentation
title: "Backstage Descriptor Format"
author: Backstage project (Spotify, CNCF)
date_published: undated (fetched 2026-11-08)
url: https://backstage.io/docs/features/software-catalog/descriptor-format
confidence: high
key_claims:
  - "Every descriptor has apiVersion, kind and metadata.name; core kinds are Component, API, Group, User, Resource, System, Domain, Location and Template."
  - "owner is required on Component, API, Resource, System and Domain, and is an entity reference to a Group or User; it is for display, not authorization."
  - "A Component can name its system, the APIs it provides and consumes, and what it depends on (Components or Resources)."
  - "A System can name its domain; a Domain can name a parent domain."
  - "Group has no owner; it carries type, parent, children and members. User carries memberOf."
tags: [catalog, ownership, descriptor]
---

# Backstage descriptor format

Primary documentation, read directly. It supplies the field-level detail that [[backstage-system-model]] left out.

## Envelope

Every entity file carries `apiVersion` (the `backstage.io/` prefix, alpha or beta versions may still change), `kind`, and `metadata.name` (unique per kind within a namespace, 1 to 63 characters). `metadata.annotations` are optional key/value strings, often pointers to external systems; the `backstage.io/` prefix is reserved.

## The owner field

`owner` is an entity reference, usually a Group or User, naming "the singular entity (commonly a team) that bears ultimate responsibility" for the entity. It is for display only, not runtime authorization.

## Fields by kind

- Component: `type` and `lifecycle` and `owner` required. Optional `system`, `subcomponentOf`, `providesApis`, `consumesApis`, `dependsOn` and `dependencyOf` (Components or Resources). Lifecycle values are experimental, production, deprecated.
- API: `type`, `lifecycle`, `owner`, `definition` required; `system` optional. Types include openapi, asyncapi, graphql, grpc.
- Resource: `type` and `owner` required; `system`, `dependsOn`, `dependencyOf` optional.
- System: `owner` required; `domain` optional; `type` optional (product, service, feature-set).
- Domain: `owner` required; `subdomainOf` optional.
- Group: no owner; `type`, `children` required; `parent`, `members`, `profile` optional.
- User: `memberOf` required; `profile` optional.

## Doc inconsistency

The Template kind's heading says `owner` is optional while its text says the field is required.

## Why it matters here

The descriptor is a small file kept in each repository. Owner, system, API provision and dependencies are the four facts a portfolio index needs. See [[Project Within a Larger System]].
