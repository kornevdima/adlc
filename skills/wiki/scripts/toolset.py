#!/usr/bin/env python3
"""Read, check and propose the vault's Toolset block (skills/wiki/references/toolset.md).

    python3 toolset.py --vault . show      # the resolved choices, one key=value per line
    python3 toolset.py --vault . check     # is each chosen tool installed on this machine
    python3 toolset.py --vault . detect    # propose a Toolset block from what the machine has
    python3 toolset.py --vault . show --key code-nav   # one value (for shell tests)

The block lives in the vault's AGENTS.md, beside `Mode:` and `Concerns:`:

    Toolset:
      reader: wiki-renderer
      code-nav: semble, serena
      design: impeccable, taste-skill
      design-system: ~/work/design-system

The one-line form `Toolset: reader=wiki-renderer; code-nav=semble,serena` is read too.
A missing key takes its default; a missing block takes every default (the pre-1.1.0
behaviour: Obsidian, graphify when a graph exists, no design tool).

`show` prints `key=value` lines plus `source=block|default` (exit 0; exit 1 when AGENTS.md
has no block, after printing the defaults). `check` prints one `ok|missing  tool  hint` line
per chosen tool (exit 0 all present, 1 something missing). `detect` prints a block (exit 0).
Exit 2 on bad input. Standard library only; reads `~/.claude.json` for MCP server *names*
only and never prints a server's env or args; writes nothing.
"""
import argparse
import glob
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys

KEYS = ("reader", "code-nav", "design", "design-system")
OPTIONS = {
    "reader": {"obsidian", "wiki-renderer", "none"},
    "code-nav": {"graphify", "semble", "serena", "none"},
    "design": {"impeccable", "taste-skill", "none"},
}
MULTI = {"code-nav", "design"}
BLOCK_KEY = re.compile(r"^\s{2,}([a-z-]+)\s*:\s*(.*?)\s*$")
ONE_LINE = re.compile(r"^Toolset:\s*(\S.*)$")


def parse_block(text):
    """Return ({key: raw value}, found) from an AGENTS.md text. Unknown keys are kept."""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        m = ONE_LINE.match(line)
        if m:
            values = {}
            for part in m.group(1).split(";"):
                if "=" in part:
                    k, v = part.split("=", 1)
                    values[k.strip()] = v.strip()
            return values, True
        if line.strip() == "Toolset:":
            values = {}
            for nxt in lines[i + 1:]:
                bm = BLOCK_KEY.match(nxt)
                if not bm:
                    break
                values[bm.group(1)] = bm.group(2)
            return values, True
    return {}, False


def split_values(raw):
    return [v.strip() for v in raw.split(",") if v.strip()]


def resolve(values, vault):
    """Apply defaults and normalise. Returns ({key: value-or-list}, warnings)."""
    out, warnings = {}, []
    for k in values:
        if k not in KEYS:
            warnings.append(f"unknown key `{k}` ignored (known: {', '.join(KEYS)})")
    reader = values.get("reader", "obsidian").strip().lower() or "obsidian"
    if reader not in OPTIONS["reader"]:
        warnings.append(f"reader `{reader}` is not one of {sorted(OPTIONS['reader'])}; using obsidian")
        reader = "obsidian"
    out["reader"] = reader

    if "code-nav" in values:
        nav = [v.lower() for v in split_values(values["code-nav"])] or ["none"]
    else:
        has_graph = any(vault.glob("**/graphify-out/graph.json")) if vault.exists() else False
        nav = ["graphify"] if has_graph else ["none"]
    bad = [v for v in nav if v not in OPTIONS["code-nav"]]
    for v in bad:
        warnings.append(f"code-nav `{v}` is not one of {sorted(OPTIONS['code-nav'])}; dropped")
    nav = [v for v in nav if v not in bad] or ["none"]
    if "none" in nav and len(nav) > 1:
        nav = [v for v in nav if v != "none"]
    out["code-nav"] = nav

    design = [v.lower() for v in split_values(values.get("design", "none"))] or ["none"]
    bad = [v for v in design if v not in OPTIONS["design"]]
    for v in bad:
        warnings.append(f"design `{v}` is not one of {sorted(OPTIONS['design'])}; dropped")
    design = [v for v in design if v not in bad] or ["none"]
    if "none" in design and len(design) > 1:
        design = [v for v in design if v != "none"]
    out["design"] = design

    ds = values.get("design-system", "none").strip() or "none"
    out["design-system"] = ds if ds.lower() == "none" else os.path.expanduser(ds)
    return out, warnings


