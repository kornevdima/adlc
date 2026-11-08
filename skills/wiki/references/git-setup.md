# Git Setup

Initialize git in the vault to get full history and protect against bad writes.

---

## Initialize

```bash
cd "$VAULT_PATH"
git init
git add -A
git commit -m "Initial vault scaffold"
```

---

## .gitattributes (always)

Create a `.gitattributes` in the vault root as part of the scaffold:

```gitattributes
* text=auto eol=lf

wiki/log.md merge=union
**/wiki/log.md merge=union
service-wikis/*/log.md merge=union
```

`* text=auto eol=lf` stores and checks out every text file with LF endings on every machine. Without it, a vault edited on Windows and macOS shows every page as changed after a checkout, and a worktree checked out with other settings disagrees with the main checkout about which files changed. Binary files are detected and left alone.

`log.md` is append-only with newest entries at the top, so concurrent sessions (teammates, parallel agents, a wrap-up racing an ingest) both prepend; a normal merge conflicts every time, while `merge=union` keeps both entries automatically. The `**/` pattern covers co-located code wikis under `services/`; the `service-wikis/` line covers the code wikis of the worktree layout ([`service-worktrees.md`](service-worktrees.md)). The team-sync protocol (`team-sync.md`) depends on this being present before the second concurrent session ever runs.

In a co-located repo (Mode B wiki inside a code repo), also add:

```gitattributes
wiki/** linguist-generated=true
```

so GitHub collapses wiki files in PR diffs — reviewers see code only. Branch topology for agent sessions (wiki branches, code-only PRs, the worktree seam) lives in [`git-flow.md`](git-flow.md).

---

## .gitignore

The root `.gitignore` in this repo already covers the right exclusions:

```
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.smart-connections/
.obsidian-git-data
.trash/
.DS_Store
```

`workspace.json` changes constantly as you move panes around. Excluding it keeps the diff clean.

---

## Obsidian Git Plugin (optional)

Install via Settings → Community Plugins → Browse → "Obsidian Git". Then:

Settings > Obsidian Git:
- Auto backup interval: **15 minutes**
- Auto backup after file change: on
- Push on backup: on (if you have a remote)
- Commit message: `vault: auto backup {{date}}`

This runs silently in the background. You get a full history of every note without thinking about it.

---

## Remote (Optional)

To back up to GitHub:

```bash
git remote add origin https://github.com/yourname/your-vault
git push -u origin main
```

Keep the repo private if the vault contains personal notes.
