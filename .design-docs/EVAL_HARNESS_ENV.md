# Evaluation Harness Integration Guide

This document describes everything the evaluation harness needs to interface with this website and its verifiers.

## Starting the Environment

```bash
cd mirror-mirror-claude
python3 server.py              # serves on http://localhost:8000
python3 server.py --port 9000  # or custom port
```

The server serves both the static website and the API endpoints. The browser agent should be pointed to the same URL (e.g., `http://localhost:8000`).

**Important**: The browser must load the page at least once before the first reset. On first page load, the app pushes its initial state to the server via `PUT /api/state`, and the server captures this as the **seed state snapshot**. All subsequent resets restore from this snapshot. Until the first page load, `GET /api/state` returns HTTP 404.

## Task Definitions

All tasks are defined in `tasks.json` at the project root:

```json
{
  "id": "task_e1",
  "difficulty": "easy",
  "instruction": "Natural language instruction for the agent.",
  "verify": "tasks/task_e1.py"
}
```

- The `instruction` field is the exact text to give the browser agent.
- The `verify` field is a path relative to the project root.

## Resetting State Between Tasks

Before each task, the harness must reset the app to seed data:

```
POST http://localhost:{port}/api/reset
```

This triggers two independent actions:

1. **Server-side (immediate)**: The server restores `GET /api/state` to the seed state snapshot. The response includes `"seed_restored": true` on success.
2. **Browser-side (async via SSE)**: The server sends a `reset` event to all connected browser tabs. The browser calls `AppState.resetToSeedData()` and navigates to the home page.

### Key Design: No Browser Round-Trip Required

The server restores the seed state directly from its captured snapshot. Verifiers can call `GET /api/state` immediately after reset and get valid seed data — **no polling is needed**.

The browser SSE notification is a separate concern: it ensures the browser UI resets so the agent sees a clean starting state. The harness should allow a brief pause (~500ms) after reset for the browser to process the SSE event before the agent begins the next task.

### First Load Requirement

The server captures the seed state from the first `PUT /api/state` push (which happens on first page load). If `POST /api/reset` is called before any browser has loaded the page, the response will include `"seed_restored": false` and `GET /api/state` will return 404. Ensure the browser loads the app at least once after server start.

## Running Verifiers

Each verifier is a Python module with a single function:

```python
def verify(server_url: str) -> tuple[bool, str]:
```

- **`server_url`**: Base URL of the running server, e.g., `"http://localhost:8000"`
- **Returns**: `(passed, message)` where `passed` is a boolean and `message` explains the result

### Invocation

```python
import importlib.util

spec = importlib.util.spec_from_file_location("verifier", "mirror-mirror-claude/tasks/task_e1.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

passed, message = mod.verify("http://localhost:8000")
```

### Dependencies

Verifiers require the `requests` library (installed in `../.venv/`).

### When to Run the Verifier

Run the verifier **after the agent signals task completion** (or after a timeout). The verifier reads the current `AppState` snapshot from the server, so it reflects whatever mutations the agent made through the UI.

There is no race condition concern here — the browser pushes state synchronously on every mutation (fire-and-forget fetch, but the state is written to the server-side variable before the verifier reads it in practice). If the agent's last action was a UI click that triggers a mutation, the state will already be on the server by the time the verifier runs (the browser's `_persist()` fires immediately on state change).

## API Endpoints Reference

| Endpoint | Method | Purpose | Used By |
|----------|--------|---------|---------|
| `/api/state` | `GET` | Read current app state as JSON | Verifiers |
| `/api/state` | `PUT` | Push app state (called automatically by browser) | Browser |
| `/api/reset` | `POST` | Reset to seed data | Harness |
| `/api/events` | `GET` | SSE stream for server→browser commands | Browser |

