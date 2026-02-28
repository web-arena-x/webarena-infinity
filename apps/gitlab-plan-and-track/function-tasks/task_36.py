import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    milestones = state.get("milestones", [])

    target = next((m for m in milestones if m.get("title") == "Backlog"), None)
    if not target:
        return False, "Milestone with title 'Backlog' not found."

    expected_desc = "Unscheduled items awaiting prioritization and scheduling."
    actual_desc = target.get("description", "")
    if actual_desc != expected_desc:
        return False, f"Milestone description is '{actual_desc}', expected '{expected_desc}'."

    return True, "Milestone 'Backlog' has the correct description."
