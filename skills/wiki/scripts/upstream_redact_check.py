#!/usr/bin/env python3
"""Check an upstream report, or a plugin page filed from one, for pointers into a private vault.

The plugin repository may be public. A report that leaves a vault, and every plugin page
written from one, carries the mechanics of what went wrong and nothing that points back at
the vault: no tracker ids, no ledger page names or line numbers, no commit hashes, no URLs,
no concrete source paths, no directory or service names, and a key that is an opaque alias.
Prose rules for this did not hold (the plugin's own pages leaked all of these on 2026-10-20),
so this check runs on the export before it is sent and on the plugin pages before they are
committed.

    # in the vault, before sending: names and the key come from the vault itself
    python3 upstream_redact_check.py --vault . .raw/exports/upstream/*.md
    python3 upstream_redact_check.py --vault . --key-only
    # in the plugin repo, before committing a page filed from a report
    python3 upstream_redact_check.py --names "<vault dir>,<product>" wiki/questions/<page>.md
    python3 upstream_redact_check.py --vault <path to the co-located vault> wiki/questions/<page>.md

Rules (each hit is printed as `file:line: RULE: match`):

  ID        a tracker id (US-179, EPIC-002, BUG-018, TC-120, BR-019, Q-005, Q-S4-1), except
            UP-nnn and a few technical acronyms (ISO-8601, SHA-256, RFC-7231, UTF-8, HTTP-2)
  SPRINT    a sprint token (S07, S8, Q-S4, "sprint 7", "wave 5")
  LEDGER    a run-ledger or as-built page name, or a page reference with a line number
            (`_run EPIC-002.md:130`, `As-built.md`, `file.ts:344`)
  HASH      a commit hash: 7 to 40 hex characters with at least one letter and one digit
  URL       a URL or a bare domain
  PATH      a concrete source path (`src/db/invites.ts`, `services/web/`); `src/db/<module>.ts`
            and `services/<service>/` are the accepted shapes
  NAME      a word that matches the vault's own directory name, one of its service directories,
            or a name passed with --names (case-insensitive, whole word)
  KEY       the vault key is not an opaque alias of the form vault-<letter>, or equals a
            directory name

What it cannot see: product and feature nouns, and people's names inside quoted
corrections. Those stay a reading rule (adlc-upstream.md § Sending it upstream).

--vault ROOT     the reporting vault's root. Its name, its first-level directories and
                 services/* give the NAME list, and its wiki/meta/adlc-upstream.md gives the
                 key when --key is not passed. Without it, NAME uses only --names and KEY only
                 --key (the plugin repo is not a vault; never point --vault at it)
--key KEY        the vault key to check instead of reading the ledger
--names N[,N]    more names to flag (a product, a client, a repo)
--allow REGEX    suppress hits that match (repeatable), e.g. a placeholder id in a template
--key-only       check only the key, no files

Exit code: 0 clean, 1 hits, 2 bad input. Stdlib only.
"""
import argparse
import re
import sys
from pathlib import Path

ID_ALLOW = {"UP", "ISO", "SHA", "RFC", "UTF", "HTTP", "TCP", "TLS", "IEEE", "CVE", "ECMA", "MD", "AES", "RSA"}
GENERIC_DIRS = {
    "wiki", "web", "docs", "doc", "infra", "api", "app", "apps", "server", "client", "services",
    "service", "scripts", "script", "src", "lib", "libs", "packages", "test", "tests", "e2e",
    "bin", "build", "dist", "public", "static", "assets", "config", "tools", "node_modules",
    "_attachments", "graphify-out", "exports", "intake", "upstream", "data", "db", "ui", "core",
    "shared", "common", "backend", "frontend", "mobile", "cli", "sdk", "www", "site",
    "skills", "agents", "hooks", "evals", "references", "templates", "fixtures",
}
KEY_RE = re.compile(r"^vault-[a-z]$")

RULES = [
    ("ID", re.compile(r"\b([A-Z]{1,8})-(?:S\d{1,2}-)?\d{2,5}\b")),
    ("SPRINT", re.compile(r"\bS\d{1,2}\b|\bQ-?S\d\b|\bsprint\s+\d{1,2}\b|\bwave\s+\d{1,2}\b", re.I)),
    ("LEDGER", re.compile(r"_run [A-Z]+-\d+|\bAs-built\.md\b|\b[\w.-]+\.(?:md|ts|tsx|js|jsx|py|go|rs|java|kt|rb|php|cs|sql|css|html)\b:\d+\b")),
    ("HASH", re.compile(r"\b[0-9a-f]{7,40}\b")),
    ("URL", re.compile(r"https?://\S+|\b[a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:com|io|dev|app|org|net|ai|co|ua|de|uk|eu)\b(?:/\S*)?", re.I)),
    ("PATH", re.compile(r"\bsrc/[\w./-]*\w\.\w{1,4}\b|\bservices/(?!<)[\w.-]+/?")),
]


