import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    events = state.get("calendarEvents", [])

    for event in events:
        if (
            event.get("title") == "Design Workshop"
            and event.get("date") == "2026-03-10"
            and event.get("startTime") == "10:00"
            and event.get("endTime") == "12:00"
            and event.get("location") == "Zoom"
        ):
            return True, "Calendar event 'Design Workshop' created correctly."

    return False, "Calendar event 'Design Workshop' with date '2026-03-10', startTime '10:00', endTime '12:00', location 'Zoom' not found."
