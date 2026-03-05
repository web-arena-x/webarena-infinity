import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that calendar event 'Q2 Planning Session' exists with correct date and calendar."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    events = state.get("calendarEvents", [])
    for event in events:
        if event.get("title") == "Q2 Planning Session":
            start = event.get("start", "")
            calendar = event.get("calendar", "")

            errors = []
            if "2026-03-20" not in start:
                errors.append(f"Expected start date to contain '2026-03-20', got {start!r}")
            # Accept case-insensitive match for calendar name
            if calendar.lower() != "work":
                errors.append(f"Expected calendar to be 'Work', got {calendar!r}")

            if errors:
                return False, "; ".join(errors)
            return True, "Calendar event 'Q2 Planning Session' exists with correct date and calendar."

    event_titles = [e.get("title") for e in events]
    return False, f"No calendar event named 'Q2 Planning Session' found. Existing events: {event_titles!r}."
