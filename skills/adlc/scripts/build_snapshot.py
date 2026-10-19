#!/usr/bin/env python3
"""Build snapshots and the tester footprint check for the ADLC story loop.

The dispatcher records the working tree after each builder round, then checks after each
tester round that the tester touched only test files. Nothing here moves the branch, the
index or the working tree (except `restore`, on paths you name), and nothing is pushed.

    python3 build_snapshot.py snapshot  --repo services/<service> --story US-042
    python3 build_snapshot.py footprint --repo services/<service> --story US-042
    python3 build_snapshot.py restore   --repo services/<service> --story US-042 src/db/<module>.ts
    python3 build_snapshot.py clean     --repo services/<service> --story US-042

snapshot   Writes the working tree (tracked + untracked, minus ignored) as a commit on
           refs/adlc/<story>/build-<n>, n = 1, 2, ... It uses a temporary GIT_INDEX_FILE,
           so the real index, the branch and the working tree are untouched.
footprint  Compares the working tree with the latest snapshot. Every path that differs, or
           was written after the snapshot even if its content is back (an edit made and then
           reverted), must match a test glob. Defaults: *.test.* *.spec.* *.itest.* tests/**
           e2e/**; pass --globs to use the service's own (its AGENTS.md "Test globs" line,
           which also names files the suite regenerates, e.g. next-env.d.ts). Paths matching
           an exempt glob are listed but never a violation: by default the service's code wiki
           (wiki/**), where the dispatcher, the reviewer and the verifier write records during a
           story. Pass --exempt to use the service's own (its AGENTS.md "Footprint exempt" line).
restore    Puts the named paths back to the latest snapshot (worktree only, index untouched).
           The one sanctioned restore: never copy a file back from a copy taken earlier.
clean      Deletes refs/adlc/<story>/*. Run it at the story commit.

Exit code: 0 clean / done, 1 footprint violations, 2 bad input or git failure.
"""
import argparse
import fnmatch
import os
import subprocess
import sys
import tempfile
import time

DEFAULT_GLOBS = ["*.test.*", "*.spec.*", "*.itest.*", "tests/**", "e2e/**"]
DEFAULT_EXEMPT = ["wiki/**"]


def git(repo, *args, env=None, check=True):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, env=env)
    if check and r.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


def ref_prefix(story):
    if not story or any(c in story for c in " ~^:?*[\\") or story.startswith("-"):
        sys.exit(f"bad story id: {story!r}")
    return f"refs/adlc/{story}/build-"


def snapshots(repo, story):
    """Existing snapshot refs for the story, oldest first."""
    prefix = ref_prefix(story)
    out = git(repo, "for-each-ref", "--format=%(refname)", f"refs/adlc/{story}/")
    refs = [r for r in out.split() if r.startswith(prefix) and r[len(prefix):].isdigit()]
    return sorted(refs, key=lambda r: int(r[len(prefix):]))


def worktree_tree(repo):
    """Tree id of the working tree, built in a throwaway index."""
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, GIT_INDEX_FILE=os.path.join(tmp, "index"))
        git(repo, "add", "-A", ".", env=env)
        return git(repo, "write-tree", env=env).strip()


def cmd_snapshot(a):
    taken = time.time()
    tree = worktree_tree(a.repo)
    parent = git(a.repo, "rev-parse", "--verify", "-q", "HEAD", check=False).strip()
    n = len(snapshots(a.repo, a.story)) + 1
    ref = f"{ref_prefix(a.story)}{n}"
    msg = f"adlc build snapshot {a.story} round {n}\n\nadlc-snapshot-time: {taken:.6f}"
    commit = git(a.repo, "commit-tree", tree, *(["-p", parent] if parent else []), "-m", msg).strip()
    git(a.repo, "update-ref", ref, commit)
    print(f"{ref} {commit[:12]}")
    return 0


def latest(repo, story):
    refs = snapshots(repo, story)
    if not refs:
        sys.exit(f"no snapshot for {story}: run `snapshot` after the builder round first")
    return refs[-1]


