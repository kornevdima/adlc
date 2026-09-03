---
type: concept
title: "One-Way Publish vs Round-Trip Wiki Sync"
created: 2026-09-03
updated: 2026-09-03
tags:
  - wiki-sharing
  - docs-as-code
  - git-sync
  - confluence
  - architecture
  - design-decision
status: developing
related:
  - "[[Wiki Sharing Patterns]]"
  - "[[SDLC Wiki Concerns]]"
  - "[[LLM Wiki Pattern]]"
sources:
  - "[[git-backed-wiki-platforms-comparison]]"
  - "[[kovetskiy-mark-readme]]"
  - "[[wiki-sharing-research]]"
---

# One-Way Publish vs Round-Trip Wiki Sync

When a git repo of markdown is the source of truth and people want a Confluence-like UI on top, every platform sits in one of two sync models. The choice decides who owns truth, where conflicts happen, and whether the vault's Obsidian dialect survives. Extends [[Wiki Sharing Patterns]] (which covers Obsidian Sync / Relay / Publish and TechDocs topology) with the team-wiki platforms.

## The two models

**One-way publish (git → UI).** A CI step or import turns the repo into pages. Humans read, search, and comment in the UI; they do not edit there, or their edits are disposable and get overwritten on the next publish. Git stays canonical; agents keep reading and writing files.

**Round-trip (git ↔ UI).** Humans edit in the UI and the platform commits back to the repo; commits in the repo update the UI. Two sources of truth reconciled by the platform's sync engine.

## Three sub-modes of one-way

| Sub-mode | Mechanism | Idempotent re-publish? | Examples |
|---|---|---|---|
| **Build-and-serve** | CI renders a static site or bundle; portal serves it | Yes — full rebuild each time | Backstage TechDocs, MkDocs / Docusaurus exports |
| **Idempotent republish** | Publisher locates each page by a stable key (space + title, path, or frontmatter ID) and updates in place | Yes — by key | Confluence via `mark` (space + title), `markdown-confluence`, Marketplace GitHub Markdown Sync; Wiki.js in pull-only mode |
| **Import-once** | UI or API creates pages from files; no memory of what came from where | No — re-import duplicates unless you script an upsert keyed on IDs you store | Docmost import, Outline ZIP / API, BookStack API / ZIP |

Only the first two are "publish from git" in a maintainable sense. Import-once is a migration path, not a sync path. (Source: [[git-backed-wiki-platforms-comparison]])

## Two sub-modes of round-trip

- **File-faithful bidirectional** — the platform stores pages as the files it pulled and pushes edits as changes to those files (Wiki.js git storage). The dialect is whatever the editor emits; wikilinks survive only as literal text.
- **Normalising bidirectional** — the platform parses files into its own model and writes back its own markdown flavour (GitBook Git Sync: `SUMMARY.md` tree, `{% hint %}` blocks). A git-canonical vault receives foreign rewrites of its own pages on every UI edit. (Source: [[git-backed-wiki-platforms-comparison]], medium confidence — the Git Sync docs page was not fetched.)

## Why the distinction matters for a git-canonical vault

1. **Conflict surface.** Round-trip reintroduces the merge problem the vault avoided by making git canonical: agent commits and UI edits collide in the platform's sync engine, not in git, with the platform's conflict policy (usually last-write-wins or a normalised rewrite). One-way has no conflicts because there is only one writer.
2. **Dialect lowering.** No surveyed platform parses `[[wikilinks]]` or Obsidian callouts natively; the exception candidate is `markdown-confluence` (unverified). One-way publish accommodates a lowering step in CI; round-trip cannot, because lowered files would be written back and replace the originals.
3. **Comment ownership.** In one-way publish, comments live only in the UI copy and must be re-anchored on republish (`mark --preserve-comments`, with known gaps when commented text is deleted). In round-trip, comments stay attached to the page but still never reach git. Either way comments are a UI-side artifact; anything that must persist has to be folded into the page by a human or an agent. (Source: [[kovetskiy-mark-readme]])
4. **Identity keys.** Title-keyed publishers (`mark`) treat a renamed title as a new page; path- or ID-keyed publishers survive renames. Choose the key before the first publish.

## The lowering step (one-way paths)

A CI stage between the repo and the publisher, producing a derived tree that is never committed back:

- `[[Page]]` and `[[Page|alias]]` → relative links to the target file (or to the target platform's page URL)
- `> [!note] Title` → the platform's callout syntax; map Obsidian-only types (`[!gap]`, `[!example]`) to the nearest supported type or plain blockquote
- YAML frontmatter → platform metadata (for `mark`: `space`, `parents` from folder path, `labels` from `tags`) and stripped from the body elsewhere
- Embeds `![[file]]` → attachments or inline images
- Dataview / Bases blocks → dropped or pre-rendered as static tables

> [!gap]
> No off-the-shelf lowering tool for Obsidian → CommonMark + Confluence metadata was identified in this session; `markdown-confluence` may cover part of it. A small script (`obsidian-export` or a remark pipeline) is the likely answer and needs a pilot.

## Decision rule

```
Must git stay the single source of truth?
├── Yes → ONE-WAY publish
│    ├── Team already lives in Confluence → mark or markdown-confluence in a GitHub Action on merge to main
│    ├── Backstage portal exists → TechDocs (per-repo mkdocs.yml, CI publish)
│    ├── Want an OSS self-hosted wiki UI → Wiki.js git storage, pull-only (accept stalled-roadmap risk)
│    └── Docmost / Outline / BookStack → only with a scripted, ID-keyed upsert you maintain
└── No — humans must edit in the UI and changes must flow back
     ├── Accept dialect rewrites and a per-site SaaS bill → GitBook Git Sync
     └── Keep files faithful, self-hosted → Wiki.js bidirectional; agents must pull before writing
```

Round-trip is the right call only when non-developers are primary authors. For the parent topic's case — agents write, people navigate and comment — one-way idempotent republish is the fit, and the interesting engineering is the lowering step plus a comment-harvest convention. (Synthesis.)

## Platform mapping

| Platform | Model | Key | Notes |
|---|---|---|---|
| Confluence + `mark` | One-way, idempotent | space + title | frontmatter-driven placement; alerts → macros |
| Confluence + `markdown-confluence` | One-way, idempotent | its own frontmatter keys | Obsidian-origin; wikilinks / callouts claimed (medium) |
| Confluence + Marketplace GitHub Markdown Sync | One-way, idempotent | repo path | hourly + webhook; vendor-hosted |
| Backstage TechDocs | One-way, build-and-serve | catalog entity | needs Backstage |
| Wiki.js pull-only | One-way, idempotent | file path | project health risk |
| Wiki.js bidirectional | Round-trip, file-faithful | file path | |
| GitBook Git Sync | Round-trip, normalising | `SUMMARY.md` path | Free plan includes it |
| Docmost / Outline / BookStack | Import-once | none (you store IDs) | migration, not sync |

## Open questions

- Does `markdown-confluence` actually round-trip Obsidian callout types and `[[wikilinks|aliases]]`, and is it maintained in 2026?
- Does Wiki.js 2.x's pull-only mode honour folder → tree mapping for a vault with spaces and Title Case filenames?
- What is the cheapest comment-harvest loop (UI comments → an agent-readable file in git) for a one-way setup?

See [[git-backed-wiki-platforms-comparison]] for the full matrix and [[Wiki Sharing Patterns]] for the topology and Obsidian-native options.
