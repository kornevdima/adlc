# ADLC permissions profile

Mode ADLC is agent-operated: the human operates the agents and should not be prompted for routine work, while destructive operations stay gated. This profile encodes that. Scaffold it into the ADLC vault's `.claude/settings.json` (project scope) at setup, then tune per project.

Principle: allow routine project work, ask on medium-risk, deny hard-destructive and anything outside the project.

## Mechanism

Claude Code permissions support three lists: `allow` (run without prompt), `ask` (confirm first), `deny` (block outright). Precedence is `deny` > `ask` > `allow`. Keep destructive patterns in `deny` / `ask`; put everything routine in `allow`. Scope file writes to the project path with `Edit(path)` rules so nothing outside is touched silently: `Edit(path)` governs every file-writing tool (Edit, Write, NotebookEdit). `Write(path)` rules are accepted but never matched, and Claude Code warns about them at startup. Bash entries use prefix matching (`Bash(git commit:*)` matches any `git commit ...`).

## Template `.claude/settings.json`

Replace `<VAULT_PATH>` with the project root. Trim patterns the project does not use.

```json
{
  "permissions": {
    "allow": [
      "Read(//<VAULT_PATH>/**)",
      "Edit(//<VAULT_PATH>/**)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git switch:*)",
      "Bash(git checkout -b:*)",
      "Bash(rg:*)",
      "Bash(grep:*)",
      "Bash(ls:*)",
      "Bash(find:*)",
      "Bash(cat:*)",
      "Bash(awk:*)",
      "Bash(jq:*)",
      "Bash(md5sum:*)",
      "Bash(npm run:*)",
      "Bash(npm test:*)",
      "Bash(npx:*)",
      "Bash(python3 *skills/wiki/scripts/relink.py *)",
      "Bash(python3 *skills/wiki/scripts/upstream_redact_check.py *)",
      "Bash(python3 *skills/wiki/scripts/glossary.py *)",
      "Bash(python3 *skills/wiki/scripts/page_history_check.py *)",
      "Bash(python3 *skills/adlc/scripts/build_snapshot.py *)",
      "Task(ba-suite-subagent)",
      "Task(architecture-subagent)",
      "Task(ba-export-subagent)",
      "Task(feature-builder)",
      "Task(feature-tester)",
      "Task(feature-reviewer)",
      "Task(feature-verifier)",
      "Task(scope-analyst)",
      "Task(doc-writer)",
      "Task(devops)",
      "Task(wiki-ingest-subagent)",
      "Bash(docker compose up:*)",
      "Bash(docker compose ps:*)",
      "Bash(docker compose logs:*)",
      "Bash(lsof -nP -iTCP:*)",
      "Bash(ps -p:*)",
      "mcp__clickup__get_task",
      "mcp__chrome-devtools__navigate_page",
      "mcp__chrome-devtools__evaluate_script",
      "mcp__chrome-devtools__take_screenshot",
      "mcp__chrome-devtools__list_console_messages",
      "mcp__chrome-devtools__list_network_requests",
      "mcp__plantuml__render_plantuml"
    ],
    "ask": [
      "Bash(git push:*)",
      "Bash(rm:*)",
      "Bash(docker compose down:*)",
      "Bash(npm install:*)",
      "Bash(gh pr:*)",
      "Bash(gh issue create:*)",
      "mcp__clickup__create_task"
    ],
    "deny": [
      "Bash(git push --force:*)",
      "Bash(git push -f:*)",
      "Bash(git reset --hard:*)",
      "Bash(git clean:*)",
      "Bash(docker compose down -v:*)",
      "Bash(docker volume rm:*)",
      "Bash(mongosh:*drop:*)",
      "Bash(gcloud:*)",
      "Bash(rm -rf /:*)",
      "Edit(//etc/**)",
      "Read(**/.env)",
      "Read(**/.env.local)",
      "Read(**/.env.*.local)",
      "Bash(docker compose config:*)",
      "Bash(docker inspect:*)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Read|Edit|Write|NotebookEdit",
        "hooks": [
          { "type": "command", "command": "if [ -f \"$CLAUDE_PROJECT_DIR/.claude/hooks/guard_env.py\" ]; then python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/guard_env.py\"; else echo 'guard_env.py missing; env guard off' >&2; fi", "statusMessage": "Guarding env files..." }
        ]
      }
    ]
  }
}
```

Notes:

