#!/usr/bin/env python3
"""Payload tests for guard_env.py: python3 skills/wiki/scripts/test_guard_env.py"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

HOOK = Path(__file__).with_name("guard_env.py")


def run(tool, **tool_input):
    payload = json.dumps({"tool_name": tool, "tool_input": tool_input})
    return subprocess.run([sys.executable, str(HOOK)], input=payload, text=True,
                          capture_output=True).returncode


def bash(command):
    return run("Bash", command=command)


HEREDOC_COMMIT = """git commit -m "$(cat <<'EOF'
feat: settings deny reads of .env.local and docker compose config
EOF
)\""""


class Blocks(unittest.TestCase):
    def test_reads(self):
        for cmd in ("cat .env", "cat web/.env.local", "sed -n p 'web/.env.local'",
                    "grep KEY .env.production", "bash -c 'cat .env'"):
            self.assertEqual(bash(cmd), 2, cmd)

    def test_tools(self):
        self.assertEqual(run("Read", file_path="/repo/web/.env.local"), 2)
        self.assertEqual(run("Edit", file_path="/repo/.env"), 2)

    def test_resolved_config(self):
        for cmd in ("docker compose config", "docker compose -f a.yml config",
                    "docker inspect api", "printenv", "ls; env"):
            self.assertEqual(bash(cmd), 2, cmd)

    def test_substitution_in_a_message_runs(self):
        for cmd in ('git commit -m "$(cat .env)"', 'gh pr create --body="`cat .env`"',
                    'gh issue create -t x -b "$(docker compose config)"'):
            self.assertEqual(bash(cmd), 2, cmd)

    def test_message_then_a_real_read(self):
        self.assertEqual(bash('git commit -m "about .env" && cat .env'), 2)
        self.assertEqual(bash('git commit -m ok; docker compose config'), 2)

    def test_heredoc_fed_to_a_shell(self):
        for cmd in ("bash <<'EOF'\ncat .env\nEOF", "cat <<'EOF' | sh\ncat .env\nEOF",
                    "tee >(sh) <<'EOF'\ncat .env\nEOF", "cat <<EOF\n$(cat .env)\nEOF"):
            self.assertEqual(bash(cmd), 2, cmd)

    def test_unbalanced_quotes_fail_closed(self):
        self.assertEqual(bash("git commit -m \"about .env"), 2)


class Passes(unittest.TestCase):
    def test_commit_messages(self):
        for cmd in ('git commit -m "settings deny reads of .env files"',
                    'git commit -am "never run docker compose config"',
                    "git commit --message='guard .env.local'",
                    'git tag -a v1 -m "drops .env.local reads"',
                    HEREDOC_COMMIT):
            self.assertEqual(bash(cmd), 0, cmd)

    def test_gh_text(self):
        self.assertEqual(bash('gh pr create --title "guard .env" --body "no docker inspect"'), 0)
        self.assertEqual(bash("gh issue create -t x --body-file - <<'EOF'\nreads .env.local\nEOF"), 0)

    def test_heredoc_to_a_file(self):
        self.assertEqual(bash("cat > notes.md <<'EOF'\nnever read .env.local\nEOF"), 0)

    def test_allowed(self):
        for cmd in ("cat .env.example", "git status", 'test -n "$API_KEY"'):
            self.assertEqual(bash(cmd), 0, cmd)
        self.assertEqual(run("Read", file_path="/repo/.env.example"), 0)


if __name__ == "__main__":
    unittest.main()
