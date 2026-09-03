---
type: concept
title: "Open Knowledge Format"
complexity: intermediate
domain: knowledge-management
aliases:
  - "OKF"
  - "OKF bundle"
  - "OKF visualizer"
created: 2026-09-03
updated: 2026-09-03
tags:
  - concept
  - okf
  - knowledge-format
  - wiki-sharing
  - viewer
  - google-cloud
status: current
related:
  - "[[Wiki Sharing Patterns]]"
  - "[[wiki-sharing-research]]"
  - "[[LLM Wiki Pattern]]"
  - "[[Hot Cache]]"
  - "[[Google ADK]]"
sources:
  - "[[okf-spec-and-reference-repo]]"
  - "[[google-cloud-okf-announcement]]"
---

# Open Knowledge Format (OKF)

Google Cloud's open, vendor-neutral spec (announced 2026-06-12) for packaging knowledge as a directory of markdown files with YAML frontmatter, one file per concept, cross-linked with ordinary markdown links. `type` is the only required field. A bundle "is a directory" — ship it as a git repo, tarball, or subdirectory; no SDK, database, or account needed to read or write it (Source: [[google-cloud-okf-announcement]], [[okf-spec-and-reference-repo]]). It formalizes the same pattern this vault already follows ([[LLM Wiki Pattern]]): the plugin's `okf_export.py` renders the wiki as a bundle mechanically.

## The "preview": a single-file graph viewer

The preview the operator remembers is the reference **visualizer** — `reference_agent visualize` in the canonical repo. It renders any bundle into one self-contained HTML file: the bundle is embedded as JSON, Cytoscape.js draws the graph, `marked` renders the markdown (both from a CDN). "No backend, no install on the viewing side, no data leaves the page." Open it locally, host it on any static file server, or commit it next to the bundle (Source: [[okf-spec-and-reference-repo]], [[google-cloud-okf-announcement]]).

What a human can do in it (high confidence):

| Confluence expectation | OKF visualizer |
|---|---|
| Page tree | No tree. A force-directed graph of concepts coloured by `type`, plus the bundle's `index.md` files (one-level directory listings) |
| Search | Search box over title, concept id, tags — not full text |
| Backlinks | Yes — "Cited by" panel computed from the reverse link graph |
| Page view | Detail panel: frontmatter + rendered markdown; internal links navigate inside the viewer |
| Permissions | None — whoever has the HTML file sees the whole bundle |
| Editing, comments, history | None; read-only snapshot of the bundle at render time |
| Offline / air-gapped | Content yes; the CDN-loaded libraries need network unless inlined |

The repo calls it "a proof-of-concept consumer of OKF, mirroring the way a reference agent is a proof-of-concept producer." It is a graph explorer for one bundle, not a documentation site.

## The hosted path: Knowledge Catalog (agent-facing)

The only Google product that consumes OKF is **Knowledge Catalog** (Dataplex Universal Catalog, renamed 2026-04-10): "updated... to be able to ingest Open Knowledge Format and serve it to our agents." A follow-up post describes the push: a one-time `gcloud dataplex` setup registers an EntryGroup, an EntryType `okf-bundle`, and an AspectType `okf`; `kcmd` (the Metadata-as-Code CLI) pushes the bundle so each concept becomes a catalog entry under standard IAM — readers need `roles/dataplex.catalogViewer` for `entries.get`, `LookupContext`, and search (medium confidence: search summaries, not fetched; Source: [[google-cloud-okf-announcement]]).

So the permission model exists only on the Google Cloud side, and what it gates is *agent lookup and catalog search* (Knowledge Catalog powers the Deep Research Agent preview in Gemini Enterprise). Neither post describes a human wiki-reading experience for a pushed bundle beyond the ordinary catalog console. No Agentspace, NotebookLM, or GitHub-hosted preview was found.

## Humans or agents?

Both by charter — "agent- and human-friendly," "readable by humans without tooling," "an engineer can `cat` a concept; an LLM can ingest it verbatim into context" — but the tooling and the v0.2 additions are agent-first: the producer is a BigQuery enrichment agent, the consumer story is "serve it to our agents," and the trust fields (`generated`, `verified`, `status`, `stale_after`) exist because "when most concepts are machine-generated, a consumer needs answers" about who verified what. Trust tiers — unverified / machine-confirmed / human-reviewed — are "advisory signals, not access control" (Source: [[okf-spec-and-reference-repo]]). Human readability here means "renders on GitHub, opens in any editor", not "navigable like Confluence".

## What a bundle needs to render

- `type` on every concept; `title`, `description`, `resource`, `tags` recommended.
- Standard markdown links (no wikilinks); bundle-relative absolute paths (`/concepts/x.md`) recommended; "consumers MUST tolerate broken links."
- `index.md` (directory listing) and `log.md` (chronological history) are reserved names, not concepts; consumers may synthesize `index.md`.
- Unknown `type` values are treated as generic concepts — the vault's `question`, `comparison`, `requirement` types are fine.

## Maturity (as of 2026-09-03)

- v0.1 launched 2026-06-12 as "a starting point, not a finished standard"; the spec is now v0.2 in a new canonical repo, `GoogleCloudPlatform/open-knowledge-format`. The `okf/` directory in `knowledge-catalog` is "a frozen snapshot, no longer maintained."
- No release tags, undated SPEC, six commits at fetch time, Apache-2.0, stewarded by Google Cloud's data-analytics org — early and single-vendor despite the "open" framing.

## Relevance to adlc

1. **Retarget the exporter.** `skills/wiki/scripts/okf_export.py` cites the frozen `knowledge-catalog/okf` path and v0.1; it writes `timestamp` (a v0.1 example field, absent from the v0.2 field list), emits relative links (allowed, but bundle-relative absolute is the recommended form), and has no handling for v0.2 `generated`/`verified`/`status`. A v0.2 pass would map `created`/`updated` → `generated.at`, the vault's `status` vocabulary (developing/current/mature/evergreen/implemented) → `draft | stable | deprecated`, and stamp `generated.by: adlc/<version>`.
2. **Reserved names.** The vault's root `index.md` and `log.md` coincide with OKF's reserved files and carry the matching semantics — a free win — but the per-folder `_index.md` files are exported as ordinary concepts; they should become `index.md` in the bundle.
3. **Sharing verdict.** For the parent question ([[Wiki Sharing Patterns]]), OKF gives a *read-only graph snapshot* a person can open from one HTML file, and an *agent-facing* governed store on Google Cloud. It does not provide a page tree, editing, comments, or permissions for people. Keep it as the inter-team interchange tier; people-facing navigation needs a docs site or an Obsidian-native sharing option ([[wiki-sharing-research]]).

> [!gap]
> Not verified: whether the visualizer handles bundles of ~100+ pages usably, whether it renders the v0.2 trust tiers, whether the Knowledge Catalog console offers a bundle browsing view for humans, and whether Gemini Enterprise / NotebookLM can import a bundle directly. The Knowledge Catalog follow-up post and IAM docs were not fetched.

## Connections

- [[okf-spec-and-reference-repo]] — spec v0.2 details and the visualizer's feature list
- [[google-cloud-okf-announcement]] — launch positioning and the Knowledge Catalog ingest path
- [[Wiki Sharing Patterns]] — the vault's sharing tiers; OKF is the inter-team interchange tier
- [[LLM Wiki Pattern]] — the pattern OKF standardizes
- [[Google ADK]] — the same vendor's agent framework; a Knowledge Catalog-served bundle is the natural context source for ADK agents
