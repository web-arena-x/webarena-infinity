"""Task E8: Set the undo send timer to 20 seconds."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    try:
        undo_delay = state["settings"]["general"]["undoSendDelay"]
    except (KeyError, TypeError) as e:
        return False, f"Could not read settings.general.undoSendDelay: {e}"

    if undo_delay != 20:
        return False, f"undoSendDelay is {undo_delay} — expected 20"

    return True, "Undo send delay is set to 20 seconds."
