import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    general = settings.get("general", {})
    default_reply = general.get("defaultReplyAction")

    if default_reply == "reply":
        return True, "Default reply action successfully changed to 'reply'."

    return False, (
        f"defaultReplyAction is '{default_reply}', expected 'reply'."
    )
