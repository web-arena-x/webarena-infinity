import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that default meeting duration has been changed to 60 minutes."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        duration = state["settings"]["calendar"]["defaultMeetingDuration"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.calendar.defaultMeetingDuration: {e}"

    if duration == 60:
        return True, "Default meeting duration is set to 60 minutes."
    return False, f"Expected settings.calendar.defaultMeetingDuration to be 60, got {duration!r}."
