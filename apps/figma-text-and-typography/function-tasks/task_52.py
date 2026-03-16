import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    if prefs.get("defaultHorizontalAlign") != "center":
        return False, f"Expected defaultHorizontalAlign 'center', got '{prefs.get('defaultHorizontalAlign')}'."

    return True, "Default alignment changed to center."
