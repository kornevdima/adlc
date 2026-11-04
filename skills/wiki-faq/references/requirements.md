# Requirements

What you need installed before adlc is useful. Most of this is optional: a vault's `AGENTS.md` carries a `Toolset:` block naming its reader, its code-navigation tool and its design tools, and you install only what that block names. `python3 <plugin>/skills/wiki/scripts/toolset.py --vault . check` lists what is missing with the install line for each. Options and defaults: `skills/wiki/references/toolset.md`.

## Host (the AI coding agent that loads adlc)

adlc is primarily a Claude Code plugin but the skills follow the cross-platform Agent Skills spec. Pick one:

| Host | Status | How it loads |
|---|---|---|
| **Claude Code** | Primary | Plugin install via local marketplace, GitHub marketplace, or `--plugin-dir`. See `README.md` install section. |
| **Cursor** | Supported | Reads `AGENTS.md` natively. Symlink `skills/` into `~/.cursor/skills/adlc` or use Cursor's plugin loader. Hooks ship with the plugin in `hooks/cursor-hooks.json` (declared in `.cursor-plugin/plugin.json`). |
| **Codex CLI** | Supported | `ln -s "$(pwd)/skills" ~/.codex/skills/adlc` |
| **OpenCode** | Supported | `ln -s "$(pwd)/skills" ~/.opencode/skills/adlc` |
| **GitHub Copilot** (cloud / CLI / JetBrains preview) | Hooks supported | Reads `AGENTS.md` natively. Plugin install via `.github/plugin/marketplace.json`; hooks ship in `hooks/copilot-hooks.json`. |

The `wiki/`, `wiki-ingest`, `wiki-query`, `wiki-lint`, `save`, `autoresearch`, `project-profile`, `obsidian-markdown`, `obsidian-bases`, `wiki-faq` skills work in any of these. The `graphify-*` skills additionally need Python (see below).

## A reader (optional: `reader` in the toolset)

The wiki is plain Markdown with YAML frontmatter, so any editor shows it. Two readers render the Obsidian-flavoured parts (wikilinks, embeds, callouts, Mermaid):

