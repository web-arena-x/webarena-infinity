import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that meeting link provider has been changed to 'zoom'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        provider = state["settings"]["calendar"]["meetingLinkProvider"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.calendar.meetingLinkProvider: {e}"

    if provider == "zoom":
        return True, "Meeting link provider is set to 'zoom'."
    return False, f"Expected settings.calendar.meetingLinkProvider to be 'zoom', got {provider!r}."
