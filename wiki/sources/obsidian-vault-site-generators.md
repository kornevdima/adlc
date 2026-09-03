---
type: source
title: "Rendering an Obsidian Vault with Docs-as-Code Site Generators (web synthesis)"
source_type: web-research-synthesis
author: "autoresearch web synthesis — official docs + GitHub READMEs (starlight-obsidian, mkdocs-obsidian-bridge, docusaurus-plugin-obsidian-vault, Quartz, Hugo export tools)"
date_published: 2026-09-03
url: https://starlight-obsidian.vercel.app/getting-started
created: 2026-09-03
updated: 2026-09-03
confidence: medium
tags:
  - source
  - docs-as-code
  - static-site
  - obsidian
  - wiki-sharing
  - mkdocs
  - docusaurus
  - starlight
  - hugo
  - quartz
status: current
related:
  - "[[Wiki Sharing Patterns]]"
  - "[[wiki-sharing-research]]"
  - "[[Obsidian Vault Portability]]"
  - "[[Quartz]]"
  - "[[LLM Wiki Pattern]]"
key_claims:
  - "Every generator family has an Obsidian bridge, but only Quartz v4 ships the full Confluence-like navigation set (folder explorer, breadcrumbs, full-text search, dark mode) with no extra plugins; MkDocs+Material and Docusaurus need one Obsidian plugin plus theme config, Starlight needs starlight-obsidian, Hugo needs a pre-processing export step"
  - "Wikilinks with aliases and #heading anchors are handled by every bridge; Hugo alone has no wikilink support and relies on obsidian-export / obsidian-to-hugo rewriting links to {{< ref >}} shortcodes"
  - "Callouts are the fragile syntax: MkDocs needs a separate extension, docusaurus-plugin-obsidian-vault maps only six admonition types, Starlight asides have four — a custom callout type such as [!gap] renders correctly only where the mapping is extensible (Quartz, Hugo 0.132+ blockquote render hooks, MkDocs admonitions)"
  - "Underscore-prefixed files (_index.md, _plan ...) are silently excluded by Docusaurus and Astro content collections; Hugo treats _index.md as its native section index; MkDocs and Quartz expect index.md"
  - "Docusaurus and starlight-obsidian emit MDX, so bare < and { in LLM-written prose break the build; MkDocs, Hugo and Quartz are plain Markdown and tolerate it"
  - "Docs versioning exists natively only in Docusaurus (MkDocs via mike, Starlight via a plugin); Confluence-style page history is better served by git-backed last-updated stamps plus history links, which all five support"
  - "All five produce static output, so private access is a hosting decision: GitHub Pages access control needs GitHub Enterprise Cloud; otherwise Cloudflare Access, Netlify/Vercel protection tiers, or a self-hosted proxy"
  - "Maintenance signals 2025-2026: starlight-obsidian (150 stars, active releases, author is a Starlight core contributor) and Quartz v4 (active releases, multiple 2025 guides) look healthy; mkdocs-obsidian-bridge is small but alive (84 stars, 44 commits); docusaurus-plugin-obsidian-vault is unproven (1 star, 2 commits); mkdocs-ezlinks is reported to generate wrong links"
---

# Source: Rendering an Obsidian Vault with Docs-as-Code Site Generators

**Scope**: Q3 of the "Sharing the Wiki with People" research (2026-09-03) — which general docs-as-code generators can render a wikilinked, callout-heavy Obsidian vault with Confluence-like navigation (page tree, search, breadcrumbs, versions), and what must be rewritten. **Method**: 5 WebSearches, 3 WebFetches (starlight-obsidian getting-started page, GooRoo/mkdocs-obsidian-bridge README, gl0bal01/docusaurus-plugin-obsidian-vault README). Hugo and Quartz claims rest on search-result summaries plus prior knowledge and are marked medium/low. No generator was run against a real vault — read the matrix as a pilot plan, not a verdict. The distilled checklist lives in [[Obsidian Vault Portability]].

## The five candidates

### MkDocs + Material

