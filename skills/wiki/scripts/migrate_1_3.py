#!/usr/bin/env python3
"""Migrate a Mode ADLC vault to the 1.3.0 operating model. Dry run by default; --apply writes.

    python3 migrate_1_3.py --vault .            # report what would change
    python3 migrate_1_3.py --vault . --apply    # do it

What it does (skills/wiki/references/migration-1.3.md has the hand procedure and the reasons):

1. Creates the new folders with an _index.md and a _changelog.md each: wiki/product/, wiki/domains/,
   wiki/epics/, wiki/releases/; and .raw/spikes/, .raw/reflection/ (with a .gitkeep in spikes).
2. Adds the ignore lines the 1.3.0 git-setup lists (`*.local.md`, `.raw/reflection/`,
   `.claude/settings.local.json`) to the vault's .gitignore when they are missing.
3. Moves epic pages (frontmatter `type: epic`, or a filename starting with EPIC-) out of wiki/sprints/
   into wiki/epics/. Wikilinks resolve by basename, so a move needs no relink.
4. Renames gate pages in every code wiki (specs/GATE-1-<SVC>.md and so on) to the artifact names and
   repoints the links with relink.py: GATE-1 -> architecture-drivers.md, GATE-1.5 -> domain-model.md,
   GATE-2 -> adrs/decisions.md (the worker splits it into one ADR per page on its next run),
   GATE-3 -> engineering-workflow.md.
5. Adds `kind: feature` to every wiki/user-stories/ page whose frontmatter has no `kind`, and an empty
   `history:` list when absent. No other story field is touched; the dates are the loop's to write.
6. Appends a `## How we work` section to AGENTS.md when it has none (the defaults from records.md),
   and writes catalog-info.yaml at the vault root when absent (owner from `Owner:`, description from
   `Purpose:`).
7. Generates wiki/board.md with board.py.

Standard library only. Exit code: 0 on success, 2 on bad input.
"""
import argparse
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
NEW_WIKI_FOLDERS = {
    "product": "The PRD (prd.md) and the C4 context with the team dependencies (context.md).",
    "domains": "Product domains: one page per domain, context-map.md for the relations between them.",
    "epics": "One record per epic: rulings table, Gates table, as-built section at the close.",
    "releases": "One record per release: what the user gets, the epics it bundles, the stories it closed.",
}
IGNORE_LINES = ["*.local.md", ".raw/reflection/", ".claude/settings.local.json"]
GATE_MAP = [
    (re.compile(r"^GATE-1-(.+)\.md$", re.I), "architecture-drivers.md"),
    (re.compile(r"^GATE-1\.5-(.+)\.md$", re.I), "domain-model.md"),
    (re.compile(r"^GATE-2-(.+)\.md$", re.I), "adrs/decisions.md"),
    (re.compile(r"^GATE-3-(.+)\.md$", re.I), "engineering-workflow.md"),
]
HOW_WE_WORK = """
## How we work

The team's choices, in plain lines; a change here is a row in the vault's changelog, not a decision record (the plugin's `skills/wiki/references/records.md`). The tools are the `Toolset:` block above.

- Branches: one branch per story named `<STORY-ID>-<slug>`, from main; code reviewed in a pull request before merge
- Review: the reviewer worker on every story; a second person on anything that touches auth, billing or data migration
- Definition of done: built, reviewed, verified against the contract, documented, committed with the trace id; the service AGENTS.md adds its own gates
- Personal settings stay in `.claude/settings.local.json`; machine setup in `wiki/meta/machine.local.md`; neither is committed
"""


def frontmatter(text):
    m = re.match(r"﻿?---\s*\n(.*?)\n---", text, re.S)
    return m


def fm_value(text, key):
    m = frontmatter(text)
    if not m:
        return ""
    v = re.search(rf"^{key}:\s*(.*?)\s*$", m.group(1), re.M)
    return v.group(1).strip().strip("\"'") if v else ""


def index_page(title, lead):
    return (f"---\ntype: index\ntitle: \"{title}\"\ncreated: {TODAY}\nupdated: {TODAY}\ntags:\n  - index\n---\n\n"
            f"# {title}\n\n{lead}\n\nHistory: [[_changelog]].\n")


def changelog_page(title):
    return (f"---\ntype: changelog\ntitle: \"{title} changelog\"\ncreated: {TODAY}\nupdated: {TODAY}\ntags:\n  - changelog\n---\n\n"
            f"# {title} changelog\n\nPages show the current state only; history goes here, newest first.\n\n"
            "| Date | Page | Change |\n|---|---|---|\n")


