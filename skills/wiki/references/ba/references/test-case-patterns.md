# Test Case Patterns — Scenario Types, Boundary Analysis, and Negative Test Design

## Purpose
Use during Steps 2–6 of ba-test-case-generator.
Section 1: scenario type guide. Section 2: boundary value analysis. Section 3: negative test patterns.

---

## Section 1 — Scenario Type Guide

### Happy Path (HP)
**Definition:** The ideal flow where the actor provides valid input and the system responds
as intended. This is the acceptance criterion scenario as written.

**Minimum required:** One HP per acceptance criterion.

**Writing standard:**
- Pre-condition: system is in the expected ready state; actor has required permissions
- Action: the actor performs exactly what the acceptance criterion describes
- Expected result: the outcome stated in the "Then" clause of the Gherkin scenario

**Pitfall to avoid:** Do not write a happy path that assumes too much. Specify the exact input
data used in Test Data; do not rely on "valid data" as a reference.

---

### Negative Path (NP)
**Definition:** A scenario where the actor provides invalid, malformed, or out-of-bounds input,
or attempts an action they are not permitted to take. The system must handle it gracefully.

**Minimum required:** One NP per acceptance criterion.

**Standard negative scenarios to generate (pick the most relevant):**
- Empty required field submitted
- Field exceeds maximum length
- Invalid data format (text in a number field, wrong date format)
- Duplicate submission (same record submitted twice)
- Actor without required permissions attempts the action
- Action attempted when the record is in the wrong state (e.g. editing a closed record)

**Expected result standard for NP tests:**
Always state: (a) the error message or validation shown, (b) that no data is persisted,
and (c) that the actor can correct and retry.
Do not accept "an error appears" as an expected result — name the error.

---

### Boundary Condition (BC)
**Definition:** Tests values at, just below, and just above the threshold defined in a
business rule or NFR. Boundary values are where most bugs occur.

**Required:** For every criterion that contains a numeric, date, or character count threshold.

**See Section 2 for full boundary value analysis rules.**

---

### Exception Condition (EC)
**Definition:** System-level failures that occur outside the actor's control: service unavailability,
timeout, database error, network interruption, concurrent modification.

**Minimum required:** One EC per integration point and one for any step with a time-sensitive dependency.

**Standard exception conditions to test:**
- Downstream service unavailable (API returns 500 or times out)
- Session expires mid-workflow
- Concurrent modification (two users edit the same record simultaneously)
- File upload fails mid-transfer
- Payment gateway timeout

**Expected result standard:** The system must: display a user-understandable message (not a
stack trace), preserve data state (not lose the in-progress work), and provide a recovery path.

---

### NFR Test (NFR)
**Definition:** Tests that the system meets quality attributes — performance, security,
accessibility, reliability — not functional correctness.

**Required:** One NFR test per measurable NFR in the requirements register.

**See Section 3 for NFR-specific test design patterns.**

---

### Integration Test (INT)
**Definition:** Tests that data flows correctly between this system and connected systems.
Verifies triggers, data mappings, error handling, and idempotency.

**Required:** One INT test per integration point in scope.

**Standard integration test scenarios:**
- Happy path: trigger event in System A → verify correct data received in System B
- Invalid data: System A sends malformed data → System B rejects gracefully and logs the error
- Latency: System B is slow to respond → System A handles timeout correctly
- Retry: first call fails → System A retries and succeeds on second attempt
- Duplicate: same event triggers twice → System B handles idempotently (no duplicate created)

---

### Regression Test (REG)
**Definition:** Verifies that existing functionality still works after a change has been made.
These are the tests most likely to catch unintended side effects.

**Required:** Identify the top 3–5 existing features most likely to be affected by the
stories in scope. Generate one REG test per affected feature.

**Approach:** Take the existing HP test case for the affected feature; mark it as REG.
It does not need to be rewritten — it just needs to be executed in every Sprint Review
where the affected code area was changed.

---

## Section 2 — Boundary Value Analysis Rules

### Single Threshold (e.g. "must be at least 8 characters")

| Test Case | Value to Use | Expected Outcome |
|-----------|-------------|-----------------|
| BC-BELOW | 7 characters | Validation fails; error message shown |
| BC-AT | 8 characters | Validation passes |
| BC-ABOVE | 9 characters | Validation passes |

