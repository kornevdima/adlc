---
type: source
title: "GitHub Docs: Markdown rendering, repository Wikis, and Pages (as vault-sharing surfaces)"
source_type: documentation
author: "GitHub Docs (docs.github.com), plus community pointers"
date_published: "2026 (living docs; fetched 2026-09-03)"
url: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
created: 2026-09-03
updated: 2026-09-03
confidence: high
tags:
  - source
  - documentation
  - github
  - markdown
  - wiki-sharing
  - publishing
status: current
related:
  - "[[Cross-Repo Wiki Access]]"
  - "[[Wiki Sharing Patterns]]"
  - "[[wiki-sharing-research]]"
  - "[[claude-code-large-codebases-docs]]"
  - "[[okf-spec-and-reference-repo]]"
key_claims:
  - "github.com renders exactly five alert types (NOTE, TIP, IMPORTANT, WARNING, CAUTION) from `> [!TYPE]`; any other marker such as `[!gap]` is an ordinary blockquote with the marker shown as text"
  - "Relative links in repository Markdown resolve relative to the current file and current branch; a leading `/` is repo-root; `./` and `../` work; the docs say nothing about spaces, which CommonMark requires to be `%20`-encoded"
  - "A repository Wiki is a separate git repository at `<repo>.wiki.git`; the first page must be created in the web UI before the repo can be cloned; the filename is the page title and `\\ / : * ? \" < > |` are forbidden"
  - "Footnotes are not supported in wikis (docs); wikis use GitHub's open-source Markup library and pick the converter by file extension"
  - "GitHub Pages builds with Jekyll by default; Jekyll consumes YAML front matter natively but skips `_`-prefixed and dot-prefixed files, and access-controlled (private) Pages sites exist only on GitHub Enterprise Cloud"
---

# Source: GitHub Docs on Markdown rendering, Wikis, and Pages

**Provenance**: docs.github.com (three pages fetched or cited), one GitHub community discussion, GitHub Marketplace actions, Obsidian community plugins. Living documentation: facts below reflect the pages as read on 2026-09-03. Fetched directly: *Basic writing and formatting syntax* and *Adding or editing wiki pages*. Cited from memory of the docs, marked medium: *About wikis*, *Changing the visibility of your GitHub Pages site*.

Read for [[Cross-Repo Wiki Access]] (question Q5 of the "Sharing the Wiki with People" research), specifically: which of the vault's Obsidian conventions survive each GitHub surface.

## 1. github.com file view (repository Markdown)

