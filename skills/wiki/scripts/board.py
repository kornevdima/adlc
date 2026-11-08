#!/usr/bin/env python3
"""Render the team's board, wiki/board.md, from the story frontmatter.

    python3 board.py --vault .            # writes wiki/board.md (and wiki/board.base with reader: obsidian)
    python3 board.py --vault . --check    # exit 1 when board.md is stale, writes nothing
    python3 board.py --vault . --no-base  # never write the .base file

The board is a view and holds no data of its own: one column (section) per story status,
one card per story with its kind, size, priority, services, epic and release, then one
table per epic and per release with the count of stories done against the total. It reads
`wiki/user-stories/*.md` (frontmatter.md, Work records); `_index.md`, `_changelog.md` and
other `_`-prefixed files are skipped. The `updated:` date is the newest story's `updated`
(or `created`), so two runs on the same vault produce the same file. Standard library only.
Exit code: 0 on success, 1 when --check finds the board stale, 2 on bad input.
"""
import argparse
import pathlib
import re
import sys

STATUSES = ["draft", "ready", "in-progress", "blocked", "done", "dropped"]
TITLES = {"draft": "Draft", "ready": "Ready", "in-progress": "In progress", "blocked": "Blocked",
          "done": "Done", "dropped": "Dropped"}
KINDS = ["feature", "defect", "risk", "debt", "spike"]
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def parse_frontmatter(text):
    """Flat YAML only: `key: value` and `key:` followed by `- item` lines. Returns {key: str | [str]}."""
    m = re.match(r"﻿?---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    fm, key = {}, None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\s+-\s+", line) and key:
            fm.setdefault(key, [])
            if isinstance(fm[key], list):
                fm[key].append(_clean(re.sub(r"^\s+-\s+", "", line)))
            continue
        kv = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not kv:
            continue
        key, raw = kv.group(1), kv.group(2).strip()
        if raw.startswith("[") and raw.endswith("]"):
            fm[key] = [_clean(v) for v in raw[1:-1].split(",") if v.strip()]
        elif raw == "":
            fm[key] = []
        else:
            fm[key] = _clean(raw)
    return fm


def _clean(raw):
    raw = re.sub(r"\s+#.*$", "", raw).strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        raw = raw[1:-1]
    return raw.strip()


def scalar(fm, key, default=""):
    v = fm.get(key, default)
    if isinstance(v, list):
        return v[0] if v else default
    return v or default


def listing(fm, key):
    v = fm.get(key, [])
    if isinstance(v, str):
        return [x.strip() for x in v.split(",") if x.strip()] if v else []
    return v


def link_name(value):
    """`[[EPIC-003 Filtering]]` -> `EPIC-003 Filtering`; a bare value stays as it is."""
    m = LINK.search(value or "")
    return m.group(1).strip() if m else (value or "").strip()


def load_stories(vault):
    folder = vault / "wiki" / "user-stories"
    stories = []
    if not folder.is_dir():
        return stories
    for path in sorted(folder.glob("*.md")):
        if path.name.startswith("_"):
            continue
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        if scalar(fm, "type") not in ("user-story", "story", ""):
            continue
        status = scalar(fm, "status", "draft")
        if status not in STATUSES:
            status = "draft"
        stories.append({
            "name": path.stem,
            "title": scalar(fm, "title", path.stem),
            "kind": scalar(fm, "kind", "feature"),
            "status": status,
            "size": scalar(fm, "size"),
            "priority": scalar(fm, "priority"),
            "services": listing(fm, "services"),
            "feature": link_name(scalar(fm, "feature")),
            "epic": link_name(scalar(fm, "epic")),
            "sprint": link_name(scalar(fm, "sprint")),
            "release": link_name(scalar(fm, "release")),
            "updated": scalar(fm, "updated") or scalar(fm, "created"),
        })
    return stories


def card(s):
    bits = [s["kind"] or "feature"]
    if s["size"]:
        bits.append(s["size"])
    if s["priority"]:
        bits.append(s["priority"])
    if s["services"]:
        bits.append(", ".join(s["services"]))
    tail = []
    if s["feature"]:
        tail.append(f"feature [[{s['feature']}]]")
    if s["epic"]:
        tail.append(f"epic [[{s['epic']}]]")
    if s["sprint"]:
        tail.append(f"sprint [[{s['sprint']}]]")
    if s["release"]:
        tail.append(f"release [[{s['release']}]]")
    line = f"- [[{s['name']}]] ({'; '.join(bits)})"
    if tail:
        line += ": " + ", ".join(tail)
    return line


