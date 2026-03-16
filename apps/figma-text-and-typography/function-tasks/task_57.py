import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    if prefs.get("nudgeAmount") != 4:
        return False, f"Expected nudgeAmount 4, got {prefs.get('nudgeAmount')}."

    return True, "Nudge amount changed to 4."