### Range Threshold (e.g. "must be between 1 and 100")

| Test Case | Value to Use | Expected Outcome |
|-----------|-------------|-----------------|
| BC-BELOW-MIN | 0 | Validation fails |
| BC-AT-MIN | 1 | Validation passes |
| BC-INSIDE | 50 (or any mid-range) | Validation passes |
| BC-AT-MAX | 100 | Validation passes |
| BC-ABOVE-MAX | 101 | Validation fails |

### Date Boundary (e.g. "date must not be in the past")

| Test Case | Value to Use | Expected Outcome |
|-----------|-------------|-----------------|
| BC-BEFORE | Yesterday's date | Validation fails |
| BC-AT | Today's date | Validation passes (if today is allowed) |
| BC-AFTER | Tomorrow's date | Validation passes |

### Character Length (text fields)

| Test Case | Value to Use | Expected Outcome |
|-----------|-------------|-----------------|
| BC-BELOW-MIN | Minimum length - 1 characters | Validation fails |
| BC-AT-MIN | Minimum length characters | Passes |
| BC-AT-MAX | Maximum length characters | Passes |
| BC-ABOVE-MAX | Maximum length + 1 characters | Validation fails; truncation or error |

---

## Section 3 — NFR Test Design Patterns

### Performance Test Design

From the NFR: "System shall respond in ≤ 2 seconds for 95% of requests under 500 concurrent users"

| Test Case | Setup | Measure |
|-----------|-------|---------|
| NFR-PERF-baseline | Single user, standard request | Response time |
| NFR-PERF-target-load | 500 concurrent users, standard requests | p95 response time ≤ 2s |
| NFR-PERF-spike | 750 concurrent users (50% above target) | System degrades gracefully; no error |
| NFR-PERF-sustained | 500 users for 30 minutes | No degradation over time; memory stable |

**Pass criteria standard:** State the threshold from the NFR. "p95 ≤ 2 seconds" is a pass criterion.
"Response is fast" is not.

---

### Security Test Design

Standard security test scenarios (adapt to the system under test):

| Test Case | Scenario | Expected Result |
|-----------|---------|-----------------|
| NFR-SEC-auth | Attempt to access a protected resource without authentication | Redirect to login; 401 response |
| NFR-SEC-authz | Attempt to access a resource that the authenticated user is not permitted to see | 403 Forbidden; no data exposed |
| NFR-SEC-inject | Submit SQL injection string in a text input field | Input is sanitised; no database error returned; no query executed |
| NFR-SEC-xss | Submit a script tag in a text input field | Script is not rendered; input is escaped |
| NFR-SEC-csrf | Submit a form request without a valid CSRF token | Request rejected |
| NFR-SEC-encrypt | Verify that data at rest is encrypted | DBA confirms AES-256 encryption; no plain text PII in database |

---

### Accessibility Test Design

Standard accessibility test scenarios based on WCAG 2.1 AA:

| Test Case | Scenario | Expected Result |
|-----------|---------|-----------------|
| NFR-ACC-keyboard | Navigate all interactive elements using keyboard only | All elements reachable; logical tab order; no keyboard trap |
| NFR-ACC-screenreader | Navigate page using a screen reader (NVDA or VoiceOver) | All content readable; images have alt text; form labels are announced |
| NFR-ACC-contrast | Check colour contrast ratio for body text | Minimum 4.5:1 contrast ratio (WCAG AA) |
| NFR-ACC-error | Submit a form with an error | Error is associated with the specific field; announced by screen reader |
| NFR-ACC-resize | Zoom browser to 200% | No content is clipped or overlapping; horizontal scroll not required |

---

## Section 4 — Test Priority Assignment

Assign test priority based on the combination of story MoSCoW and scenario type:

| Story MoSCoW | HP | NP | BC | EC | NFR |
|-------------|----|----|----|----|-----|
| Must Have | Critical | Critical | High | High | High |
| Should Have | High | High | Medium | Medium | Medium |
| Could Have | Medium | Medium | Low | Low | Low |
| Won't Have | — | — | — | — | — |

**Smoke test set:** All Critical and High HP tests from Must Have stories.
Run this set after every deployment to confirm basic functionality before full regression.
