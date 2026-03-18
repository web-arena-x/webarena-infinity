import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    refills = settings.get("defaultRefills")
    if refills != 3:
        return False, f"Default refills is {refills}, expected 3."

    return True, "Default refills changed to 3."
