import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    auto_advance = settings.get("autoAdvance")

    if auto_advance == "list":
        return True, "Task completed successfully."
    else:
        return False, f"Auto-advance is not set to 'list' (autoAdvance='{auto_advance}')."
