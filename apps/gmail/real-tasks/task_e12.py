"""
Task: Turn off hover actions.
Verify: state["settings"]["hoverActions"] == False.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    settings = state.get("settings", {})

    hover_actions = settings.get("hoverActions")
    if hover_actions is not False:
        return False, (
            f"Hover actions are not disabled. "
            f"hoverActions={hover_actions}"
        )

    return True, "Hover actions are disabled (hoverActions=False)."
