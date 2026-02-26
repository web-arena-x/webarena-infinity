import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    hover_actions = settings.get("hoverActions")

    if hover_actions is False:
        return True, "Task completed successfully."
    else:
        return False, f"Hover actions are not disabled (hoverActions={hover_actions})."
