"""
Task: Change the spelling language to French.
Verify: preferences.spellingLanguage == 'French'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    preferences = state.get("preferences", {})
    spelling_language = preferences.get("spellingLanguage")

    if spelling_language != "French":
        return False, f"Expected 'spellingLanguage' to be 'French', got '{spelling_language}'."

    return True, "Spelling language is set to French."
