import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    sessions = state.get("sessions", [])

    if len(sessions) != 1:
        return False, f"Expected exactly 1 session, but found {len(sessions)}."

    if not sessions[0].get("isCurrent"):
        return False, "The remaining session does not have isCurrent == True."

    return True, "Only 1 session remains and it is the current session."
