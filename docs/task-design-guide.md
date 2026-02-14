# Overview

This document describes how to automatically construct evaluation tasks for browser-use agents based on the implementation of a website.

# Expected Output

You will generate a list of tasks, each paired with a corresponding programmatic verifier.

## Task Requirements

You must design tasks across three difficulty levels: **easy**, **medium**, and **hard**.

The difficulty level should be determined by:

1. **Task complexity** — approximately measured by the number of steps required to complete the task. This depends on both:
   - The workflow design of the website.
   - The inherent complexity of the task itself.

2. **Dependencies and prerequisites** — some tasks may appear simple on the surface but are challenging due to:
   - Implicit or unspoken prerequisites.
   - Data structure constraints.
   - Validation rules.
   - System-specific workflow designs that must be satisfied during execution.

Take these factors into account when defining and categorizing tasks.

When authoring hard tasks, consider evenly splitting between two categories:

- **Multi-step**: Require completing two distinct operations in sequence, often on different pages. Tests the agent's ability to chain actions and navigate between contexts.
- **Deep-constraint**: A single logical operation that is challenging due to deep navigation, multiple interacting form controls, cross-scope boundaries, or custom UI components (date pickers, comma-separated inputs). Tests precision and UI manipulation.

The number of tasks per difficulty level will be decided separately. Task design should prioritize coverage and variety of workflows.

## Agent Constraints

The browser-use agent being evaluated can **only interact with the website through the front-end UI**. Specifically, the agent can:

- Click elements
- Type text into inputs
- Scroll the page
- Read visible text and element attributes

The agent **cannot**:

- Execute JavaScript in the page context (e.g., `page.evaluate()`)
- Directly manipulate `localStorage`, `AppState`, or any internal state
- Make HTTP requests to API endpoints

## Authoring Guidelines

Each task must be **completable through the UI alone** by the current user. Before finalizing a task, verify the following:

**Permissions and seed data.** Trace the full permission chain: (1) what UI action does the task require? (2) what permission check does the application enforce? (3) does the current user have that role/permission in the seed data? If not, update the seed data to grant the necessary access. Missing permissions cause the UI to hide buttons or reject actions, making the task impossible regardless of agent capability.

**Task-data alignment.** Task instructions reference specific entities (users, groups, emails, etc.) by name. Ensure:
- The entity exists in seed data with the exact name used in the instruction.
- The entity is reachable — e.g., a user referenced in "add member" must not already be a member (direct or inherited) of the target, or the UI will filter them out.
- UI filtering won't exclude it — modals often filter out existing members, inherited members, or entities that don't meet certain criteria.

**UI-verifier alignment.** Every value a verifier expects must be achievable through the UI:
- If a verifier checks for a specific dropdown value, that value must exist as a dropdown option.
- Task instructions must use the exact label text visible in the UI, not paraphrased versions.
- If the UI and verifier use different names for the same concept, one or both must be fixed.

## Task Schema

Each task is defined as a JSON object:

```json
{
  "id": "task_001",
  "difficulty": "easy | medium | hard",
  "instruction": "Natural language instruction for the agent.",
  "verify": "path/to/verifier.py"
}
```

- **id**: Unique identifier.
- **difficulty**: One of `easy`, `medium`, `hard`.
- **instruction**: The task description given to the agent. Should be unambiguous but should not reveal internal implementation details.
- **verify**: Path to the Python verifier script/function.

# Guide for Programmatic Verifiers

## Privileged Access

You are able to write robust verifiers because you have privileged access to the website implementation. You can:

- Access the backend directly.
- Inspect the database, filesystem, or application state.
- Check internal website state.
- Add new APIs if necessary to simplify verification.

## Understanding the Data Store

The location and nature of the data store is **website-dependent**. Each website implementation determines where its authoritative data lives — it could be a SQL database, a filesystem, a key-value store, browser storage, or something else entirely.

Before writing verifiers, you must determine:

1. **Where does the data live?** (database, files, browser storage, server memory, etc.)
2. **How can a Python verifier access it?** (direct file reads, HTTP API, database queries, etc.)
3. **What bridge infrastructure is needed?** (API endpoints, state sync mechanisms, etc.)

For browser-based web apps in this benchmark, the data store is typically the browser's `localStorage`, which is not directly accessible from Python. A state synchronization mechanism bridges this gap (see below and `docs/environment-protocol.md`).

## Verification Architecture

### State Sync: Browser → Server

The application's `AppState` is the single source of truth. On every mutation, the browser:

