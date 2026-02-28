import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    epics = state.get("epics", [])

    target = next((e for e in epics if e.get("title") == "Mobile App v2"), None)
    if not target:
        return False, "Epic with title 'Mobile App v2' not found."

    status = target.get("status", "")
    if status != "closed":
        return False, f"Epic status is '{status}', expected 'closed'."

    return True, "Epic 'Mobile App v2' has status 'closed'."
