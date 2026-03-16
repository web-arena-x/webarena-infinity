import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    if prefs.get("showFontPreview") is not False:
        return False, f"Expected showFontPreview to be False, got {prefs.get('showFontPreview')}."

    return True, "Show font preview disabled."
