---
type: source
source_type: documentation
title: "GitHub Docs, About code owners and About push protection"
author: GitHub
date_published: 2026-11-08
url: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
confidence: high
key_claims:
  - "CODEOWNERS lives in .github/, the root or docs/ of the branch it governs; the last matching pattern wins."
  - "Code owners are requested automatically when a PR touches their files; one owner's approval satisfies the rule."
  - "Review is mandatory only when Require review from Code Owners is enabled in a branch protection rule or ruleset."
  - "CODEOWNERS over 3 MB is not loaded; owners need write access; draft PRs do not request owners."
  - "Push protection blocks a push containing a detected secret; anyone with write access can bypass with a reason unless delegated bypass is set; bypasses are logged."
  - "Push protection does not cover secrets already in the repository."
tags: [github, codeowners, secret-scanning, push-protection]
---

# GitHub Docs, code owners and push protection

Two GitHub documentation pages, both undated, so date_published is the fetch date. The second is https://docs.github.com/en/code-security/concepts/secret-security/about-push-protection. Confidence is high. Repository-level push protection needs a paid GitHub Secret Protection plan, so check availability per account.

Code owners: a gitignore-style file maps paths to users or teams. Patterns are evaluated in order and the last match wins, so a `*` line sets defaults. Each branch has its own file, and a PR uses the base branch's file. A missing or under-privileged owner is silently not assigned, and an invalid line is skipped. To protect the file itself, give it an owner.

Push protection: blocks partner, generic and custom patterns at push time (CLI, web UI, REST API). User-level protection is on by default for public repositories; repository-level is off by default. Bypass reasons ("used in tests", "false positive", "fix later") create alerts, the last one open. A secret that was already committed needs rotation, which these pages do not discuss.

See [[Shared Remote Collaboration for Agent Teams]].
