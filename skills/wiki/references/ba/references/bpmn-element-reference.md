# BPMN Element Reference — Definitions and Draw.io Mappings

## Purpose
Use during Step 2 (Extract Process Elements) and diagram generation in ba-process-modeler.
Each element includes its BPMN definition, when to use it, and the Draw.io shape to apply.

---

## Events

### Start Event
**Definition:** The trigger that initiates the process. Every process has exactly one start event
(or one per pool if multiple pools exist).
**Draw.io shape:** Circle, thin border (`strokeWidth=1`), green fill `#D5E8D4`
**Label:** What initiates the process — "Request received", "Timer: daily 09:00", "Message: invoice arrived"
**Types to distinguish:**
- Plain start: process begins on demand
- Timer start: process begins on a schedule (label with schedule)
- Message start: process begins when a message/event is received from outside

### End Event
**Definition:** The terminal state of the process. A process may have multiple end events for
different outcomes (approved, rejected, escalated, abandoned).
**Draw.io shape:** Circle, thick border (`strokeWidth=3`), red fill `#F8CECC`
**Label:** The outcome state — "Order fulfilled", "Claim rejected", "Escalated to manager"
**Rule:** Every process path must terminate at an end event. No hanging arrows.

### Intermediate Event (Catching)
**Definition:** Something that happens during the process that affects flow — a timer expiry,
a notification received, a condition met.
**Draw.io shape:** Circle, double border (`strokeWidth=1`, inner ring), white fill
**Label:** "Reminder sent", "Approval timeout (48h)", "Exception raised"

---

## Activities

### Task
**Definition:** A single, atomic unit of work performed by one actor or one system. If a step
requires two different actors, it is two tasks.
**Draw.io shape:** Rounded rectangle, `arcSize=20`
**Human task fill:** `#DAE8FC` (blue) — a person performs this step
**System task fill:** `#E1D5E7` (purple) — a system performs this step autonomously
**Label:** Verb + noun: "Submit request", "Validate data", "Send confirmation"
**Rule:** One actor per task. If two actors are involved, split the task.

### Sub-Process (Collapsed)
**Definition:** A named process that is documented separately. Referenced here but not expanded.
**Draw.io shape:** Rounded rectangle with a small `[+]` marker at bottom centre
**Fill:** `#F5F5F5` (light grey)
**Label:** Name of the sub-process: "Credit check process", "Onboarding workflow"
**When to use:** When a step involves more than 3–4 tasks that are already documented, or when
the detail would make the current diagram unreadable.

---

## Gateways

### Exclusive Gateway (XOR) — Decision
**Definition:** Exactly one outgoing path is taken based on a condition. This is the most common
gateway. Use for: if/else, approval/rejection, yes/no decisions.
**Draw.io shape:** Diamond, yellow fill `#FFF2CC`, border `#D6B656`
**Label:** The decision question — "Approved?", "Amount > £1000?", "Data valid?"
**Outgoing arrow labels:** Label every outgoing arrow — "Yes" / "No", "Approved" / "Rejected"
**Rule:** Never leave gateway outgoing arrows unlabelled.

### Parallel Gateway (AND) — Split/Join
**Definition:** All outgoing paths are taken simultaneously (split), or all incoming paths must
complete before the flow continues (join).
**Draw.io shape:** Diamond with `+` symbol inside, same yellow fill
**Label:** Not required on the gateway itself; label the lanes or tasks that run in parallel
**When to use:** "At the same time", "simultaneously", "in parallel"
**Rule:** A parallel split must always have a corresponding parallel join downstream.

### Inclusive Gateway (OR)
**Definition:** One or more outgoing paths may be taken. Less common; use only when truly
inclusive conditions exist (not just "pick one").
**Draw.io shape:** Diamond with `O` symbol inside, same yellow fill
**When to use:** "Any combination of", "one or more of the following"
**Rule:** Use sparingly. If in doubt, use XOR with explicit conditions.

---

## Connecting Objects

### Sequence Flow
**Definition:** The order of activities within a single pool (same organisation or system boundary).
**Draw.io:** Solid arrow, `endArrow=block`, `strokeColor=#000000`
**Rule:** Only connects elements within the same pool/lane boundary.

### Message Flow
**Definition:** Communication between two separate pools (different organisations or external systems).
**Draw.io:** Dashed arrow, `endArrow=open`, `dashed=1`, `strokeColor=#000000`
**When to use:** Customer submits to company system. External API returns a response.
**Rule:** Never use a message flow within a single pool.

### Association
**Definition:** Links an annotation or data object to a flow element. Not a flow path.
**Draw.io:** Dotted line, no arrowhead
**When to use:** Attaching a pain point annotation, a business rule note, or a data object reference.

---

## Swimlane Structure

### Pool
**Definition:** Represents a single participant — an organisation, a system boundary, or a
distinct autonomous entity. Pools do not share sequence flows.
**When to use:** When the process crosses an organisational or system boundary (e.g., customer
places an order, company processes it — two pools).

### Lane
**Definition:** A subdivision within a pool representing a role, department, or system.
Lanes within the same pool share the same sequence flow.
**Draw.io:** Horizontal band within the pool container
**Labelling:** Role title (not person name), system name for system lanes
**Maximum:** 6 lanes per diagram. Beyond 6, split into sub-processes.

---

## Annotation and Markers

### Text Annotation
**Definition:** A free-text note linked to a specific element.
**Draw.io:** Rectangle with open left edge (`shape=note`), linked with association line
**When to use:** Business rules, SLA targets, volume data, or anything that contextualises
a step without being part of the flow itself.

### Pain Point Hotspot (BA extension, not standard BPMN)
**Definition:** Marks a known pain point or inefficiency on an AS-IS model.
**Draw.io:** Rounded rectangle, orange fill `#FFE6CC`, border `#D79B00`
**Placement:** Above or beside the affected task, linked with association
**Label:** Brief pain point description: "Manual data re-entry", "Average 3-day delay", "Frequent errors here"

### Automation Candidate Marker (BA extension)
**Definition:** Marks a step on AS-IS that is a candidate for automation in TO-BE.
**Draw.io:** Small star or diamond annotation, amber fill
**Label:** "Automation candidate: [pattern]" e.g. "Automation candidate: rule-based routing"
