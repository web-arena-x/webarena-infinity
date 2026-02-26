import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    delay = state["settings"].get("undoSendDelay")
    if delay != 30:
        return False, f"Expected undoSendDelay 30, got {delay}."

    return True, "Undo send cancellation period changed to 30 seconds."
