"""Task H13: Create a calendar event for team lunch on March 9th from 12 PM to 1 PM at TechCorp Cafe."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    calendar_events = state.get("calendarEvents", [])
    if not calendar_events:
        return False, "No calendarEvents found in state."

    for event in calendar_events:
        title = event.get("title", "")
        start = event.get("start", "")
        location = event.get("location", "")

        title_match = "lunch" in title.lower()
        date_match = "2026-03-09" in start
        location_match = "techcorp cafe" in location.lower()

        if title_match and date_match and location_match:
            return True, f"Found matching calendar event: title='{title}', start='{start}', location='{location}'."

    return False, "No calendar event found with 'lunch' in title, date 2026-03-09, and location containing 'TechCorp Cafe'."
