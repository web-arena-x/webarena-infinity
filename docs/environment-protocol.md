# Environment Protocol

Every new web application must follow this structure and API contract to work with the evaluation harness.

## Required Directory Structure

```
{app-name}/
├── server.py           # HTTP server with standard API (see below)
├── tasks.json          # Task definitions (see format below)
├── tasks/              # Verifier scripts (one .py per task)
│   ├── task_e1.py
│   ├── task_e2.py
│   └── ...
├── index.html          # Entry point served by server
├── js/                 # Application logic
├── css/                # Styles
└── Dockerfile          # For containerized deployment
```

## Required Server API

The server must expose these HTTP endpoints:

| Endpoint        | Method | Purpose                                      |
|-----------------|--------|----------------------------------------------|
| `/api/state`    | GET    | Return current app state as JSON (for verifiers) |
| `/api/state`    | PUT    | Accept state pushes from browser on every mutation |
| `/api/reset`    | POST   | Reset state to seed data, notify browsers via SSE |
| `/api/events`   | GET    | SSE stream for pushing reset commands to browser |
| `/*`            | GET    | Static file serving (HTML/CSS/JS)            |

### State Sync Contract

1. **First load**: Browser JS must `PUT /api/state` with full initial state on page load
2. **Seed capture**: Server captures the first PUT as immutable `_seed_state` (deep copy)
3. **On mutation**: Browser JS calls `PUT /api/state` with updated state after every change
4. **On reset**: Server restores `_app_state = deepcopy(_seed_state)`, sends SSE `reset` event
5. **Browser reset handler**: On receiving SSE `reset`, browser must reload seed data and navigate home

### Server Globals (per process — enables parallel isolation)

```python
_app_state = None       # Current state (written by browser, read by verifiers)
_seed_state = None      # Immutable snapshot of first state push
_clients = []           # SSE client queues
_state_lock = threading.Lock()
_clients_lock = threading.Lock()
```

### CLI Interface

```bash
python server.py --port PORT   # Default: 8000
```

## Task Definition Format (tasks.json)

```json
[
  {
    "id": "task_e1",
    "difficulty": "easy",
    "instruction": "Human-readable task description for the agent.",
    "verify": "tasks/task_e1.py"
  }
]
```

- **id**: `task_{difficulty_letter}{number}` — e.g. `task_e1`, `task_m3`, `task_h8`
- **difficulty**: `"easy"`, `"medium"`, or `"hard"`
- **instruction**: What the agent should do (natural language)
- **verify**: Relative path to verifier script

### ID Convention
- `e` = easy, `m` = medium, `h` = hard
- 8 tasks per difficulty level (24 total in gitlab-org-management)

## Verifier Script Pattern

Each `tasks/task_*.py` must export a `verify` function:

```python
import requests

def verify(server_url: str) -> tuple[bool, str]:
    """
    Args:
        server_url: e.g. "http://localhost:8000"
    Returns:
        (passed, message) — message explains result for the report
    """
    resp = requests.get(f"{server_url}/api/state")
    state = resp.json()

    # Check conditions against state...
    if not condition:
        return False, "Expected X but got Y."

    return True, "Task completed successfully."
```

- Verifiers read state via `GET /api/state` — never interact with the browser
- Return `(bool, str)` — the string appears in the HTML report
- Must handle missing/unexpected data gracefully

## Browser-Side Requirements

The web app's JavaScript must:

1. **Push state on load**: `PUT /api/state` with full serializable state on first page load
2. **Push state on mutation**: Every user action that changes state must trigger a state push
3. **Listen for SSE reset**: Connect to `/api/events`, on `reset` event → restore seed data + navigate home
4. **State must be JSON-serializable**: No functions, DOM refs, or circular structures

### Recommended JS Pattern (from gitlab-org-management)

```javascript
// After any state mutation:
AppState.notify()  →  _persist() + _pushStateToServer()

function _pushStateToServer() {
    fetch('/api/state', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(getSerializableState())
    });
}

// SSE listener:
const eventSource = new EventSource('/api/events');
eventSource.onmessage = (e) => {
    if (e.data === 'reset') {
        resetToSeedData();
        navigateHome();
    }
};
```

## Dockerfile Template

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY server.py index.html tasks.json ./
COPY js/ ./js/
COPY css/ ./css/
COPY tasks/ ./tasks/
EXPOSE 8000
CMD ["python", "server.py"]
```

## Reference Implementation

`gitlab-org-management/` is the reference. When creating a new environment, model it after that directory structure and server.py implementation.
