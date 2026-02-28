import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    milestones = state.get("milestones", [])

    target_title = "v4.3 - Mobile Optimization"
    milestone = next((m for m in milestones if m.get("title") == target_title), None)

    if milestone is None:
        return False, f"Could not find milestone with title '{target_title}'."

    if milestone.get("status") != "closed":
        return False, f"Milestone '{target_title}' status is '{milestone.get('status')}', expected 'closed'."

    return True, f"Milestone '{target_title}' is closed."
