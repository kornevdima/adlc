#!/bin/sh
# Add one service to a vault that uses the worktree layout (Toolset `layout: worktrees`,
# skills/wiki/references/service-worktrees.md): the service's code lives on its own branch,
# checked out as a git worktree at services/<service>, and its code wiki lives on the vault's
# main branch at service-wikis/<service>/.
#
# Usage: sh add-service-worktree.sh <vault> <service>
#
# - ignores /services/ on the main branch (appends to .gitignore when missing)
# - checks out branch <service> at services/<service>; creates it as an orphan branch when it
#   does not exist yet (git 2.42 or later), so the service's history never contains the wiki
# - seeds service-wikis/<service>/ with index.md, log.md and the Mode B folders, each with
#   _index.md and _changelog.md; existing files are left alone
#
# Safe to rerun. Commits nothing: commit the .gitignore and the new wiki on the main branch,
# and the first code on the service branch, separately. Works in Git Bash on Windows and in sh
# on Linux or macOS.
set -e
[ $# -eq 2 ] || { echo "usage: $0 <vault> <service>" >&2; exit 2; }
VAULT=$(CDPATH= cd -- "$1" && pwd)
SVC=$2
case "$SVC" in *[!a-z0-9-]*|"") echo "service name must be lowercase letters, digits and dashes: $SVC" >&2; exit 2 ;; esac
git -C "$VAULT" rev-parse --verify -q HEAD >/dev/null || { echo "$VAULT has no commit yet: commit the vault scaffold first" >&2; exit 1; }
TODAY=$(date +%Y-%m-%d)

touch "$VAULT/.gitignore"
if ! grep -qxE '/?services/?' "$VAULT/.gitignore"; then
  printf '\n# code lives on its own branches, checked out here as worktrees\n/services/\n' >> "$VAULT/.gitignore"
  echo "added /services/ to .gitignore"
fi

if [ -e "$VAULT/services/$SVC/.git" ]; then
  echo "services/$SVC is already checked out"
elif git -C "$VAULT" show-ref --verify -q "refs/heads/$SVC"; then
  git -C "$VAULT" worktree add -q "services/$SVC" "$SVC"
  echo "checked out branch $SVC at services/$SVC"
elif git -C "$VAULT" show-ref --verify -q "refs/remotes/origin/$SVC"; then
  git -C "$VAULT" worktree add -q --track -b "$SVC" "services/$SVC" "origin/$SVC"
  echo "checked out origin/$SVC at services/$SVC"
else
  git -C "$VAULT" worktree add -q --orphan -b "$SVC" "services/$SVC"
  echo "created orphan branch $SVC at services/$SVC"
fi

W="$VAULT/service-wikis/$SVC"
seed() { # path title body
  [ -e "$1" ] && return 0
  mkdir -p "$(dirname "$1")"
  printf -- '---\ntype: %s\ntitle: "%s"\nstatus: active\ncreated: %s\nupdated: %s\ntags: [%s]\n---\n\n# %s\n\n%s\n' \
    "$4" "$2" "$TODAY" "$TODAY" "$4" "$2" "$3" > "$1"
}
seed "$W/index.md" "$SVC wiki" "The code of this service is on the \`$SVC\` branch, checked out at \`services/$SVC\`; its commands and definition of done are in that folder's \`AGENTS.md\`.

| Folder | Holds |
|---|---|
| [[modules/_index\\|modules]] | code areas |
| [[flows/_index\\|flows]] | request and data paths |
| [[decisions/_index\\|decisions]] | decisions that affect this service only |
| [[dependencies/_index\\|dependencies]] | toolchain and libraries |" index
seed "$W/log.md" "$SVC log" "Append-only. New entries go at the top." log
for f in modules flows decisions dependencies; do
  seed "$W/$f/_index.md" "$SVC $f" "No pages yet. History: [[$f/_changelog|changelog]]." index
  seed "$W/$f/_changelog.md" "$SVC $f changelog" "Pages show the current state only; history goes here, newest first.

| Date | Page | Change |
|---|---|---|" changelog
done
echo "code wiki at service-wikis/$SVC"
echo "next: commit .gitignore and service-wikis/$SVC on the main branch; then run /project-profile in services/$SVC"
