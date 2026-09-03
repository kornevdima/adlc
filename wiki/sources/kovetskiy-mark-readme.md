---
type: source
title: "kovetskiy/mark — Sync your markdown files with Confluence pages (README)"
source_type: github-readme
author: "Egor Kovetskiy and contributors"
date_published: 2025
url: "https://github.com/kovetskiy/mark"
created: 2026-09-03
updated: 2026-09-03
confidence: high
tags:
  - source
  - confluence
  - docs-as-code
  - git-sync
  - cli
  - github-actions
status: current
related:
  - "[[git-backed-wiki-platforms-comparison]]"
  - "[[One-Way Publish vs Round-Trip Wiki Sync]]"
  - "[[Wiki Sharing Patterns]]"
key_claims:
  - "mark is strictly one-way: it reads markdown, creates or updates the Confluence page via REST API, and never pulls Confluence edits back to files"
  - "Page placement is driven by metadata in the markdown itself — YAML front matter (space, parents, folders, title, attachments, labels) or legacy HTML-comment headers — so a vault that already carries frontmatter can drive Confluence placement from it"
  - "Relative links to other markdown files are rewritten to Confluence tiny links that survive page renames; --check-links internal validates them before publish"
  - "GitHub-style alert blockquotes are converted to Confluence info / tip / note / warning macros; custom macros can be defined with regex + template"
  - "Missing parents are created on the fly; changing a Parent header moves the page; Folders are Confluence Cloud only"
  - "Maintenance is explicitly low-priority ('I don't really prioritize working on this project in my free time'); v16.x, ~1.6k stars, 85 open issues at fetch time"
---

# Source: kovetskiy/mark README

**Repo**: [github.com/kovetskiy/mark](https://github.com/kovetskiy/mark) | **Language**: Go | **Distribution**: binary, Docker image `kovetskiy/mark:latest` | **Fetched**: 2026-09-03

## Summary

"Mark — a tool for syncing your markdown documentation with Atlassian Confluence pages." It reads a markdown file, finds the target page by space + title (creating it if absent), uploads attachments, converts markdown to Confluence storage-format HTML, and updates the page via the REST API. It is the longest-lived tool in the git-to-Confluence niche (created 2015) and the one whose README documents the most edge cases.

## Metadata: how a file says where it lives

Two equivalent formats. With the `frontmatter` feature enabled:

```yaml
---
space: KEY
parents: [Parent One, Parent Two]
folders: [Folder A]
title: Page Title
attachments: [diagrams/flow.png]
labels: [adlc, wiki]
---
```

Legacy form is HTML comments at the top of the file (`<!-- Space: KEY -->`, `<!-- Parent: ... -->`, `<!-- Title: ... -->`, `<!-- Attachment: ... -->`, `<!-- Label: ... -->`), plus optional `Property`, `Layout`, `Type` and `Order` headers.

Relevance to this vault: the wiki's pages already carry YAML frontmatter (`type`, `title`, `tags`, `status`). A CI lowering step could derive `space` from the vault, `parents` from the folder path, and `labels` from `tags` without touching page bodies. (Synthesis, not in the README.)

## Page tree

Multiple `parents` entries produce a nested chain; "If Mark can't find specified parent by title, Mark creates it." Changing the parent header moves the existing page. Folders (Cloud-only) and parents can be mixed. Page identity is space + title, so **renaming a page's title creates a new Confluence page** rather than moving the old one — a known consequence of title-keyed identity (synthesis from the mechanism; the README does not state it as a warning).

## Links, alerts, macros

- "A relative link to another Markdown file is replaced with a link to the Confluence page that file publishes." Links are resolved to tiny links that survive page renames. `--check-links internal` validates references pre-publish.
- GitHub-style alert syntax (`> [!NOTE]`, `> [!TIP]`, `> [!WARNING]`, `> [!IMPORTANT]`, `> [!CAUTION]`) converts to Confluence macros. Basic Obsidian callouts share this shape; Obsidian-only types (e.g. `[!gap]`, `[!example]`) and fold / title syntax are outside the supported set (synthesis).
- Built-in templates: status badges, info / tip / note / warning boxes, Jira tickets, YouTube widgets. Custom macros via regex pattern + template.
- `[[wikilinks]]` are not mentioned anywhere in the README; treat as unsupported.

## CI usage

Find all `*.md` files and run mark against each; `--output-format github` emits GitHub Actions workflow commands so failures annotate the offending file in a pull request. The README's recommended flow: push freely to feature branches (nothing publishes), review via PR, publish on merge — i.e. the git branch model gates what reaches Confluence.

## Sync direction

One-way. Markdown is the source of truth; the tool updates pages and never reads them back. UI edits in Confluence are overwritten on the next publish. `--preserve-comments` attempts to keep Confluence inline comments across republishes, with the limitation that "links to deleted commented text cannot be relocated".

## Compatibility and limitations

- Confluence Cloud and Server / Data Center; Folders are Cloud-only.
- Labels are not applied when `--minor-edit` is used.
- Images ≥ 760 px wide are centred regardless of alignment settings.
- MathJax-unparseable formulas fail the whole file.

## Maintenance state

v16.x at fetch time; ~1.6k stars; 85 open issues. The maintainer states: "I don't really prioritize working on this project in my free time" and welcomes contributions. An ecosyste.ms snapshot surfaced by search reported 1,108 stars and last push 2025-05-07 — stale relative to the README page, but consistent with a slow cadence. Treat as **usable but unhurried**: fine for a CI step you can pin, risky as a dependency you expect to evolve.

## Related tools (not fetched)

- `markdown-confluence/markdown-confluence` — NPM CLI + `markdown-confluence/publish` GitHub Action; Obsidian-origin project, claims wikilink and callout support (unverified).
- `Telefonica/markdown-confluence-sync-action` — create / update / delete from a directory.
- `axro-gmbh/markdown-to-confluence-sync` — file or folder under a parent page; first `# ` heading as title.
- Atlassian Marketplace "GitHub Markdown Sync for Confluence" — repo / branch / path, hourly sync + webhook.

See [[git-backed-wiki-platforms-comparison]] for how these sit against Wiki.js, GitBook, Docmost, Outline, BookStack and TechDocs.
