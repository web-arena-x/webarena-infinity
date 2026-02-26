import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    conv_view = state["settings"].get("conversationView")
    if conv_view is not False:
        return False, f"Expected conversationView to be false, got '{conv_view}'."

    return True, "Conversation view has been disabled."