1. Writes to `localStorage` (for page-reload persistence)
2. Pushes the full state to the server via `PUT /api/state` (for external access)

This means the server always holds a current copy of the application state.

### Server API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/state` | `GET` | Read the current application state as JSON |
| `/api/state` | `PUT` | Update the server-side state copy (called by browser) |
| `/api/reset` | `POST` | Reset app to seed data (clears browser + server state) |
| `/api/events` | `GET` | SSE stream for pushing commands to the browser |

### Running the Server

```bash
python3 server.py              # default port 8000
python3 server.py --port 9000  # custom port
```

The core logic, data flow, and navigation of system components are described in each environment's `ARCHITECTURE.md`. Make sure you fully understand the system architecture before designing verifiers. You are also encouraged to navigate the codebase whenever the description is not clear to you.

## Verifier Interface

All verifiers must implement the following Python function signature:

```python
def verify(server_url: str) -> tuple[bool, str]:
    """
    Verify that a task was completed successfully.

    Args:
        server_url: Base URL of the running server (e.g., 'http://localhost:8000')

    Returns:
        A tuple of (passed, message):
        - passed: True if the task was completed successfully, False otherwise.
        - message: Human-readable explanation of the result.
    """
```

### Example Verifier

```python
import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check that a group named 'Test Group' exists
    match = [g for g in state['groups'] if g['name'] == 'Test Group']
    if not match:
        return False, "Group 'Test Group' not found."

    group = match[0]
    if group['visibility'] != 'public':
        return False, f"Expected visibility 'public', got '{group['visibility']}'."

    return True, "Group 'Test Group' exists with correct visibility."
```

## Verifier Design Principles

1. **Check internal state, not UI**: Verifiers must validate that the operation genuinely completed by inspecting `AppState` via `GET /api/state`, not by checking what the browser displays.

2. **Prevent shortcuts**: The agent should not be able to pass verification without actually performing the task through the UI. Since the agent cannot call APIs or run JavaScript, and the verifier checks server-side state, this is enforced by design.

3. **Be specific**: Check not just that an entity exists, but that its properties are correct (name, visibility, parent, membership roles, etc.).

4. **Check side effects**: Many operations have cascading effects. For example:
   - Creating a group also creates an Owner membership for the current user.
   - Deleting a group removes its descendants, their projects, and all associated memberships/shares.
   - Transferring a group may reduce its visibility.

   Verifiers should check these side effects where relevant.

5. **Handle ID unpredictability**: New entities get auto-incremented IDs. Verifiers should search by name/path rather than hardcoding IDs.

### Verification Patterns

| Pattern | Description |
|---------|-------------|
| Entity existence (by name) | Search by name/path, not by ID (IDs are auto-incremented) |
| Entity absence | Confirm deletion or removal succeeded |
| Property match | Check specific field values after update |
| Side effect check | Verify implicit consequences (e.g., creating a group also creates an Owner membership) |
| Membership with constraints | Check role, membership type, and optional expiry date |
| Relationship check | Verify parent-child or share relationships between entities |
| Multi-condition | Multiple independent checks must all pass |
| State sync | Verify that the same data is consistent across multiple representations (e.g., `currentUser` and `users[]` array) |

### Verifier Conventions

These conventions prevent common bugs in verifier code:

**1. Dereference structured fields.** If the application stores enum-like values as objects (e.g., `role: {id: 50, name: "Owner", level: 50}`), the serialized JSON preserves the full structure. Verifiers must dereference to the primitive:

```python
# Correct — role is an object after JSON serialization
membership.get("role", {}).get("name") == "Developer"

# Wrong — object != string, always False
membership.get("role") == "Developer"
```

**2. Use canonical field names.** Verifiers must use the exact property names from the application's state model, not abbreviated names from form field IDs or UI labels. Cross-reference against the data schema.

**3. Account for persistence timing.** Verifiers read state from a server API. If the application has separate in-memory state and server-side persistence, every mutation handler must persist state before the verifier reads it. A missed persistence call means the verifier sees stale data.

## State Reset

State reset between tasks is handled by the **evaluation harness**, not by individual verifiers. The harness calls `POST /api/reset` before each task, which:

1. Broadcasts a reset signal to the browser via SSE
2. The browser calls `AppState.resetToSeedData()`, restoring all seed data
3. The browser pushes the seed state back to the server via `PUT /api/state`
4. Clears the server-side state copy

Verifiers should assume they run against a state that started from seed data and was modified only by the agent's actions.
