import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    epics = state.get("epics", [])

    target = next((e for e in epics if e["title"] == "Analytics Dashboard"), None)
    if not target:
        return False, "Epic with title 'Analytics Dashboard' not found."

    if target.get("status") != "open":
        return False, f"Epic status is '{target.get('status')}', expected 'open'."

    return True, "Epic 'Analytics Dashboard' has status 'open'."
