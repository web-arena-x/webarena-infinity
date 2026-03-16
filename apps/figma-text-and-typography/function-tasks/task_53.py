import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    if prefs.get("defaultTextDirection") != "rtl":
        return False, f"Expected defaultTextDirection 'rtl', got '{prefs.get('defaultTextDirection')}'."

    return True, "Default text direction changed to RTL."
