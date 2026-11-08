# Toolset: the reader, code navigation, design tools, layout, engineering method and cost plugin a vault uses

A vault declares which reader shows its pages, which tool its workers navigate code with, which design tools its design worker runs, where its services' code and code wikis live, which engineering method gates a code change, and whether a cost plugin trims its sessions. The plugin ships defaults (Obsidian, graphify, no design tool) but requires none of them: a vault read in wiki-renderer, navigated with Semble and Serena or with the JetBrains IDE's own MCP server, and reviewed with impeccable works the same way. The declaration is a `Toolset:` block in the vault's `AGENTS.md`, beside `Mode:` and `Concerns:`. Every skill and worker that used to assume Obsidian or graphify reads this block first.

## The block

The scaffold writes it (wiki skill, step 3a) from `toolset.py detect` and the operator's answers. Edit it by hand to change a choice later. The block is the team's tool choice, one of the four decision levels in [`records.md`](records.md): a tool selection is never a page in `decisions/` or an ADR unless reversing it would cost more than a story; a change to the block is one row in the vault's changelog. The rest of the team's choices (branching, review, the definition of done) is the `## How we work` section beside it.

```markdown
Mode: ADLC
Concerns: qa, design
Toolset:
  reader: wiki-renderer
  code-nav: semble, serena
  design: impeccable, taste-skill
  design-system: ~/work/design-system
  layout: worktrees
  engineering: ub-mode
  cost: tokeneconomizer
```

Rules:

- Seven keys, all optional: `reader`, `code-nav`, `design`, `design-system`, `layout`, `engineering`, `cost`. A missing key takes the default from the table below; a missing block takes every default, which is how vaults created before 1.1.0 behave. The last three came in 1.2.0, and their defaults are what every vault did before.
- `code-nav` and `design` take one or more values, comma-separated. `none` is a value.
- `design-system` is a folder path (`~` allowed) or `none`. Everything else is a word from the options list.
- The one-line form `Toolset: reader=wiki-renderer; code-nav=semble,serena` is accepted too, for vaults that keep the header compact.
- `python3 <plugin>/skills/wiki/scripts/toolset.py --vault . show` prints the resolved choices; `check` tells you which chosen tools are installed; `detect` proposes a block from what the machine has; `code-wiki <service>` prints where that service's code wiki is for the vault's layout.

## Slots, options and defaults

The slots and what each one decides:

| Slot | Options | Default when absent | Decides |
|---|---|---|---|
| `reader` | `obsidian`, `wiki-renderer`, `none` | `obsidian` | Which reader-only artefacts the skills write (Bases, Canvas, Dataview, `.obsidian/app.json`, `board.base` beside `board.md`, `context.canvas` beside `product/context.md`), what the scaffold tells the operator to open, whether the Obsidian MCP notes apply |
| `code-nav` | `graphify`, `semble`, `serena`, `idea`, `none` (several allowed) | `graphify` when the service has `graphify-out/graph.json`, else `none` | How workers find and read code, how `wiki-query` answers structural questions, whether the graph skills and the graph refresh run |
| `design` | `impeccable`, `taste-skill`, `none` (several allowed) | `none` | Whether the `feature-designer` worker is dispatched and which design skills it runs |
| `design-system` | a folder path, `none` | `none` | Where the designer reads the brand book, tokens and dated rulings |
| `layout` | `symlinks`, `worktrees` | `symlinks` | Whether services are separate repositories linked into `services/` with their code wiki inside, or branches of the vault's repository checked out as worktrees with their code wikis in `service-wikis/` |
| `engineering` | `ub-mode`, `none` | `none` | Whether code changes follow the ub-mode skill and its three tool gates, which the service `AGENTS.md` then lists as its definition of done |
| `cost` | `tokeneconomizer`, `none` | `none` | Whether the TokenEconomizer plugin trims the operator's sessions (unused tools, learned repository facts, stuck-turn notes) |

