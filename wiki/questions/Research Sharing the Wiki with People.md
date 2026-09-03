---
type: synthesis
title: "Research: Sharing the Wiki with People"
created: 2026-09-03
updated: 2026-09-03
tags:
  - research
  - sharing
  - publishing
  - okf
  - confluence
  - github
status: developing
related:
  - "[[Wiki Sharing Patterns]]"
  - "[[Open Knowledge Format]]"
  - "[[Vault Publishing Topologies]]"
  - "[[Obsidian Vault Portability]]"
  - "[[One-Way Publish vs Round-Trip Wiki Sync]]"
  - "[[Cross-Repo Wiki Access]]"
  - "[[Quartz]]"
  - "[[obsidian-static-publishers-comparison]]"
  - "[[obsidian-vault-site-generators]]"
  - "[[git-backed-wiki-platforms-comparison]]"
  - "[[kovetskiy-mark-readme]]"
  - "[[github-docs-markdown-wikis-pages]]"
  - "[[claude-code-large-codebases-docs]]"
  - "[[okf-spec-and-reference-repo]]"
  - "[[google-cloud-okf-announcement]]"
sources:
  - "[[okf-spec-and-reference-repo]]"
  - "[[google-cloud-okf-announcement]]"
  - "[[obsidian-static-publishers-comparison]]"
  - "[[obsidian-vault-site-generators]]"
  - "[[git-backed-wiki-platforms-comparison]]"
  - "[[kovetskiy-mark-readme]]"
  - "[[github-docs-markdown-wikis-pages]]"
  - "[[claude-code-large-codebases-docs]]"
---

# Research: Sharing the Wiki with People

Navigation: [[index]] | [[Wiki Sharing Patterns]] (May 2026 pass: Obsidian Sync / Relay / Publish, docs-as-code topologies, Backstage)

## Overview

The operator's constraint is fixed: the git repo of Obsidian-flavoured Markdown stays the source of truth, agents already read and write it across repos, and people should be able to navigate it the way they navigate Confluence — page tree, search, backlinks, permissions. Five questions were researched in parallel (OKF preview; Obsidian-native publishers; docs-as-code generators; git-fed team wikis; GitHub's own surfaces plus cross-repo agent access). The result splits cleanly along one axis: **where the publish is triggered from**. Routes that rebuild from the repo on push keep agent commits live for readers with no human in the loop; routes pushed from an app or imported by hand do not ([[Vault Publishing Topologies]]). No route outside Obsidian itself speaks the vault's dialect natively, so every one needs a small "lowering" step for `[[wikilinks]]`, callouts and `_index.md` — a step the plugin's OKF exporter already half-implements ([[One-Way Publish vs Round-Trip Wiki Sync]], [[Obsidian Vault Portability]]).

## Key Findings

