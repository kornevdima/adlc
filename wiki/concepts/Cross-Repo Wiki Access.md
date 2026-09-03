---
type: concept
title: "Cross-Repo Wiki Access"
created: 2026-09-03
updated: 2026-09-03
tags:
  - wiki-sharing
  - github
  - multi-repo
  - publishing
  - design-decision
status: developing
related:
  - "[[Wiki Sharing Patterns]]"
  - "[[AGENTS.md]]"
  - "[[Hot Cache]]"
  - "[[Harness Engineering]]"
sources:
  - "[[github-docs-markdown-wikis-pages]]"
  - "[[claude-code-large-codebases-docs]]"
  - "[[wiki-sharing-research]]"
  - "[[agents-md-spec]]"
  - "[[okf-spec-and-reference-repo]]"
---

# Cross-Repo Wiki Access

How a vault that lives in its own GitHub repository (the **source of truth**, read and written by agents through git) is reached by two audiences that are not in that repository: **people** who want to browse it like Confluence, and **agents working in another repository**. Companion to [[Wiki Sharing Patterns]], which compares tools and topologies; this page is about the GitHub surfaces and the git plumbing specifically.

The vault's conventions that any route has to survive: YAML front matter on every page; `[[wikilinks]]` resolved by basename; Obsidian callouts including a custom `> [!gap]`; folder and file names with spaces and mixed case; `_index.md` per folder; `index.md` / `log.md` / `hot.md`; a generated `index.json`; a hidden `.raw/` of immutable sources beside `wiki/`.

## Part A — people browsing on GitHub

Three surfaces, none of which speaks Obsidian natively (Source: [[github-docs-markdown-wikis-pages]]):

