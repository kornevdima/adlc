---
type: source
title: "How the Open Knowledge Format can improve data sharing (Google Cloud launch post)"
source_type: blog
author: "Sam McVeety (Tech Lead, Data Analytics) and Amir Hormati (Tech Lead, BigQuery), Google Cloud"
date_published: 2026-06-12
url: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
created: 2026-09-03
updated: 2026-09-03
confidence: high
tags:
  - source
  - blog
  - okf
  - knowledge-catalog
  - google-cloud
  - wiki-sharing
status: current
related:
  - "[[Open Knowledge Format]]"
  - "[[okf-spec-and-reference-repo]]"
  - "[[Wiki Sharing Patterns]]"
  - "[[wiki-sharing-research]]"
key_claims:
  - "OKF is 'a vendor-neutral, agent- and human-friendly standard' — 'readable by humans and parseable by agents: the same file, no translation layer'"
  - "'OKF v0.1 is a starting point, not a finished standard'; the reference agent and visualizer are 'proofs of concept, deliberately'"
  - "The preview is 'a static HTML visualizer that turns any OKF bundle into an interactive graph view in a single self-contained file; no backend, no install on the viewing side, no data leaves the page'"
  - "'We have also updated Google Cloud's Knowledge Catalog to be able to ingest Open Knowledge Format and serve it to our agents' — the hosted path is agent-facing"
  - "A follow-up post describes pushing a bundle into Knowledge Catalog via gcloud dataplex + kcmd, where each concept becomes an entry governed by standard IAM (readers need roles/dataplex.catalogViewer)"
  - "The launch post does not address permissions, a human-facing catalog UI for bundles, or Gemini Enterprise / NotebookLM consumption"
---

# Source: How the Open Knowledge Format can improve data sharing

**Authors**: Sam McVeety, Amir Hormati (Google Cloud) | **Date**: 2026-06-12 | **Fetched**: 2026-09-03
**Follow-up (not fetched, medium confidence)**: *Scale OKF bundles across an organization with Knowledge Catalog* — `cloud.google.com/blog/products/data-analytics/scale-okf-bundles-across-an-organization-with-knowledge-catalog` (undated in search results)

## Summary

The launch post for the [[Open Knowledge Format]]. Google positions OKF as "a vendor-neutral, agent- and human-friendly standard for representing the metadata, context, and curated knowledge that modern AI systems need." The pitch is that the same markdown file is "readable by humans and parseable by agents... no translation layer": "Just markdown — readable in any editor, renderable on GitHub, indexable by any search tool" and "Just files — shippable as a tarball, hostable in any git repo, mountable on any filesystem." No SDK, database, or proprietary account is needed to read or write a bundle.

The v0.1 frontmatter example is catalog-shaped: `type: BigQuery Table`, `title`, `description`, `resource` (a BigQuery console URL), `tags`, `timestamp`. The design centre is dataset metadata, with prose knowledge as a generalization (Source: this post; spec details in [[okf-spec-and-reference-repo]]).

## What ships with it

Two reference implementations, both "proofs of concept, deliberately":

- **Producer** — an enrichment agent that "walks a BigQuery dataset, drafts an OKF concept document for every table and view, then runs a second LLM pass that crawls authoritative documentation and enriches each concept with citations, schemas, and join paths."
- **Consumer / the "preview"** — "a static HTML visualizer that turns any OKF bundle into an interactive graph view in a single self-contained file; no backend, no install on the viewing side, no data leaves the page." Three sample bundles (GA4 e-commerce, Stack Overflow, Bitcoin public datasets) are provided to browse.

"The agent demonstrates one way to produce OKF; nothing about the format requires a specific agent framework or LLM."

## The hosted path: Knowledge Catalog

"We have also updated Google Cloud's Knowledge Catalog to be able to ingest Open Knowledge Format and serve it to our agents." Knowledge Catalog is the April 2026 rename of Dataplex Universal Catalog — a Gemini-powered catalog that "builds a dynamic context graph that grounds AI agents in enterprise truth" and powers the Deep Research Agent (preview) in Gemini Enterprise (Google Cloud docs and product page via search, 2026; medium confidence — not fetched).

The follow-up post (search summary only) describes the mechanics: a one-time setup registers an **EntryGroup** for the bundle, an **EntryType** `okf-bundle`, and an **AspectType** `okf` carrying the OKF signal fields; wrappers call `gcloud dataplex` for setup and delegate the push to `kcmd`, the Metadata-as-Code CLI in the knowledge-catalog repo. Governance is "standard Knowledge Catalog IAM" on the EntryGroup; reading agents need `roles/dataplex.catalogViewer` (`entries.get`, `LookupContext`, search). Third-party coverage summarized it as turning "a 9-concept OKF bundle into 17 access-controlled catalog entries" (ppc.land, 2026; low-medium confidence).

What this means for people: the permission model exists only on the Google Cloud side, and it governs *agent* lookups and catalog search; neither post describes a human wiki-style reading experience for a pushed bundle beyond the ordinary Knowledge Catalog console.

## Maturity

"OKF v0.1 is a starting point, not a finished standard." The launch was 2026-06-12; by 2026-09 the canonical repo had moved and the spec was at v0.2 ([[okf-spec-and-reference-repo]]). Announced as an open spec, but stewardship sits with Google Cloud's data-analytics org; no foundation or multi-vendor governance is mentioned.

> [!gap]
> Permissions, a human catalog UI for bundles, and NotebookLM / Gemini Enterprise consumption of OKF are not covered by the launch post. The follow-up post and the Knowledge Catalog docs were not fetched (budget) — the IAM details above are from search summaries.

## Connections

- [[Open Knowledge Format]] — concept synthesis (viewer, hosting, humans vs agents, implications for the vault exporter)
- [[okf-spec-and-reference-repo]] — the spec and tooling this post announces
- [[Wiki Sharing Patterns]] — the parent question: sharing the vault with people, Confluence-style
- [[wiki-sharing-research]] — earlier survey of Obsidian Publish / Sync / docs-as-code options
