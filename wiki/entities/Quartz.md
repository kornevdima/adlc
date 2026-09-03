---
type: entity
title: "Quartz"
entity_type: product
created: 2026-09-03
updated: 2026-09-03
confidence: medium
tags:
  - entity
  - tool
  - static-site
  - obsidian
  - digital-garden
status: current
related:
  - "[[obsidian-vault-site-generators]]"
  - "[[obsidian-static-publishers-comparison]]"
  - "[[Obsidian Vault Portability]]"
  - "[[Vault Publishing Topologies]]"
  - "[[Wiki Sharing Patterns]]"
---

# Quartz

Open-source static-site generator by Jacky Zhang (jackyzha0) built specifically to publish Obsidian vaults as browsable websites ("digital gardens"). Version 3 was a Hugo theme; **v4** is a from-scratch Node.js rewrite with JSX components, aimed at being usable by non-technical people while staying extensible for developers (Source: [[obsidian-vault-site-generators]]). The current release is **v5.0.0 (2026-06-11)**, per the official homepage; MIT-licensed; deploys to GitHub Pages, Cloudflare Pages, Netlify or Vercel, rebuilding from the vault repo on push — which is what lets agent commits reach readers without a human re-publishing (Source: [[obsidian-static-publishers-comparison]]; see [[Vault Publishing Topologies]]).

> [!note] Two research passes, one page
> Q2 fetched the homepage (v5.0.0); Q3 worked from search summaries that still describe "Quartz 4" as current. Treat v4 feature descriptions below as the baseline and v5 as the release to pilot — the v5 changelog was not fetched.

## What it does out of the box

- Understands Obsidian syntax natively — wikilinks, aliases, callouts — through its own Markdown transformer, so a vault publishes without a bridge plugin.
- Default page layout includes **Explorer** (folder tree), **Breadcrumbs**, **Search** (full text) and **Darkmode** components — the closest single-tool match to Confluence-style navigation among the generators surveyed.
- Documented GitHub Pages workflow: push to the `v4` branch, an Actions workflow builds and deploys.
- Content lives in a `content/` folder; exclusions go in `ignorePatterns` in the config (medium confidence — not fetched this session).

## Limits

No docs versioning, no built-in auth (static output; access control is the hosting layer), single-author defaults, and it is a garden tool rather than a docs framework — no equivalent of MkDocs' TechDocs integration or Docusaurus' versioned docs. `index.md` (not `_index.md`) is the folder page, so a vault with `_index.md` sub-indexes needs a build-time copy step (see [[Obsidian Vault Portability]]).

## Maintenance

Active releases page; multiple independent how-to guides dated 2025 (August, December); widest adoption of the Obsidian-publishing tools found. Medium confidence — based on search-result summaries, not a fetched changelog.

> [!gap] Not verified: what changed in v5.0.0 (callouts, Explorer, dot-folder and `_index.md` defaults), transclusion (`![[note]]`) support depth, and how custom callout types such as `[!gap]` render. A pilot build on a 20-page vault slice would settle these.

## Connections

- [[obsidian-vault-site-generators]] | [[obsidian-static-publishers-comparison]] | [[Obsidian Vault Portability]] | [[Vault Publishing Topologies]] | [[Wiki Sharing Patterns]]