- `Task(ba-suite-subagent)` lets the ADLC ingest pass dispatch the BA worker without a prompt. Add other `Task(...)` workers the vault uses.
- Bash prefix matching cannot express every dangerous shape (for example "rm -rf anywhere outside the project"). `ask` on bare `rm` plus the guard hook below covers the rest.
- `relink.py` is the wiki-maintenance path: bulk relinks (the epic close, `wiki-lint` dead-link fixes) go through it, not `sed -i`. The rule names the script, not `Bash(sed:*)`, which would allow in-place edits to any path. The `*` before `skills/` matches the versioned plugin install path.
- `upstream_redact_check.py` reads the files it is given and the vault's ledger frontmatter, prints hits and exits; it writes nothing. `/adlc upstream` runs it on every export before the operator sees it (`adlc-upstream.md` § Sending, step 1).
- `glossary.py` writes only `wiki/glossary.md` (`build`) and first-mention links in wiki pages (`link --apply`; dry run by default). `page_history_check.py` writes nothing: it lists history kept inside pages and folders without a linked `_changelog.md` (`wiki-lint`, `wrap-up` step 6a). Both are in `allow` for the same reason as `relink.py`: the shipped script is the routine path, so auto mode never has to judge an ad-hoc rewrite.
- **The hook command is anchored on `$CLAUDE_PROJECT_DIR`.** A cwd-relative `python3 .claude/hooks/guard_env.py` broke in one vault as soon as the session's working directory moved into a subdirectory: Python exited 2 ("can't open file"), Claude Code read exit 2 as a block, and every Bash, Read, Edit and Write call was refused, including the edit that would have fixed the settings. The `if … fi` form keeps a real block (exit 2 from the hook) and lets a missing hook file pass with a warning on stderr, because `if` returns the status of the last command it ran; stdin still reaches Python.
- `build_snapshot.py` is the dispatcher's build snapshot and tester footprint check (`/adlc` Step 2.3a / 2.4a). It writes only `refs/adlc/<story>/*` through a throwaway index, and `restore` touches only the paths it is given, so it is safe to allow; it never pushes.
- `lsof -nP -iTCP` and `ps -p` are read-only: the hand-back check and `wrap-up` step 7c list what is still listening and who owns it. Stopping a process (`kill`, `docker compose stop`) is not allowed here, so it prompts.
- `Task(devops)` only allows the dispatch. Its outward actions stay gated: `git push` and `gh pr` are in `ask`, `gcloud` is denied by this template. A project that lets `devops` deploy adds its exact deploy command to `ask`, never to `allow`.
- `gh issue create` is in `ask` for `/adlc upstream`: an export leaves the vault only after the operator reads it. Where GitHub is unreachable, the manual hand-off needs no rule.
- **Env files are never read, by any tool.** Workers read `.env*` files to learn a variable's shape, and the tool output lands in the transcript: in one vault a `docker compose config` printed a dev private key and a `sed` over `.env.local` echoed fragments of it, on the same day, with a packet rule in force. The `deny` rules above cover `Read` on the common names and the two commands that print resolved config. Bash patterns cannot carve `.env.example` out of `.env*`, so the hook `guard_env.py` (copied from the plugin's `skills/wiki/scripts/` into `.claude/hooks/` at scaffold) is the enforcement: it blocks any tool on a file named `.env` or `.env.<x>`, any Bash command that names one (commit and PR message text and literal heredoc bodies excepted, unless they can run code), and bare `env` / `printenv` / `set` / `docker compose config` / `docker inspect`; `.env.example`, `.sample`, `.template` and `.dist` stay readable. Workers take variable names from the compose file or `.env.example` and check presence with `test -n "$VAR"`. The hook also stops the dispatcher from copying `.env.example` to `.env`: that is the operator's step, by hand. The hook never prints the blocked command or path in full.
- MCP: reads (`mcp__clickup__get_task`) and local verification (`mcp__chrome-devtools__*`, `mcp__plantuml__render_plantuml`, `docker compose up`) are pre-allowed; outward-facing tracker writes (`mcp__clickup__create_task`) are in `ask` because they leave the repo.

## Auto mode

In auto mode a classifier judges each action the allow list does not settle. Two facts decide what this profile can do (Claude Code docs, `auto-mode-config`):

- **A narrow `permissions.allow` rule is resolved before the classifier runs.** The `relink.py` rule above therefore runs in auto mode without a classifier decision. Broad rules (`Bash(*)`) are suspended in auto mode, and `autoMode.classifyAllShell: true` sends every shell command to the classifier regardless.
- **The classifier never reads `autoMode` from project settings** (`.claude/settings.json` or `.claude/settings.local.json`), so a checked-in repo cannot plant its own allow rules. Do not put `autoMode` in this template; it would be ignored.

Shell edits the allow list does not name (an ad-hoc `sed -i`, a one-off Python rewrite) are the classifier's call, and it may deny them. Prefer the shipped script. If an operator wants the classifier to treat other wiki maintenance as routine, they add a prose rule to `autoMode.allow` in their **user** settings (`~/.claude/settings.json`), scoped to the path, for example: "In-place edits to Markdown files under `<VAULT_PATH>/wiki/` are routine wiki maintenance." That is the operator's decision; the scaffold never writes user settings.

## Optional guard hook (deterministic backstop)

Pattern lists miss novel command shapes. For a hard backstop, add a `PreToolUse` hook on `Bash|Write` that blocks dangerous commands and writes to untracked or outside-project paths, beside the `guard_env.py` hook the template already wires. One production vault uses a `guard-untracked.py` of this kind. Document it; do not require it.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Write",
        "hooks": [
          { "type": "command", "command": "if [ -f \"$CLAUDE_PROJECT_DIR/.claude/hooks/guard.py\" ]; then python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/guard.py\"; else echo 'guard.py missing; guard off' >&2; fi", "statusMessage": "Guarding destructive ops..." }
        ]
      }
    ]
  }
}
```

## What stays the human's call

Sign-off, production deploys, force pushes, schema drops, and anything that leaves the repo. The agent proposes; the human approves. This is the gate that keeps ADLC safe to run unattended-ish.
