import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify timezone changed to 'Europe/London' and theme changed to 'light'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cu = state.get("currentUser", {})
    prefs = state.get("preferences", {})

    tz = cu.get("timezone")
    theme = prefs.get("theme")

    if tz != "Europe/London":
        return False, f"Expected timezone='Europe/London', got '{tz}'."
    if theme != "light":
        return False, f"Expected theme='light', got '{theme}'."

    return True, "Timezone changed to 'Europe/London' and theme changed to 'Light'."
