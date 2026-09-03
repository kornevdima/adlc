---
type: source
title: "Open Knowledge Format — canonical spec repo (v0.2) and reference visualizer"
source_type: repository
author: "Google Cloud Platform (GoogleCloudPlatform/open-knowledge-format)"
date_published: 2026-06
url: https://github.com/GoogleCloudPlatform/open-knowledge-format
created: 2026-09-03
updated: 2026-09-03
confidence: high
tags:
  - source
  - repository
  - okf
  - knowledge-format
  - wiki-sharing
  - viewer
status: current
related:
  - "[[Open Knowledge Format]]"
  - "[[google-cloud-okf-announcement]]"
  - "[[Wiki Sharing Patterns]]"
  - "[[wiki-sharing-research]]"
  - "[[LLM Wiki Pattern]]"
key_claims:
  - "The canonical home of the spec is GoogleCloudPlatform/open-knowledge-format; the okf/ directory in knowledge-catalog is 'a frozen snapshot, no longer maintained, and anything built against it will drift out of date'"
  - "Spec is at v0.2: `type` is the only required field; title/description/resource/tags recommended; v0.2 adds trust fields generated, verified, status (draft|stable|deprecated), stale_after"
  - "index.md and log.md are reserved filenames (directory listing, chronological history) and must not be concept documents"
  - "The only viewer is `reference_agent visualize`: a self-contained HTML file with a Cytoscape.js force-directed graph, a detail panel rendering the markdown, 'Cited by' backlinks, search over title/id/tags, and a type filter"
  - "Both reference tools (enrich agent, visualizer) are explicitly proofs of concept; the format is 'human- and agent-readable' with no SDK between reader and content"
  - "Trust tiers (unverified / machine-confirmed / human-reviewed) are 'advisory signals, not access control'; the spec has no permission model"
---

# Source: Open Knowledge Format — spec repo and reference visualizer

**Publisher**: Google Cloud Platform GitHub org | **License**: Apache-2.0 | **Fetched**: 2026-09-03 (repo README + `SPEC.md`; the SPEC carries no date of its own — `date_published` above is the June 2026 announcement month, see [[google-cloud-okf-announcement]])
**Related URLs**: frozen original at `github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf`; spec at `github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md`

## Summary

The canonical repository for the Open Knowledge Format ([[Open Knowledge Format]]). OKF is "a universal, vendor-neutral format for representing knowledge as plain markdown files with YAML frontmatter", organized in a directory hierarchy. The repo holds the v0.2 spec, sample bundles, and a Python `reference_agent` module with two subcommands: `enrich` (produces bundles from BigQuery metadata plus optional web sources) and `visualize` (renders any bundle to interactive HTML). The README frames both as proofs of concept: the agent shows "one way to produce OKF"; the visualizer is "a proof-of-concept consumer of OKF, mirroring the way a reference agent is a proof-of-concept producer."

The repo move matters: the `okf/` directory inside `GoogleCloudPlatform/knowledge-catalog` — the path this plugin's exporter targets — now says "Stop using the copy under okf/ in this repository. It is a frozen snapshot, no longer maintained."

## The visualizer (the "preview")

`visualize` emits one self-contained HTML file: the bundle is serialized as a JSON blob inside the page; Cytoscape.js draws the graph and `marked` renders markdown, both loaded from a CDN. What a human gets:

- a force-directed graph of every concept, nodes coloured by `type`, directed edges from each cross-link;
- a detail panel showing frontmatter and the rendered markdown body, with internal links rewired to navigate inside the viewer;
- a "Cited by" backlinks list computed from the reverse link graph;
- a search box matching title, concept id, and tags; a type filter; switchable layouts (cose / concentric / breadth-first / circle / grid).

It can be "opened in any modern browser, shared as an artifact, hosted on a static file server, or committed next to the bundle." There is no backend, no auth, no editing, no comments, and no page tree beyond the bundle's `index.md` files.

## Spec v0.2 essentials (what a bundle needs)

- **Frontmatter**: `type` required ("a short string identifying the kind of concept"). Recommended: `title`, `description` (one sentence), `resource` (URI of the underlying asset), `tags`. Optional families: provenance (`sources[]` with `id`/`resource`/`title`/`author`/`usage_count`/`last_modified`, `usage_window`), trust (`generated: {by, at}`, `verified: [{by, at}]`), lifecycle (`status: draft | stable | deprecated`, absent = stable; `stale_after` ISO instant), and an *Attested Computation* type with `runtime`/`parameters`/`computation`/`executor`/`attester`.
- **Layout**: flat directory, optional subdirectories, each may hold an `index.md` (directory listing) and the root a `log.md` (chronological history). Both names are reserved. "Consumers MAY generate `index.md` automatically" or synthesize one on the fly. Auto-generated `index.md` files "let an agent or human navigate the hierarchy one level at a time."
- **Links**: standard markdown links only (no wikilinks). Bundle-relative absolute paths (`/dir/concept.md`) are "the recommended form because it is stable when documents are moved"; ordinary relative paths also allowed. "Consumers MUST tolerate broken links."
- **Distribution**: git repository (recommended), tarball, or a subdirectory of a larger repo. "A bundle is a directory."
- **Actors**: `human:<id>` for people, `<producer>/<version>` for agents, `process:<id>` for automation. Trust tiers derive from `verified`: none → unverified; non-human only → machine-confirmed; any `human:` → human-reviewed. "Trust tiers are advisory signals, not access control."
- **Tolerance**: consumers MUST treat unknown `type` values as generic concepts and consume best-effort when the version is unknown.

## Audience

"Human- and agent-readable. No SDK or query language stands between a reader and the content. An engineer can `cat` a concept; an LLM can ingest it verbatim into context." The spec's own framing: "authored by people, generated by agents, exchanged across organizations, and consumed by both." The trust fields exist because "when most concepts are machine-generated, a consumer needs answers" about verification and freshness — i.e. the default assumption is agent-written, human-reviewed content.

## Maturity

No release tags visible; the repo showed six commits when fetched. The README calls the visualizer and enrichment agent proofs of concept; the announcement post calls v0.1 "a starting point, not a finished standard" ([[google-cloud-okf-announcement]]). Named export sources are catalogs (Dataplex, Unity Catalog, Collibra) — the design centre is data-catalog metadata, not prose wikis.

> [!gap]
> The SPEC is undated and the repo has no changelog; the v0.1 → v0.2 transition date is unknown. Whether the visualizer is expected to keep pace with the spec (e.g. render trust tiers) was not stated.

## Connections

- [[Open Knowledge Format]] — the concept page that synthesizes this source with the product side
- [[google-cloud-okf-announcement]] — the June 2026 launch post and the Knowledge Catalog ingest path
- [[Wiki Sharing Patterns]] — where the OKF bundle sits among the vault's sharing tiers
- [[LLM Wiki Pattern]] — OKF formalizes the same markdown-plus-frontmatter, one-file-per-concept pattern
