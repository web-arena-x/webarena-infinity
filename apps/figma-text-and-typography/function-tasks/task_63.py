import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    if prefs.get("defaultFontStyle") != "Bold":
        return False, f"Expected defaultFontStyle 'Bold', got '{prefs.get('defaultFontStyle')}'."

    return True, "Default font style changed to Bold."
