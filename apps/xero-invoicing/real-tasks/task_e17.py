import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("invoiceSettings", {})

    due_date = settings.get("defaultDueDate", {})
    due_type = due_date.get("type")
    if due_type != "endOfFollowingMonth":
        return False, f"Expected defaultDueDate.type to be 'endOfFollowingMonth', got '{due_type}'."

    return True, "Default payment terms have been changed to end of following month."
