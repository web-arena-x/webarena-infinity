"""
Task: Set the nudge amount to 4 pixels.
Verify: preferences.nudgeAmount == 4.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    prefs = state.get("preferences", {})
    val = prefs.get("nudgeAmount")

    if val != 4:
        return False, f"Expected 'nudgeAmount' to be 4, got '{val}'."

    return True, "Nudge amount is set to 4 pixels."
