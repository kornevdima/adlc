---
type: source
title: "Obsidian-native publishers compared: Quartz, Flowershow, Digital Garden, Perlite, Obsidian Publish"
source_type: web-research synthesis
author: "web-research synthesis (official docs + GitHub READMEs; secondary blogs for pricing only)"
date_published: 2026-09-03
created: 2026-09-03
updated: 2026-09-03
url: https://quartz.jzhao.xyz/
confidence: medium
tags:
  - source
  - research
  - obsidian
  - publishing
  - static-site
  - wiki-sharing
status: current
related:
  - "[[Wiki Sharing Patterns]]"
  - "[[wiki-sharing-research]]"
  - "[[Vault Publishing Topologies]]"
  - "[[Quartz]]"
  - "[[LLM Wiki Pattern]]"
key_claims:
  - "Quartz released v5.0.0 on 2026-06-11; it builds a vault into a static site with wikilinks, transclusions, backlinks, graph view, full-text search, and deploys to GitHub Pages, Cloudflare, Netlify, or Vercel"
  - "Only two of the five publishers rebuild from the vault's own git repo on push (Quartz via CI, Flowershow cloud via its GitHub integration); Digital Garden and Obsidian Publish are pushed from the Obsidian app, so agent commits reach readers only after a human re-publishes"
  - "Digital Garden publishes only notes carrying dg-publish: true into a separate 11ty repo hosted on Vercel/Netlify; the vault needs frontmatter, not restructuring, and there is no password/auth option"
  - "Perlite is not a static generator: a PHP viewer renders the checked-out vault at request time, supports callouts/frontmatter/backlinks/embeds but only wikilink-style links (not markdown links), and its graph view needs the Metadata Extractor plugin run inside Obsidian"
  - "Obsidian Publish costs $8/site/month annually ($10 monthly), single tier, 4 GB, and its only access control is one site-wide password — no per-page or per-folder permissions, no SSO"
  - "None of the five offers per-folder permissions; folder-level RBAC remains a Relay-only feature (see Wiki Sharing Patterns)"
---

# Source: Obsidian-native publishers compared (2026-09)

**Type**: web-research synthesis | **Date**: 2026-09-03 | **Method**: 5 searches, 3 fetches (Quartz homepage, Digital Garden README, Flowershow docs — the last returned navigation only). Pricing for Flowershow and Obsidian Publish comes from secondary 2026 blogs and is marked medium.

Question answered: which Obsidian-native publishers turn a vault in a GitHub repo into a navigable website, and how do they compare on the features a Confluence-style reader expects (page tree, search, backlinks, permissions)? Companion to the broader sharing survey in [[wiki-sharing-research]] and the option table in [[Wiki Sharing Patterns]], which lists Obsidian Publish and "static site export" as single rows; this page opens those rows up.

## The distinction that matters first

The five tools split by **where the publish is triggered from**, not by feature list. Quartz and Flowershow cloud rebuild from the vault's git repo on push; Digital Garden and Obsidian Publish are pushed from inside the Obsidian app, note by note; Perlite renders a live checkout on a server you run. For a vault that agents write via git, only the first and last keep readers current without a human clicking Publish. The pattern is written up as [[Vault Publishing Topologies]].

## Tool profiles

### Quartz (jackyzha0/quartz) — build-from-repo, static

