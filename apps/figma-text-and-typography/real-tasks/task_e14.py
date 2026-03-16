"""
Task: Change the default font size to 14.
Verify: preferences.defaultFontSize == 14.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    prefs = state.get("preferences", {})
    val = prefs.get("defaultFontSize")

    if val != 14:
        return False, f"Expected 'defaultFontSize' to be 14, got '{val}'."

    return True, "Default font size is set to 14."
