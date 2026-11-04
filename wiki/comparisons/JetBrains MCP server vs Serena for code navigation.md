---
type: comparison
title: "JetBrains MCP server vs Serena for code navigation"
subjects:
  - "IntelliJ IDEA's built-in MCP server (2026.2.3), the `idea` code-nav option"
  - "Serena 2.1.0 with the language-server backend, the `serena` code-nav option"
dimensions:
  - "Finding a symbol and reading its signature"
  - "Callers and callees"
  - "File overview and symbol-level edits"
  - "Diagnostics and inspections"
  - "Languages and file types seen"
  - "Project binding and what has to be running"
verdict: "Neither replaces the other. The IDE server answers with the IDE's own precision (signatures, call hierarchy, inspections, HTML-embedded scripts) and covers every service open in the IDE, but only while the IDE runs; Serena works headless from the working directory, gives file overviews and symbol-level edits, and covers 40 languages. The toolset offers both as `code-nav` values; a vault may name either or both, Semble beside them for search by meaning."
created: 2026-11-04
updated: 2026-11-04
tags:
  - comparison
  - toolset
  - code-navigation
  - mcp
status: current
related:
  - "[[Configurable toolset for reader, code navigation and design]]"
  - "[[Workers and the dispatch pipeline]]"
  - "[[Shared references]]"
---

# JetBrains MCP server vs Serena for code navigation

Measured on 2026-11-04 to decide whether a vault with IntelliJ's MCP server still needs Serena. The answer shaped the toolset: `idea` became a fourth `code-nav` value beside `graphify`, `semble` and `serena`, and neither replaced the other.

## Method

The same lookups were run through both servers on code they both saw: the IDE server through the operator's open vault project, which symlinks every service into `services/`; Serena through a session bound to this repository (Python) and a second server started on a TypeScript service for the TypeScript rows. IDE timings are HTTP round trips to the local server; Serena timings were taken inside its process, so add about a tenth of a second for transport. Single runs. Serena's cold TypeScript calls include the language server's warm-up.

## Results

The operations and what each server returned:

| Operation | JetBrains MCP server | Serena (language servers) |
|---|---|---|
| Find a symbol by name across all services (TypeScript) | 0.25 s; 20 hits as file and coordinates, no symbol names or kinds (5.8 KB) | 1.85 s cold, instant warm; name path, kind, file and lines (161 characters for one hit) |
| Signature and docs of a symbol | `get_symbol_info` 0.17 s; the signature with resolved types and the doc comment (1.9 KB) | `find_symbol` with the body, instant; the body itself |
| Overview of one file's symbols | none; a one-letter `search_symbol` over one file returned 2 of its symbols | 0.26 s cold, instant warm; every symbol grouped by kind |
| Callers, TypeScript | `analyze_calls` 0.57 s; needs the exact signature from its ambiguity list; missed the call made through an aliased deep import, although `get_symbol_info` resolves that import | `find_referencing_symbols` 2.5 s; 5 files, each with a 3-line snippet (2.7 KB) |
| Callers, Python | unsupported ("No callable symbol found") | 0.11 s, with the snippet |
| Diagnostics | the IDE's inspections, 0.8 s per file (duplicated-code weak warnings), batch through `lint_files` | Pyright and TypeScript diagnostics, 2.5 to 5 s per file |
| Scripts inside HTML files | understood: a function in an HTML partial came back with its signature | not parsed ("Cannot extract symbols") |
| Apps Script `.gs` | no symbols | not parsed |
| Project binding | the projects open in the running IDE, `projectPath` on every call; one open vault covered six services through symlinks | one project per server, from the working directory; the server was up in 1 s |
| Edits | `apply_patch` (diff), `rename_refactoring`, `reformat_file` | symbol-body replace and insert, safe delete, rename, multi-file replace with a dry run |
| Beyond navigation | build, run configurations, the IDE terminal, database tools, a debugger, decompiled jars | memories; shell (off in the Claude Code context) |

## What follows for the toolset

- **Both stay options.** The IDE server's strengths are the IDE's: resolved signatures, call hierarchy, inspections, HTML-embedded scripts, every service in one open project. Its conditions are the IDE's too: it must be running with the project open, every call carries `projectPath`, and a missing project is an environment mismatch, not something to guess around. Serena needs nothing running and nothing open, and it is the only one of the two with a file overview and symbol-level edits.
- **Semble is unaffected.** It finds code by meaning, which neither of these does; it stays the first call in any mix.
- **The IDE server's call tree is checked, not trusted.** The aliased-import miss and the missing Python support make `search_text` the confirmation step in the worker playbook.
- **Grants are explicit.** The server also exposes the IDE terminal, run configurations, `apply_patch` and the database tools, which sit outside the vault's permission profile; the workers list the nine read tools (and the builder the rename), never `mcp__idea__*`.
- **Serena's own JetBrains plugin backend** is a third shape, not a middle ground: Serena's tools over the IDE's analysis, the same IDE-open condition, and a paid plugin (7-day trial per the Marketplace listing). The free built-in server already gives the IDE's analysis, so the toolset does not model it.

## Sources

- JetBrains, [MCP server (IntelliJ IDEA 2026.2 help)](https://www.jetbrains.com/help/idea/2026.2/mcp-server.html): bundled since 2025.2, the tool list, `projectPath`, Auto-Configure for Claude Code.
- JetBrains, [mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains): the deprecated proxy, superseded by the built-in server.
- Oraios, [Serena](https://github.com/oraios/serena) and its docs: [project workflow](https://oraios.github.io/serena/02-usage/040_workflow.html) (one active project per server, `--project-from-cwd`, `query-projects` mode), [the JetBrains plugin backend](https://oraios.github.io/serena/02-usage/025_jetbrains_plugin.html), [language support](https://oraios.github.io/serena/01-about/020_programming-languages.html).
- JetBrains Marketplace, [Serena plugin](https://plugins.jetbrains.com/api/plugins/28946): pricing model paid, trial period 7.
