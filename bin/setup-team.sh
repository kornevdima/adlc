#!/usr/bin/env sh
# setup-team.sh <vault>: the joining checklist for a vault that gains a second person
# (skills/wiki/references/team-sync.md, "When a second person joins").
#
# Writes, when absent: CODEOWNERS (from the Roles: block of AGENTS.md), CONTRIBUTING.md (from the
# "## How we work" section), and a pre-commit hook that runs `gitleaks protect --staged`. Never
# overwrites a file that exists; prints what it skipped. Installs nothing: gitleaks is the operator's
# install (https://github.com/gitleaks/gitleaks), and the hook says so when it is missing.
set -eu

VAULT="${1:-.}"
cd "$VAULT"
[ -f AGENTS.md ] || { echo "error: no AGENTS.md in $VAULT" >&2; exit 2; }
[ -d .git ] || { echo "error: $VAULT is not a git repository (run git init first)" >&2; exit 2; }

# CODEOWNERS from the Roles: block. Each role line is "- <role>: <folder>, <folder>"; the operator
# maps roles to handles afterwards. A fallback owner line covers everything else.
if [ -f CODEOWNERS ]; then
  echo "skip   CODEOWNERS exists"
else
  {
    echo "# Written by adlc setup-team.sh from the Roles: block of AGENTS.md."
    echo "# Replace each @<role> with the GitHub handles or team of that role; keep one line per path."
    echo "*  @operator"
    awk '
      /^Roles:/ { inblock=1; next }
      inblock && /^[A-Za-z]+:/ && !/^  / { inblock=0 }
      inblock && /^ *- / {
        line=$0; sub(/^ *- */, "", line)
        n=index(line, ":"); if (n==0) next
        role=substr(line, 1, n-1); paths=substr(line, n+1)
        gsub(/ /, "", role); gsub(/^ +| +$/, "", paths)
        m=split(paths, p, ",")
        for (i=1; i<=m; i++) { q=p[i]; gsub(/^ +| +$/, "", q); gsub(/`/, "", q); if (q!="") printf "wiki/%s  @%s\n", q, role }
      }' AGENTS.md
  } > CODEOWNERS
  echo "wrote  CODEOWNERS ($(grep -c '@' CODEOWNERS) lines; map the @<role> placeholders to handles)"
fi

# CONTRIBUTING.md from "## How we work".
if [ -f CONTRIBUTING.md ]; then
  echo "skip   CONTRIBUTING.md exists"
else
  {
    echo "# Contributing"
    echo
    echo "How this vault is worked on. The rules below come from the \`## How we work\` section of \`AGENTS.md\`, which stays the source; edit there first."
    echo
    awk '/^## How we work/ { on=1; next } on && /^## / { on=0 } on { print }' AGENTS.md
    echo
    echo "## Before a commit"
    echo
    echo "- The pre-commit hook runs \`gitleaks protect --staged\`; a hit blocks the commit. Spike logs under \`.raw/spikes/\` are committed, so a secret printed by a command is removed from the log first."
    echo "- Personal settings stay in \`.claude/settings.local.json\`; machine setup in \`wiki/meta/machine.local.md\`. Neither is committed."
    echo "- Pull before you read the boards or a run ledger; one \`/adlc\` dispatcher per epic (the plugin's \`mission-control.md\`, When more than one session runs)."
    echo
    echo "## Branch protection"
    echo
    echo "Reviews required and no force push on the main branch is set in the hosting service by the operator; this repository cannot set it for you."
  } > CONTRIBUTING.md
  echo "wrote  CONTRIBUTING.md"
fi

# Pre-commit hook: gitleaks on the staged changes.
HOOK=.git/hooks/pre-commit
if [ -f "$HOOK" ]; then
  echo "skip   $HOOK exists (add 'gitleaks protect --staged' to it by hand)"
else
  cat > "$HOOK" <<'EOF'
#!/usr/bin/env sh
# adlc setup-team.sh: secret scan on the staged changes before every commit.
if command -v gitleaks >/dev/null 2>&1; then
  gitleaks protect --staged --redact || { echo "pre-commit: gitleaks found a secret in the staged changes; remove it and commit again" >&2; exit 1; }
else
  echo "pre-commit: gitleaks is not installed; install it (https://github.com/gitleaks/gitleaks) so secrets are scanned before each commit" >&2
fi
EOF
  chmod +x "$HOOK"
  echo "wrote  $HOOK"
fi

command -v gitleaks >/dev/null 2>&1 && echo "ok     gitleaks $(gitleaks version 2>/dev/null | head -1)" \
  || echo "note   gitleaks is not on PATH; the hook warns until it is installed"
echo "next   set branch protection on the main branch in the hosting service (the operator's step)"
