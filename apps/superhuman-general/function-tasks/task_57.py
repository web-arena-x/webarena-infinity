import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    events = state.get("calendarEvents", [])

    for event in events:
        if event.get("title") == "Lunch Meeting":
            errors = []

            date = event.get("date", "")
            if date != "2026-03-09":
                errors.append(f"date is '{date}', expected '2026-03-09'")

            start_time = event.get("startTime", "")
            if start_time != "12:00":
                errors.append(f"startTime is '{start_time}', expected '12:00'")

            end_time = event.get("endTime", "")
            if end_time != "13:00":
                errors.append(f"endTime is '{end_time}', expected '13:00'")

            location = event.get("location", "")
            if "Blue Bottle Coffee" not in location:
                errors.append(f"location is '{location}', expected to contain 'Blue Bottle Coffee'")

            attendees = event.get("attendees", [])
            attendee_strs = [str(a) for a in attendees]
            if not any("marcus.w@designhub.io" in a for a in attendee_strs):
                errors.append(f"attendees {attendees} does not include 'marcus.w@designhub.io'")

            if errors:
                return False, "Calendar event 'Lunch Meeting' found but has issues: " + "; ".join(errors)

            return True, "Calendar event 'Lunch Meeting' created correctly."

    return False, "No calendar event titled 'Lunch Meeting' found."
