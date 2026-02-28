import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    milestones = state.get("milestones", [])

    target = next((m for m in milestones if m.get("title") == "v4.4 - Internationalization"), None)
    if not target:
        return False, "Milestone with title 'v4.4 - Internationalization' not found."

    start_date = target.get("startDate", "")
    if start_date != "2026-07-16":
        return False, f"Milestone startDate is '{start_date}', expected '2026-07-16'."

    due_date = target.get("dueDate", "")
    if due_date != "2026-09-30":
        return False, f"Milestone dueDate is '{due_date}', expected '2026-09-30'."

    status = target.get("status", "")
    if status != "active":
        return False, f"Milestone status is '{status}', expected 'active'."

    return True, "Milestone 'v4.4 - Internationalization' exists with correct startDate, dueDate, and status."
