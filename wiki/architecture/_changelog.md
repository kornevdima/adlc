---
type: changelog
title: "Architecture changelog"
created: 2026-10-22
updated: 2026-11-08
tags: [changelog, architecture]
---

# Architecture changelog

Change history for pages in this folder. Pages show the current state only; history goes here, newest first.

| Date | Page | Change |
|---|---|---|
| 2026-11-08 | [[Workers and the dispatch pipeline]], [[Scripts]] | The delivery loop, `wrap-up`, `wiki-query` and `wiki-lint` follow the `layout` and `engineering` keys: the code wiki path and the ub-mode definition of done ride in the packets, a story makes two commits under worktrees, `build_index_json.py` walks `service-wikis/*` beside `services/*/wiki` (2 tests); `tells_check.py` skips `log.md` |
| 2026-11-08 | [[Scripts]], [[Shared references]] | 1.2.0: three new `Toolset:` keys (`layout`, `engineering`, `cost`) in `toolset.py` with `code-wiki`; `tells_check.py` in `technical-writer`; `bin/add-service-worktree.sh`, `bin/setup-ub-mode.sh`, `bin/ub-tool.sh`; references `service-worktrees.md` and `engineering-ub-mode.md` |
| 2026-11-04 | [[Skills and routing]], [[Workers and the dispatch pipeline]], [[Scripts]], [[Shared references]], [[Use cases and modes]] | `idea` (the JetBrains IDE's MCP server) as a fourth `code-nav` value: worker read tools, `toolset.py check` probes the IDE, playbook in `toolset.md` |
| 2026-11-04 | [[Plugin architecture overview]], [[Skills and routing]], [[Shared references]], [[Workers and the dispatch pipeline]], [[Scripts]], [[Use cases and modes]] | 1.1.0: the vault `Toolset:` block (reader, code navigation, design tools); `toolset.md` and `toolset.py` added; sixteenth worker `feature-designer`; Obsidian and graphify become defaults the skills read, not requirements |
| 2026-10-23 | [[Scripts]] | `glossary.py` settles ids shared by two filenames, reads `ID-slug` filenames, resolves register owners by path; vault tests added (vault-d/UP-004, 1.0.9) |
| 2026-10-22 | [[Hooks and host adapters]], [[Scripts]] | Env guard skips message text and literal heredocs; payload tests added (vault-a/UP-024, 1.0.9) |
| 2026-10-22 | [[Plugin architecture overview]], [[Skills and routing]], [[Shared references]], [[Workers and the dispatch pipeline]], [[Hooks and host adapters]], [[Scripts]], [[Evals]], [[Use cases and modes]], [[Release and upstream flow]] | Folder created at plugin version 1.0.9: as-built description of the plugin, split out of the README |