1. **github.com file view.** Zero setup; permissions are the repo's. Renders GitHub Flavored Markdown: five alert types, relative links resolved per file and branch, front matter shown as a key/value table. `[[wikilinks]]` stay literal text — the navigation the wiki is built on does not work, though full-text search and the file tree do.
2. **Repository Wiki.** A separate repo at `<repo>.wiki.git`, initialised from the web first. Supports `[[Page Name]]` links resolved by title in a flat namespace (which matches the vault's resolve-by-basename rule), a `_Sidebar.md`, a `Home.md` landing page, its own search box. Visibility follows the repo; private-repo wikis need a paid plan. Can be **filled by CI** — marketplace actions push a folder from the main repo into the wiki repo on every merge.
3. **GitHub Pages.** Jekyll by default, which consumes front matter natively but drops `_`- and dot-prefixed files and cannot run a wikilink plugin without a custom Actions build. Private (access-controlled) sites only on GitHub Enterprise Cloud; everywhere else a Pages site is public even from a private repo — a hard stop for an internal wiki on a Team plan.

### What breaks where, and the cheapest fix

| Vault convention | github.com file view | Repository Wiki | GitHub Pages (default Jekyll) | Cheapest mitigation |
|---|---|---|---|---|
| YAML front matter | Rendered as a table above the body — noisy, harmless | Probably shown raw (unverified) | Consumed natively; unknown keys ignored | None for github.com; strip or map at publish for the Wiki |
| `[[wikilinks]]` by basename | Literal text, no link | Works — same basename semantics; alias order may differ (low) | Literal text unless a plugin + custom build | Rewrite to relative `.md` links at publish time — `okf_export.py::rewrite_links` already does this (`[[Page\|alias]]` → `[alias](../dir/Page.md)`, unresolved targets degrade to plain text) |
| `> [!note]` callouts | Renders as an alert if the marker is alone on its line and the type is one of five | Same renderer (medium) | Plain blockquote, marker shown as text | Publish-time map: `[!gap]` → `[!WARNING]`, move Obsidian titles to a bold first line, keep the five types |
| Spaces / mixed case in paths | Browsing fine; Markdown links need `%20` | Spaces become hyphens in page URLs; folders flatten, so basenames must be unique (they already are) | URL-encoded; slugs usually preferred | Keep the names; encode link targets when rewriting |
| `_index.md` per folder | Ordinary file, no folder landing | `_`-prefixed names are the wiki's own special files (`_Sidebar`) — risky | **Not published** by default (`_` prefix) | Rename to `README.md` (github.com) / `Home.md` (Wiki) / `index.md` (Pages) in the mirror, or Jekyll `include:` |
| `index.md`, `log.md`, `hot.md` | Files; only `README.md` is a folder landing | `Home.md` is the landing | `index.md` becomes `/index.html` — natural | Copy `index.md` → `README.md` / `Home.md` in the mirror |
| `index.json` locator | JSON viewer | Not a wiki page; harmless | Copied verbatim | None |
| Hidden `.raw/` | Visible in the tree like `.github/` | Not mirrored unless you push it | Excluded (dot prefix) | Mirror `wiki/` only; never publish `.raw/` on a public Pages site |
| Dataview / Bases / `![[embeds]]` | Nothing renders | Nothing | Nothing | Keep them out of pages meant for sharing, or pre-render tables |

The pattern across all three columns: the vault is fine as a **source**, and each surface wants a **derived view**. The exporter that already exists for OKF — `skills/wiki/scripts/okf_export.py` builds a filename-stem → path map, rewrites every `[[wikilink]]` to a relative Markdown link, and counts unresolved targets — is most of a "GitHub mirror" publisher; the remaining work is the callout map, the `_index.md` → landing-file rename, and a workflow that pushes the output to `.wiki.git` (or to a Pages artifact). Same idea as the OKF rule that consumers get "standard markdown links only" (Source: [[okf-spec-and-reference-repo]]).

> [!note] Cheapest viable route for a private team on a non-Enterprise plan
> github.com browsing of the source repo, plus a CI-mirrored repository Wiki for the Confluence-like experience (`[[links]]`, sidebar, search, repo permissions). Pages is only worth it on Enterprise Cloud or for a wiki that may be public.

## Part B — an agent in another repository

The agent needs two things: a **path** to the vault and a **grant** to read/write outside its own repo. The vault's [[AGENTS.md]] "Wiki Knowledge Base" section supplies the first (`Path: ~/path/to/vault`, then hot → index → sub-index → page, and a do-not-read list); Claude Code's directory grants supply the second (Source: [[claude-code-large-codebases-docs]]). The pointer alone is not enough — Claude Code starts with access to the start directory's subtree only.

| Route | Freshness | Write access | CI / setup cost | Verdict |
|---|---|---|---|---|
| **Sibling clone + AGENTS.md pointer** (current practice) | `git pull` before the session (the pull-first habit in `skills/wiki/references/team-sync.md`) | Full: commit and push to the vault repo | None; path is machine-local, so the pointer must stay a `~`-style or relative path, never a teammate's absolute path | Default |
| `--add-dir` / `/add-dir` | Same as the clone it points at | Read and edit | Zero, per session, not persisted; also loads the vault's skills | Pair with the sibling clone for one-off sessions |
| `additionalDirectories` in `.claude/settings.json` | Same | Read and edit | One committed line, relative to the start dir, so it holds team-wide only with a shared layout (`../<vault>`); never loads the vault's CLAUDE.md or skills | Pair with the sibling clone for standing access |
| git submodule | Pinned commit; stale until `git submodule update --remote` plus a pointer-bump commit in the consumer | Possible but two commits per change (push in submodule, bump in parent) | CI checkout needs `submodules: true`; reproducible | Only when a consumer needs a pinned, reproducible snapshot |
| git subtree | Copy in-tree; `subtree pull/push` are merges that drift silently | Two-way but easy to fork off | No special CI | Worst fit for a single source of truth |
| Sparse checkout of the vault repo (`git sparse-checkout set wiki`) | Full on pull; skips `.raw/` | Full | One command per machine; note Claude Code's `worktree.sparsePaths` is same-repo only | Good when `.raw/` is large |
| MCP server over the vault | Live | Tool-mediated | A server to run and configure | Deferred in the roadmap; the docs endorse MCP for an existing index |

Recommended combination: sibling clone as the transport, the AGENTS.md pointer as the reading protocol, and `permissions.additionalDirectories: ["../<vault>"]` committed in the consuming repo (or `--add-dir` when the layout varies). Freshness is a habit, not a mechanism — pull first, wrap up last — which is why the submodule's pinning looks safer but costs a bump commit every time the wiki moves.

> [!gap] Open
> Whether `GITHUB_TOKEN` alone can push into the same repo's wiki from Actions (action READMEs say yes; not confirmed in GitHub docs); how the Wiki renders a leading YAML block; the alias argument order in Wiki links; whether a "GitHub mirror" mode belongs in `okf_export.py` or a sibling script. Field feedback from the first CI-mirrored wiki should settle the first three.