def counts(stories, key, label):
    """Rows `| <label> | done | total | blocked |` for every distinct value of `key`, unassigned last."""
    groups = {}
    for s in stories:
        groups.setdefault(s[key] or "", []).append(s)
    rows = []
    for name in sorted(k for k in groups if k) + ([""] if "" in groups else []):
        g = groups[name]
        done = sum(1 for s in g if s["status"] == "done")
        blocked = sum(1 for s in g if s["status"] == "blocked")
        total = sum(1 for s in g if s["status"] != "dropped")
        shown = f"[[{name}]]" if name else f"(no {label})"
        rows.append(f"| {shown} | {done} | {total} | {blocked} |")
    return rows


def render(stories):
    updated = max((s["updated"] for s in stories if s["updated"]), default="")
    out = ["---", "type: board", 'title: "Board"', f"updated: {updated}", "generated_by: board.py",
           "source: user-stories/", "tags:", "  - board", "  - meta", "---", "", "# Board", ""]
    out.append("Generated from the frontmatter of every page in `user-stories/` by the plugin's `board.py`; "
               "edit the story pages, never this one. One section per status; a card shows the story's kind, "
               "size, priority and services, then its feature, epic, sprint and release.")
    out.append("")
    total = len(stories)
    out.append(f"Stories: {total}. "
               + ", ".join(f"{TITLES[st].lower()} {sum(1 for s in stories if s['status'] == st)}" for st in STATUSES)
               + ".")
    out.append("")
    for st in STATUSES:
        col = [s for s in stories if s["status"] == st]
        out.append(f"## {TITLES[st]} ({len(col)})")
        out.append("")
        if col:
            out.extend(card(s) for s in col)
        else:
            out.append("- none")
        out.append("")
    out.append("## Epics")
    out.append("")
    out.append("Stories done against the total per epic; dropped stories are not counted. "
               "The epic record itself is in `epics/`.")
    out.append("")
    out.append("| Epic | Done | Total | Blocked |")
    out.append("|---|---|---|---|")
    out.extend(counts(stories, "epic", "epic") or ["| (no stories) | 0 | 0 | 0 |"])
    out.append("")
    out.append("## Releases")
    out.append("")
    out.append("Stories done against the total per release. The release record in `releases/` says what the user gets.")
    out.append("")
    out.append("| Release | Done | Total | Blocked |")
    out.append("|---|---|---|---|")
    out.extend(counts(stories, "release", "release") or ["| (no stories) | 0 | 0 | 0 |"])
    out.append("")
    return "\n".join(out)


BASE = """\
# Generated by board.py beside board.md; renders in Obsidian only (toolset.md, Reader).
filters:
  and:
    - file.inFolder("wiki/user-stories")
    - type == "user-story"
views:
  - type: table
    name: "Board"
    groupBy:
      property: status
      direction: ASC
    order:
      - file.name
      - kind
      - size
      - priority
      - services
      - epic
      - sprint
      - release
  - type: table
    name: "By epic"
    groupBy:
      property: epic
      direction: ASC
    order:
      - file.name
      - status
      - kind
      - release
  - type: table
    name: "By release"
    groupBy:
      property: release
      direction: ASC
    order:
      - file.name
      - status
      - epic
"""


def reader_is_obsidian(vault):
    try:
        sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
        import toolset  # noqa: WPS433
        _, values, _ = toolset.load(vault)
        res, _ = toolset.resolve(values, vault)
        return res.get("reader") == "obsidian"
    except Exception:  # noqa: BLE001 - a vault without toolset.py beside this script keeps the default
        return True


def main():
    ap = argparse.ArgumentParser(description="Render wiki/board.md from the story frontmatter.")
    ap.add_argument("--vault", default=".", help="vault root (holds wiki/)")
    ap.add_argument("--out", help="output page (default: <vault>/wiki/board.md)")
    ap.add_argument("--check", action="store_true", help="exit 1 when the board is stale; write nothing")
    ap.add_argument("--no-base", action="store_true", help="never write board.base")
    args = ap.parse_args()
    vault = pathlib.Path(args.vault).resolve()
    if not (vault / "wiki").is_dir():
        print(f"error: no wiki/ under {vault}", file=sys.stderr)
        return 2
    stories = load_stories(vault)
    text = render(stories) + "\n"
    out = pathlib.Path(args.out) if args.out else vault / "wiki" / "board.md"
    if args.check:
        current = out.read_text(encoding="utf-8") if out.is_file() else ""
        if current == text:
            print(f"board current: {out.relative_to(vault) if out.is_relative_to(vault) else out}")
            return 0
        print(f"board stale: {out.relative_to(vault) if out.is_relative_to(vault) else out} (run board.py to regenerate)")
        return 1
    out.write_text(text, encoding="utf-8")
    written = [out]
    if not args.no_base and reader_is_obsidian(vault):
        base = out.with_suffix(".base")
        base.write_text(BASE, encoding="utf-8")
        written.append(base)
    print(f"wrote {', '.join(p.as_posix() for p in written)}: {len(stories)} stories, "
          + ", ".join(f"{st} {sum(1 for s in stories if s['status'] == st)}" for st in STATUSES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
