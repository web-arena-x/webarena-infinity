# Overview

This document describes how to construct evaluation tasks for browser-use agents based on the implementation of a website.

# Expected Output

You will generate a list of tasks, each paired with a corresponding programmatic verifier.

## Task Requirements
The key requirement of the task is **realism** where the task intent should match real user's need and workflows. The intent should be clear, but encode the natue of language usage, which is often brief and underspecified. Think about how an actual worker can specific tasks. But make sure the task is still unambiguous. There are a few axis to think about:

### Difficulty Levels
You must design tasks across three difficulty levels: **easy**, **medium**, and **hard**.

The difficulty level should be determined by:

1. **Task complexity** — approximately measured by the number of steps required to complete the task. This depends on both:
   - The workflow design of the website.
   - The inherent complexity of the task itself such as requiring multiple sub-tasks, understand complex relations etc.

2. **Dependencies and prerequisites** — some tasks may appear simple on the surface but are challenging due to:
   - Implicit or unspoken prerequisites where the task can only be accomplished by navigating the system to discover necessary information or features, permissions etc

### Realism 
The intruction can be flexible. It should be realistic and reflect how users would naturally express the task. For example, users can define the workflow, sometimes they define the expected outcome etc. You should consider different dimensions. 

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

## Task Schema

Each task is defined as a JSON object:

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

# Guide for Programmatic Verifiers

## Privileged Access

You are able to write robust verifiers because you have privileged access to the website implementation. You can:

- Access the backend directly.
- Inspect the database, filesystem, or application state.
- Check internal website state.
- Add new APIs if necessary to simplify verification.

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
