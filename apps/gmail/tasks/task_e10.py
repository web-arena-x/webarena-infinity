import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    conversation_view = settings.get("conversationView")

    if conversation_view is False:
        return True, "Task completed successfully."
    else:
        return False, f"settings.conversationView is {conversation_view}, expected false."
