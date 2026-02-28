import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    todos = state.get("todos", [])

    pending_todos = [t for t in todos if t.get("status") == "pending"]
    if pending_todos:
        pending_ids = [t.get("id", "unknown") for t in pending_todos]
        return False, f"Found {len(pending_todos)} todo(s) still with status 'pending': {pending_ids}."

    return True, "No todos have status 'pending'. All previously pending todos are now 'done'."
