"""Task H27: Turn off the Personal calendar and delete every Personal calendar event."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    failures = []

    # Check Personal calendar is disabled
    calendars = state.get("settings", {}).get("calendar", {}).get("calendars", [])
    for cal in calendars:
        if cal.get("id") == "cal_personal":
            if cal.get("enabled") is not False:
                failures.append(f"Personal calendar enabled is {cal.get('enabled')}, expected False")
            break
    else:
        failures.append("cal_personal not found in settings calendars")

    # Check Personal calendar events are deleted (cal_005, cal_013, cal_015)
    personal_event_ids = {"cal_005", "cal_013", "cal_015"}
    calendar_events = state.get("calendarEvents", [])
    for event in calendar_events:
        if event.get("id") in personal_event_ids:
            failures.append(f"{event['id']} ({event.get('title')}) still exists in calendarEvents")

    if failures:
        return False, "Personal calendar checks failed: " + "; ".join(failures)

    return True, "Personal calendar disabled and all 3 Personal events deleted."
