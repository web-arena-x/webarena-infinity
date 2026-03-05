import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that show weekends has been disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        show_weekends = state["settings"]["calendar"]["showWeekends"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.calendar.showWeekends: {e}"

    if show_weekends is False:
        return True, "Show weekends is disabled."
    return False, f"Expected settings.calendar.showWeekends to be False, got {show_weekends!r}."
