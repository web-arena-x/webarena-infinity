"""
Task: Change undo send timer to 30 seconds.
Verify: state["settings"]["undoSendDelay"] == 30.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    settings = state.get("settings", {})

    undo_send_delay = settings.get("undoSendDelay")
    if undo_send_delay != 30:
        return False, (
            f"Undo send delay is not set to 30 seconds. "
            f"undoSendDelay={undo_send_delay} (expected 30)"
        )

    return True, "Undo send delay is set to 30 seconds (undoSendDelay=30)."