- **The OKF "preview" is a proof of concept, not a wiki.** `reference_agent visualize` renders a bundle into one self-contained HTML file: a Cytoscape concept graph, a rendered-markdown detail panel, "Cited by" backlinks, title/id/tag search, a type filter. No backend, no auth, no page tree, no editing. The only hosted consumer is Google Cloud Knowledge Catalog (Dataplex renamed, 2026-04), which ingests bundles into IAM-governed entries to serve *agents*, not a human UI. (Source: [[okf-spec-and-reference-repo]], [[google-cloud-okf-announcement]]; high)
- **Our exporter targets a frozen path.** OKF moved to v0.2 in `GoogleCloudPlatform/open-knowledge-format` (2026-06-12); the `knowledge-catalog/okf` directory that `skills/wiki/scripts/okf_export.py` cites is "a frozen snapshot, no longer maintained". v0.2 replaces `timestamp` with `generated` / `verified` / `status` / `stale_after` and reserves `index.md` per folder. (Source: [[okf-spec-and-reference-repo]]; high) → plugin follow-up, see Open Questions.
- **Quartz is the one tool that ships Confluence-style navigation with no plugin.** Folder explorer, breadcrumbs, full-text search, backlinks, graph, dark mode, wikilinks with aliases, callouts; v5.0.0 released 2026-06-11, MIT, builds from the vault repo on push to GitHub Pages / Cloudflare / Netlify / Vercel. Works on the repo as-is given an ignore list for `.raw/` and a build-time copy of `_index.md` → `index.md`. (Source: [[obsidian-static-publishers-comparison]], [[obsidian-vault-site-generators]]; high on features, medium on v5 changes)
- **Of the five Obsidian publishers only two are repo-triggered.** Quartz and Flowershow rebuild on push; Digital Garden and Obsidian Publish ($8/mo annual, $10 monthly, site-wide password only) are pushed from the Obsidian app, so agent commits reach readers only after a human re-publishes; Perlite live-renders a checkout via PHP. None has per-folder permissions — auth is a fronting layer (Cloudflare Access, SSO proxy). (Source: [[obsidian-static-publishers-comparison]]; high for Quartz / Digital Garden / Publish, medium Perlite, low Flowershow)
- **Docs-as-code generators all need a bridge, and MDX bites.** MkDocs + Material needs `mkdocs-obsidian-bridge` plus a callouts extension; Astro Starlight needs `starlight-obsidian` (active); Docusaurus' bridge is unproven (1 star); Hugo needs a pre-export rewrite. Docusaurus and Astro silently drop `_`-prefixed files (`_index.md`) and fail builds on bare `<` or `{` in prose; the custom `[!gap]` callout is outside every mapped set. Versioning "as on Confluence" is git history on all of them; private access is a hosting decision. (Source: [[obsidian-vault-site-generators]]; medium, doc-derived)
- **Only Wiki.js and GitBook sync with git natively, and both round-trip by default.** Wiki.js's git storage module can be set pull-only (2.x maintained, 3.0 stalled); GitBook Git Sync is bidirectional on every plan. Docmost, Outline and BookStack accept markdown only as one-shot imports with no sync memory. (Source: [[git-backed-wiki-platforms-comparison]]; medium)
- **Every git-to-Confluence route is one-way with markdown canonical** — `kovetskiy/mark`, `markdown-confluence`, the GitHub Actions, the Marketplace sync app. `mark` is maintained at a slow cadence and converts GitHub-alert syntax, not Obsidian callouts; `[[wikilinks]]` are unsupported everywhere except possibly `markdown-confluence` (unverified). (Source: [[kovetskiy-mark-readme]], [[git-backed-wiki-platforms-comparison]]; high for mark, medium for the rest)
- **GitHub's own surfaces do not speak Obsidian, but the repo Wiki is the closest free match.** github.com renders frontmatter as a table, only the five GFM alert types, and `[[wikilinks]]` as literal text. The repository Wiki is a separate `.wiki.git`, resolves `[[Page Name]]` by title in a flat namespace (exactly the vault's basename rule), has a sidebar, search and repo-bound permissions (private with a private repo), and can be filled by CI. GitHub Pages' default Jekyll drops `_`- and dot-prefixed files, and private Pages exist only on Enterprise Cloud. (Source: [[github-docs-markdown-wikis-pages]]; high on rendering, medium on CI push)
- **Cross-repo agent access is a permissions question, not a topology one.** Claude Code will not read outside its start directory until granted: `--add-dir` is per-session and loads the vault's skills; `permissions.additionalDirectories` is committable but never loads the vault's CLAUDE.md or skills; sparse worktrees are same-repo only. Recommended: sibling clone + the AGENTS.md pointer + a committed `additionalDirectories: ["../<vault>"]`; submodules only for consumers that need a pinned snapshot; subtree is the worst fit for a single source of truth. (Source: [[claude-code-large-codebases-docs]], [[Cross-Repo Wiki Access]]; high on the docs, medium on the trade-off analysis)

