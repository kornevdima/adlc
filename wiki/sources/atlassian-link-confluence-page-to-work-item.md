---
type: source
title: "Atlassian: link a Confluence page to a work item"
source_type: documentation
author: Atlassian
date_published: undated
url: https://support.atlassian.com/jira-software-cloud/docs/link-a-confluence-page-to-an-epic/
confidence: medium
key_claims:
  - A Confluence page can be linked to a parent-level work item such as an epic, or to a standard work item, when the Jira site is linked to Confluence.
  - A page can be created from the work item and is linked automatically.
  - The link shows on both sides: in the page's details and in the work item.
  - A work item holds up to 2000 links, Confluence pages included.
---

# Atlassian: link a Confluence page to a work item

Atlassian support documentation. It was read through search-result excerpts of the help article and its sibling articles ("Use Jira and Confluence together", "Automate linking of Confluence pages to Jira Cloud work items"), not by fetching the full page, so confidence is medium. No date is shown.

## Claims

- Open the work item, choose to add related work, then Page, then Link page. Search for the page or paste its URL. This works on an epic and on a standard work item.
- The same menu creates a new page, which is linked to the work item automatically.
- Once linked, the work item appears in the page's details, and Confluence shows a Jira links button. The link is visible from both sides.
- A work item takes up to 2000 links, counting pages.
- Automation rules cannot link pages directly; a "send web request" action calling the Jira REST API can.
- The Confluence product requirements template has a placeholder that creates an epic in Jira.

## What it does not state

No page in this set states a rule for which content belongs in a page and which in a work item.

## Relevance

Confirms two-way linking between knowledge pages and tracker items (Source: [[atlassian-link-confluence-page-to-work-item]]). Used in [[Knowledge Layer and Work Tracker Split]].
