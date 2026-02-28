import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    epics = state.get("epics", [])

    target = next((e for e in epics if e.get("title") == "Search Performance"), None)
    if not target:
        return False, "Epic with title 'Search Performance' not found."

    parent_epic = next((e for e in epics if e.get("title") == "Performance Initiative"), None)
    if not parent_epic:
        return False, "Parent epic 'Performance Initiative' not found."

    parent_epic_id = parent_epic.get("id")
    actual_parent = target.get("parentEpicId")
    if actual_parent != parent_epic_id:
        return False, f"Epic parentEpicId is '{actual_parent}', expected '{parent_epic_id}' (Performance Initiative)."

    return True, "Epic 'Search Performance' exists with parentEpicId pointing to 'Performance Initiative'."
