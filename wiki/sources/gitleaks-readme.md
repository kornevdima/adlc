---
type: source
source_type: documentation
title: "Gitleaks README"
author: Gitleaks maintainers
date_published: 2026-11-08
url: https://github.com/gitleaks/gitleaks
confidence: high
key_claims:
  - "Gitleaks runs as a pre-commit hook through the pre-commit framework: add the gitleaks repo and hook id to .pre-commit-config.yaml, then run pre-commit install."
  - "Use pre-commit autoupdate to refresh the pinned revision; SKIP=gitleaks before a commit command skips the check once."
  - "The git and dir commands scan history and files; detect and protect were deprecated in v8.19.0 but still work."
  - "Allowlists: a gitleaks:allow comment on a line, a .gitleaksignore file of finding fingerprints, and allowlists or rules.allowlists tables in .gitleaks.toml."
  - "A baseline is a prior report passed with --baseline-path so later scans show only new findings."
  - "The tool is feature complete; future releases are security patches only."
---

# Gitleaks README

Project README for a secret scanner. It is the primary source for the local layer of secret defense.

## Hook setup

(Source: this page.) With the pre-commit framework, a `.pre-commit-config.yaml` at the repository root names the gitleaks repo, a pinned `rev` and the `gitleaks` hook id (`gitleaks-docker` runs the official image instead). `pre-commit install` registers the hook in each clone, so every contributor installs it once. A native git hook is also offered via an example script in the repository.

## Commands

`gitleaks git` scans commit history, `gitleaks dir` scans files, `stdin` scans piped text. The older `detect` and `protect` names still work but are hidden. The README as fetched did not describe a `--staged` flag.

## Allowlists and baselines

Known test secrets are marked inline with `gitleaks:allow`. Reviewed false positives are listed by fingerprint in `.gitleaksignore` (marked experimental) or configured by path, regex, commit or stopword in `.gitleaks.toml`. An existing report is the baseline that lets a legacy repository starts clean and only new findings fail.

## Limit

A hook runs on the author's machine and can be skipped, so it complements remote push protection; see [[github-code-owners-and-push-protection]].

Related: [[Shared Remote Collaboration for Agent Teams]].
