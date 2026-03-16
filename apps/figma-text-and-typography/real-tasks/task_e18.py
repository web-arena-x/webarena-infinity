"""
Task: Disable smart symbols.
Verify: preferences.smartSymbols is False.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    prefs = state.get("preferences", {})
    val = prefs.get("smartSymbols")

    if val is not False:
        return False, f"Expected 'smartSymbols' to be False, got '{val}'."

    return True, "Smart symbols is disabled."
