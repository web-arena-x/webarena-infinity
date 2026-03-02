import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    sessions = state.get("sessions", [])

    for session in sessions:
        if session.get("deviceName") == "Windows Desktop":
            return False, "Session 'Windows Desktop' still exists in sessions."

    return True, "Session 'Windows Desktop' has been removed."
