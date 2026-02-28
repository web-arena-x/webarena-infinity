import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    epics = state.get("epics", [])

    target_title = "Frontend Modernization"
    epic = next((e for e in epics if e.get("title") == target_title), None)

    if epic is None:
        return False, f"Could not find epic with title '{target_title}'."

    if epic.get("status") != "closed":
        return False, f"Epic '{target_title}' status is '{epic.get('status')}', expected 'closed'."

    return True, f"Epic '{target_title}' is closed."
