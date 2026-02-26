"""
Task: Set the default reply behavior to Reply all.
Verify: state["settings"]["defaultReplyBehavior"] == "reply_all".
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    settings = state.get("settings", {})

    reply_behavior = settings.get("defaultReplyBehavior")
    if reply_behavior != "reply_all":
        return False, (
            f"Default reply behavior is not 'reply_all'. "
            f"defaultReplyBehavior='{reply_behavior}'"
        )

    return True, "Default reply behavior is set to 'reply_all'."
