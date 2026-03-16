import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    if prefs.get("defaultFontSize") != 14:
        return False, f"Expected defaultFontSize 14, got {prefs.get('defaultFontSize')}."

    return True, "Default font size changed to 14."
