"""Tests for toolset.py: the block parser and the defaults. Run: python3 -m pytest -q test_toolset.py
or python3 test_toolset.py."""
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import toolset  # noqa: E402

BLOCK = """# A vault

Mode: ADLC
Concerns: qa, design
Toolset:
  reader: wiki-renderer
  code-nav: semble, serena
  design: impeccable, taste-skill
  design-system: ~/work/design-system

## Structure
"""


def _vault(text=None):
    d = pathlib.Path(tempfile.mkdtemp())
    if text is not None:
        (d / "AGENTS.md").write_text(text, encoding="utf-8")
    return d


def test_block_form_is_read():
    values, found = toolset.parse_block(BLOCK)
    assert found
    assert values == {"reader": "wiki-renderer", "code-nav": "semble, serena",
                      "design": "impeccable, taste-skill", "design-system": "~/work/design-system"}
    res, warnings = toolset.resolve(values, _vault())
    assert warnings == []
    assert res["reader"] == "wiki-renderer"
    assert res["code-nav"] == ["semble", "serena"]
    assert res["design"] == ["impeccable", "taste-skill"]
    assert res["design-system"].endswith("/work/design-system") and "~" not in res["design-system"]


def test_one_line_form_is_read():
    values, found = toolset.parse_block("Mode: B\nToolset: reader=none; code-nav=semble\n")
    assert found
    res, _ = toolset.resolve(values, _vault())
    assert res["reader"] == "none"
    assert res["code-nav"] == ["semble"]
    assert res["design"] == ["none"]


def test_block_ends_at_first_unindented_line():
    values, _ = toolset.parse_block("Toolset:\n  reader: obsidian\nOwner: x\n  design: impeccable\n")
    assert values == {"reader": "obsidian"}


def test_missing_block_gives_defaults():
    v = _vault("Mode: B\nConcerns: none\n")
    agents, values, found = toolset.load(v)
    assert not found and values == {}
    res, warnings = toolset.resolve(values, v)
    assert res == {"reader": "obsidian", "code-nav": ["none"], "design": ["none"], "design-system": "none",
                   "layout": "symlinks", "engineering": "none", "cost": "none"}
    assert warnings == []


def test_layout_engineering_and_cost_are_read():
    values, found = toolset.parse_block(
        "Toolset:\n  reader: wiki-renderer\n  layout: worktrees\n  engineering: ub-mode\n  cost: tokeneconomizer\n")
    assert found
    res, warnings = toolset.resolve(values, _vault())
    assert warnings == []
    assert (res["layout"], res["engineering"], res["cost"]) == ("worktrees", "ub-mode", "tokeneconomizer")


def test_unknown_layout_engineering_and_cost_fall_back_with_warnings():
    res, warnings = toolset.resolve({"layout": "submodules", "engineering": "tdd", "cost": "cheap"}, _vault())
    assert (res["layout"], res["engineering"], res["cost"]) == ("symlinks", "none", "none")
    assert len(warnings) == 3


def test_code_wiki_path_follows_the_layout():
    v = _vault()
    assert toolset.code_wiki_path({"layout": "symlinks"}, v, "api") == v / "services" / "api" / "wiki"
    assert toolset.code_wiki_path({"layout": "worktrees"}, v, "api") == v / "service-wikis" / "api"


def test_worktree_check_needs_services_ignored():
    v = _vault()
    ok, detail, _ = toolset.check_layout("worktrees", v)
    assert not ok and "/services/" in detail
    (v / ".gitignore").write_text("/services/\n/tools/\n", encoding="utf-8")
    ok, _, _ = toolset.check_layout("worktrees", v)
    assert ok


def test_ub_mode_check_needs_the_skill_and_the_tools():
    v = _vault()
    ok, detail, hint = toolset.check_tool("ub-mode", v)
    assert not ok and "setup-ub-mode.sh" in hint
    (v / ".claude" / "skills" / "ub-mode").mkdir(parents=True)
    (v / ".claude" / "skills" / "ub-mode" / "SKILL.md").write_text("x", encoding="utf-8")
    for name in ("crapper", "dryer", "mutator"):
        (v / "tools" / name / ".venv").mkdir(parents=True)
    ok, _, _ = toolset.check_tool("ub-mode", v)
    assert ok


def test_default_code_nav_is_graphify_when_a_graph_exists():
    v = _vault("Mode: B\n")
    (v / "graphify-out").mkdir()
    (v / "graphify-out" / "graph.json").write_text("{}")
    res, _ = toolset.resolve({}, v)
    assert res["code-nav"] == ["graphify"]


def test_unknown_values_are_dropped_with_a_warning():
    res, warnings = toolset.resolve({"reader": "notion", "code-nav": "graphify, sourcegraph", "design": "figma",
                                     "colour": "blue"}, _vault())
    assert res["reader"] == "obsidian"
    assert res["code-nav"] == ["graphify"]
    assert res["design"] == ["none"]
    assert len(warnings) == 4
    assert any("unknown key `colour`" in w for w in warnings)


def test_idea_is_a_code_nav_option_in_any_mix():
    res, warnings = toolset.resolve({"code-nav": "semble, idea"}, _vault())
    assert res["code-nav"] == ["semble", "idea"] and warnings == []
    res, _ = toolset.resolve({"code-nav": "idea"}, _vault())
    assert res["code-nav"] == ["idea"]


def test_idea_server_answers_rejects_a_closed_port():
    up, info = toolset.idea_server_answers("http://127.0.0.1:9/stream", timeout=0.5)
    assert up is False and info == ""


def test_none_beside_a_tool_is_dropped():
    res, _ = toolset.resolve({"code-nav": "none, semble"}, _vault())
    assert res["code-nav"] == ["semble"]


def test_fmt_block_round_trips():
    res = {"reader": "wiki-renderer", "code-nav": ["semble", "serena"], "design": ["impeccable"], "design-system": "none",
           "layout": "worktrees", "engineering": "ub-mode", "cost": "tokeneconomizer"}
    text = toolset.fmt_block(res)
    values, found = toolset.parse_block(text)
    assert found
    back, warnings = toolset.resolve(values, _vault())
    assert warnings == []
    assert back == res


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"ok    {name}")
            except AssertionError as e:
                failures += 1
                print(f"FAIL  {name}: {e}")
    sys.exit(1 if failures else 0)
