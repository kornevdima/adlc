#!/usr/bin/env python3
"""Vault tests for glossary.py: python3 skills/wiki/scripts/test_glossary.py"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("glossary.py")

GLOSSARY = """---
type: glossary
updated: 2026-01-01
---

# Glossary

## Registers

| Section | Lead-in | Owner | ID pattern | Entry |
|---|---|---|---|---|
{rows}
"""


def page(type_, body=""):
    return f"---\ntype: {type_}\n---\n\n{body}\n"


class VaultCase(unittest.TestCase):
    def make(self, files, rows=""):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        files = {"glossary.md": GLOSSARY.format(rows=rows), **files}
        for rel, text in files.items():
            path = root / "wiki" / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return root

    def run_cmd(self, root, *args):
        return subprocess.run([sys.executable, str(SCRIPT), "--vault", str(root), *args],
                              text=True, capture_output=True)

    def read(self, root, rel):
        return (root / "wiki" / rel).read_text(encoding="utf-8")


class OwnPages(VaultCase):
    STORIES = {f"user-stories/US-00{n} Story {n}.md": page("user-story", f"# US-00{n} Story {n}")
               for n in range(1, 4)}

    def test_work_page_does_not_take_the_id(self):
        root = self.make({**self.STORIES,
                          "planning/US-002 Census 2026-10-22.md": page("census", "Blocked until US-002 ships."),
                          "notes.md": page("note", "See US-002.")})
        out = self.run_cmd(root, "link", "--apply")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("id-clash: US-002 -> user-stories/US-002 Story 2.md", out.stdout)
        self.assertIn("[[US-002 Story 2|US-002]]", self.read(root, "notes.md"))
        self.assertIn("[[US-002 Story 2|US-002]]", self.read(root, "planning/US-002 Census 2026-10-22.md"))

    def test_unresolved_clash_is_not_linked(self):
        root = self.make({"a/US-001 One.md": page("user-story"), "b/US-001 Other.md": page("user-story"),
                          "notes.md": page("note", "See US-001.")})
        out = self.run_cmd(root, "link", "--apply")
        self.assertEqual(out.returncode, 1)
        self.assertIn("id-clash: US-001 unresolved", out.stdout)
        self.assertNotIn("[[", self.read(root, "notes.md"))

    def test_slug_filenames_are_own_pages(self):
        root = self.make({"decisions/ADR-005-short-title.md": page("decision", "# ADR-005 — Short title"),
                          "notes.md": page("note", "Per ADR-005.")})
        self.assertEqual(self.run_cmd(root, "build").returncode, 0)
        self.assertIn("| [[ADR-005-short-title\\|ADR-005]] | Short title |", self.read(root, "glossary.md"))
        self.run_cmd(root, "link", "--apply")
        self.assertIn("[[ADR-005-short-title|ADR-005]]", self.read(root, "notes.md"))


class Owners(VaultCase):
    def test_owner_resolves_by_path_and_alias(self):
        register = "| ID | Name |\n|---|---|\n| OQ-001 | Which region? |\n"
        root = self.make({"architecture/_index.md": page("index"),
                          "decisions/_index.md": page("index", register)},
                         rows="| Questions | Open ones. | [[decisions/_index\\|catalog]] | OQ-\\d{3} | {1} |")
        out = self.run_cmd(root, "build")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("### OQ-001\n\nWhich region?", self.read(root, "glossary.md"))

    def test_ambiguous_basename_fails(self):
        root = self.make({"architecture/_index.md": page("index"), "decisions/_index.md": page("index")},
                         rows="| Questions | Open ones. | [[_index]] | OQ-\\d{3} | {1} |")
        out = self.run_cmd(root, "build")
        self.assertEqual(out.returncode, 2)
        self.assertIn("matches 2 pages", out.stderr)


if __name__ == "__main__":
    unittest.main()