def load(vault):
    agents = vault / "AGENTS.md"
    if not agents.is_file():
        return None, {}, False
    values, found = parse_block(agents.read_text(encoding="utf-8", errors="replace"))
    return agents, values, found


# ── availability checks ───────────────────────────────────────────────────────

def home():
    return pathlib.Path(os.path.expanduser("~"))


def mcp_server_names():
    """Names of MCP servers configured for Claude Code at user or any project scope."""
    names = set()
    cfg = home() / ".claude.json"
    if cfg.is_file():
        try:
            d = json.loads(cfg.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            d = {}
        names.update((d.get("mcpServers") or {}).keys())
        for proj in (d.get("projects") or {}).values():
            names.update(((proj or {}).get("mcpServers") or {}).keys())
    return names


def project_mcp_names(vault):
    names = set()
    f = vault / ".mcp.json"
    if f.is_file():
        try:
            names.update((json.loads(f.read_text(encoding="utf-8")).get("mcpServers") or {}).keys())
        except (OSError, ValueError):
            pass
    return names


def plugin_present(marketplace, plugin, probe):
    pattern = str(home() / ".claude" / "plugins" / "cache" / marketplace / plugin / "*" / probe)
    return bool(glob.glob(pattern))


def graphify_python(vault):
    """A Python that imports graphify: the pin under any graphify-out/, else PATH candidates."""
    cands = []
    for pin in vault.glob("**/graphify-out/.graphify_python"):
        try:
            cands.append(pin.read_text(encoding="utf-8").strip())
        except OSError:
            pass
    cands += ["python3.13", "python3.12", "python3.11", "python3.10", "python3"]
    for c in cands:
        exe = c if os.path.isabs(c) else shutil.which(c)
        if not exe:
            continue
        try:
            r = subprocess.run([exe, "-c", "import graphify"], capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            continue
        if r.returncode == 0:
            return exe
    return None


def check_tool(name, vault):
    """(ok, detail, hint) for one tool name."""
    mcp = mcp_server_names() | project_mcp_names(vault)
    if name == "obsidian":
        found = (pathlib.Path("/Applications/Obsidian.app").exists() or shutil.which("obsidian")
                 or (home() / ".local/share/flatpak/exports/bin/md.obsidian.Obsidian").exists()
                 or pathlib.Path("/var/lib/flatpak/exports/bin/md.obsidian.Obsidian").exists())
        return bool(found), "Obsidian app", "install from https://obsidian.md/download, or set reader: none"
    if name == "wiki-renderer":
        found = shutil.which("wiki-renderer") or (home() / ".wiki-renderer").is_dir()
        return bool(found), "wiki-renderer CLI", "curl -fsSL https://raw.githubusercontent.com/kornevdima/wiki-renderer/main/install.sh | sh"
    if name == "graphify":
        py = graphify_python(vault)
        return bool(py), f"graphify in {py}" if py else "no Python imports graphify", "bash <plugin>/bin/setup-graphify.sh <project>"
    if name == "semble":
        cli = shutil.which("semble") or shutil.which("uvx")
        return ("semble" in mcp and bool(cli)), (
            f"MCP server {'configured' if 'semble' in mcp else 'missing'}, CLI {'semble' if shutil.which('semble') else ('uvx' if shutil.which('uvx') else 'missing')}"
        ), 'claude mcp add -s user semble -- uvx --from "semble[mcp]==0.7.0" semble'
    if name == "serena":
        cli = shutil.which("serena")
        return ("serena" in mcp and bool(cli)), (
            f"MCP server {'configured' if 'serena' in mcp else 'missing'}, CLI {'on PATH' if cli else 'missing'}"
        ), "install Serena (https://github.com/oraios/serena), then: claude mcp add -s user serena -- serena start-mcp-server --context=claude-code --project-from-cwd"
    if name == "impeccable":
        ok = plugin_present("impeccable", "impeccable", "skills/impeccable/scripts/impeccable")
        return ok, "impeccable plugin", "claude plugin marketplace add pbakaus/impeccable && claude plugin install impeccable@impeccable"
    if name == "taste-skill":
        ok = plugin_present("taste-skill", "taste-skill", "skills/taste-skill/SKILL.md")
        return ok, "taste-skill plugin", "claude plugin marketplace add leonxlnx/taste-skill && claude plugin install taste-skill@taste-skill"
    return False, "unknown tool", ""


def check_design_system(path):
    p = pathlib.Path(path)
    if not p.is_dir():
        return False, f"{path} is not a folder", "set design-system to the folder holding DESIGN.md or the brand book, or none"
    markers = [m for m in ("DESIGN.md", "tokens.json", "project/tokens.json", "AGENTS.md", "README.md") if (p / m).exists()]
    if "DESIGN.md" in markers or "tokens.json" in markers or "project/tokens.json" in markers:
        return True, f"{path} ({', '.join(markers)})", ""
    return False, f"{path} has no DESIGN.md or tokens file ({', '.join(markers) or 'empty'})", "run `impeccable document` in that repo, or point at the folder that has them"


def detect(vault):
    """Propose a block from what the machine has."""
    reader = "obsidian" if check_tool("obsidian", vault)[0] else ("wiki-renderer" if check_tool("wiki-renderer", vault)[0] else "none")
    if check_tool("wiki-renderer", vault)[0] and reader == "obsidian":
        reader = "wiki-renderer"  # a renderer install is a deliberate choice; Obsidian is often just present
    nav = [t for t in ("semble", "serena") if check_tool(t, vault)[0]]
    if not nav and check_tool("graphify", vault)[0]:
        nav = ["graphify"]
    design = [t for t in ("impeccable", "taste-skill") if check_tool(t, vault)[0]]
    return {"reader": reader, "code-nav": nav or ["none"], "design": design or ["none"], "design-system": "none"}


def fmt_block(res):
    lines = ["Toolset:", f"  reader: {res['reader']}", f"  code-nav: {', '.join(res['code-nav'])}",
             f"  design: {', '.join(res['design'])}", f"  design-system: {res['design-system']}"]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Read, check or propose the vault's Toolset block.")
    ap.add_argument("--vault", default=".", help="vault root (the directory holding AGENTS.md and wiki/)")
    ap.add_argument("command", choices=["show", "check", "detect"])
    ap.add_argument("--key", choices=KEYS, help="show: print one value only")
    args = ap.parse_args()
    vault = pathlib.Path(args.vault).resolve()
    if not vault.is_dir():
        print(f"error: {vault} is not a directory", file=sys.stderr)
        return 2

    if args.command == "detect":
        res = detect(vault)
        print(fmt_block(res))
        print("# proposed from this machine; set design-system to your design system's folder, or leave none", file=sys.stderr)
        return 0

    agents, values, found = load(vault)
    res, warnings = resolve(values, vault)
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)

    if args.command == "show":
        if args.key:
            v = res[args.key]
            print(", ".join(v) if isinstance(v, list) else v)
        else:
            for k in KEYS:
                v = res[k]
                print(f"{k}={', '.join(v) if isinstance(v, list) else v}")
            print(f"source={'block' if found else 'default'}")
        if not found:
            where = agents if agents else vault / "AGENTS.md"
            print(f"note: no Toolset block in {where}; defaults shown (toolset.md § The block)", file=sys.stderr)
            return 1
        return 0

    # check
    missing = 0
    tools = ([res["reader"]] if res["reader"] != "none" else []) + \
            [t for t in res["code-nav"] if t != "none"] + [t for t in res["design"] if t != "none"]
    for t in tools:
        ok, detail, hint = check_tool(t, vault)
        print(f"{'ok     ' if ok else 'missing'}  {t:<13} {detail}" + ("" if ok else f"  -> {hint}"))
        missing += 0 if ok else 1
    if res["design-system"] != "none":
        ok, detail, hint = check_design_system(res["design-system"])
        print(f"{'ok     ' if ok else 'missing'}  {'design-system':<13} {detail}" + ("" if ok else f"  -> {hint}"))
        missing += 0 if ok else 1
    elif res["design"] != ["none"]:
        print("note     design-system none: the designer works from the service's own DESIGN.md or asks for one")
    if not tools and res["design-system"] == "none":
        print("nothing to check: every slot is none")
    if not found:
        print("note: no Toolset block; checked the defaults", file=sys.stderr)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
