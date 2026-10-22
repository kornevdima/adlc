# vault-a/UP-024 The env guard blocks commands that only mention an env file or the resolved-config command in text

- **Kind:** bug
- **Target:** `skills/wiki/scripts/guard_env.py`: the env-file token pattern and the resolved-config patterns run over the whole Bash command string; its test payloads.
- **Plugin version:** 1.0.9
- **Seen:** 2× in one session (2026-10-22).

## What happened

The PreToolUse hook matches its patterns anywhere in the Bash command text, quoted arguments included. In one session two commits were refused:

1. a `git commit -m "…"` whose message said the settings now deny reads of env files, using an env file name as a word in the sentence;
2. the retry, whose message instead named the command that prints a compose project's resolved config.

Nothing was read and no config was printed; the text was prose inside the commit message. The same happens for an issue body, a PR title or an `echo`. The operator saw two blocked tool calls for a routine commit.

## Proposed fix

- Split the command with `shlex` and apply the env-file name check and the resolved-config patterns only to command words and file arguments. Skip the values of message-like options (`-m`, `--message`, `--body`, `--title`) and quoted heredoc bodies.
- When the split fails (unbalanced quotes), keep today's whole-string match, so the hook still fails closed.
- Add test payloads: a commit message that names an env file passes; reading an env file with `cat`, `sed` or the Read tool still blocks; the resolved-config command run for real still blocks.

## Workaround

Write the message to a file and commit with `git commit -F <file>`.
