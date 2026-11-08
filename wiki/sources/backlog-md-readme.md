---
type: source
title: "Backlog.md README (markdown-native task manager)"
source_type: github-readme
author: "MrLesk and contributors"
date_published: undated (2025-2026 content, MIT licensed)
url: "https://github.com/MrLesk/Backlog.md"
created: 2026-11-08
updated: 2026-11-08
confidence: medium
tags:
  - source
  - file-based-tracker
  - markdown
  - git
key_claims:
  - "Every task is a plain .md file in the repository, in a backlog folder that is configurable (high)."
  - "Task ids carry a configurable prefix, for example TASK-1 (high)."
  - "Tasks hold description, acceptance criteria, a Definition of Done checklist, plan, notes and a final summary, plus dependencies (high)."
  - "Milestones group larger efforts; tasks can be archived with id and links kept (high)."
  - "A terminal board, a local web board and board export to Markdown are views over the files (high)."
  - "An MCP server exposes the backlog to agents, with workflow guides (high)."
  - "Search spans tasks, docs and decisions, but the README does not say how a task links to a doc (medium)."
---

# Backlog.md README

Backlog.md shows the file-based tracker model: the work layer is a folder of Markdown files in the same git repository as the code, and boards are views computed from those files. The README gives no release date; it mentions version 1.40 and 2025 talks.

## Model

- One file per task under `backlog/tasks`, with a prefixed id.
- Statuses such as To Do and Done drive the board columns.
- Dependencies are recorded per task, in both directions.
- Milestones group tasks. Docs live beside tasks under `backlog/docs`; decision records are searchable too.
- Git is optional: a filesystem-only mode exists. With git, history is the audit trail.
- The README advises changing tasks through the CLI, MCP or web UI, not by hand, to keep metadata consistent.

## Gaps

Frontmatter field names, the link syntax between a task and a doc, and the full status list are not in the README (they sit in separate instruction files). Not verified here.

Used in [[Knowledge Layer and Work Tracker Split]].
