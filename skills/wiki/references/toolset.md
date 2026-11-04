# Toolset: the reader, code navigation and design tools a vault uses

A vault declares which reader shows its pages, which tool its workers navigate code with, and which design tools its design worker runs. The plugin ships defaults (Obsidian, graphify, no design tool) but requires none of them: a vault read in wiki-renderer, navigated with Semble and Serena, and reviewed with impeccable works the same way. The declaration is a `Toolset:` block in the vault's `AGENTS.md`, beside `Mode:` and `Concerns:`. Every skill and worker that used to assume Obsidian or graphify reads this block first.

## The block

The scaffold writes it (wiki skill, step 3a) from `toolset.py detect` and the operator's answers. Edit it by hand to change a choice later.

```markdown
Mode: ADLC
Concerns: qa, design
Toolset:
  reader: wiki-renderer
  code-nav: semble, serena
  design: impeccable, taste-skill
  design-system: ~/work/design-system
```

Rules:

- Four keys, all optional: `reader`, `code-nav`, `design`, `design-system`. A missing key takes the default from the table below; a missing block takes every default, which is how vaults created before 1.1.0 behave.
- `code-nav` and `design` take one or more values, comma-separated. `none` is a value.
- `design-system` is a folder path (`~` allowed) or `none`. Everything else is a word from the options list.
- The one-line form `Toolset: reader=wiki-renderer; code-nav=semble,serena` is accepted too, for vaults that keep the header compact.
- `python3 <plugin>/skills/wiki/scripts/toolset.py --vault . show` prints the resolved choices; `check` tells you which chosen tools are installed; `detect` proposes a block from what the machine has.

## Slots, options and defaults

The slots and what each one decides:

| Slot | Options | Default when absent | Decides |
|---|---|---|---|
| `reader` | `obsidian`, `wiki-renderer`, `none` | `obsidian` | Which reader-only artefacts the skills write (Bases, Canvas, Dataview, `.obsidian/app.json`), what the scaffold tells the operator to open, whether the Obsidian MCP notes apply |
| `code-nav` | `graphify`, `semble`, `serena`, `none` (several allowed) | `graphify` when the service has `graphify-out/graph.json`, else `none` | How workers find and read code, how `wiki-query` answers structural questions, whether the graph skills and the graph refresh run |
| `design` | `impeccable`, `taste-skill`, `none` (several allowed) | `none` | Whether the `feature-designer` worker is dispatched and which design skills it runs |
| `design-system` | a folder path, `none` | `none` | Where the designer reads the brand book, tokens and dated rulings |

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

| Where | `graphify` | `semble` and/or `serena` | `none` |
|---|---|---|---|
| Install | `bash <plugin>/bin/setup-graphify.sh <project>` once; the skills skip the installer when the pinned interpreter imports `graphify` | the MCP servers below, once per machine; Semble indexes a repository on first search and caches it | nothing |
| `graphify-ingest`, `graphify-update`, `graphify-query` / `-path` / `-explain` | run | refuse with a pointer to this block (add `graphify` to run them) | refuse |
| Workers' orientation step | one `graphify query` call before reading code | Semble to find, Serena to read and edit symbols (the playbook below) | Grep, Glob, Read |
| `wiki-query` structural questions | the graph CLI | `mcp__semble__search` on the service repo, then the file at the returned line | wiki pages, then Grep |
| `wiki-lint` graph layer | runs when `graphify-out/graph.json` exists | skipped | skipped |
| `/adlc` epic close, `wrap-up` | `/graphify-update` on every changed service | nothing to refresh | nothing |
| Dispatch packet | "this service has `graphify-out/`, orient there first" | the service's `## Code navigation` lines (below) | nothing |

Grep is right in every option for every occurrence of a literal across the repo (all callers of one function, every `onclick=`). Count with Grep; locate with the navigation tool.

### The playbook workers follow with Semble and Serena

This text is what the generic workers do when the block names `semble` or `serena`. A repo-local binding (`<service>/.claude/agents/`) adds the repo's specifics; it never contradicts this.

