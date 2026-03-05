"""Task E13: Change the default reply action to Reply instead of Reply All."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    try:
        reply_action = state["settings"]["general"]["defaultReplyAction"]
    except (KeyError, TypeError) as e:
        return False, f"Could not read settings.general.defaultReplyAction: {e}"

    if reply_action != "reply":
        return False, f"defaultReplyAction is '{reply_action}' — expected 'reply'"

    return True, "Default reply action is set to 'reply'."
