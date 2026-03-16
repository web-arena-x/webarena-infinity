"""
Task: Change the default font to Roboto and the default size to 14.
Verify: preferences.defaultFontFamily='Roboto' and preferences.defaultFontSize=14.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    prefs = state.get("preferences", {})

    if prefs.get("defaultFontFamily") != "Roboto":
        return False, f"Expected defaultFontFamily='Roboto', got '{prefs.get('defaultFontFamily')}'."

    default_size = prefs.get("defaultFontSize")
    if not isinstance(default_size, (int, float)) or abs(default_size - 14) > 0.001:
        return False, f"Expected defaultFontSize=14, got '{default_size}'."

    return True, "Default font set to Roboto and default size set to 14."
