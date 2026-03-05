import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    sessions = state.get("sessions", [])

    for session in sessions:
        if session.get("deviceName") == "iPhone 15 Pro":
            return False, "Session 'iPhone 15 Pro' still exists in sessions."

    return True, "Session 'iPhone 15 Pro' has been removed."
