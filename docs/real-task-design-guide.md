# Real Task Design Guide

This document describes how to design **realistic evaluation tasks** for browser-use agents. Unlike function tests (which target feature coverage), real tasks measure whether an agent can accomplish the kinds of things actual users ask for — expressed in natural, sometimes terse language.

## Expected Output

A set of tasks, each paired with a programmatic verifier. Tasks are stored in `real-tasks.json` and verifiers in `real-tasks/` under each app directory.

## Task Design

### Core Principle: Realism

The defining requirement is that every task should reflect a **genuine user need**. Think about what a real person would ask a colleague or assistant to do in this application — then write that as the instruction. This means:

- **Natural phrasing.** Real users don't describe UI steps ("click the settings gear, then select the dropdown…"). They state intent: "Turn off email notifications" or "Add Sarah to the project."
- **Appropriate brevity.** Users are often terse. A task like "archive the Q3 reports" is more realistic than "navigate to the reports section and archive all reports from Q3." Don't over-explain.
- **Varied instruction styles.** Some tasks describe a workflow ("Move all unread emails to the archive"), others describe a desired end state ("The project should be set to private"), others reference context ("Update the timezone to match the London office"). Mix these styles across the task set.
- **Unambiguous despite being brief.** Realism doesn't mean vagueness. The task must have a single correct interpretation. If a terse phrasing could be read two ways, add just enough context to disambiguate — but no more.
- **No implementation leaks.** Never reference internal state keys, API endpoints, localStorage, or code structure. The instruction should read as if the user has only ever seen the UI.

### Difficulty Levels

Design tasks across three difficulty levels: **easy**, **medium**, and **hard**. Difficulty is determined by two factors:

#### 1. Step count and complexity
The number of discrete UI interactions required, which depends on both the website's workflow design and the inherent complexity of the task.
- **Easy** — A single, focused action. One or two steps: toggle a setting, rename an item, delete something. A human completes it in seconds.
- **Medium** — A short workflow requiring several coordinated steps: fill out a multi-field form, navigate to a non-obvious page and make a change, or perform an action that requires reading existing data first.
- **Hard** — A multi-part task that chains several operations together, or requires the agent to synthesize information from different parts of the app. A human would need several minutes.

#### 2. Implicit prerequisites
Some tasks appear simple on the surface but are challenging because they require the agent to:
- Discover information by navigating the app (e.g., finding which team a user belongs to before reassigning them).
- Understand relationships between entities (e.g., a project's visibility depends on its parent group).
- Locate features that aren't immediately visible (e.g., settings buried in a sub-menu, or actions available only through a context menu).

A task can be "hard" even with few steps if the prerequisites are non-obvious.

### What Makes a Good Task

| Quality | Example | Anti-example |
|---------|---------|--------------|
| Realistic intent | "Mute the #announcements channel" | "Change the muted field to true for channel ID 7" |
| Appropriate brevity | "Add a label called 'urgent' with a red color" | "Navigate to settings, find labels, click new label, type urgent, select red, save" |
| Unambiguous | "Archive the email from David about invoices" | "Archive that email" (which one?) |
| Exercises real workflow | "Forward the budget report to Lisa" | "Forward the budget email titled 'Q1 budget estimation' to Lisa Chen" |

## Agent Constraints

The browser-use agent can **only interact through the front-end UI**:
- Click elements
- Type text into inputs
- Scroll the page
- Read visible text and element attributes

The agent **cannot**:
- Execute JavaScript (`page.evaluate()`)
- Directly manipulate `localStorage`, `AppState`, or internal state
- Make HTTP requests to API endpoints

Design tasks with these constraints in mind. Every required action must be achievable through visible, interactive UI elements.

## Task Schema

Each task is a JSON object in `tasks.json`:

```json
{
  "id": "task_e1",
  "difficulty": "easy",
  "instruction": "Turn off desktop notifications.",
  "verify": "tasks/task_e1.py"
}
```

| Field | Description |
|-------|-------------|
| `id` | Unique identifier. Convention: `task_e*` (easy), `task_m*` (medium), `task_h*` (hard). |
| `difficulty` | One of `easy`, `medium`, `hard`. |
| `instruction` | Natural-language task given to the agent. Unambiguous, no implementation details. |
| `verify` | Path to the verifier script. |

## Verifier Design

### Privileged Access
Verifiers have full backend access — they can query application state, inspect the database/filesystem, and add internal APIs if needed. This privilege is what makes robust verification possible.

### Verifier Interface
All verifiers implement this signature:

```python
def verify(server_url: str) -> tuple[bool, str]:
    """
    Args:
        server_url: Base URL of the running server (e.g., 'http://localhost:8000')

    Returns:
        (passed, message) — passed is True if the task was completed correctly,
        message is a human-readable explanation.
    """
```

### Verification Architecture
The application's `AppState` is the single source of truth. On every mutation, the browser pushes the full state to the server via `PUT /api/state`. Verifiers read this state via `GET /api/state`.

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/state` | `GET` | Read current application state as JSON |
| `/api/state` | `PUT` | Browser pushes state on every mutation |
| `/api/reset` | `POST` | Reset to seed state (called by eval harness, not verifiers) |
| `/api/events` | `GET` | SSE stream for reset notifications |

### Example
```python
import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    match = [g for g in state['groups'] if g['name'] == 'Test Group']
    if not match:
        return False, "Group 'Test Group' not found."

    group = match[0]
    if group['visibility'] != 'public':
        return False, f"Expected visibility 'public', got '{group['visibility']}'."

    return True, "Group 'Test Group' exists with correct visibility."
```

### Handling Ambiguous Outcomes with LLM Judges
Some realistic tasks produce outcomes that can't be verified with exact string matching — for example, composing an email body, writing a description, or renaming something where multiple phrasings are acceptable. In these cases, use an LLM judge to evaluate the content:
- **Use LLM judging only at the atomic level.** Judge individual field values (e.g., "does this email body convey a meeting cancellation?"), not entire state trees.
- **Prefer deterministic checks wherever possible.** If a field has a finite set of valid values, use exact matching. Reserve LLM judging for genuinely open-ended content.
- **Combine both approaches.** Verify structural properties deterministically (correct recipient, correct label applied, item exists), then use an LLM judge only for the free-text fields.

### Design Principles
1. **Validate state, not UI.** Always read from `GET /api/state`. Never parse HTML or check visual properties.
2. **Be specific.** Check exact properties and relationships — not just that an entity exists, but that its fields have the correct values.
3. **Validate side effects.** If an action has cascading consequences (e.g., deleting a group removes its members), verify those too.
4. **Locate entities by stable attributes.** Use names or other natural keys, not hardcoded IDs that break when seed data changes.
5. **Don't reset state.** The eval harness calls `POST /api/reset` before each task. Verifiers should assume the app started from seed data and only the agent's actions modified it.