def snapshot_time(repo, ref):
    """The exact time the snapshot was taken (the commit date has only one-second resolution)."""
    for line in git(repo, "log", "-1", "--format=%B", ref).splitlines():
        if line.startswith("adlc-snapshot-time: "):
            return float(line.split(": ", 1)[1])
    return float(git(repo, "log", "-1", "--format=%ct", ref).strip())


def matches(path, globs):
    parts = path.split("/")
    for g in globs:
        if g.endswith("/**"):
            seg = g[:-3].strip("/").split("/")
            if any(parts[i:i + len(seg)] == seg for i in range(len(parts) - len(seg))):
                return True
        elif "/" in g:
            if fnmatch.fnmatch(path, g):
                return True
        elif fnmatch.fnmatch(parts[-1], g):
            return True
    return False


def cmd_footprint(a):
    ref = latest(a.repo, a.story)
    since = snapshot_time(a.repo, ref)
    tree = worktree_tree(a.repo)
    diff = git(a.repo, "diff-tree", "-r", "--name-status", "--no-renames", f"{ref}^{{tree}}", tree)
    changed = {}
    for line in diff.splitlines():
        status, path = line.split("\t", 1)
        changed[path] = status
    # Edits made and reverted leave the content equal but the mtime newer than the snapshot.
    listed = git(a.repo, "ls-files", "-co", "--exclude-standard", "-z").split("\0")
    root = git(a.repo, "rev-parse", "--show-toplevel").strip()
    touched = []
    for path in filter(None, listed):
        if path in changed:
            continue
        try:
            if os.stat(os.path.join(root, path)).st_mtime > since:
                touched.append(path)
        except FileNotFoundError:
            pass
    globs = a.globs or DEFAULT_GLOBS
    exempt_globs = DEFAULT_EXEMPT if a.exempt is None else a.exempt
    exempt = sorted(p for p in set(changed) | set(touched) if matches(p, exempt_globs))
    bad_changed = sorted(p for p in changed if not matches(p, globs) and p not in exempt)
    bad_touched = sorted(p for p in touched if not matches(p, globs) and p not in exempt)
    print(f"footprint vs {ref}: {len(changed)} changed, {len(touched)} rewritten with content unchanged")
    if exempt:
        print(f"  exempt ({' '.join(exempt_globs)}): {len(exempt)} path(s), records written by other roles")
    for p in bad_changed:
        print(f"  VIOLATION {changed[p]} {p}")
    for p in bad_touched:
        print(f"  VIOLATION rewritten (edited then reverted?) {p}")
    if bad_changed or bad_touched:
        print(f"globs: {' '.join(globs)}. Stop the story for a ruling; restore only with `restore`.")
        return 1
    print("clean: every path the tester touched matches a test glob")
    return 0


def cmd_restore(a):
    if not a.paths:
        sys.exit("restore needs the paths to put back")
    ref = latest(a.repo, a.story)
    git(a.repo, "restore", f"--source={ref}", "--worktree", "--", *a.paths)
    print(f"restored {len(a.paths)} path(s) from {ref}")
    return 0


def cmd_clean(a):
    refs = snapshots(a.repo, a.story)
    for r in refs:
        git(a.repo, "update-ref", "-d", r)
    print(f"deleted {len(refs)} snapshot ref(s) for {a.story}")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("command", choices=["snapshot", "footprint", "restore", "clean"])
    p.add_argument("paths", nargs="*", help="restore: the paths to put back")
    p.add_argument("--repo", required=True, help="the service checkout")
    p.add_argument("--story", required=True, help="the story id, e.g. US-042")
    p.add_argument("--globs", nargs="+", help="test globs (default: %s)" % " ".join(DEFAULT_GLOBS))
    p.add_argument("--exempt", nargs="*", help="globs never counted as violations (default: %s; "
                   "pass --exempt with no globs to exempt nothing)" % " ".join(DEFAULT_EXEMPT))
    a = p.parse_args()
    if not os.path.isdir(a.repo):
        sys.exit(f"no such repo: {a.repo}")
    return {"snapshot": cmd_snapshot, "footprint": cmd_footprint,
            "restore": cmd_restore, "clean": cmd_clean}[a.command](a)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as e:
        if isinstance(e.code, str):
            print(e.code, file=sys.stderr)
            sys.exit(2)
        raise
