import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that calendar event 'Company Holiday — No Meetings' has been deleted."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    events = state.get("calendarEvents", [])
    for event in events:
        title = event.get("title", "")
        # Check for both em-dash and regular dash variants
        if "Company Holiday" in title and "No Meetings" in title:
            return False, f"Calendar event '{title}' still exists."

    return True, "Calendar event 'Company Holiday — No Meetings' has been deleted."
