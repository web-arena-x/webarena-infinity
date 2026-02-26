# Function Task Design Guide

This document describes how to design **function-test tasks** for browser-use agents. Unlike real tasks (which prioritize natural language and realism), function tests target **broad feature coverage** — systematically exercising the application's functionality, edge cases, and side effects.

## Expected Output

A set of tasks, each paired with a programmatic verifier. Tasks are stored in `function-tasks.json` and verifiers in `function-tasks/` under each app directory.

## Task Design

### Core Principle: Feature Coverage

The goal is to collectively exercise as much of the application's functionality as possible. Because you have privileged access to the implementation, intentionally design tasks that target:
- **Core features.** Every major user flow should be covered by at least one task.
- **Edge cases.** Boundary conditions, empty states, maximum-length inputs, special characters.
- **Side effects.** Actions that trigger cascading changes (e.g., deleting a parent entity removes its children).
- **Validation logic.** Required fields, format constraints, conditional requirements.

Instructions can be more explicit than real tasks since the goal is testing the app, not measuring natural-language understanding. Be precise enough to exercise the exact feature you're targeting.

### Coverage Dimensions

To ensure well-rounded coverage, design tasks across these four dimensions. A good task set has representation in each:

| Dimension | What it tests | Example |
|-----------|--------------|---------|
| **Direct** | A single feature works in isolation. | "Create a new label called 'urgent' with red color." |
| **Navigation-dependent** | The feature exists but must be discovered through the app's information architecture. | "Change the notification preferences for the #backend channel." (requires navigating to the right channel's settings) |
| **Cross-referencing** | Data from one part of the app is needed to act correctly in another. | "Add all members of the Design team to the Alpha project." (must read team membership, then modify the project) |
| **Side-effect** | An action triggers cascading state changes beyond the immediate target. | "Delete the 'Infrastructure' group." (verifier checks that child projects, memberships, and shares are also removed) |

Use these dimensions to audit coverage gaps. If a task set has many direct tasks but no cross-referencing tasks, the app's relational integrity is untested.

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

Every feature you want to test must be reachable through the UI. If a feature has no UI surface, it cannot be tested by these tasks.

## Task Schema

Each task is a JSON object in `function-tasks.json`:

```json
{
  "id": "task_1",
  "instruction": "Create a new group named 'Test Group' with public visibility.",
  "verify": "function-tasks/task_1.py"
}
```

| Field | Description |
|-------|-------------|
| `id` | Unique identifier (e.g., `task_1`, `task_2`, …). |
| `instruction` | Unambiguous task description. Should not reveal internal implementation details. |
| `verify` | Path to the verifier script. |

## Verifier Design

### Privileged Access
Verifiers have full backend access — they can query application state, inspect the database/filesystem, and add internal APIs if needed.

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
The application's `AppState` is the single source of truth. On every mutation, the browser pushes the full state to the server via `PUT /api/state`. Verifiers read this state via `GET /api/state`. See `docs/environment-protocol.md` for full details.

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

### Design Principles
1. **Validate state, not UI.** Always read from `GET /api/state`. Never parse HTML or check visual properties.
2. **Be specific.** Check exact properties and relationships — not just that an entity exists, but that its fields have the correct values.
3. **Validate side effects.** If an action has cascading consequences (e.g., deleting a group removes its members), verify those too.
4. **Locate entities by stable attributes.** Use names or other natural keys, not hardcoded IDs that break when seed data changes.
5. **Don't reset state.** The eval harness calls `POST /api/reset` before each task. Verifiers should assume the app started from seed data and only the agent's actions modified it.
