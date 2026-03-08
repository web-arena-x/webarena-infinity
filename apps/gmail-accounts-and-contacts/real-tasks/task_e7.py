# Task: Dismiss CloudNine merge.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    suggestions = state.get("mergeSuggestions", [])
    for suggestion in suggestions:
        if suggestion.get("id") == "merge_1":
            if suggestion.get("dismissed") is True:
                return True, "CloudNine merge suggestion has been dismissed."
            else:
                return False, f"merge_1 dismissed is {suggestion.get('dismissed')}, expected true."

    return False, "Merge suggestion 'merge_1' not found in state."