The Markdown dialect does not change with the reader. Pages stay Obsidian-flavoured Markdown (`[[wikilinks]]`, `![[embeds]]`, `> [!note]` callouts, Mermaid blocks, YAML frontmatter), which Obsidian and wiki-renderer both render and which any editor shows as plain text. The `obsidian-markdown` skill stays the dialect reference for every reader.

## Reader

What changes with each reader:

| Where | `obsidian` | `wiki-renderer` or `none` |
|---|---|---|
| Scaffold, last step | "Open the project folder in Obsidian" | `wiki-renderer add <vault root>` then `wiki-renderer` (opens `http://127.0.0.1:4700`); for `none`, no open step |
| `graphify-ingest` | writes a default `.obsidian/app.json` that hides code folders from the sidebar; writes `wiki/code/graph.canvas` | writes neither; `graphify-out/graph.html` is the visual layer |
| `wiki-lint` | Dataview dashboard (`wiki/meta/dashboard.md` with ```dataview blocks), `wiki/meta/overview.canvas` | a plain Markdown dashboard page listing the same four queries' results as tables; no canvas |
| `obsidian-bases` skill, `meta/ba-activity.base` | available | not used; the Markdown pages are the view |
| `mcp-setup.md` (Obsidian REST API and CLI) | applies | does not apply; agents write files and the renderer re-reads the folder on its recheck interval (`WIKI_RECHECK_MS`, default 1000 ms) |
| Live boards and ledgers | "live in Obsidian" | live in the reader's tab; the renderer refuses to save a page that changed on disk since it was opened, so an operator who edits in the browser reloads after an agent writes |

wiki-renderer (https://github.com/kornevdima/wiki-renderer, MIT) is a local web app that reads Obsidian-flavoured Markdown wikis from the folders they live in, renders wikilinks, embeds, callouts, Mermaid, frontmatter and highlighted code, searches the whole wiki and saves a page back to its file. It binds to `127.0.0.1` only and has no sign-in. It does not render `.base` or `.canvas` files, which is why those artefacts are Obsidian-only above.

## Code navigation

What changes with each option:

| Where | `graphify` | `semble`, `serena`, `idea` (MCP servers, any mix) | `none` |
|---|---|---|---|
| Install | `bash <plugin>/bin/setup-graphify.sh <project>` once; the skills skip the installer when the pinned interpreter imports `graphify` | the MCP servers below, once per machine; Semble indexes a repository on first search and caches it; the IDE server needs IntelliJ running with a project open that contains the service | nothing |
| `graphify-ingest`, `graphify-update`, `graphify-query` / `-path` / `-explain` | run | refuse with a pointer to this block (add `graphify` to run them) | refuse |
| Workers' orientation step | one `graphify query` call before reading code | Semble to find by meaning, Serena or the IDE server to read symbols, callers and diagnostics (the playbooks below) | Grep, Glob, Read |
| `wiki-query` structural questions | the graph CLI | `mcp__semble__search` on the service repo, or `mcp__idea__search_symbol` then `get_symbol_info`, then the file at the returned line | wiki pages, then Grep |
| `wiki-lint` graph layer | runs when `graphify-out/graph.json` exists | skipped | skipped |
| `/adlc` epic close, `wrap-up` | `/graphify-update` on every changed service | nothing to refresh | nothing |
| Dispatch packet | "this service has `graphify-out/`, orient there first" | the service's `## Code navigation` lines (below); for `idea`, the `projectPath` of the open IDE project | nothing |

Which MCP server for which vault: **Semble** finds code by meaning and is the first call in every mix. **Serena** runs headless from the working directory with no IDE, gives a file's symbol overview and symbol-level edits, and covers 40 languages through language servers. **The JetBrains server** (`idea`) is free with IntelliJ 2025.2 and later, answers from the IDE's own index (signatures with resolved types and doc comments, call hierarchy, inspections, rename), reads the scripts inside HTML files that a TypeScript language server does not see, and indexes every service at once when they are symlinked into the open project; it needs the IDE running, has no file overview, and its call hierarchy is uneven (none for Python functions; an aliased import call site was missing from one tree in a test). A vault may name both `serena` and `idea`; the worker uses whichever answers, Serena first when both do. The measured comparison is in the plugin wiki ([[JetBrains MCP server vs Serena for code navigation]]).

Grep is right in every option for every occurrence of a literal across the repo (all callers of one function, every `onclick=`). Count with Grep; locate with the navigation tool.

### The playbook workers follow with Semble and Serena

This text is what the generic workers do when the block names `semble` or `serena`. A repo-local binding (`<service>/.claude/agents/`) adds the repo's specifics; it never contradicts this.

- **Find with Semble.** For "where is X" or "what does Y", call `mcp__semble__search` with `repo` set to the service checkout path and a query that names the behaviour or the symbol. `content="code"` searches source files, `content="docs"` Markdown and HTML, `content="config"` configuration files, `content="all"` everything. Go straight to the returned file and line and read that function or class; do not grep for the same thing again. `mcp__semble__find_related` with a result's file and line finds siblings, callers and the existing pattern to reuse. Without the MCP server, the CLI does the same: `semble search "<query>" <repo> --content code --max-snippet-lines 10`, `semble find-related <file> <line> <repo>`; when `semble` is not on `PATH`, `uvx --from "semble[mcp]==0.7.0" semble`.
- **Read and edit symbols with Serena** in the languages its language server covers (the service's `## Code navigation` lines say which). Call `mcp__serena__initial_instructions` once per session, then `mcp__serena__serena_repl` with `s.lsp.get_symbols_overview`, `s.lsp.find_symbol(..., include_body=True)` and `s.lsp.find_referencing_symbols` before reading a whole file. For an edit to a symbol prefer `s.edit.replace_symbol_body`, `s.edit.insert_after_symbol`, `s.lsp.rename_symbol` and `s.lsp.safe_delete_symbol`; for a few lines inside a symbol, `s.edit.replace_content`. Serena's line numbers are 0-based. After an edit, read the changed symbol back with Serena, not the whole file.
- **Not through Serena:** no `s.shell` in place of Bash, no `s.mem` memories and no onboarding (knowledge goes to the wiki through the dispatcher), no edit outside the scope the worker's own rules allow.
- **Say which instrument found each claim** (Semble, Serena, Grep) in the report, so the dispatcher can re-check it.
- **What neither tool sees** (file types Semble does not index, languages Serena does not parse) is found with Grep and read at the function. The service's `## Code navigation` lines list them.

### The playbook workers follow with the JetBrains IDE server (`idea`)

The IDE server is IntelliJ's built-in MCP server (2025.2 and later, bundled and on by default). It answers only for projects open in the IDE and needs `projectPath` on every call: the open project that contains the service, which in a delivery vault is the vault root when services are symlinked into `services/`, else the service checkout itself. The service's `## Code navigation` lines name it.

- **Find**: `mcp__idea__search_symbol` with `q` (an identifier fragment) and, to narrow, `paths` (project-relative globs). It returns files and coordinates only, no names or kinds, so follow each hit with `mcp__idea__get_symbol_info` at the position (the signature with resolved types, the doc comment, the declaring file) or `mcp__idea__read_file` at the line. For "where is this literal", `mcp__idea__search_text` and `search_regex` are indexed and fast, with the same `paths` filter; `search_file` for globs.
- **Callers and callees**: `mcp__idea__analyze_calls` with `symbolFqn` and `INCOMING_CALLS` or `OUTGOING_CALLS`. A short name usually comes back as an ambiguity error listing exact signatures; pass one back verbatim. Confirm a caller list with `search_text` before relying on it: the tree can miss a call made through an aliased import, and it has no entries for Python functions.
- **Gates**: `mcp__idea__get_file_problems` on a file, `mcp__idea__lint_files` on every file you changed, before hand-back. These are the IDE's inspections (errors and warnings), a cheap check beside the service's own lint and typecheck; they do not replace them.
- **Rename** through `mcp__idea__rename_refactoring` when a worker's rules allow the edit; it updates every reference. Other edits stay in the worker's own Edit and Write tools: never `apply_patch`, never `execute_terminal_command`, `execute_run_configuration`, `build_project` or the database tools in place of Bash and the service's wired commands, since they run inside the IDE and outside the vault's permission profile.
- **No open project** ("Unable to determine the target project", or the path "doesn't correspond to any open project") is `ENV_MISMATCH`: report it and stop; the dispatcher asks the operator to open the project in the IDE. Never fall back to guessing a path.
- **Say which instrument found each claim**, as with Semble and Serena.

### What the service `AGENTS.md` adds

`/project-profile` writes a `## Code navigation` section when the vault's block names `semble`, `serena` or `idea`; the dispatcher inlines it into every packet. Four or five lines are enough:

```markdown
## Code navigation

- Semble `repo`: the path of this checkout. `content="code"` covers `.ts`, `.tsx`, `.mjs`; `content="docs"` covers the HTML partials and `wiki/`.
- Semble does not index `.gs`: find those files with Grep, then read at the function.
- Serena's language server: TypeScript only; it does not parse the scripts inside HTML files.
- IDE server `projectPath`: the vault root (this service is `services/<name>` inside it); the IDE understands the TypeScript and the scripts inside the HTML partials, not `.gs`.
- Grep for every occurrence of a literal (all callers of `appsScriptRequest`).
```

### Installing the servers

Once per machine, at user scope, so every vault and service sees them:

```bash
claude mcp add -s user semble -- uvx --from "semble[mcp]==0.7.0" semble
claude mcp add -s user serena -- serena start-mcp-server --context=claude-code --project-from-cwd
```

Semble needs `uv` (`uvx` on `PATH`). Serena needs its own CLI on `PATH`; install it per its README (https://github.com/oraios/serena) and check with `which serena`.

The JetBrains IDE server is part of IntelliJ 2025.2 and later: in the IDE, Settings | Tools | MCP Server, then **Auto-Configure** for Claude Code, which writes the server (named `idea`, HTTP stream on the IDE's built-in web server port) into the client config; or copy the config and add it by hand with `claude mcp add --transport http -s user idea http://127.0.0.1:<port>/stream`. Each running IDE instance has its own port, so a second IDE window needs its own entry. `toolset.py check` reports all three, and for `idea` whether the IDE is answering.

## Design

The `feature-designer` worker (`agents/feature-designer.md`) runs only when `design` names a tool. It has two modes: `shape` before the build turns a story's UI change into a design brief grounded in the design system, and `review` after the code review judges the built UI against the brief, the design system and the tools' heuristics. It never edits app code; findings go to `feature-builder` through the dispatcher. Visual acceptance stays the operator's under the business-input engagement pole (`operator-profile.md`); the designer's verdict gates craft, not taste.

What each tool contributes:

| Tool | Used for | How the designer reaches it |
|---|---|---|
| `impeccable` (https://github.com/pbakaus/impeccable) | `shape` (the design brief), `critique` (heuristic design review), `audit` (accessibility, performance, theming, responsive checks), `detect --json` (the deterministic markup scan), `context` (loads the repo's `PRODUCT.md` and `DESIGN.md`) | the `impeccable:impeccable` skill through the Skill tool; the launcher at `~/.claude/plugins/cache/impeccable/impeccable/<version>/skills/impeccable/scripts/impeccable`, run with the service as the working directory |
| `taste-skill` (https://www.tasteskill.dev/) | the brief-inference and dial reading for Persuade surfaces (landing pages, marketing, portfolios: `taste-skill:taste-skill`); the audit checklist for an existing UI (`taste-skill:redesign-skill`); the AI-tell list every review checks | the skills through the Skill tool, or their `SKILL.md` files read from the plugin cache |
| `design-system` folder | the brand book and its dated rulings, the tokens, the component specs, `DESIGN.md` (impeccable's summary) and `.impeccable/design.json` | read directly; the folder's own `AGENTS.md` or README names which file wins |

Rules the designer applies in both modes:

- **The design system wins over the tools.** A dated ruling in the brand book, or a standing ruling in `meta/operator-profile.md`, beats an impeccable heuristic or a taste-skill tell. When a tool disagrees with a ruling, the record reports the disagreement; it is never filed as a finding against the build.
- **Tokens only.** A colour, size or z-index literal in UI code is a finding when the design system has a token for it.
- **Operate surfaces (admin apps, dashboards, forms) follow the design system and impeccable's Operate mode.** taste-skill's landing-page skill is not applied to them; its redesign audit and tell list are.
- **Both themes** when the design system has light and dark sets.

Installing the plugins:

```bash
claude plugin marketplace add pbakaus/impeccable && claude plugin install impeccable@impeccable
claude plugin marketplace add leonxlnx/taste-skill && claude plugin install taste-skill@taste-skill
```

A design-system folder is any folder that holds a `DESIGN.md` in impeccable's format (frontmatter with the colours and type ramp, then the rules), or a brand book with tokens. `impeccable document` generates `DESIGN.md` from an existing codebase when a project has none.

## Layout

What changes with each layout:

| Where | `symlinks` | `worktrees` |
|---|---|---|
| A service's code | its own repository, linked at `services/<svc>` (machine-local, per `team-sync.md`) | branch `<svc>` of the vault's repository, a git worktree at `services/<svc>`; `services/` is ignored on the main branch |
| A service's code wiki | `services/<svc>/wiki/` in the service repository | `service-wikis/<svc>/` on the vault's main branch |
| Adding a service | clone it and link it | `sh <plugin>/bin/add-service-worktree.sh <vault> <svc>` |
| Commits per story | code in the service repository, wiki on the session's wiki branch | code on branch `<svc>`, every wiki change on the main branch; never in one commit |
| Workers and the dispatcher | the code wiki path `services/<svc>/wiki/` | the path `toolset.py code-wiki <svc>` prints, passed in the packet |

The procedure, the commit rule and the line-ending setting are in [`service-worktrees.md`](service-worktrees.md).

## Engineering

`engineering: ub-mode` installs Robert C. Martin's ub-mode skill and its three measuring tools (crapper, dryer, mutator) into the vault with `sh <plugin>/bin/setup-ub-mode.sh <vault>`. `/project-profile` writes the tools' commands and the four-point definition of done into each service's `AGENTS.md`; `feature-builder` follows the skill and runs the gates, and `feature-reviewer` re-runs them on the diff. With `none`, the service `AGENTS.md` alone says how code is changed. The gates, the template and the three places where an ADLC rule overrides the skill (push, glossary, log) are in [`engineering-ub-mode.md`](engineering-ub-mode.md).

## Cost

`cost: tokeneconomizer` records that the operator runs [TokenEconomizer](https://github.com/microsoft/TokenEconomizer) (Microsoft Research and UC Berkeley, Apache-2.0), a Claude Code plugin that learns from a repository's past session logs. It has three mechanisms, each switched on its own in `~/.tokeneconomizer/config.json`: tool pruning (leaves out tools a repository's sessions have not used), micro-skills (repository facts learned from repeated failures, added at session start) and a loop guard (one note to a turn that keeps hitting the same failure). Nothing in the vault changes with this key; it tells the scaffold and `toolset.py check` to expect the plugin, and it tells the dispatcher two things:

- Tool pruning writes deny rules to `.claude/settings.local.json`, which the scaffold's `.gitignore` already excludes. Set pruning to `propose` (lists tools, changes nothing until `toolprune apply`) rather than `on` in a delivery vault, because a worker type the loop dispatches rarely, such as `devops` or `feature-designer`, can look unused for many sessions.
- Subagent sessions are logged with their parent, so the workers' calls count towards the plugin's numbers and its pruning decisions.

Install, once per machine at user scope:

```bash
git clone https://github.com/microsoft/TokenEconomizer
claude plugin marketplace add "$PWD/TokenEconomizer"
claude plugin install tokeneconomizer@tokeneconomizer
```

Claude Code runs the plugin from the clone, so the clone must stay where it is.

## Permissions

Add to the vault's `.claude/settings.json` `allow` list the lines for the tools the block names (`permissions.md` lists them in the template as optional):

| Tool | Allow lines |
|---|---|
| Semble | `mcp__semble__search`, `mcp__semble__find_related` |
| Serena | `mcp__serena__initial_instructions`, `mcp__serena__serena_repl` |
| JetBrains IDE server | allow the read set: `mcp__idea__search_symbol`, `mcp__idea__get_symbol_info`, `mcp__idea__analyze_calls`, `mcp__idea__read_file`, `mcp__idea__search_text`, `mcp__idea__search_regex`, `mcp__idea__search_file`, `mcp__idea__get_file_problems`, `mcp__idea__lint_files`; put `mcp__idea__rename_refactoring` in `ask`; leave `mcp__idea__execute_terminal_command`, `execute_run_configuration`, `build_project`, `apply_patch` and the database tools out (never `mcp__idea__*`, which would allow them all) |
| impeccable | `Bash(*/skills/impeccable/scripts/impeccable *)` |
| the designer | `Task(feature-designer)` |
| ub-mode | `Bash(sh scripts/tool.sh *)`, `Bash(sh ../../scripts/tool.sh *)` |
| worktree layout | `Bash(git worktree list:*)`, `Bash(git -C services/*)`; leave `git worktree remove` to the operator |

The generic workers list `mcp__semble__*`, `mcp__serena__*` and the IDE server's read set (plus `rename_refactoring` for the builder) in their `tools:` so they can use the servers when a vault has them; a vault without the servers loses nothing, the entries resolve to no tool and the worker runs with the rest.

## Changing the toolset

Edit the block, run `toolset.py check`, then:

- **Adding or dropping the IDE server:** nothing in the repo changes; the service `AGENTS.md` gains or loses its `projectPath` line, and the vault's permission lines follow. A vault whose operators sometimes work without the IDE keeps `serena` beside `idea`.
- **graphify to Semble and Serena:** the graph skills stop running. `graphify-out/` and `wiki/code/` can stay as a dated snapshot or be deleted; `wiki/code/` is graphify-owned, so remove its `_index.md` link from `index.md` if you delete it. Run `/project-profile` on each service so its `AGENTS.md` gains the `## Code navigation` lines, and let `/adlc distill` fold repo specifics into the local bindings.
- **Obsidian to wiki-renderer:** nothing in `wiki/` changes. `.base` and `.canvas` files stop rendering; keep them for teammates on Obsidian or delete them. `.obsidian/` can stay git-ignored as before.
- **Adding a design tool:** install the plugin, set `design-system`, and the next `/adlc` story that touches a UI surface dispatches the designer.
- **Symlinks to worktrees:** for each service, push its repository's history into a branch of the vault's repository (`git fetch <service-repo> main:<svc>`), move the code wiki's pages from `services/<svc>/wiki/` to `service-wikis/<svc>/`, replace the symlink with `add-service-worktree.sh`, and set `layout: worktrees`. Links inside the moved pages keep working, because wikilinks resolve by file name.
- **Adding ub-mode:** run `setup-ub-mode.sh`, then `/project-profile` on each service so its `AGENTS.md` gains the commands and the definition of done. Existing code is measured at the next story that touches it, not all at once.
- **Adding or dropping TokenEconomizer:** install or uninstall the plugin; nothing in the vault changes.