- **What**: "a fast, batteries-included static-site generator that transforms Markdown content into fully functional websites". v4 (2023) was a from-scratch Node.js/JSX rewrite replacing the Hugo-based v3; **v5.0.0 released 2026-06-11** (homepage, high). Source: https://quartz.jzhao.xyz/ and https://github.com/jackyzha0/quartz
- **Fidelity**: Obsidian compatibility, wikilinks, transclusions, backlinks, graph view, full-text search, LaTeX, popover previews, i18n, comments, Docker support (homepage list, high). Wikilink resolution is configurable across Obsidian's three strategies — shortest, absolute, relative (third-party guide, medium-high). Callouts and the Explorer folder tree come from the Obsidian-flavoured-Markdown transformer and the Explorer component in the v4 docs (assistant knowledge, medium — not re-verified on the v5 site).
- **Private pages**: `draft: true` frontmatter excludes a page; an ExplicitPublish plugin flips the default to opt-in `publish: true` (medium).
- **CI / hosting**: "Deploy to GitHub Pages, Cloudflare, Netlify, or Vercel" (high). The vault is fed in as the `content/` directory (copy, symlink, submodule, or the build's directory flag), so the repo stays as-is.
- **Auth**: none built in; a static site needs a fronting layer (Cloudflare Access, basic auth on Netlify/Vercel paid tiers, or a private GitHub Pages site on Enterprise) (medium).
- **Cost / licence**: free, MIT. **Maintenance**: active — major release in June 2026. Entity page: [[Quartz]].

### Flowershow — build-from-repo (hosted) or self-host

- **What**: publishes "docs, blogs, wikis, and knowledge bases in a fully hosted platform"; core is free and open source under the **AGPL** — Next.js app, Go CLI, markdown packages. Source: https://github.com/flowershow/flowershow and https://flowershow.app/ (high). A companion Obsidian plugin (datopian/obsidian-flowershow) publishes without touching git (high).
- **Fidelity**: aims at "all core Obsidian syntax, including wiki-links, embeds, callouts, Canvas, and even Bases"; the default theme ships a backlinks section, math, mermaid, dark/light mode (official blog + README snippets, high). Sidebar navigation and site search exist (medium). Graph view: not found in any snippet (gap).
- **CI**: the hosted edition connects to a GitHub repo and republishes on push (forum announcement of the hosted edition, medium).
- **Private pages / auth**: not captured — the docs fetch returned navigation only (gap).
- **Cost**: free plan on a Flowershow subdomain with footer attribution; premium reported at ~$50/year versus Obsidian Publish's $96–120/year (Unmarkdown blog, 2026, medium). **Maintenance**: active — site dated 2026, changelog, docs section for "Agents" (medium).

### Obsidian Digital Garden (oleeskild) — app-pushed, static

- **What**: Obsidian plugin that "takes the markdown files selected for publishing, bundling them up into a github repository, that is then rendered into a static website using the 11ty static site generator", with a one-click "Deploy to Vercel" template repo; Netlify is the documented alternative and a local export exists for self-hosting (README, high). Source: https://github.com/oleeskild/obsidian-digital-garden
- **Selection**: "Only notes you explicitly mark with `dg-publish: true` ever leave your vault"; "Linked notes are never auto-published"; `dg-home: true` marks the entry page (high). Restructuring: none — frontmatter only (high).
- **Fidelity**: wikilinks incl. heading anchors (`Note#Header` form), transclusions, callouts, Dataview (codeblocks, inline, dataviewjs), Bases, Canvas, Excalidraw, PDFs, MathJax, mermaid, PlantUML (high).
- **Site features**: "Fast search with live preview, Filetree navigation, Backlinks, Local graph, Global graph, Table of contents", link previews on hover (high). Search, previews, timestamps and math are themselves plugins on the garden's plugin API (medium).
- **Auth**: none; privacy is the opt-in flag only (high). **Cost**: free, MIT; Vercel "hosted free of charge" (high).
- **CI caveat**: Vercel/Netlify do rebuild on push — but the push originates from the Obsidian app, not from the vault repo's CI. A third-party `obsidian-digital-garden-sync` project exists (unverified). **Maintenance**: 2.5k stars, 594 commits; latest release date not captured (gap).

### Perlite (secure-77/Perlite) — live render, self-hosted server

- **What**: "A web-based markdown viewer optimized for Obsidian" — "you put your whole Obsidian vault or markdown folder/file structure in your web directory and the page builds itself" (PHP, Docker image; README, high). Source: https://github.com/secure-77/Perlite
- **Fidelity**: callouts, frontmatter, tags, LaTeX, mermaid, internal links, backlinks, embedded content (high). "For internal links ... only Wikilinks are supported" — markdown-style links do not resolve (high). **Graph** requires the Metadata Extractor Obsidian plugin to export metadata, i.e. someone must run Obsidian to refresh it (high).
- **Search / tree**: vault folder tree and a search function are part of the viewer (medium). Folders can be hidden via settings (wiki "Perlite Settings", medium).
- **CI**: nothing is built; "deploy" is a `git pull` into the web directory (cron or webhook). **Auth**: the README only warns to keep raw `.md` files from being served directly; access control is the reverse proxy's job (basic auth / SSO proxy) (medium-low).
- **Cost**: free, open source. **Maintenance**: many 2025–26 forks and an active main branch; release date not captured (gap).

### Obsidian Publish (official) — app-pushed, hosted

- **Cost**: **$8/site/month annual, $10 monthly**, single tier, no free plan, 4 GB storage (2026 pricing round-ups, medium-high; the $10 figure matches [[Wiki Sharing Patterns]]).
- **Fidelity**: native — wikilinks, aliases, folder-less resolution, callouts render exactly as in the app (high). Backlinks and outgoing links per page, graph view, full-text search, custom domain, custom CSS (high).
- **Selection / private**: pages are chosen in the Publish dialog; `publish: true` frontmatter auto-selects (high). **Auth**: "site-wide only and you cannot password-protect individual pages or sections" (high). No SSO, no user accounts.
- **CI**: none — publishing happens from the Obsidian app; a `github.com/obsidian-publish` org surfaced in search and is unverified (gap). **Maintenance**: official, continuously maintained (high).

## Feature matrix

| Tool | Wikilinks + aliases | Callouts | Backlinks | Graph | Search | Folder tree | Private pages |
|---|---|---|---|---|---|---|---|
| Quartz v5 | Yes; 3 resolution modes | Yes (medium) | Yes | Yes | Yes | Explorer (medium) | `draft: true` / opt-in plugin |
| Flowershow | Yes + embeds | Yes | Yes | Not found (gap) | Yes (medium) | Sidebar (medium) | Gap |
| Digital Garden | Yes incl. headers | Yes | Yes | Local + global | Yes, live preview | Yes | Opt-in `dg-publish` only |
| Perlite | Wikilinks only | Yes | Yes | Needs Metadata Extractor | Yes (medium) | Yes | Hidden folders (medium) |
| Obsidian Publish | Native | Native | Yes | Yes | Yes | Yes | Per-note selection |

| Tool | Input / trigger | CI on push | Auth | Cost | State 2025–26 |
|---|---|---|---|---|---|
| Quartz v5 | Vault repo → CI build | GH Pages / Cloudflare / Netlify / Vercel | None; front it yourself | Free, MIT | v5.0.0 2026-06-11 |
| Flowershow | GitHub repo (cloud) or plugin; AGPL self-host | Cloud rebuilds on push (medium) | Gap | Free tier; ~$50/yr premium (medium) | Active 2026 |
| Digital Garden | Obsidian plugin → derived 11ty repo | Vercel/Netlify build the derived repo | None | Free, MIT | 2.5k stars; release date gap |
| Perlite | Server over a checkout | `git pull`, not a build | Reverse proxy | Free, OSS | Active; release date gap |
| Obsidian Publish | Obsidian app | None | One site-wide password | $8–10/site/mo | Official |

## Fit for a git-hosted, agent-written vault

- **Works on the repo as-is**: Quartz (feed the vault folder as content), Flowershow cloud (point at the repo), Perlite (mount the checkout). All three need an ignore list for `.raw/`, `_index.md` pages and any private folders; Quartz and Perlite expose that in config, Flowershow's mechanism was not captured.
- **Needs per-note frontmatter, not restructuring**: Digital Garden (`dg-publish`), Obsidian Publish (`publish` or manual selection).
- **Folder names with spaces**: static builders slugify paths (Quartz turns spaces into hyphens, medium); Perlite serves the folder names verbatim. Neither breaks wikilinks.
- **Permissions**: none of the five does per-folder access. The realistic options are one shared password (Obsidian Publish), a fronting SSO/Access layer (Quartz, Perlite, self-hosted Flowershow), or the opt-in selection gate (Digital Garden, Publish). Folder-level RBAC stays a Relay-only feature per [[Wiki Sharing Patterns]].

> [!gap] Not verified: Flowershow's private-page and password options and its exact plan prices; whether Quartz v5 changed callout/Explorer behaviour from v4; Digital Garden's and Perlite's latest release dates; what the `obsidian-publish` GitHub org is. Flowershow docs need a direct fetch of `/docs/getting-started` rather than the docs landing page.

## Connections

- [[Vault Publishing Topologies]] — the concept extracted from this comparison
- [[Quartz]] — entity page for the build-from-repo frontrunner
- [[Wiki Sharing Patterns]] — the wider option table this page refines
- [[wiki-sharing-research]] — earlier survey (Sync, Relay, Publish, docs-as-code topologies)
- [[LLM Wiki Pattern]] — the vault being published
