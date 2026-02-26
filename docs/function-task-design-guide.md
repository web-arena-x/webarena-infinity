# Overview
This document describes how to design evaluation tasks for a browser-based agent that tests the functional correctness of a web application.

# Expected Output
Produce a list of tasks. Each task must be paired with a corresponding programmatic verifier. The tasks will be stored under `tasks-function-test` under each app.

## Task Requirements
The primary goal is broad feature coverage. Collectively, the tasks should exercise a wide range of functionality and user flows in the application. Because you have privileged access to the implementation, intentionally design tasks that target specific features, edge cases, and important side effects.

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

# Task Schema
Each task must be defined as a JSON object:
```json
{
  "id": "task_e1",
  "difficulty": "easy | medium | hard",
  "instruction": "Natural language instruction for the agent.",
  "verify": "tasks/task_e1.py"
}
```
- **id**: Unique identifier.
- **difficulty**: One of `easy`, `medium`, `hard`.
- **instruction**: The task description given to the agent. Should be unambiguous but should not reveal internal implementation details.
- **verify**: Path to the Python verifier script/function.

# Writing Programmatic Verifiers
## Privileged Access
Verifiers can use full backend access. They may query the backend directly, inspect the database, filesystem, or application state, and add internal APIs if needed to simplify verification.

## Understanding the Data Store
Before writing verifiers, determine: (1) where the data lives (database, files, browser storage, server memory, etc.), (2) how the verifier can access it (API, file read, DB query, etc.), and (3) what bridging infrastructure exists. In this benchmark, application state is typically stored in localStorage and synchronized to the server. You can check `docs/environment-protocol.md` for more details.

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

# Verifier Design Principles
1. Validate internal state, not UI. Use GET /api/state.
2. Be specific. Check exact properties and relationships.
3. Validate side effects. Confirm cascading changes where applicable.
4. Avoid hardcoding IDs. Locate entities by stable attributes (e.g., name).

# State Reset
State reset is handled by the evaluation harness before each task via POST /api/reset. Assume the app starts from seed data and only the agent’s actions modified the state. Do not perform resets inside verifiers.