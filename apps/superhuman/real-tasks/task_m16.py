"""Task M16: Change the calendar week start to Monday."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    settings = state.get("settings", {})
    calendar = settings.get("calendar", {})
    week_starts_on = calendar.get("weekStartsOn")

    if week_starts_on == "monday":
        return True, "Calendar week starts on Monday"
    return False, f"Calendar weekStartsOn is '{week_starts_on}', expected 'monday'"
