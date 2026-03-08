# Task: Turn off calendar sync.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    sync = state.get("accountSettings", {}).get("syncSettings", {})
    calendar_sync = sync.get("calendarSync")

    if calendar_sync is False:
        return True, "Calendar sync is now disabled."
    else:
        return False, f"calendarSync is {calendar_sync}, expected false."
