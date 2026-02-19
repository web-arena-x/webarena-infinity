import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that theme is 'dark' and font size is 'large'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    theme = prefs.get("theme")
    font_size = prefs.get("fontSize")

    if theme != "dark":
        return False, f"Expected theme='dark', got '{theme}'."
    if font_size != "large":
        return False, f"Expected fontSize='large', got '{font_size}'."

    return True, "Theme set to 'Dark' and font size set to 'Large'."