- **Find with Semble.** For "where is X" or "what does Y", call `mcp__semble__search` with `repo` set to the service checkout path and a query that names the behaviour or the symbol. `content="code"` searches source files, `content="docs"` Markdown and HTML, `content="config"` configuration files, `content="all"` everything. Go straight to the returned file and line and read that function or class; do not grep for the same thing again. `mcp__semble__find_related` with a result's file and line finds siblings, callers and the existing pattern to reuse. Without the MCP server, the CLI does the same: `semble search "<query>" <repo> --content code --max-snippet-lines 10`, `semble find-related <file> <line> <repo>`; when `semble` is not on `PATH`, `uvx --from "semble[mcp]==0.7.0" semble`.
- **Read and edit symbols with Serena** in the languages its language server covers (the service's `## Code navigation` lines say which). Call `mcp__serena__initial_instructions` once per session, then `mcp__serena__serena_repl` with `s.lsp.get_symbols_overview`, `s.lsp.find_symbol(..., include_body=True)` and `s.lsp.find_referencing_symbols` before reading a whole file. For an edit to a symbol prefer `s.edit.replace_symbol_body`, `s.edit.insert_after_symbol`, `s.lsp.rename_symbol` and `s.lsp.safe_delete_symbol`; for a few lines inside a symbol, `s.edit.replace_content`. Serena's line numbers are 0-based. After an edit, read the changed symbol back with Serena, not the whole file.
- **Not through Serena:** no `s.shell` in place of Bash, no `s.mem` memories and no onboarding (knowledge goes to the wiki through the dispatcher), no edit outside the scope the worker's own rules allow.
- **Say which instrument found each claim** (Semble, Serena, Grep) in the report, so the dispatcher can re-check it.
- **What neither tool sees** (file types Semble does not index, languages Serena does not parse) is found with Grep and read at the function. The service's `## Code navigation` lines list them.

### What the service `AGENTS.md` adds

`/project-profile` writes a `## Code navigation` section when the vault's block names `semble` or `serena`; the dispatcher inlines it into every packet. Four lines are enough:

```markdown
## Code navigation

- Semble `repo`: the path of this checkout. `content="code"` covers `.ts`, `.tsx`, `.mjs`; `content="docs"` covers the HTML partials and `wiki/`.
- Semble does not index `.gs`: find those files with Grep, then read at the function.
- Serena's language server: TypeScript only; it does not parse the scripts inside HTML files.
- Grep for every occurrence of a literal (all callers of `appsScriptRequest`).
```

### Installing the servers

Once per machine, at user scope, so every vault and service sees them:

```bash
claude mcp add -s user semble -- uvx --from "semble[mcp]==0.7.0" semble
claude mcp add -s user serena -- serena start-mcp-server --context=claude-code --project-from-cwd
```

Semble needs `uv` (`uvx` on `PATH`). Serena needs its own CLI on `PATH`; install it per its README (https://github.com/oraios/serena) and check with `which serena`. `toolset.py check` reports both.

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

## Permissions

Add to the vault's `.claude/settings.json` `allow` list the lines for the tools the block names (`permissions.md` lists them in the template as optional):

| Tool | Allow lines |
|---|---|
| Semble | `mcp__semble__search`, `mcp__semble__find_related` |
| Serena | `mcp__serena__initial_instructions`, `mcp__serena__serena_repl` |
| impeccable | `Bash(*/skills/impeccable/scripts/impeccable *)` |
| the designer | `Task(feature-designer)` |

The generic workers list `mcp__semble__*` and `mcp__serena__*` in their `tools:` so they can use the servers when a vault has them; a vault without the servers loses nothing, the entries resolve to no tool and the worker runs with the rest.

## Changing the toolset

Edit the block, run `toolset.py check`, then:

- **graphify to Semble and Serena:** the graph skills stop running. `graphify-out/` and `wiki/code/` can stay as a dated snapshot or be deleted; `wiki/code/` is graphify-owned, so remove its `_index.md` link from `index.md` if you delete it. Run `/project-profile` on each service so its `AGENTS.md` gains the `## Code navigation` lines, and let `/adlc distill` fold repo specifics into the local bindings.
- **Obsidian to wiki-renderer:** nothing in `wiki/` changes. `.base` and `.canvas` files stop rendering; keep them for teammates on Obsidian or delete them. `.obsidian/` can stay git-ignored as before.
- **Adding a design tool:** install the plugin, set `design-system`, and the next `/adlc` story that touches a UI surface dispatches the designer.
