import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    if prefs.get("smartQuotes") is not False:
        return False, f"Expected smartQuotes to be False, got {prefs.get('smartQuotes')}."

    return True, "Smart quotes disabled."