class Migration:
    def __init__(self, vault, apply):
        self.vault = vault
        self.apply = apply
        self.actions = []

    def say(self, line):
        self.actions.append(line)
        print(("did  " if self.apply else "would") + " " + line)

    def write(self, path, text):
        if self.apply:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    # 1
    def folders(self):
        wiki = self.vault / "wiki"
        for name, lead in NEW_WIKI_FOLDERS.items():
            folder = wiki / name
            if not (folder / "_index.md").exists():
                self.say(f"create wiki/{name}/_index.md and _changelog.md")
                self.write(folder / "_index.md", index_page(name.capitalize(), lead))
                self.write(folder / "_changelog.md", changelog_page(name.capitalize()))
        for raw in ("spikes", "reflection"):
            folder = self.vault / ".raw" / raw
            if not folder.is_dir():
                self.say(f"create .raw/{raw}/")
                if self.apply:
                    folder.mkdir(parents=True, exist_ok=True)
                if raw == "spikes":
                    self.write(folder / ".gitkeep", "")

    # 2
    def gitignore(self):
        path = self.vault / ".gitignore"
        current = path.read_text(encoding="utf-8") if path.is_file() else ""
        have = {l.strip() for l in current.splitlines()}
        missing = [l for l in IGNORE_LINES if l not in have]
        if missing:
            self.say(f"add to .gitignore: {', '.join(missing)}")
            text = current + ("" if current.endswith("\n") or not current else "\n") + "\n".join(missing) + "\n"
            self.write(path, text)

    # 3
    def move_epics(self):
        sprints = self.vault / "wiki" / "sprints"
        epics = self.vault / "wiki" / "epics"
        if not sprints.is_dir():
            return
        for page in sorted(sprints.glob("*.md")):
            if page.name.startswith("_"):
                continue
            text = page.read_text(encoding="utf-8")
            if fm_value(text, "type") == "epic" or re.match(r"^EPIC-", page.name, re.I):
                self.say(f"move wiki/sprints/{page.name} -> wiki/epics/ (links resolve by basename; no relink)")
                if self.apply:
                    epics.mkdir(parents=True, exist_ok=True)
                    page.rename(epics / page.name)

    # 4
    def code_wikis(self):
        found = []
        for pattern in ("services/*/wiki", "service-wikis/*"):
            for w in sorted(self.vault.glob(pattern)):
                if w.is_dir() and not w.name.startswith("."):
                    found.append(w)
        return found

    def rename_gates(self):
        for wiki in self.code_wikis():
            for page in sorted(wiki.rglob("GATE-*.md")):
                for rx, target in GATE_MAP:
                    if rx.match(page.name):
                        dest = wiki / target
                        rel_wiki = wiki.relative_to(self.vault).as_posix()
                        if dest.exists():
                            self.say(f"skip {rel_wiki}/{page.relative_to(wiki).as_posix()}: {target} already exists")
                            break
                        self.say(f"rename {rel_wiki}/{page.relative_to(wiki).as_posix()} -> {rel_wiki}/{target} and relink [[{page.stem}]] -> [[{dest.stem}]]")
                        if self.apply:
                            dest.parent.mkdir(parents=True, exist_ok=True)
                            page.rename(dest)
                            for scan in [self.vault / "wiki", *self.code_wikis()]:
                                subprocess.run([sys.executable, str(HERE / "relink.py"), "--from", page.stem, "--to", dest.stem,
                                                "--vault", str(scan), "--apply"], check=False, capture_output=True)
                        break

    # 5
    def story_fields(self):
        folder = self.vault / "wiki" / "user-stories"
        if not folder.is_dir():
            return
        for page in sorted(folder.glob("*.md")):
            if page.name.startswith("_"):
                continue
            text = page.read_text(encoding="utf-8")
            m = frontmatter(text)
            if not m:
                continue
            add = []
            if not re.search(r"^kind:", m.group(1), re.M):
                add.append("kind: feature")
            if not re.search(r"^history:", m.group(1), re.M):
                add.append("history: []")
            if add:
                self.say(f"add {', '.join(a.split(':')[0] for a in add)} to wiki/user-stories/{page.name}")
                new_fm = m.group(1) + "\n" + "\n".join(add)
                self.write(page, text[:m.start(1)] + new_fm + text[m.end(1):])

    # 6
    def agents_and_catalog(self):
        agents = self.vault / "AGENTS.md"
        if agents.is_file():
            text = agents.read_text(encoding="utf-8")
            if "## How we work" not in text:
                self.say("append '## How we work' (defaults) to AGENTS.md")
                self.write(agents, text.rstrip("\n") + "\n" + HOW_WE_WORK)
            owner = re.search(r"^Owner:\s*(.+)$", text, re.M)
            purpose = re.search(r"^Purpose:\s*(.+)$", text, re.M)
        else:
            owner = purpose = None
        catalog = self.vault / "catalog-info.yaml"
        if not catalog.exists():
            self.say("write catalog-info.yaml (owner and description from AGENTS.md; fill in name and domain)")
            self.write(catalog, (
                "apiVersion: backstage.io/v1alpha1\nkind: System\nmetadata:\n"
                f"  name: {self.vault.name.lower().replace(' ', '-')}\n"
                f"  description: {purpose.group(1).strip() if purpose else '<the vault purpose>'}\n"
                "spec:\n"
                f"  owner: {owner.group(1).strip() if owner else '<team or role>'}\n"
                "  domain: <the product domain this system belongs to>\n"))

    # 7
    def board(self):
        self.say("generate wiki/board.md with board.py")
        if self.apply:
            subprocess.run([sys.executable, str(HERE / "board.py"), "--vault", str(self.vault)], check=False)

    def run(self):
        self.folders()
        self.gitignore()
        self.move_epics()
        self.rename_gates()
        self.story_fields()
        self.agents_and_catalog()
        self.board()
        return self.actions


def main():
    ap = argparse.ArgumentParser(description="Migrate a Mode ADLC vault to the 1.3.0 operating model.")
    ap.add_argument("--vault", default=".", help="vault root (holds wiki/ and AGENTS.md)")
    ap.add_argument("--apply", action="store_true", help="write the changes (default: dry run)")
    args = ap.parse_args()
    vault = pathlib.Path(args.vault).resolve()
    if not (vault / "wiki").is_dir():
        print(f"error: no wiki/ under {vault}", file=sys.stderr)
        return 2
    actions = Migration(vault, args.apply).run()
    mode = "applied" if args.apply else "dry run"
    print(f"{mode}: {len(actions)} action(s)" + ("" if args.apply else "; pass --apply to write"))
    return 0


TODAY = __import__("datetime").date.today().isoformat()

if __name__ == "__main__":
    sys.exit(main())
