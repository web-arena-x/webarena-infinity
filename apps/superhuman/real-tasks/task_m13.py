"""Task M13: Set the default meeting duration to 60 minutes."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    settings = state.get("settings", {})
    calendar = settings.get("calendar", {})
    duration = calendar.get("defaultMeetingDuration")

    if duration == 60:
        return True, "Default meeting duration is 60 minutes"
    return False, f"Default meeting duration is {duration}, expected 60"
