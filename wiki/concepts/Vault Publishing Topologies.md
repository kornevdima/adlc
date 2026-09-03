---
type: concept
title: "Vault Publishing Topologies"
created: 2026-09-03
updated: 2026-09-03
confidence: medium
tags:
  - concept
  - publishing
  - wiki-sharing
  - obsidian
status: developing
related:
  - "[[obsidian-static-publishers-comparison]]"
  - "[[Wiki Sharing Patterns]]"
  - "[[wiki-sharing-research]]"
  - "[[Quartz]]"
  - "[[LLM Wiki Pattern]]"
---

# Vault Publishing Topologies

Tools that turn an Obsidian vault into a website differ less by feature list than by **where the publish is triggered from**. Three topologies cover every Obsidian-native publisher surveyed in [[obsidian-static-publishers-comparison]]:

| Topology | Trigger | Examples | What readers see after an agent commits |
|---|---|---|---|
| **A. Build-from-repo** | A push to the vault's git repo starts a CI build | [[Quartz]] on GitHub Pages / Cloudflare / Netlify / Vercel; Flowershow cloud; MkDocs-style exports | The new commit, minutes later, no human involved |
| **B. App-pushed** | A human selects notes in the Obsidian app and clicks Publish; the tool pushes them to a hosted site or a derived repo | Obsidian Digital Garden (`dg-publish: true` → separate 11ty repo → Vercel); Obsidian Publish | The old site until someone re-publishes |
| **C. Live render** | A server reads the checked-out vault at request time; "deploy" is `git pull` | Perlite (PHP, Docker) | The new commit as soon as the checkout is refreshed |

(Source: [[obsidian-static-publishers-comparison]])

## Why the split matters for an agent-written vault

The wiki in this project is written by coding agents through git ([[LLM Wiki Pattern]]); no human opens Obsidian on every change. Under topology B the website drifts from the repo until a person re-publishes, so B either adds a curation gate (a feature, if the team wants a reviewed public surface) or a staleness tax (a cost, if the site is meant to be the live source). A and C keep the site current for free but publish whatever is committed, so the exclusion list — `.raw/`, `_index.md` sub-indexes, private folders, drafts — has to live in build config rather than in someone's judgment.

## Permissions are orthogonal to topology

None of the five surveyed tools gives per-folder or per-role access. The choices are: one shared password (Obsidian Publish), a fronting identity layer such as Cloudflare Access or an SSO reverse proxy (any A or C site you host), or the per-note opt-in gate of topology B. Folder-level RBAC remains the Relay-only feature already recorded in [[Wiki Sharing Patterns]]. So "share it like Confluence" decomposes into two independent decisions: the topology (who triggers publish) and the auth layer in front of it.

## Selection heuristic

- Site must track git without a human → **A** (Quartz is the maintained default: v5.0.0 June 2026, free, all Obsidian features) or **C** if the team already runs Docker and wants zero build step.
- Team wants a curated public subset with an explicit release moment → **B**; Digital Garden if free and self-owned matters, Obsidian Publish if zero maintenance and native fidelity matter more than $8–10/month.
- Team needs real permissions → put an identity proxy in front of A or C; no publisher solves it alone.

> [!gap] The heuristic is derived from tool documentation, not from a trial deployment of this vault. Unknowns that could change it: whether Flowershow cloud offers private sites, and how Quartz v5 handles dot-folders and `_index.md` out of the box.

## Connections

- [[obsidian-static-publishers-comparison]] — the evidence base
- [[Quartz]] — topology A frontrunner
- [[Wiki Sharing Patterns]] — the wider access/topology decision tree this plugs into
- [[wiki-sharing-research]] — docs-as-code topologies for where the vault lives
