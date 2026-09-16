# Story Splitting Patterns

## Purpose
Use during Step 2 (Apply Story Splitting) of ba-user-story-factory.
Apply a minimum of 2 patterns per epic. Start with Workflow Step split as the default first pass.

---

## Pattern 1 — Workflow Step Split

**When to apply:** The epic or feature covers a multi-step user journey. Each step has
independent value and can be demoed separately.

**How to split:** Identify each discrete step in the workflow. One story per step.

**Example:**
- Epic: "Submit and track an expense claim"
- Splits into:
  - Story: Submit a new expense claim with required fields
  - Story: Upload receipts and attach them to a submitted claim
  - Story: View the status of a submitted claim
  - Story: Receive notification when a claim is approved or rejected

**Rule:** Only split on steps that have standalone testable value. "Save draft" is a step;
"click a button" is not.

---

## Pattern 2 — User Role Split

**When to apply:** Different types of users interact with the same feature but need different
capabilities, permissions, or interfaces.

**How to split:** One story per distinct user role that interacts with the feature differently.

**Example:**
- Epic: "Manage user accounts"
- Splits into:
  - Story: As a system administrator, I want to create and deactivate user accounts
  - Story: As a line manager, I want to view the accounts of my direct reports
  - Story: As a user, I want to update my own profile information

**Rule:** Do not create role splits if the roles have identical interactions — combine them.

---

## Pattern 3 — Business Rule Variation Split

**When to apply:** The same action produces different outcomes depending on a business rule,
condition, or threshold. Each rule is complex enough to warrant its own acceptance criteria.

**How to split:** One story for each significant business rule variant.

**Example:**
- Epic: "Process loan applications"
- Splits into:
  - Story: Automatically approve loan applications where credit score ≥ 750 and amount ≤ £10,000
  - Story: Route loan applications to manual review where credit score is 600–749
  - Story: Automatically reject loan applications where credit score < 600

**Rule:** Do not split on trivial variations (different field labels). Split when the rule
changes the workflow, permissions, or integration behaviour.

---

## Pattern 4 — Happy Path / Exception Path Split

**When to apply:** The happy path is well-understood but exception handling is complex,
risky, or separately valuable.

**How to split:** One story for the happy path; one or more stories for exception conditions.

**Example:**
- Epic: "Process payment"
- Splits into:
  - Story: Process a successful payment via credit card (happy path)
  - Story: Handle a declined payment with a clear user message and retry option
  - Story: Handle a payment gateway timeout with a safe retry mechanism

**Rule:** Happy path story goes first — it is always Must Have. Exception stories are
Should Have unless the exception is a regulatory or safety concern.

---

## Pattern 5 — Data Variation Split

**When to apply:** The feature operates on different data types, sources, or formats that
each require meaningfully different handling.

**How to split:** One story per data type or source that has distinct processing logic.

**Example:**
- Epic: "Import customer data"
- Splits into:
  - Story: Import customer records from a CSV file with field mapping
  - Story: Import customer records via API integration with the CRM system
  - Story: Handle duplicate detection and merge during import

**Rule:** Only split on data variations that change the processing logic. Visual format
differences (different column order) do not warrant a split.

---

## Pattern 6 — Interface / Channel Split

**When to apply:** The same capability needs to be available on multiple interfaces or channels,
and each interface has meaningfully different UX requirements.

**How to split:** One story per channel if the implementation differs significantly.

**Example:**
- Epic: "Submit a support request"
- Splits into:
  - Story: Submit a support request via the web portal
  - Story: Submit a support request via the mobile application
  - Story: Submit a support request via email (parsed and auto-created)

**Rule:** Only split channels if they have genuinely different UX or integration requirements.
If responsive web covers both web and mobile, do not split.

---

## Pattern 7 — CRUD Operation Split

**When to apply:** A feature covers full Create/Read/Update/Delete operations and they
have different complexity, permissions, or frequency of use.

**How to split:** One story per operation. Prioritise Read and Create first (users need to see
and create before they can update or delete).

**Example:**
- Epic: "Manage product catalogue"
- Splits into:
  - Story: View the product catalogue with search and filter
  - Story: Add a new product to the catalogue
  - Story: Edit an existing product's details
  - Story: Archive a product (soft delete)

**Rule:** Do not split CRUD mechanically if the operations are trivially simple. Combine
if they share a single screen and have no access control differences.

---

## Pattern 8 — Performance / Quality Attribute Split

**When to apply:** The basic function is one story, but performance, security, or accessibility
requirements add complexity that should be tracked and tested separately.

**How to split:** Basic functional story first; NFR story as a separate item.

**Example:**
- Epic: "Search product catalogue"
- Splits into:
  - Story: Search the product catalogue by keyword and return results (functional)
  - Story: Search returns results in ≤ 500ms for up to 10,000 product records (performance NFR)
  - Story: Search results are accessible to screen reader users (accessibility NFR)

**Rule:** NFR stories always reference the functional story they apply to.
Tag them as Story Type = NFR in the backlog register.

---

## Pattern 9 — Spike (Investigation) Split

**When to apply:** A story cannot be estimated because the team lacks the knowledge to scope it.
A time-boxed investigation is needed first.

**How to split:** Create a Spike story to answer a specific question; defer the implementation
story until the Spike is Done.

**Spike format:**
`As a Development Team, I want to investigate [specific question] so that we can make an
informed decision about [implementation approach or feasibility].`
Acceptance criteria: "A documented recommendation is available, covering [specific decisions
the team needs to make]."
Time-box: state the maximum time to spend (e.g. "Time-box: 2 days").

**Example:**
- Spike: Investigate whether the legacy billing API supports the required transaction
  data format, or whether a transformation layer is needed. Time-box: 1 day.
  Outcome: recommendation document with integration approach.

**Rule:** Spikes produce knowledge, not software. They should never be larger than 2 days.
If the investigation would take longer than 2 days, split the investigation itself.
