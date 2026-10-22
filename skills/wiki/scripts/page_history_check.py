#!/usr/bin/env python3
"""Check that wiki pages hold the current state only, with history in per-folder changelogs.

    python3 page_history_check.py --vault .
    python3 page_history_check.py --vault . --exclude 'comparisons/*'
    python3 page_history_check.py --vault . --no-changelog     # markers only

The rule (writing-style.md § Pages that stay current): a page reads as if written today. Dated
"Update", "Correction" or "Revision" blocks, "as filed" markers, "superseded by" sentences and
"was X, now Y" wording are history, and history lives in the folder's `_changelog.md`, linked
from the folder's `_index.md`. Frontmatter `status: superseded` + `superseded_by:` is the one
allowed in-page pointer.

Findings, one per line as `code  path:line  text`:
- `history`            a marker in a page body (frontmatter and fenced code are not scanned)
- `changelog-missing`  a folder with authored pages and no `_changelog.md`
- `changelog-unlinked` a `_changelog.md` its folder's `_index.md` does not link
- `changelog-stale`    a `_changelog.md` whose `updated:` is older than its newest row

Not scanned: `_changelog.md`, `log.md`, log archives, lint reports, `hot.md`, `sources/`
(a summary describes its source as of its date) and `meta/` (ledgers and boards are records),
plus `--exclude` globs matched against the wiki-relative path. Standard library only; writes
nothing. Exit 0 when clean, 1 on findings, 2 on bad input.
"""
import argparse
import fnmatch
import pathlib
import re
import sys

DEFAULT_EXCLUDES = ["_changelog.md", "log.md", "log-archive*.md", "lint-report-*.md", "hot.md",
                    "sources/*", "meta/*"]
DATE = r"(?:\d{4}-\d{2}-\d{2}|\d{1,2}\.\d{1,2}\.\d{4}|\d{4}-\d{2})"
WORD = r"(?:Updates?|Updated|Corrections?|Corrected|Revisions?|Revised|Amendments?|Change\s+history|Revision\s+history|Changelog|Change\s+log)"
MARKERS = [
    # a heading that is a history block: "## Update 2026-10-20", "### Correction (2026-09-12)", "## Revision history"
    re.compile(rf"^#{{1,6}}\s+(?:\*\*)?{WORD}\b.*{DATE}", re.I),
    re.compile(rf"^#{{1,6}}\s+(?:\*\*)?(?:Updates?|Corrections?|Revisions?|Change\s+history|Revision\s+history|Changelog|Change\s+log|History)(?:\*\*)?\s*$", re.I),
    # a dated lead-in: "**Update 2026-10-20:**", "> **Correction (12.10.2026)**", "> [!note] Update 2026-10-20"
    re.compile(rf"^\s*(?:>\s*)*(?:\[![a-z]+\]\s*)?(?:\*\*|__)?{WORD}\b[^\n]{{0,30}}?{DATE}", re.I),
    re.compile(rf"^\s*(?:>\s*)+\[![a-z]+\]\s*{WORD}\b", re.I),
    # in-page history wording
    re.compile(r"\bas filed\b", re.I),
    re.compile(r"\bsuperseded by\b|\bsupersedes\b[^\n]{0,40}\[\[", re.I),
    re.compile(r"\(was\b[^)]{1,60}\)", re.I),
    re.compile(r"~~[^~\n]+~~\s*\S"),
]
TABLE_DATE_ROW = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|")


def body_lines(text):
    """(line_no, line) for the page body: frontmatter and fenced code excluded."""
    lines = text.split("\n")
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1
    in_code = False
    for n in range(i, len(lines)):
        line = lines[n]
        if line.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
            continue
        if not in_code:
            yield n + 1, line


def excluded(rel, patterns):
    name = rel.rsplit("/", 1)[-1]
    return any(fnmatch.fnmatch(rel, p) or fnmatch.fnmatch(name, p) for p in patterns)


def main():
    ap = argparse.ArgumentParser(description="Find history kept inside wiki pages instead of per-folder changelogs.")
    ap.add_argument("--vault", default=".", help="vault root (the directory holding wiki/)")
    ap.add_argument("--exclude", action="append", default=[], metavar="GLOB",
                    help="extra wiki-relative path or file-name glob to skip (repeatable)")
    ap.add_argument("--no-changelog", action="store_true", help="skip the changelog structure checks")
    args = ap.parse_args()

    wiki = pathlib.Path(args.vault).resolve() / "wiki"
    if not wiki.is_dir():
        print(f"page_history_check: no wiki/ under {args.vault}", file=sys.stderr)
        sys.exit(2)
    patterns = DEFAULT_EXCLUDES + args.exclude
    findings = []

    for path in sorted(wiki.rglob("*.md")):
        rel = path.relative_to(wiki).as_posix()
        if excluded(rel, patterns):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for n, line in body_lines(text):
            if any(m.search(line) for m in MARKERS):
                findings.append(("history", f"{rel}:{n}", line.strip()[:120]))

    if not args.no_changelog:
        for folder in sorted(p for p in wiki.rglob("*") if p.is_dir()):
            rel = folder.relative_to(wiki).as_posix()
            if excluded(rel + "/x", patterns) or rel.split("/")[0] in ("sources", "meta"):
                continue
            authored = [p for p in folder.glob("*.md") if not p.name.startswith("_")]
            if not authored:
                continue
            changelog = folder / "_changelog.md"
            if not changelog.is_file():
                findings.append(("changelog-missing", rel + "/", f"{len(authored)} pages, no _changelog.md"))
                continue
            index = folder / "_index.md"
            if not index.is_file() or not re.search(r"\[\[[^\]]*_changelog", index.read_text(encoding="utf-8", errors="replace")):
                findings.append(("changelog-unlinked", rel + "/_changelog.md",
                                 "not linked from _index.md" if index.is_file() else "folder has no _index.md"))
            text = changelog.read_text(encoding="utf-8", errors="replace")
            updated = re.search(r"^updated:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
            rows = TABLE_DATE_ROW.findall(text)
            if updated and rows and max(rows) > updated.group(1):
                findings.append(("changelog-stale", rel + "/_changelog.md",
                                 f"updated: {updated.group(1)}, newest row {max(rows)}"))

    for code, where, what in findings:
        print(f"{code:18} {where}  {what}")
    n = len(findings)
    print(f"page_history_check: {n} finding{'s' if n != 1 else ''}" if n else "page_history_check: clean")
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
