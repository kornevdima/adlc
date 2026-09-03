---
type: source
title: "Claude Code Docs: Set up Claude Code in a monorepo or large codebase (additional directories, sparse worktrees)"
source_type: documentation
author: "Anthropic — Claude Code documentation"
date_published: "2026 (living docs; fetched 2026-09-03)"
url: https://code.claude.com/docs/en/large-codebases
created: 2026-09-03
updated: 2026-09-03
confidence: high
tags:
  - source
  - documentation
  - claude-code
  - multi-repo
  - wiki-sharing
  - harness
status: current
related:
  - "[[Cross-Repo Wiki Access]]"
  - "[[AGENTS.md]]"
  - "[[Harness Engineering]]"
  - "[[Context Engineering for Coding Agents]]"
  - "[[github-docs-markdown-wikis-pages]]"
key_claims:
  - "Where you launch `claude` determines file access: from a subdirectory Claude sees that subtree only until granted more; from the repo root it sees every file"
  - "`permissions.additionalDirectories` in `.claude/settings.json` grants read and edit access to directories outside the working directory; relative paths resolve against the start directory; it never loads the directory's CLAUDE.md, rules, or skills"
  - "`--add-dir` at launch or `/add-dir` mid-session grants the same read/edit access for one session, loads that directory's skills, and loads its CLAUDE.md and `.claude/rules/` only when `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` is set"
  - "`worktree.sparsePaths` uses git sparse-checkout so `--worktree` sessions write only the listed directories plus root-level files; `symlinkDirectories` shares `node_modules`; both apply to worktrees of the same repository, not to other repositories"
  - "`Read` deny rules cover the built-in file tools and recognised Bash file commands (`cat`, `head`, `grep`, `find`) when a denied path is an argument; `grep -r` and `find` output can still list denied paths"
  - "An organisation that already runs a code-search or RAG index can expose it as an MCP tool so Claude queries it instead of reading files"
---

# Source: Claude Code docs — monorepos and large codebases

**Provenance**: official Claude Code documentation page "Set up Claude Code in a monorepo or large codebase" (code.claude.com), read 2026-09-03. Living page; version notes inside it mention v2.1.207 and v2.1.211 behaviour changes, so the content is from mid-2026. Two community pointers (GitHub issues #21138 and #23404 on anthropics/claude-code) document that `--add-dir` gained CLAUDE.md loading in v2.1.20 and skills loading in v2.1.32 before the docs caught up (medium).

Read for the agent-side half of [[Cross-Repo Wiki Access]]: how an agent working in one repository reaches the vault checked out elsewhere.

## Where you start decides what Claude can touch

| Start from | File access | CLAUDE.md loaded at launch |
|---|---|---|
| Repository root | Every file | Root only; subdirectory files load on demand |
| A subdirectory | That subtree only, until you grant more | That directory's plus every ancestor's |

Project settings (`.claude/settings.json`) are **not** inherited from parent directories the way CLAUDE.md files are. Implication for the vault pattern: a sibling checkout of the vault is outside the subtree by definition and needs an explicit grant.

## Granting access to a sibling package or another repository

"The same mechanism grants access to a separately-checked-out repository." Two forms:

1. **Committed**: `permissions.additionalDirectories` in `.claude/settings.json` (or personal `.claude/settings.local.json`):
   ```json
   { "permissions": { "additionalDirectories": ["../shared", "../web"] } }
   ```
   "Relative paths resolve against the directory you start Claude from." For sibling directories everyone needs, commit it; for a personal selection use the local file.
2. **Runtime**: `claude --add-dir ../shared` at launch, or `/add-dir` inside a session. Not persisted; the next session starts from the working directory again.

"However you add a directory, Claude can read and edit files in it." What else loads depends on the form:

| Added with | Loads CLAUDE.md and rules | Loads skills |
|---|---|---|
| `additionalDirectories` setting | Never | Never |
| `--add-dir` flag or `/add-dir` command | Only with `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` | Yes |

The environment variable has no effect on `additionalDirectories` entries. Skills discovered from an added sibling join the skill list Claude chooses from, and long lists get their descriptions shortened, so a vault added with `--add-dir` contributes its `.claude/skills/` to the session (relevant when the vault repo is also the plugin repo).

## Sparse worktrees (same repository only)

`--worktree` starts a session in a new git worktree; `worktree.sparsePaths` lists the directories to check out (repo-root-relative; root-level files always included; add `.claude` explicitly); `worktree.symlinkDirectories` shares heavy folders such as `node_modules`. Sparse checkout sets `extensions.worktreeConfig` in the repo's `.git/config` while a sparse worktree exists (removed automatically since v2.1.207 if Claude Code added it). Lists merge across scopes: a local file can add paths to the committed list but not remove them. This is a same-repo mechanism — it does not fetch another repository.

## Keeping irrelevant content out

- `claudeMdExcludes` skips specific CLAUDE.md/rules files by glob (absolute-path matching; start relative patterns with `**/`). Managed-policy files cannot be excluded.
- `permissions.deny` `Read(...)` rules block reads of vendored or generated paths; relative patterns anchor at the session's cwd, so use `Read(//abs/path/**)` when starting from subdirectories. Before v2.1.211 `.claude/settings.local.json` loaded only from the starting directory.
- Content searches respect `.gitignore` by default.
- Code-intelligence plugins (`/plugin install typescript-lsp@claude-plugins-official`) replace scan-and-grep with language-server lookups.
- "If your organization already runs a code search or RAG index over the repository, expose it as an MCP tool so Claude queries it instead of reading files directly."

## Cross-package changes

Give Claude the whole cross-package change in one session; plan first in plan mode — the plan file is re-injected after each context compaction, so it survives where conversation history may not.

> [!note] Why this matters for the vault
> The vault's [[AGENTS.md]] pointer ("Wiki Knowledge Base — Path: ~/path/to/vault") tells the agent *where* the wiki is and *how* to read it (hot → index → sub-index → page), but Claude Code will not read or write outside the start directory until the path is granted. The grant is the missing half of the pattern: commit `additionalDirectories: ["../<vault>"]` alongside the pointer, or pass `--add-dir` per session. See [[Cross-Repo Wiki Access]].