## Decision table

| If the need is… | Route | Agent commits live? | Private? | Lowering needed |
|---|---|---|---|---|
| Navigate like Confluence, read-only, free | **Quartz v5** on GitHub Pages / Cloudflare Pages | Yes (CI on push) | Cloudflare Access or SSO proxy in front | ignore `.raw/`; `_index.md` → `index.md`; check `[!gap]` rendering |
| Free and private without an Enterprise plan | **CI-mirrored GitHub Wiki** | Yes (Action on push) | Yes, with the repo | callout map; `_index.md` → `Home.md`; wikilinks already native |
| Readers already live in Confluence (spaces, comments, permissions) | **One-way publish** via `mark` / `markdown-confluence` in CI | Yes | Confluence's | `[[wikilinks]]` → links; callouts → alerts; IDs in page titles for idempotent upsert |
| Humans must edit in a UI and changes must flow back | **GitBook Git Sync** or **Wiki.js** git storage | Yes | Platform's | same as above, plus conflict handling against the single-writer rule for `index.md` / `log.md` / `hot.md` (`team-sync.md`) |
| A quick look at the bundle's shape for an agent-interop partner | **OKF visualizer** (one HTML file) | n/a | none | export via `okf_export.py` (after retargeting to v0.2) |
| Richest reader, people willing to install Obsidian | git clone + Obsidian (Sync / Relay for non-git users) | Yes | repo's | none — see [[Wiki Sharing Patterns]] |

Recommendation for this vault: pilot **Quartz v5** on a 20-page slice (one hour, closes most gaps below), keep the **GitHub Wiki mirror** as the free-private fallback, and reserve Confluence publishing for teams whose readers are already there. All three keep git canonical and agent commits live. Round-trip sync is the only route that competes with the agents for writes — avoid it unless UI editing is a hard requirement.

## Key Entities

- [[Quartz]]: the recommended pilot — Obsidian-native static generator with the full navigation set, repo-triggered builds, v5.0.0 (2026-06).
- Google Cloud Knowledge Catalog: the only hosted OKF consumer; IAM-governed, agent-facing (no entity page yet — page cap).
- `kovetskiy/mark`, `markdown-confluence`: one-way git-to-Confluence publishers (profiled in [[kovetskiy-mark-readme]] and [[git-backed-wiki-platforms-comparison]]).
- Flowershow, Obsidian Digital Garden, Perlite, Obsidian Publish, Docmost, Outline, Wiki.js, BookStack, GitBook: profiled inside the comparison source pages; no entity pages (page cap).

## Key Concepts

- [[Open Knowledge Format]]: Google's markdown + YAML interchange format for agent knowledge; v0.2; humans-and-agents charter, agent-first tooling.
- [[Vault Publishing Topologies]]: publishers split by trigger — rebuild-from-repo vs push-from-app vs live-render — and what that means for agent-written content.
- [[Obsidian Vault Portability]]: portability tiers 0–3 for a vault, the three build rules, and the Confluence-expectation map.
- [[One-Way Publish vs Round-Trip Wiki Sync]]: the sub-modes, the lowering-step spec, and the decision tree for a git-canonical wiki.
- [[Cross-Repo Wiki Access]]: how an agent in another repo reaches the vault (add-dir, additionalDirectories, submodule / subtree / sibling clone) and which vault conventions break under each GitHub surface.

## Contradictions

