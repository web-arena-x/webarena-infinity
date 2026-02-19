import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'Firefox on Ubuntu' session was revoked."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    sessions = state.get("sessions", [])

    firefox_session = [s for s in sessions if s.get("deviceName") == "Firefox on Ubuntu"]
    if firefox_session:
        return False, "Session 'Firefox on Ubuntu' still exists."

    return True, "Session 'Firefox on Ubuntu' successfully revoked."
