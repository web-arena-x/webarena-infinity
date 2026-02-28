import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    milestones = state.get("milestones", [])
    milestone = next((m for m in milestones if m.get("title") == "v4.4 - Integrations"), None)
    if milestone is None:
        return False, "Could not find a milestone titled 'v4.4 - Integrations'."

    if milestone.get("startDate") != "2026-08-01":
        return False, f"Expected startDate '2026-08-01' but got '{milestone.get('startDate')}'."

    if milestone.get("dueDate") != "2026-09-30":
        return False, f"Expected dueDate '2026-09-30' but got '{milestone.get('dueDate')}'."

    if milestone.get("status") != "active":
        return False, f"Expected status 'active' but got '{milestone.get('status')}'."

    return True, "Milestone 'v4.4 - Integrations' created with correct dates and active status."
