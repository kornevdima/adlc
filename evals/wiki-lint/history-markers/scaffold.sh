#!/usr/bin/env bash
# vault-base plus one page that keeps its history inline; concepts/ has no _changelog.md.
set -euo pipefail
bash "$(dirname "$0")/../../_fixtures/use.sh" vault-base
cat > "wiki/concepts/Projection Rebuild.md" <<'EOF'
---
type: concept
title: "Projection Rebuild"
created: 2026-09-01
updated: 2026-10-01
tags: [cqrs, projections]
status: developing
related:
  - "[[CQRS]]"
  - "[[Event Sourcing]]"
---

# Projection Rebuild

A read model in [[CQRS]] can be dropped and rebuilt by replaying the event store from
[[Event Sourcing]]. The rebuild runs against a shadow table and swaps it in when it catches up.

## Update 2026-10-01

Correction: the rebuild now runs against a shadow table (was: in place, with the read side
offline). Swap-in happens when the shadow table has caught up with the live stream.
EOF
printf '%s\n' '- [[Projection Rebuild]] — dropping and replaying a read model' >> wiki/index.md
