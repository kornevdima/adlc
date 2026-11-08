#!/bin/sh
# Install the ub-mode engineering method into a vault (Toolset `engineering: ub-mode`,
# skills/wiki/references/engineering-ub-mode.md):
#
# - the ub-mode skill by Robert C. Martin (MIT) into <vault>/.claude/skills/ub-mode/,
#   unchanged from upstream at a pinned commit
# - its three quality tools (crapper, dryer, mutator) into <vault>/tools/<tool>/ at pinned
#   commits, each with its own virtualenv
# - <vault>/scripts/tool.sh, which runs one tool from a service folder and finds the
#   virtualenv's interpreter on Windows (Scripts/python.exe) and elsewhere (bin/python)
# - /tools/ and .metrics/ in <vault>/.gitignore
#
# Usage: sh setup-ub-mode.sh <vault>
# Safe to rerun. Needs git and Python 3.10 or later. Works in Git Bash on Windows and in sh on
# Linux or macOS. Commits nothing.
set -e
[ $# -eq 1 ] || { echo "usage: $0 <vault>" >&2; exit 2; }
VAULT=$(CDPATH= cd -- "$1" && pwd)
HERE=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
PY=$(command -v python3 || command -v python || true)
[ -n "$PY" ] || { echo "no python3 or python on PATH" >&2; exit 1; }

UB_MODE_REV=3da62bf3fcfd2034de41f30d920d2739e566171f
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
git clone -q https://github.com/unclebob/ub-mode.git "$TMP/ub-mode"
git -C "$TMP/ub-mode" checkout -q "$UB_MODE_REV"
mkdir -p "$VAULT/.claude/skills/ub-mode"
cp "$TMP/ub-mode/SKILL.md" "$TMP/ub-mode/LICENSE" "$VAULT/.claude/skills/ub-mode/"
echo "ub-mode skill at $UB_MODE_REV"

mkdir -p "$VAULT/tools"
for spec in \
  "crapper 6fd92c4c9bcc56efb64a2f8743d5a2993bcfd42d" \
  "dryer 66ff6d21a42c04afcad89c78a80066176d1294b0" \
  "mutator a5a0cb803b66e0cdb8bf471b3b08af701d424a41"
do
  set -- $spec
  name=$1 rev=$2 dir="$VAULT/tools/$1"
  [ -d "$dir/.git" ] || git clone -q "https://github.com/unclebob/$name.git" "$dir"
  git -C "$dir" fetch -q origin && git -C "$dir" checkout -q "$rev"
  if [ ! -d "$dir/.venv" ]; then
    "$PY" -m venv "$dir/.venv"
    if [ -x "$dir/.venv/Scripts/python.exe" ]; then vpy="$dir/.venv/Scripts/python.exe"; else vpy="$dir/.venv/bin/python"; fi
    "$vpy" -m pip install -q --disable-pip-version-check -e "$dir"
  fi
  echo "$name ready at $rev"
done

mkdir -p "$VAULT/scripts"
cp "$HERE/ub-tool.sh" "$VAULT/scripts/tool.sh"
echo "scripts/tool.sh written"

touch "$VAULT/.gitignore"
grep -qxE '/?tools/?' "$VAULT/.gitignore" || printf '\n# ub-mode quality tools, cloned by setup-ub-mode.sh\n/tools/\n' >> "$VAULT/.gitignore"
grep -qx '.metrics/' "$VAULT/.gitignore" || printf '.metrics/\n' >> "$VAULT/.gitignore"
echo "next: add the definition of done to each service's AGENTS.md (engineering-ub-mode.md), then commit .claude/skills/ub-mode, scripts/tool.sh and .gitignore"
