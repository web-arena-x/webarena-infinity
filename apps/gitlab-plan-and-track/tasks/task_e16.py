import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    milestones = state.get("milestones", [])

    milestone = next((m for m in milestones if m.get("title") == "Backlog"), None)

    if milestone is not None:
        return False, "Milestone 'Backlog' still exists but should have been deleted."

    return True, "Milestone 'Backlog' has been deleted."
