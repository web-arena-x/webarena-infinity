import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    undo_send_delay = settings.get("undoSendDelay")

    if undo_send_delay == 30:
        return True, "Task completed successfully."
    else:
        return False, f"settings.undoSendDelay is {undo_send_delay}, expected 30."
