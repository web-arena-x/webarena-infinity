"""
Task: Turn off conversation view.
Verify: state["settings"]["conversationView"] == False.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    settings = state.get("settings", {})

    conversation_view = settings.get("conversationView")
    if conversation_view is not False:
        return False, (
            f"Conversation view is not turned off. "
            f"conversationView={conversation_view} (expected False)"
        )

    return True, "Conversation view is turned off (conversationView=False)."
