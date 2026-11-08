#!/bin/sh
# Run one ub-mode quality tool from the current directory (a service root).
# setup-ub-mode.sh copies this file to <vault>/scripts/tool.sh.
# Usage, from services/<service>: sh ../../scripts/tool.sh crapper|dryer|mutator [args...]
#
# The upstream launchers expect the Unix virtualenv layout (.venv/bin); Windows uses
# .venv/Scripts, so this looks in both.
set -e
ROOT=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)
name=$1; shift
dir="$ROOT/tools/$name"
if [ -x "$dir/.venv/Scripts/python.exe" ]; then vpy="$dir/.venv/Scripts/python.exe"
elif [ -x "$dir/.venv/bin/python" ]; then vpy="$dir/.venv/bin/python"
else echo "$name is not set up: run sh <plugin>/bin/setup-ub-mode.sh <vault>" >&2; exit 1; fi
exec "$vpy" -m "$name" "$@"
