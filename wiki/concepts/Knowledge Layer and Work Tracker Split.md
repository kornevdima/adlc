---
type: concept
title: "Knowledge Layer and Work Tracker Split"
created: 2026-11-08
updated: 2026-11-08
confidence: medium-high
tags:
  - concept
  - knowledge-layer
  - work-layer
  - docs-as-code
sources:
  - "[[atlassian-what-is-an-epic]]"
  - "[[backlog-md-readme]]"
  - "[[obsidian-bases-help]]"
  - "[[writethedocs-docs-as-code]]"
  - "[[atlassian-link-confluence-page-to-work-item]]"
---

# Knowledge layer and work tracker split

Put what stays true in the knowledge layer and what moves through states in the work layer, and link them by id in both directions. This is the Confluence and Jira division, and it carries over to a wiki plus a Markdown backlog in one git repository.

## The division (Confluence and Jira)

- Unstructured, lasting material (architecture, specs, decisions, retrospectives, manuals) goes in pages. Items with typed fields, a workflow and reporting (requirements, tasks, bugs) go in issues. This split is repeated across Atlassian community answers and vendor guides; the Atlassian help pages read describe the linking mechanics but state no page-versus-issue rule, so the rule itself stays medium to low confidence.
- Links run both ways: a page links to the issues that implement it, and an issue links to the page that explains it. Pages can embed live issue lists and boards, so the page reads the tracker instead of copying it. Atlassian documents the two-way link: a page can be linked to an epic or a standard work item, created from the work item, and the link shows on both sides (Source: [[atlassian-link-confluence-page-to-work-item]], medium confidence, read from excerpts). The epic page points to the same article (Source: [[atlassian-what-is-an-epic]]).
- Retrospectives and learnings live in a page; the follow-up actions live as issues linked from it. Duplicating status in both places is the known failure: the ticket says one thing and the page another.

## Docs as code

Write the Docs defines docs-as-code as writing documentation with the same tools as code: issue trackers, Git, plain-text markup, code review and automated tests. Teams share ownership and can block a merge that lacks docs (Source: [[writethedocs-docs-as-code]], undated, medium confidence). Keeping the knowledge layer in the code repository gives pages the same review and history as code.

## The work layer as files

A file-based tracker keeps one Markdown file per task in the repository, with a prefixed id, status, dependencies, acceptance criteria and a final summary. Boards are views over those files (Source: [[backlog-md-readme]]). In Obsidian, Bases is a core plugin whose views read notes and their properties, with data staying in the Markdown files. Its view types are Table, List, Cards, Kanban and Map, and the Kanban view shows files as cards in columns based on a grouped property, so a `status` field can drive the lanes (Source: [[obsidian-bases-help]], high confidence). The separate Kanban community plugin describes its boards as markdown-backed (its README, github.com/mgmeyers/obsidian-kanban); its README did not say whether lanes map to a note property, so use Bases when lanes must follow a note's state. Status lives once, in the task file's frontmatter. Pages hold the stable reasoning and link to task ids.

## Epics, sprints, boards

An epic is a large body of work broken into stories and delivered across several sprints; its scope may change, while a sprint is a time box (Source: [[atlassian-what-is-an-epic]]). A story belongs to one epic and at most one sprint, so one sprint naturally carries stories from several epics, and one epic spans several sprints. A board is only a view over this: the Scrum board shows the sprint, the epic groups the backlog. In a file tracker this means `epic` and `sprint` are two independent frontmatter fields on each task (inference, medium confidence).

## Rules that follow

1. One home for each fact: reasoning in a page, state in a task.
2. Link by stable id, both directions, so a rename breaks nothing.
3. Epics and sprints are separate fields, never nested folders.
4. Boards and reports are generated views, never edited as the source.
