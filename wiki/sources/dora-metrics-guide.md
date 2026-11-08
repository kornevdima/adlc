---
type: source
title: "DORA Metrics Guide (dora.dev)"
source_type: documentation
author: "Nathen Harvey, DORA (Google Cloud)"
date_published: 2026-01-05
url: "https://dora.dev/guides/dora-metrics/"
confidence: high
status: reviewed
created: 2026-11-08
updated: 2026-11-08
tags: [source, dora, metrics, lead-time]
key_claims:
  - "Throughput has three parts: change lead time, deployment frequency, failed deployment recovery time."
  - "Instability has two parts: change fail rate and deployment rework rate."
  - "Change lead time runs from commit in version control to deployed in production."
  - "Failed deployment recovery time replaced MTTR."
  - "The page gives no tier thresholds and says the data sits in several places."
---

# DORA Metrics Guide (dora.dev)

The DORA research program's own page defines five measures. The date is the page's "last updated" stamp; the original date is not stated. (confidence: high for definitions)

| Measure | Definition |
|---|---|
| Change lead time | Commit to version control until the change is deployed in production |
| Deployment frequency | Deployments per period, or time between them |
| Failed deployment recovery time | Time to recover from a deployment that fails and needs immediate intervention (replaced MTTR) |
| Change fail rate | Share of deployments needing immediate intervention, often rollback or hotfix |
| Deployment rework rate | Share of deployments that are unplanned and caused by a production incident |

The page does not use "reliability" for any of these. The 2025 State of AI-assisted Software Development report (Google Cloud, 2025) is the latest report; search summaries say it adds reliability as a further outcome, but this run did not read the report text (confidence: low on the reliability definition).

Tier thresholds are not on this page. Secondary summaries of the 2024 report (Octopus, Port; medium confidence) give elite as on-demand deployment, change lead time under one day and recovery under one hour; high as daily to weekly deploys; medium as weekly to monthly; low as less often than monthly. These secondary sources disagree on low-tier recovery and failure-rate cutoffs, so check the report before using them as a benchmark.

The 2024 clusters were 19% elite, 22% high, 35% medium, 25% low (secondary source, medium confidence). The 2024 report also found medium and high clusters with inverted change fail rates.

Used in [[Delivery Metrics and Their Data Sources]].