Python, plain Markdown (Python-Markdown), the base of Backstage TechDocs (see [[wiki-sharing-research]]). Obsidian bridges: **mkdocs-obsidian-bridge** (GooRoo) expands `[[internal links]]` and incomplete Markdown links to real paths, picks the shortest path when several notes match, accepts partial-path hints like `[[2021/Books]]`, and marks invalid links (`warn_on_invalid_links`, `invalid_link_attributes`); it does not do callouts itself — enable the separate `obsidian_callouts` Markdown extension. Python 3.10+, BSD-3, 84 stars, 44 commits, 3 open issues (high confidence, fetched). The README's stated reason for existing: **mkdocs-roamlinks** does not resolve shortest or incomplete paths and leaves unresolved `[[links]]` as text; **mkdocs-ezlinks** generated incorrect links and cannot tell valid from invalid links (medium — one author's comparison; ezlinks has been forked as mkdocs-obsidian-links / mkdocs-ezlinked-plugin, a sign of upstream stall). **mkdocs-callouts** converts `> [!type]` blocks into Material admonitions (medium, not fetched). **mkdocs-obsidian-support-plugin** (ndy2) is a second all-in-one converter (pointer only). **mkdocs-publisher** did not surface in searches — unverified. Material gives folder-driven navigation (`navigation.sections`, `navigation.indexes` for a folder's `index.md`), built-in client-side search, a `palette` dark-mode toggle, `mike` for versioning, and `git-revision-date-localized` for last-updated stamps; breadcrumbs (`navigation.path`) were historically an Insiders-only feature — verify.

### Docusaurus

React/MDX. **docusaurus-plugin-obsidian-vault** (gl0bal01) syncs a vault into `docsPath` at build time (regenerated each build, vault untouched), rewrites `[[Page]]`, `[[folder/Page|Label]]` and `[[Page#Section]]` with correct `../` depth, converts callouts to admonitions for exactly note, tip, info, warning, danger, caution, preserves frontmatter and auto-fills `title`, copies assets to a static dir, auto-generates `_category_.json` per folder with a `categoryIndexFile` option (e.g. `START.md`) as the category page, supports a GitHub repo as `vaultSource` (token for private repos; must be cloned first in CI), and escapes "problematic characters for MDX". Options: `vaultSource`, `docsPath`, `transformations`, `exclude`, `include`, `generateCategories`, `categoryLabels`, `bannerTop`, `bannerBottom`, `debug`. MIT, **1 star, 2 commits** — feature-complete on paper, unproven in use (high confidence on that state, fetched). Docusaurus itself provides autogenerated sidebars, built-in breadcrumbs, native docs versioning, dark mode, `showLastUpdateTime`, and search via Algolia DocSearch (free for OSS) or a local-search plugin. Two structural hazards: MDX strictness, and the default `exclude` that drops every `_`-prefixed file and folder.

### Astro Starlight + starlight-obsidian

**starlight-obsidian** (HiDeoo, a Starlight core contributor) copies a vault (`vault: "../path"`) into a place Starlight can consume, converts it to MDX, and generates sidebar entries exposed as `obsidianSidebarEntries` that you nest into any sidebar group; Mermaid diagrams need Playwright with Chromium; the docs warn to check rendered pages before publishing. 150 stars; releases page shows ongoing MDX conversion fixes (high, fetched/searched). Wikilinks, callouts-to-asides, embeds, `ignore` globs and frontmatter copying are documented on its configuration page, which was not fetched (medium). Starlight itself: folder-autogenerated sidebar, Pagefind search built in, dark mode built in, `lastUpdated` from git, versioning via the community `starlight-versions` plugin; breadcrumbs only via community plugins (low). Astro content collections ignore `_`-prefixed files and enforce a frontmatter schema, so custom keys must be dropped or declared.

### Hugo

Go, Goldmark Markdown, no wikilink support of its own. Toolchain: **obsidian-export** (Rust; converts Obsidian Markdown to CommonMark and adds empty frontmatter where missing — used in a pre-commit hook in Jacob Kaplan-Moss's TIL), **obsidian-to-hugo** (Python; rewrites wikilinks to Hugo shortcodes; PyPI versions date to 2023), and **obsidian-hugo-export** (sagarbehere; `publish: true` filtering, `process-wikilinks.py` to `[Title]({{< ref "path" >}})`, `add-backlinks.py`). Callouts: Hugo 0.132+ blockquote render hooks expose an alert type for `> [!type]` blocks, so any callout type maps to whatever template you write (medium). Hugo's `_index.md` section-index convention is exactly the vault's sub-index convention — the only generator where that file needs no rename. Navigation, search (Fuse/Pagefind), breadcrumbs (`.Ancestors`) and dark mode are theme-supplied (Book, Docsy, Hextra); no versioning. [[Quartz]] v3 was a Hugo theme; v4 dropped Hugo.

### Quartz v4

Node.js rewrite of the Hugo-based v3, built for Obsidian vaults (see [[Quartz]]). Default layout ships Breadcrumbs, Search (full text), Darkmode and Explorer (folder tree) components; Obsidian syntax (wikilinks, aliases, callouts) is handled by its own transformer; GitHub Pages deploy is the documented workflow (push to the `v4` branch, Actions builds). Active releases; guides dated 2025-08 and 2025-12 (medium — search summaries). No versioning, no auth; it is a digital-garden tool rather than a docs framework.

## Feature matrix

| Capability | MkDocs + Material | Docusaurus | Starlight | Hugo | Quartz v4 |
|---|---|---|---|---|---|
| Wikilinks, aliases, `#heading` | obsidian-bridge (roamlinks weaker) | vault plugin | starlight-obsidian | pre-export rewrite to `ref` | native |
| Callouts | callouts extension → admonitions | 6 types → admonitions | → asides (4 types) | render hook, any type | native, many types |
| Frontmatter | unknown keys ignored | preserved, `title` auto | strict schema | native; `_index.md` native | passthrough |
| Sidebar / page tree from folders | `navigation.sections/indexes` | auto `_category_.json` | `obsidianSidebarEntries` | theme | Explorer |
| Search | built in | Algolia or local plugin | Pagefind built in | theme | built in |
| Versioning | `mike` | native | `starlight-versions` | none | none |
| Breadcrumbs | `navigation.path` (verify) | built in | community plugin | theme / `.Ancestors` | built in |
| Dark mode | `palette` toggle | built in | built in | theme | built in |
| Last-updated from git | plugin | `showLastUpdateTime` | `lastUpdated` | `enableGitInfo` | built in |
| CI to GitHub Pages | `mkdocs gh-deploy` / Actions | Actions | Actions | Actions | Actions template |
| Markdown dialect | Python-Markdown (tolerant) | MDX (strict) | MDX via plugin (strict) | Goldmark (tolerant) | remark (tolerant) |
| Conversion effort for this vault | low-medium | high | high | medium | low |

## What this vault shape needs rewritten

Vault shape: YAML frontmatter with custom keys (`type`, `status`, `related` lists of quoted wikilinks), wikilinks with aliases, Obsidian callouts including a custom `[!gap]` type, folder names with spaces, `_index.md` sub-indexes, root `index.md` / `log.md` / `hot.md`, a hidden `.raw/` folder, Dataview dashboards, `.base` and `.canvas` files, `_plan ...` artifacts.

1. **Wikilinks** — no rewrite on any route except Hugo. obsidian-bridge's invalid-link marking doubles as a dead-link lint.
2. **Callouts** — `[!gap]` is outside the Docusaurus plugin's six types and Starlight's four aside kinds; alias it to `warning` in a pre-pass or extend the mapping. MkDocs admonitions render unknown types with a generic style; Quartz and Hugo render hooks take any type.
3. **Frontmatter** — kept as data everywhere except Starlight's strict schema (declare or drop custom keys). Quoted wikilinks inside YAML lists stay strings; a "related" panel would need a small theme component on any route.
4. **`_index.md` and `_plan` files** — Docusaurus and Astro drop `_`-prefixed files silently (sub-indexes vanish; plan artifacts conveniently vanish). MkDocs renders `_index.md` as a page titled "_index" unless copied to `index.md` with `navigation.indexes`; Quartz wants `index.md` per folder; Hugo consumes `_index.md` natively. Do the rename in a build-time copy, never in the vault — skills and agents reference `_index.md`.
5. **Folder names with spaces** — all tolerate them; MkDocs and Docusaurus keep spaces (`%20` URLs), Astro/Hugo/Quartz slugify. No renames needed.
6. **`.raw/`** — exclude explicitly everywhere (`exclude_docs`, plugin `exclude`, starlight-obsidian `ignore`, Hugo `ignoreFiles`, Quartz `ignorePatterns`); do not rely on dot-folder defaults.
7. **MDX hazards** (Docusaurus, Starlight) — bare `<placeholder>` and `{...}` in prose fail the build; LLM-written pages contain these routinely. Needs an escape pass and a CI build gate.
8. **Dataview, Bases, Canvas** — nothing renders them; Dataview blocks degrade to code, `.base` / `.canvas` must be excluded.
9. **Root pages** — `index.md` becomes the home on MkDocs/Quartz; Docusaurus needs `slug: /` or docs-only mode.
10. **Embeds `![[note]]`** — Quartz transcludes notes; starlight-obsidian documents embeds (unverified); obsidian-bridge only media via an extension; Docusaurus plugin undocumented. Low impact for a vault that rarely embeds.

## Versioning vs page history

Confluence "versions" means per-page history, which here is git. All five can stamp last-updated from git and link to GitHub history. Docs versioning (Docusaurus native, `mike`, `starlight-versions`) is for parallel release lines — not this need.

## Private hosting

Static output in all cases, so access control is the hosting layer: GitHub Pages access control requires GitHub Enterprise Cloud; alternatives are Cloudflare Pages + Cloudflare Access (free tier for small teams), Netlify or Vercel password/SSO protection (paid tiers), a self-hosted reverse proxy behind SSO, or Backstage TechDocs — MkDocs-based, so the MkDocs route composes with it (see [[wiki-sharing-research]]). Medium confidence; tiers shift.

## Maintenance state (2025-2026 signals)

| Tool | Signal | Confidence |
|---|---|---|
| starlight-obsidian (HiDeoo) | 150 stars; active releases (MDX void-element fixes); author is a Starlight core contributor | high |
| Quartz v4 (jackyzha0) | active releases; guides dated 2025-08 and 2025-12; widest Obsidian-publishing adoption | medium |
| mkdocs-obsidian-bridge (GooRoo) | 84 stars, 44 commits, 3 open issues, BSD-3; commit dates not extracted | medium |
| mkdocs-callouts, mkdocs-roamlinks | not fetched; roamlinks leaves unresolved links as text (per bridge README) | low |
| mkdocs-ezlinks | reported to generate incorrect links (per bridge README); forked twice | low-medium |
| mkdocs-publisher (pub-obsidian) | did not surface; unverified | gap |
| docusaurus-plugin-obsidian-vault (gl0bal01) | 1 star, 2 commits, MIT; unproven | high (on the state) |
| obsidian-export, obsidian-to-hugo, obsidian-hugo-export | obsidian-to-hugo PyPI versions from 2023; obsidian-export used in pre-commit hooks (Kaplan-Moss TIL) | low |

> [!gap] Not verified this session: starlight-obsidian's full feature list (only getting-started fetched); whether Material's `navigation.path` breadcrumbs are still Insiders-only; starlight-obsidian's handling of unknown callout types and frontmatter copying; Docusaurus behaviour on unknown frontmatter keys; whether Astro and Hugo skip dot-folders by default; mkdocs-publisher's state. A pilot build of a 20-page slice would settle all of these in about an hour.

## Verdict for the synthesis

Two short paths. (a) [[Quartz]] v4 — fewest rewrites (copy `_index.md` to `index.md`, add `.raw`, `.base`, `.canvas` to `ignorePatterns`) and the full Confluence navigation set out of the box, but a digital-garden tool: no versioning, single-author defaults. (b) MkDocs + Material + mkdocs-obsidian-bridge + a callouts extension — the most corporate-looking, composes with Backstage TechDocs, tolerant Markdown, but needs the `_index.md` copy step and a callouts extension. Docusaurus and Starlight impose MDX strictness on LLM-written prose and drop `_`-prefixed files, making them the most conversion-heavy; Hugo is natively aligned with `_index.md` but has no wikilinks without a pre-processing step. Options and topology context: [[Wiki Sharing Patterns]].

## Sources

- starlight-obsidian docs — https://starlight-obsidian.vercel.app/getting-started (fetched) and repo https://github.com/HiDeoo/starlight-obsidian (releases page via search)
- GooRoo/mkdocs-obsidian-bridge README — https://github.com/GooRoo/mkdocs-obsidian-bridge (fetched)
- gl0bal01/docusaurus-plugin-obsidian-vault README — https://github.com/gl0bal01/docusaurus-plugin-obsidian-vault (fetched)
- ndy2/mkdocs-obsidian-support-plugin — https://github.com/ndy2/mkdocs-obsidian-support-plugin (pointer)
- Mara-Li/mkdocs-obsidian-links (ezlinks fork) — https://github.com/mara-Li/mkdocs-obsidian-links (pointer)
- jackyzha0/quartz releases — https://github.com/jackyzha0/quartz/releases; guides: mizzy.org 2025-08-30, tofutush.github.io 2025-12-16, notes.nicolevanderhoeven.com (GitHub Pages how-to)
- Hugo: Jacob Kaplan-Moss TIL https://jacobian.org/til/hugo-obsidian/; sagarbehere/obsidian-hugo-export https://github.com/sagarbehere/obsidian-hugo-export; devidw/obsidian-to-hugo https://github.com/devidw/obsidian-to-hugo
- Obsidian forum thread on Docusaurus publishing (pointer) — https://forum.obsidian.md/t/idea-publishing-obsidian-vault-via-docusaurus/48266
