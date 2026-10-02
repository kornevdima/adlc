#!/usr/bin/env python3
"""Repoint wikilinks from one page to another across a vault.

Dry run by default: prints per-file counts and changes nothing. Pass --apply to write.

    python3 relink.py --from "_run EPIC-001" --to "EPIC-001 As-built" --vault wiki/
    python3 relink.py --from "_run EPIC-001" --to "EPIC-001 As-built" --vault wiki/ --apply

Matches [[old]], [[old|alias]], [[old#anchor]], [[old#anchor|alias]], embeds (![[old]]),
path-qualified targets ([[sprints/old]]) and an optional .md suffix. The basename is
compared case-insensitively, as Obsidian resolves it. Aliases and anchors are kept;
anchored links are listed so you can check the anchor still exists on the new page.
Links inside fenced code blocks and inline code are left alone.

History is not rewritten: log.md, log archives and dated lint reports are excluded by
default (add more with --exclude, a glob matched against the vault-relative path and the
file name). Exit code: 0 on success (also when nothing matched), 2 on bad input.
"""
import argparse
import fnmatch
import re
import sys
from pathlib import Path

DEFAULT_EXCLUDES = ["log.md", "log-archive*.md", "lint-report-*.md"]

LINK = re.compile(r"(!?)\[\[([^\[\]|#]+)(#[^\[\]|]*)?(\|[^\[\]]*)?\]\]")
FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`\n]*`")


def basename(target):
    name = target.strip().rsplit("/", 1)[-1]
    return name[:-3] if name.lower().endswith(".md") else name


def relink_line(line, old, new, anchors):
    # Mask inline code so links inside it are not touched.
    spans = [m.span() for m in INLINE_CODE.finditer(line)]

    def in_code(pos):
        return any(a <= pos < b for a, b in spans)

    count = 0

    def sub(m):
        nonlocal count
        bang, target, anchor, alias = m.group(1), m.group(2), m.group(3) or "", m.group(4) or ""
        if in_code(m.start()) or basename(target).lower() != old.lower():
            return m.group(0)
        count += 1
        if anchor:
            anchors.append(anchor)
        return f"{bang}[[{new}{anchor}{alias}]]"

    return LINK.sub(sub, line), count


def relink_text(text, old, new):
    out, total, anchors, fenced = [], 0, [], False
    for line in text.splitlines(keepends=True):
        if FENCE.match(line):
            fenced = not fenced
            out.append(line)
            continue
        if fenced:
            out.append(line)
            continue
        line, n = relink_line(line, old, new, anchors)
        total += n
        out.append(line)
    return "".join(out), total, anchors


def excluded(rel, patterns):
    return any(fnmatch.fnmatch(rel, p) or fnmatch.fnmatch(Path(rel).name, p) for p in patterns)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from", dest="old", required=True, help="page name the links point at now")
    ap.add_argument("--to", dest="new", required=True, help="page name (or vault path) to point them at")
    ap.add_argument("--vault", default="wiki", help="folder to scan (default: wiki)")
    ap.add_argument("--exclude", action="append", default=[], help="extra glob to skip (repeatable)")
    ap.add_argument("--no-default-excludes", action="store_true", help="also rewrite logs and lint reports")
    ap.add_argument("--apply", action="store_true", help="write the changes (default: dry run)")
    args = ap.parse_args()

    root = Path(args.vault)
    if not root.is_dir():
        print(f"error: vault folder not found: {root}", file=sys.stderr)
        return 2
    old, new = basename(args.old), args.new.strip()
    if not old or not new or old.lower() == basename(new).lower():
        print("error: --from and --to must be two different page names", file=sys.stderr)
        return 2
    patterns = ([] if args.no_default_excludes else DEFAULT_EXCLUDES) + args.exclude

    files = links = 0
    skipped = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        text = path.read_text(encoding="utf-8")
        if excluded(rel, patterns):
            if LINK.search(text) and relink_text(text, old, new)[1]:
                skipped.append(rel)
            continue
        new_text, n, anchors = relink_text(text, old, new)
        if not n:
            continue
        files += 1
        links += n
        note = f"  (anchors to check: {', '.join(sorted(set(anchors)))})" if anchors else ""
        print(f"{n:4d}  {rel}{note}")
        if args.apply:
            path.write_text(new_text, encoding="utf-8")

    mode = "rewrote" if args.apply else "would rewrite"
    print(f"{mode} {links} link(s) in {files} file(s): [[{old}]] -> [[{new}]]")
    if skipped:
        print(f"left as history ({len(skipped)}): {', '.join(skipped)}")
    if not args.apply and links:
        print("dry run: pass --apply to write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
