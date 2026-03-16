"""
Task: Turn off smart quotes.
Verify: preferences.smartQuotes is False.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    preferences = state.get("preferences", {})
    smart_quotes = preferences.get("smartQuotes")

    if smart_quotes is not False:
        return False, f"Expected 'smartQuotes' to be False, got '{smart_quotes}'."

    return True, "Smart quotes are turned off."
