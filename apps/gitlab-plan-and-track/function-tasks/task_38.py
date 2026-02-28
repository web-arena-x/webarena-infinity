import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    milestones = state.get("milestones", [])

    target = next((m for m in milestones if m.get("title") == "v3.9 - Maintenance"), None)
    if not target:
        return False, "Milestone with title 'v3.9 - Maintenance' not found."

    status = target.get("status", "")
    if status != "active":
        return False, f"Milestone status is '{status}', expected 'active'."

    return True, "Milestone 'v3.9 - Maintenance' has status 'active'."