- **Alerts.** Syntax `> [!NOTE]` on its own line, then the quoted body. Supported types: NOTE, TIP, IMPORTANT, WARNING, CAUTION — five, no custom types (high, docs). The docs show the keyword upper-case and do not say whether it is case-sensitive; in practice lower-case `[!note]` also renders as an alert (medium, not stated in docs). A vault-specific marker such as `> [!gap]` is therefore just a blockquote with the literal text `[!gap]` in it (high, follows from the five-type list). Obsidian's title-on-the-marker-line form (`> [!note] Operational protocol shipped`) is not the GitHub form, where the marker stands alone on its first line; expect it to fall back to a plain blockquote (medium).
- **Relative links.** "GitHub will automatically transform your relative link or image path based on whatever branch you're currently on, so that the link or path always work. The path of the link will be relative to the current file." Leading `/` means repository root; `./` and `../` are supported (high, docs). Spaces in paths: the docs are silent; per CommonMark a destination with spaces must be `%20`-encoded or wrapped in `<...>` (high for the CommonMark rule, medium that github.com has no leniency).
- **Section anchors.** Generated from headings: lower-cased, spaces to hyphens, other punctuation removed; custom `<a name="...">` anchors are allowed but not shown in the outline (high, docs). So Obsidian's `[[Page#Heading Here]]` maps to `page.md#heading-here`.
- **YAML front matter.** Not mentioned on the formatting page. github.com renders a leading `---` block of a `.md` file as a key/value table above the body — long-standing behaviour that a 2025-2026 community discussion (#178337, "Improve display of YAML frontmatter in Markdown previews") asks GitHub to improve (high that it renders as a table; medium on how list-valued keys look inside cells).
- **`[[wikilinks]]`.** Not part of GitHub Flavored Markdown; in repository files they render as literal `[[text]]` (high).
- **Folder landing.** github.com shows a folder's `README.md` under the file list; an `index.md` or `_index.md` gets no special treatment (high). Dot-folders such as `.raw/` are visible in the tree like `.github/` (high).
- **Footnotes** `[^1]` are supported in repository Markdown but "Footnotes are not supported in wikis" (high, docs).

## 2. Repository Wiki

- "Wikis are part of Git repositories, so you can make changes locally and push them to your repository using a Git workflow." Clone with `git clone https://github.com/USER/REPO.wiki.git`. "Once you've created an initial page on GitHub, you can clone the repository" — the wiki must be initialised from the web first (high, docs).
- "The filename determines the title of your wiki page." Forbidden characters in titles: `\ / : * ? " < > |` (high, docs). Spaces are allowed in titles; URLs show them as hyphens (medium).
- Converter chosen by file extension via GitHub's Markup library (`.md` Markdown, `.textile` Textile, and others); the editor's "Edit mode" dropdown selects the format (high, docs).
- MediaWiki-style `[[Page Name]]` links are supported in wiki pages and resolve by page title across the whole wiki, which behaves as a flat namespace even when files sit in sub-folders of the wiki repo (medium — long-standing behaviour, not on the page fetched). The aliased form's argument order differs from Obsidian historically (`[[text|Page]]` vs Obsidian's `[[Page|alias]]`) — verify before relying on aliases (low).
- `_Sidebar.md` and `_Footer.md` customise the sidebar and footer on every page; `Home.md` is the landing page (medium — widely documented, not on the page fetched). The wiki has its own "Search this wiki" box; GitHub's global search also has a Wikis result type (medium).
- Permissions follow the repository: private-repo wikis are visible only to collaborators; by default only people with write access can edit, and public repos can open editing to everyone. Wikis on **private** repositories require a paid plan (Pro, Team, Enterprise Cloud/Server); Free plans get wikis on public repos only (medium — *About wikis*, from memory of the docs).
- **CI mirroring.** The wiki repo has no Actions of its own, but a workflow in the main repo can push a folder into `<repo>.wiki.git`. Marketplace actions doing exactly this: `Andrew-Chen-Wang/github-wiki-action` (folder to wiki; a PAT is needed only when targeting *another* repo's wiki), `kawamataryo/github-wiki-sync-actions` (bidirectional, `conflict-strategy` option, uses `secrets.GITHUB_TOKEN`), `newrelic/wiki-sync-action`, `marjane-connect/action-wiki-sync` (medium — action READMEs, not GitHub docs). The web-first initialisation rule still applies.

## 3. GitHub Pages

- Default build is Jekyll from a branch root or `/docs` folder; Jekyll consumes YAML front matter natively (it is Jekyll's own convention), copies files without front matter verbatim, and **skips files and folders whose names start with `_` or `.`** unless listed under `include:` in `_config.yml` — so `_index.md` and `.raw/` would not be published by default (high, Jekyll behaviour).
- GitHub's built-in Jekyll build only allows a fixed allow-list of plugins; a wikilink plugin (e.g. `jekyll-wikilinks`) or any other generator (Quartz, MkDocs, Obsidian Digital Garden templates) needs a custom Actions workflow that builds and uploads the site artifact (high for the allow-list, medium for the plugin names).
- Obsidian-side publishers that rewrite `[[wikilinks]]` to relative links before pushing to a Pages repo: the *GitHub Pages share* community plugin ("converts Obsidian wikilinks to relative links on the published page"), *Enveloppe* (formerly obsidian-github-publisher; converts wikilinks to markdown links, targets MkDocs/Jekyll/Hugo), `adriansteffan/obsidian-to-jekyll` (medium — plugin listings).
- **Visibility.** Pages sites are public on Free/Pro/Team even when the repository is private; access-controlled ("private") Pages for private and internal repositories exist only on GitHub Enterprise Cloud (high — *Changing the visibility of your GitHub Pages site*, from memory of the docs). Publishing Pages from a private repo at all requires a paid plan (high).

> [!gap] Not verified against the docs on this pass
> Case-insensitivity of alert markers; how the Wiki renders a leading YAML block (raw text vs table); whether `GITHUB_TOKEN` can push to the same repo's wiki without a PAT (the action READMEs suggest yes); the current argument order of aliased wiki links. Each is marked medium or low above.

## Pointers (not fetched)

- GitHub community discussion #178337 — front matter shown as a table in previews.
- GitHub Docs *Using YAML frontmatter* — describes the docs team's own front-matter conventions, not github.com rendering; easy to confuse with the rendering question.
