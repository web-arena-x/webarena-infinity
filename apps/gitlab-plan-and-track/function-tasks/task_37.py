import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    milestones = state.get("milestones", [])

    target = next((m for m in milestones if m.get("title") == "Q1 2026 Planning"), None)
    if not target:
        return False, "Milestone with title 'Q1 2026 Planning' not found."

    status = target.get("status", "")
    if status != "closed":
        return False, f"Milestone status is '{status}', expected 'closed'."

    return True, "Milestone 'Q1 2026 Planning' has status 'closed'."
