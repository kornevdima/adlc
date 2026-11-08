# Service worktrees: one repository, a branch per service

A vault with `layout: worktrees` in its `Toolset:` block keeps every service in the vault's own repository. Each service's code is on its own branch, checked out as a git worktree at `services/<service>`, and each service's code wiki is a folder on the main branch at `service-wikis/<service>/`. The main branch ignores `services/`, so its history holds no code, and a service branch holds no wiki page. The default, `layout: symlinks`, keeps each service in a repository of its own and links its checkout into `services/` ([`modes.md`](modes.md) § Mode ADLC).

Use worktrees when the operator wants code and documentation in separate commits but does not want a repository and a remote per service. Use symlinks when the services already have their own repositories, or when different teams own them.

## Layout

The table shows what each branch holds and where it is checked out, for a vault with two services.

| Branch | Checked out at | Holds |
|---|---|---|
| `main` (or `master`) | the vault root | `wiki/`, `service-wikis/`, `.claude/`, scripts, `AGENTS.md` |
| `<service-a>` | `services/<service-a>` (a worktree) | that service's code and its own `AGENTS.md` |
| `<service-b>` | `services/<service-b>` (a worktree) | that service's code and its own `AGENTS.md` |

The branches never merge into each other. Each service branch starts as an orphan branch, so it shares no history with the main branch.

```
<vault>/
├── .gitignore            # contains /services/
├── wiki/                 # the product or ADLC wiki
├── service-wikis/
│   ├── <service-a>/      # index.md, log.md, modules/, flows/, decisions/, dependencies/
│   └── <service-b>/
└── services/             # ignored on main; one worktree per service branch
    ├── <service-a>/
    └── <service-b>/
```

## Setting it up

For each service, run the plugin's script from anywhere:

```bash
sh <plugin>/bin/add-service-worktree.sh <vault> <service>
```

It adds `/services/` to `.gitignore` when the line is missing, checks out the service branch at `services/<service>` (creating it as an orphan branch with `git worktree add --orphan`, which needs git 2.42 or later), and seeds `service-wikis/<service>/` with an index, a log and the Mode B folders, each with `_index.md` and `_changelog.md`. It is safe to rerun and commits nothing. Then:

1. Commit `.gitignore` and `service-wikis/<service>/` on the main branch.
2. Run `/project-profile` in `services/<service>` to write the service's `AGENTS.md`, and commit the first code on the service branch.
3. Set `layout: worktrees` in the vault's `Toolset:` block.

A fresh clone gets the worktrees back with `git worktree add services/<service> <service>` per service, or by rerunning the script. Push each branch on its own; the main branch's push does not carry them.

## Where workers write

The code wiki moves: `services/<svc>/wiki/` under symlinks is `service-wikis/<svc>/` under worktrees. Every worker page and reference that names `services/<svc>/wiki/` means "the service's code wiki", and the dispatcher passes the resolved path in the packet:

```bash
python3 <plugin>/skills/wiki/scripts/toolset.py --vault . code-wiki <service>
```

Code is still read, built and tested in `services/<svc>/`. Workers never write wiki pages inside a worktree, because a wiki page there would land on the service branch.

## Commits

Code and documentation never share a commit. A story that changes a service makes two commits:

| Change | Where you work | Branch it commits to |
|---|---|---|
| service code | `services/<service>/` | `<service>` |
| that service's code wiki | `service-wikis/<service>/` | main |
| product wiki, skills, scripts | the vault root | main |

The `/adlc` loop commits the story's code in the worktree (`git -C services/<svc> commit`), then the wiki changes at the vault root. The story's trace ID goes in both messages, so `git log --all --grep <ID>` finds the pair. Because every wiki is on one branch, [`git-flow.md`](git-flow.md)'s `wiki/<epic-id>` branch is optional here: a session that wants one cuts it from main as usual, and the service branches are unaffected.

## Line endings

Worktrees on Windows and macOS share one object store, so a file checked out with CRLF in one worktree shows as changed in another. Add to `.gitattributes` on the main branch and on each service branch:

```gitattributes
* text=auto eol=lf
```

## Reading the wikis

wiki-renderer reads every wiki under the vault root, `service-wikis/` included: `wiki-renderer add <vault>`. To browse one service wiki alone, add its folder too: `wiki-renderer add <vault>/service-wikis/<service>`. Obsidian opens the vault root and shows `service-wikis/` as ordinary folders.

## Cleaning up

`git worktree remove services/<service>` drops a checkout and keeps the branch. `git worktree prune` clears entries whose folder was deleted by hand. Neither touches `service-wikis/`.
