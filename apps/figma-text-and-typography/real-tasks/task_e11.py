"""
Task: Turn off font preview in the settings.
Verify: preferences.showFontPreview is False.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    prefs = state.get("preferences", {})
    val = prefs.get("showFontPreview")

    if val is not False:
        return False, f"Expected 'showFontPreview' to be False, got '{val}'."

    return True, "Font preview is turned off."