- **Quartz version.** [[obsidian-static-publishers-comparison]] (homepage fetched) reports v5.0.0 on 2026-06-11; [[obsidian-vault-site-generators]] (search summaries) still describes v4 as current. The homepage wins; v4 feature descriptions are the baseline and the v5 changelog is unfetched. Reconciled on [[Quartz]].
- **MkDocs wikilink plugin.** [[git-backed-wiki-platforms-comparison]] names `mkdocs-roamlinks` / `mkdocs-ezlinks`; [[obsidian-vault-site-generators]] rates `mkdocs-obsidian-bridge` stronger, citing the bridge README's claim that ezlinks "generated incorrect links" — a competitor's claim, unverified. Treat the bridge as the current default and verify in a pilot.
- **Obsidian Publish price.** [[Wiki Sharing Patterns]] (May 2026) says $10/mo; 2026 round-ups say $8/mo on annual billing, $10 month-to-month. Refinement, not conflict; noted on that page.
- **`mark` maintenance.** An ecosyste.ms snapshot shows a last push in 2025-05; the README at fetch shows v16.x and 85 open issues. Slow cadence either way; the maintainer calls it low priority.
- **Wiki.js health.** Positioned as active by some sources, "stalled roadmap" by a 2026 homelab review. Reconciled as 2.x maintained, 3.0 stalled.
- **OKF spec drift.** The launch post describes v0.1 with `timestamp` and "no CLI"; the canonical repo is v0.2 with trust fields and a `reference_agent` CLI. Version drift over three months, not disagreement.

## Open Questions

- **Plugin follow-up (not a research gap):** retarget `okf_export.py` to `GoogleCloudPlatform/open-knowledge-format` v0.2 — map vault `status` to `draft | stable | deprecated`, emit `generated`, rename per-folder `_index.md` to the reserved `index.md`; wiki-lint's OKF note should cite v0.2.
- Flowershow: private pages, pricing, graph view — the docs fetch returned navigation only.
- Quartz v5 changelog: callouts / Explorer changes, dot-folder and `_index.md` defaults; Digital Garden and Perlite latest release dates.
- Whether `markdown-confluence` converts `[[wikilinks|aliases]]` and Obsidian callout types, and whether it is maintained in 2026 — the single most decision-relevant unknown for the Confluence route.
- GitBook conflict handling and Wiki.js sync direction / interval — both docs pages failed to fetch.
- Whether the Knowledge Catalog console gives humans a bundle-browsing view; whether the OKF visualizer stays usable at 100+ pages; whether Gemini Enterprise or NotebookLM import bundles.
- Whether `GITHUB_TOKEN` alone can push to the same repo's wiki from Actions (action READMEs say yes; GitHub docs not fetched); whether the Wiki renders a leading YAML block as a table.
- `starlight-obsidian` full feature list; whether Material's `navigation.path` breadcrumbs remain Insiders-only; `mkdocs-publisher` state.
- Submodule / subtree / sparse-checkout trade-offs are reasoned from git semantics, not sourced — an experience-report search would ground them.
- Entity pages not created (page cap): Google Knowledge Catalog, Flowershow, Obsidian Digital Garden, Perlite, Obsidian Publish, Docmost, Outline, Wiki.js, BookStack, GitBook, markdown-confluence.

## Sources

- [[okf-spec-and-reference-repo]]: GoogleCloudPlatform/open-knowledge-format, v0.2, 2026-06 (high)
- [[google-cloud-okf-announcement]]: McVeety & Hormati, Google Cloud, 2026-06-12 (high)
- [[obsidian-static-publishers-comparison]]: web synthesis, 2026-09-03 (medium; Quartz homepage + Digital Garden README fetched)
- [[obsidian-vault-site-generators]]: web synthesis, 2026-09-03 (medium; starlight-obsidian, mkdocs-obsidian-bridge, docusaurus-plugin-obsidian-vault fetched)
- [[git-backed-wiki-platforms-comparison]]: web synthesis, 2026-09-03 (medium)
- [[kovetskiy-mark-readme]]: mark README, fetched 2026-09-03 (high)
- [[github-docs-markdown-wikis-pages]]: GitHub Docs, fetched 2026-09-03 (high on rendering, medium on Wiki CI)
- [[claude-code-large-codebases-docs]]: Claude Code Docs, fetched 2026-09-03 (high)
