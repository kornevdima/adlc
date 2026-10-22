---
type: meta
title: "Architecture Index"
created: 2026-10-22
updated: 2026-10-22
tags:
  - meta
  - index
  - architecture
status: evergreen
related:
  - "[[index]]"
  - "[[Plugin architecture overview]]"
  - "[[architecture/_changelog]]"
---

# Architecture Index

Navigation: [[index]] | [[concepts/_index|Concepts]] | [[entities/_index|Entities]] | [[sources/_index|Sources]] | [[architecture/_changelog|Changelog]]

How the adlc plugin is built: the parts, what each one owns, and how a request moves through them. The concept pages hold the research and design reasoning; these pages hold the as-built state. The README stays the install and quick-reference page.

---

- [[Plugin architecture overview]] — the one folder that is a plugin, a vault and a repo; the layers and the path a request takes through them (status: active)
- [[Skills and routing]] — the 20 skills in three families, what triggers each, which agents and scripts each one calls (status: active)
- [[Shared references]] — the 61 reference documents under the wiki skill that other skills and workers read: method libraries, templates, conventions (status: active)
- [[Workers and the dispatch pipeline]] — the 15 subagents, the per-story pipeline, what a worker may and may not do (status: active)
- [[Hooks and host adapters]] — the manifests and hook files for Claude Code, Cursor and Copilot; the vault-side guard hooks (status: active)
- [[Scripts]] — the 15 Python scripts and the installer: what each does and who runs it (status: active)
- [[Evals]] — the plugin eval cases, fixture layers and graders, and the two older local runners (status: active)
- [[Use cases and modes]] — what the plugin is for: vault modes, concerns, the delivery loop, manual work, intake, sharing (status: active)
- [[Release and upstream flow]] — how a vault's lesson becomes a plugin change and a version (status: active)

Changes to these pages are recorded in [[architecture/_changelog]].
