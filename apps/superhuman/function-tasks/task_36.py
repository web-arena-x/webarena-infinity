import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    general = settings.get("general", {})
    undo_send_delay = general.get("undoSendDelay")

    if undo_send_delay == 30:
        return True, "Undo-send delay successfully changed to 30 seconds."

    return False, (
        f"undoSendDelay is {undo_send_delay}, expected 30."
    )
