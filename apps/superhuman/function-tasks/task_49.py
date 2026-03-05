import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that calendar default view has been changed to 'day'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        default_view = state["settings"]["calendar"]["defaultView"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.calendar.defaultView: {e}"

    if default_view == "day":
        return True, "Calendar default view is set to 'day'."
    return False, f"Expected settings.calendar.defaultView to be 'day', got {default_view!r}."
