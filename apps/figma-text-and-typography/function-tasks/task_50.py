import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    if prefs.get("defaultFontFamily") != "Roboto":
        return False, f"Expected defaultFontFamily 'Roboto', got '{prefs.get('defaultFontFamily')}'."

    return True, "Default font family changed to Roboto."
