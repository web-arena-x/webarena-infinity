import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    auto_check = settings.get("autoCheckInteractions")
    if auto_check is not False:
        return False, f"autoCheckInteractions is {auto_check}, expected False."

    return True, "Auto-check drug interactions has been disabled (autoCheckInteractions is False)."
