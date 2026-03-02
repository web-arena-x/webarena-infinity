import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state["preferences"]["desktopApp"]["enableSpellCheck"]
    if val is not False:
        return False, f"Expected enableSpellCheck to be False, got '{val}'."

    return True, "Spell check disabled."
