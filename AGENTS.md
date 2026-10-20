# adlc: Agent Instructions

This repo is a Claude Code plugin **and** an Obsidian vault that builds persistent, compounding knowledge bases using Andrej Karpathy's LLM Wiki pattern. Cursor reads this file natively; Claude Code reads it alongside the auto-loaded skill descriptions. Codex CLI, OpenCode, and other Agent Skills-compatible hosts can use the skills via the symlink pattern below.

The skills follow the cross-platform Agent Skills spec. Frontmatter uses only `name` and `description` (no Claude-specific extensions).

## Project Structure

This single folder serves three roles simultaneously:

| Role | What lives here |
|---|---|
| Plugin source | `.claude-plugin/`, `agents/`, `hooks/`, `skills/`, `bin/` |
| Obsidian vault | `wiki/` (knowledge base), `.raw/` (immutable sources), `_attachments/` |
| Working repo | git history, `README.md`, `LICENSE`, `ATTRIBUTION.md` |

Open the entire project folder as the Obsidian vault root, not just `wiki/`. The `.obsidian/app.json` `userIgnoreFilters` (set on first open) hides plugin directories (`agents/`, `hooks/`, `skills/`) from the Obsidian sidebar, so the same folder cleanly serves as vault + plugin + repo without UI clutter.

## Skills Discovery

All skills live in `skills/<name>/SKILL.md`. Claude Code installs them via the plugin manifest (`.claude-plugin/plugin.json`); any Agent Skills-compatible host (Codex CLI, OpenCode, …) can pick them up by symlinking the directory into its own skill path:

```bash
ln -s "$(pwd)/skills" ~/.codex/skills/adlc
ln -s "$(pwd)/skills" ~/.opencode/skills/adlc
```

For the full skill list with trigger phrases, see [README.md](README.md). For individual skill behavior, read `skills/<name>/SKILL.md` directly.

## Subagents

Subagents (in `agents/<name>.md`) are dispatched by skills via the Agent tool with `subagent_type: "<name>"`. They run in their own context and return a single message — used for parallel batch work and context isolation.

| Subagent | Dispatched by | Purpose |
|---|---|---|
| `wiki-ingest-subagent` | `wiki-ingest` skill (batch mode, 3+ sources) | Process one source fully (read, extract, file pages); returns a summary |
| `wiki-lint-subagent` | `wiki-lint` skill (default for vaults ≥20 pages) | Read the whole vault and produce a structured lint report |
| `graphify-extract-subagent` | `graphify-ingest` and `graphify-update` skills | Read a chunk of files, extract entities/edges/hyperedges per the graphify schema, write JSON to disk |
| `research-subagent` | `autoresearch` skill (one per plan question) | Answer one research question: search, fetch, file source/entity/concept pages; returns a structured report |
| `mechanical-scanner-subagent` | `project-profile` skill | Scan project configs and return structured AGENTS.md mechanical sections |
| `ba-suite-subagent` | Mode ADLC ingest pass, `wrap-up` | Run one BA task with the bundled method docs; file deliverables as wiki Markdown with stable IDs |
| `architecture-subagent` | Mode ADLC technical-planning pass | Refine requirements into a per-service shift-left spec (Gates 1 / 1.5 / 2 / 3) in that service's code wiki |
| `ba-export-subagent` | `ba-export` skill | Render one wiki deliverable to Office / PlantUML under `.raw/exports/` |
| `scope-analyst` | `adlc` loop (census before the contract when scope is unknown; reconcile after review) | Measure a story's real scope against the code; propose plan revisions. Never rules, never writes feature code |
| `feature-builder` → `feature-tester` → `feature-reviewer` → `feature-verifier` → `doc-writer` | `adlc` loop, per story | The per-service build pipeline: build → test → review → verify → document |
| `devops` | `adlc` loop, optional, only on the operator's word | Push, PR, deploy through the service's documented path, then verify the deployed revision. Never touches infra or secrets, never rolls back on its own |

Skills handle orchestration; subagents handle isolated work.

## Key Conventions

- **Vault root**: the directory containing `wiki/` and `.raw/`
- **Hot cache**: `wiki/hot.md` (read at session start, updated at session end)
- **Source documents**: `.raw/` (immutable: agents never modify these)
- **Generated knowledge**: `wiki/` (agent-owned, links to sources via wikilinks)
- **Manifest**: `.raw/.manifest.json` tracks ingested sources (delta tracking)
- **Upstream intake**: reports from vaults that use the plugin arrive in `.raw/upstream/` (hand-delivered) or as GitHub issues titled `[upstream]`. When reviewing new proposals, check there, and in the co-located vaults' `wiki/meta/adlc-upstream.md`, not only this repo. File each report as a `wiki/questions/` page with `upstream: [<vault_key>/UP-nnn]`; a release that ships one adds a row to `skills/adlc/references/upstream-shipped.md`. **Redact at filing time** (`skills/wiki/references/adlc-upstream.md` § On the plugin side): a page, log line or shipped row carries no tracker ids, ledger or record page names, line numbers, commit hashes, URLs, concrete source paths, product or feature nouns, or a vault's directory name; a vault is its opaque key only, aliased here when its own key is not opaque. Before committing, run `python3 skills/wiki/scripts/upstream_redact_check.py --names "<the vault's names>" <touched files>` and fix every hit.

## Writing for the operator

Every reply, change report and wiki page a person reads in this repo follows `skills/wiki/references/writing-style.md`, the same method the plugin gives its vaults (`technical-writer` skill, `doc-writer`, the `/adlc` and `wrap-up` reports). In short: lead with the answer; say what changed and where, in plain words, with the id in brackets after the words, never an id alone and never a string of sprint, epic and ticket codes the reader has to translate; every code explained where it first appears; a lead-in before every table; totals as numbers; one line for what is assumed or unverified; no recap of the request and no filler. The operator should understand a report without the board, the ledger or a ticket open.

## Bootstrap

When the user opens this project for the first time:

1. Read this file (`AGENTS.md`) for full context.
2. Read `skills/wiki/SKILL.md` for the orchestration pattern.
3. If `wiki/hot.md` exists, read it silently to restore recent context.
4. If the user types `/wiki` (or "set up wiki"), follow the wiki skill's scaffold workflow.

## Cross-Project Access

To reference this vault as a knowledge base from another project, add to that project's `AGENTS.md`:

```markdown
## Wiki Knowledge Base
Path: /path/to/adlc

When you need context not already in this project:
1. Read wiki/hot.md first (recent context, ~500 words)
2. If not enough, read wiki/index.md
3. If you need domain specifics, read wiki/<domain>/_index.md
4. Only then read individual wiki pages

Do NOT read the wiki for general coding questions or things already in this project.
```

## MCP (Optional)

If you configure an Obsidian MCP server, an agent can read and write vault notes directly. See `skills/wiki/references/mcp-setup.md`.

## Reference

- Pattern source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Local copy of the LLM Wiki Pattern spec: [`.raw/llm-wiki-pattern-spec.md`](.raw/llm-wiki-pattern-spec.md)
- Cross-reference: https://github.com/kepano/obsidian-skills (authoritative Obsidian-specific skills)
