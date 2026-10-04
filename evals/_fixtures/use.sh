#!/usr/bin/env bash
# Build a case workspace from fixture layers, in order, into the current directory.
# Called from a case's scaffold.sh (claude plugin eval --scaffold runs it in the
# case workspace). Arguments are layer names under evals/_fixtures/, plus:
#   @commit   git init + commit everything so far (later layers become uncommitted changes)
#   @large    generate a 60-page vault and wiki/index.json (needs vault-base first)
set -euo pipefail
FIX="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN="$(cd "$FIX/../.." && pwd)"
for layer in "$@"; do
  case "$layer" in
    @commit)
      git init -q && git add -A \
        && git -c user.name=eval -c user.email=eval@example.invalid commit -qm "fixture baseline" ;;
    @large)
      python3 "$FIX/gen_large_vault.py" . \
        && python3 "$PLUGIN/skills/wiki-query/scripts/build_index_json.py" . >/dev/null ;;
    *)
      [ -d "$FIX/$layer" ] || { echo "unknown fixture layer: $layer" >&2; exit 2; }
      cp -R "$FIX/$layer/." . ;;
  esac
done
