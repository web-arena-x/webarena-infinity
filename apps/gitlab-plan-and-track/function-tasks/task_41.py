import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    epics = state.get("epics", [])

    old_epic = next((e for e in epics if e.get("title") == "Documentation Overhaul"), None)
    if old_epic is not None:
        return False, "Epic 'Documentation Overhaul' still exists; it should have been renamed."

    new_epic = next((e for e in epics if e.get("title") == "Documentation Overhaul v2"), None)
    if new_epic is None:
        return False, "Epic 'Documentation Overhaul v2' not found."

    return True, "Epic 'Documentation Overhaul' no longer exists and epic 'Documentation Overhaul v2' exists."
