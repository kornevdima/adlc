"""Tests for migrate_1_3.py on a fixture vault shaped like a 1.2.0 ADLC vault.
Run: python3 -m pytest -q test_migrate_1_3.py  or  python3 test_migrate_1_3.py."""
import pathlib
import subprocess
import sys
import tempfile

SCRIPT = pathlib.Path(__file__).parent / "migrate_1_3.py"


def _vault():
    d = pathlib.Path(tempfile.mkdtemp())
    (d / "AGENTS.md").write_text("# V: LLM Wiki\n\nMode: ADLC\nToolset:\n  reader: none\nPurpose: A test vault\nOwner: ops\n",
                                 encoding="utf-8")
    (d / ".gitignore").write_text(".DS_Store\n", encoding="utf-8")
    us = d / "wiki" / "user-stories"
    us.mkdir(parents=True)
    (us / "US-001 Old story.md").write_text("---\ntype: user-story\ntitle: \"US-001 Old story\"\nstatus: ready\nepic: EPIC-001\n---\n\n# US-001\n",
                                           encoding="utf-8")
    sp = d / "wiki" / "sprints"
    sp.mkdir()
    (sp / "EPIC-001 Filtering.md").write_text("---\ntype: epic\ntitle: \"EPIC-001 Filtering\"\n---\n\n# EPIC-001\n", encoding="utf-8")
    (sp / "S01.md").write_text("---\ntype: sprint\n---\n", encoding="utf-8")
    specs = d / "services" / "web" / "wiki" / "specs"
    specs.mkdir(parents=True)
    (specs / "GATE-2-WEB.md").write_text("---\ntype: spec\n---\n\n# Decisions\n", encoding="utf-8")
    (specs / "GATE-1.5-WEB.md").write_text("---\ntype: spec\n---\n\n# Model, see [[GATE-2-WEB]]\n", encoding="utf-8")
    feat = d / "wiki" / "features"
    feat.mkdir()
    (feat / "FEAT-01.md").write_text("Spec: [[GATE-2-WEB|the decisions]] and [[GATE-1.5-WEB]].\n", encoding="utf-8")
    return d


def _run(vault, *extra):
    return subprocess.run([sys.executable, str(SCRIPT), "--vault", str(vault), *extra], capture_output=True, text=True)


def test_dry_run_changes_nothing():
    v = _vault()
    r = _run(v)
    assert r.returncode == 0, r.stderr
    assert "would" in r.stdout and "dry run" in r.stdout
    assert not (v / "wiki" / "epics").exists()
    assert (v / "wiki" / "sprints" / "EPIC-001 Filtering.md").exists()


def test_apply_migrates_everything():
    v = _vault()
    r = _run(v, "--apply")
    assert r.returncode == 0, r.stderr + r.stdout
    for f in ("product", "domains", "epics", "releases"):
        assert (v / "wiki" / f / "_index.md").exists() and (v / "wiki" / f / "_changelog.md").exists()
    assert (v / ".raw" / "spikes" / ".gitkeep").exists() and (v / ".raw" / "reflection").is_dir()
    ignore = (v / ".gitignore").read_text(encoding="utf-8")
    assert "*.local.md" in ignore and ".raw/reflection/" in ignore and ".DS_Store" in ignore
    assert (v / "wiki" / "epics" / "EPIC-001 Filtering.md").exists()
    assert not (v / "wiki" / "sprints" / "EPIC-001 Filtering.md").exists()
    assert (v / "wiki" / "sprints" / "S01.md").exists()
    web = v / "services" / "web" / "wiki"
    assert (web / "adrs" / "decisions.md").exists() and (web / "domain-model.md").exists()
    assert not list((web / "specs").glob("GATE-*"))
    feat = (v / "wiki" / "features" / "FEAT-01.md").read_text(encoding="utf-8")
    assert "[[decisions|the decisions]]" in feat and "[[domain-model]]" in feat
    assert "[[decisions]]" in (web / "domain-model.md").read_text(encoding="utf-8")
    story = (v / "wiki" / "user-stories" / "US-001 Old story.md").read_text(encoding="utf-8")
    assert "kind: feature" in story and "history: []" in story and "status: ready" in story
    agents = (v / "AGENTS.md").read_text(encoding="utf-8")
    assert "## How we work" in agents
    catalog = (v / "catalog-info.yaml").read_text(encoding="utf-8")
    assert "owner: ops" in catalog and "description: A test vault" in catalog
    assert (v / "wiki" / "board.md").exists()
    assert "[[US-001 Old story]]" in (v / "wiki" / "board.md").read_text(encoding="utf-8")


def test_second_apply_is_a_no_op_apart_from_the_board():
    v = _vault()
    assert _run(v, "--apply").returncode == 0
    r = _run(v, "--apply")
    assert r.returncode == 0
    lines = [l for l in r.stdout.splitlines() if l.startswith("did")]
    assert lines == ["did   generate wiki/board.md with board.py"] or lines == ["did  generate wiki/board.md with board.py"]


def test_missing_wiki_is_an_error():
    d = pathlib.Path(tempfile.mkdtemp())
    assert _run(d).returncode == 2


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"ok   {name}")
            except AssertionError as e:  # noqa: PERF203
                failures += 1
                print(f"FAIL {name}: {e}")
    sys.exit(1 if failures else 0)