- **Obsidian** (`reader: obsidian`, the default for vaults without a block). Any version 1.7+ works; 1.12+ adds the native CLI.
  - macOS: `brew install --cask obsidian` or download from [obsidian.md/download](https://obsidian.md/download)
  - Linux: `flatpak install flathub md.obsidian.Obsidian`
  - Windows: `winget install Obsidian.Obsidian`

  adlc ships **no bundled Obsidian plugins or themes**. The first time you open a project folder in Obsidian it creates a fresh `.obsidian/` config; install whatever community plugins you want. Bases (`.base`), Canvas (`.canvas`) and Dataview dashboards are Obsidian-only artefacts; the skills write them only for this reader.
- **wiki-renderer** (`reader: wiki-renderer`): a local web app that reads the vault from its folder, renders it and saves edits back (MIT, https://github.com/kornevdima/wiki-renderer). Install with `curl -fsSL https://raw.githubusercontent.com/kornevdima/wiki-renderer/main/install.sh | sh`, then `wiki-renderer add <vault root>` and `wiki-renderer` (opens `http://127.0.0.1:4700`; binds to localhost only, no sign-in).
- **none**: nothing to install; read the files in your editor.

## Code navigation (optional: `code-nav` in the toolset)

The workers find and read code with the tool the block names. `graphify` builds a structural graph per project; `semble` and `serena` are MCP servers installed once per machine, with nothing to build per project.

### Semble and Serena (`code-nav: semble, serena`)

```bash
claude mcp add -s user semble -- uvx --from "semble[mcp]==0.7.0" semble
claude mcp add -s user serena -- serena start-mcp-server --context=claude-code --project-from-cwd
```

Semble needs `uv` (`uvx` on `PATH`); it indexes a repository on first search and caches the index. Serena needs its CLI on `PATH` (install per https://github.com/oraios/serena) and reads code through the language server of each language it supports. Add the `mcp__semble__*` and `mcp__serena__*` allow lines from `toolset.md` § Permissions to the vault's `.claude/settings.json`.

### The JetBrains IDE server (`code-nav: idea`)

IntelliJ IDEA 2025.2 and later ship an MCP server, bundled and on by default. In the IDE: Settings | Tools | MCP Server, then **Auto-Configure** for Claude Code; it registers the server as `idea` (HTTP stream on the IDE's built-in web server port). It answers only while the IDE runs with the project open, and every call carries `projectPath`; a delivery vault that symlinks its services into `services/` is one open project that covers them all. It gives signatures with resolved types and doc comments, the call hierarchy, the IDE's inspections and a reference-aware rename, and it reads the scripts inside HTML files; it has no file overview and no Python call hierarchy, so vaults that need those, or that sometimes run without the IDE, keep `serena` beside it. Add the read-set allow lines from `toolset.md` § Permissions, never a bare `mcp__idea__*`.

### graphify (`code-nav: graphify`): Python

graphify is a Python library (`graphifyy` on PyPI) that powers the structural code-graph layer. Required only if you use:

- `/graphify-ingest`
- `/graphify-update`
- `/graphify-query`
- `/graphify-path`
- `/graphify-explain`

**Version constraint: Python `>=3.10,<3.14`.** Python 3.14 is excluded because some of graphify's dependencies don't yet support it.

Recommended install via [pyenv](https://github.com/pyenv/pyenv):

```bash
pyenv install 3.13
pyenv global 3.13
```

Or Homebrew on macOS:

```bash
brew install python@3.13
```

Then run the bundled installer **once per project** the first time you graphify it:

```bash
bash bin/setup-graphify.sh /path/to/your-code-project
```

This:
1. Detects a compatible Python on the system
2. Installs `graphifyy` via pip / `--user` / `--break-system-packages` / venv (in that fallback order)
3. Pins the resolved interpreter path to `<project>/graphify-out/.graphify_python` so all subsequent skill runs use the same one

If you skip `bin/setup-graphify.sh`, the first `/graphify-ingest` runs it for you; later runs reuse the pinned interpreter and skip the installer. When the vault's block names a `code-nav` without graphify, the graphify skills refuse to run and say so.

## Design tools (optional: `design` and `design-system` in the toolset)

The `feature-designer` worker runs only when the block names a tool:

```bash
claude plugin marketplace add pbakaus/impeccable && claude plugin install impeccable@impeccable
claude plugin marketplace add leonxlnx/taste-skill && claude plugin install taste-skill@taste-skill
```

`design-system` is the folder that holds your brand book, tokens and `DESIGN.md` (impeccable's summary; `impeccable document` generates one from an existing codebase). The designer reads its dated rulings as law and the tools' heuristics as advice.

## Git (recommended)

adlc hooks (`SessionStart` load hot cache, `Stop` refresh hot cache) and graphify's manifest tracking work best in a git working tree. None of the skills *require* git, but several of them recommend it for change tracking.

## What you do NOT need

- **Node.js / npm**: not used. (We dropped the `defuddle` skill and its npm dep.)
- **An MCP server for the vault**: optional, and only with `reader: obsidian`. `skills/wiki/references/mcp-setup.md` describes adding an Obsidian MCP server if you want agents to read/write the vault through it. The skills write files directly and work without it; wiki-renderer re-reads the folder on its own.
- **Obsidian itself**: only when the toolset says `reader: obsidian`.
- **graphify**: only when the toolset says `code-nav: graphify`.
- **GitHub Copilot setup files**: not required — the existing `AGENTS.md` is enough. The plugin's Copilot hooks come with the plugin install.

## Verifying the install

After install:

- Open Claude Code, Cursor, or your host of choice in this repo.
- Run `/wiki-faq` (this skill) to confirm the skill registry is loaded.
- Run `python3 <plugin>/skills/wiki/scripts/toolset.py --vault . check` in a vault: every line should read `ok`.
- For graphify: run `/graphify-ingest` on a small code project to confirm the Python path resolves.
- For hot cache: `wiki/hot.md` should print at the top of every new session in this repo (the `SessionStart` hook does this).