def hash_ok(m: str) -> bool:
    return any(c.isdigit() for c in m) and any(c.isalpha() for c in m)


def id_ok(m: re.Match) -> bool:
    return m.group(1).upper() not in ID_ALLOW


def vault_names(root: Path) -> set[str]:
    names = set()
    if root.name and root.name.lower() not in GENERIC_DIRS:
        names.add(root.name)
    try:
        for p in root.iterdir():
            if p.is_dir() and not p.name.startswith(".") and p.name.lower() not in GENERIC_DIRS:
                names.add(p.name)
        services = root / "services"
        if services.is_dir():
            for p in services.iterdir():
                if p.is_dir() and p.name.lower() not in GENERIC_DIRS:
                    names.add(p.name)
    except OSError:
        pass
    return names


def ledger_key(root: Path) -> str | None:
    ledger = root / "wiki" / "meta" / "adlc-upstream.md"
    if not ledger.is_file():
        return None
    for line in ledger.read_text(encoding="utf-8", errors="replace").splitlines()[:30]:
        m = re.match(r"^vault_key:\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip().strip("\"'")
    return None


def check_key(key: str | None, names: set[str]) -> list[str]:
    if key is None:
        return []
    out = []
    if not KEY_RE.match(key):
        out.append(f"KEY: `{key}` is not an opaque alias (expected vault-<letter>)")
    if key.lower() in {n.lower() for n in names}:
        out.append(f"KEY: `{key}` is a directory name")
    return out


def scan(path: Path, names: set[str], allow: list[re.Pattern]) -> list[str]:
    hits = []
    name_re = None
    if names:
        name_re = re.compile(r"\b(" + "|".join(re.escape(n) for n in sorted(names, key=len, reverse=True)) + r")\b", re.I)
    in_fence = False
    for no, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
        found = []
        for rule, rx in RULES:
            for m in rx.finditer(line):
                text = m.group(0)
                if rule == "HASH" and not hash_ok(text):
                    continue
                if rule == "ID" and not id_ok(m):
                    continue
                if rule == "LEDGER" and text.startswith("_run") and "<" in line[m.start():m.end() + 2]:
                    continue
                found.append((rule, text))
        if name_re:
            for m in name_re.finditer(line):
                found.append(("NAME", m.group(0)))
        for rule, text in found:
            if any(a.search(text) for a in allow):
                continue
            hits.append(f"{path}:{no}: {rule}: {text}")
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="*", help="reports or pages to check")
    ap.add_argument("--vault", help="the reporting vault's root, for names and the ledger key")
    ap.add_argument("--key", help="the vault key, instead of reading the ledger")
    ap.add_argument("--names", default="", help="extra names to flag, comma-separated")
    ap.add_argument("--allow", action="append", default=[], help="regex; matching hits are suppressed")
    ap.add_argument("--key-only", action="store_true", help="check only the key")
    a = ap.parse_args()

    root = None
    if a.vault:
        root = Path(a.vault).resolve()
        if not root.is_dir():
            print(f"not a directory: {a.vault}", file=sys.stderr)
            return 2
    try:
        allow = [re.compile(x) for x in a.allow]
    except re.error as e:
        print(f"bad --allow: {e}", file=sys.stderr)
        return 2
    names = {n.strip() for n in a.names.split(",") if n.strip()}
    key = a.key
    if root:
        names |= vault_names(root)
        key = key or ledger_key(root)
    if a.key_only and key is None:
        print("no key: pass --key or --vault", file=sys.stderr)
        return 2

    hits = check_key(key, names)
    if not a.key_only:
        if not a.files:
            print("no files given (or pass --key-only)", file=sys.stderr)
            return 2
        for f in a.files:
            p = Path(f)
            if not p.is_file():
                print(f"not a file: {f}", file=sys.stderr)
                return 2
            hits.extend(scan(p, names, allow))
    for h in hits:
        print(h)
    if hits:
        print(f"{len(hits)} hit(s). Replace each with a role (\"a later story\", \"the run ledger\", "
              f"\"src/db/<module>.ts\") or pass --allow for a deliberate placeholder.", file=sys.stderr)
        return 1
    print("clean" + (f" (key {key})" if key else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
