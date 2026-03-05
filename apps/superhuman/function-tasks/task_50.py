import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that week starts on has been changed to 'monday'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        week_starts_on = state["settings"]["calendar"]["weekStartsOn"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.calendar.weekStartsOn: {e}"

    if week_starts_on == "monday":
        return True, "Week starts on is set to 'monday'."
    return False, f"Expected settings.calendar.weekStartsOn to be 'monday', got {week_starts_on!r}."
