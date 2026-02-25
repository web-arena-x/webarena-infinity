import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    inbox_type = settings.get("inboxType")

    if inbox_type == "unread_first":
        return True, "Task completed successfully."
    else:
        return False, f"settings.inboxType is '{inbox_type}', expected 'unread_first'."
