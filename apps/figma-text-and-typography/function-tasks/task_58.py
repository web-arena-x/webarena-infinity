import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    if prefs.get("bigNudgeAmount") != 20:
        return False, f"Expected bigNudgeAmount 20, got {prefs.get('bigNudgeAmount')}."

    return True, "Big nudge amount changed to 20."
