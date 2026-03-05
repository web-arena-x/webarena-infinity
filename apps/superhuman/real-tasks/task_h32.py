"""Task H32: Change event notifications to 30 minutes before and switch default calendar view to day."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    failures = []

    cal_settings = state.get("settings", {}).get("calendar", {})

    event_notif = cal_settings.get("eventNotifications")
    if event_notif != "30-minutes":
        failures.append(f"eventNotifications is '{event_notif}', expected '30-minutes'")

    default_view = cal_settings.get("defaultView")
    if default_view != "day":
        failures.append(f"defaultView is '{default_view}', expected 'day'")

    if failures:
        return False, "Calendar settings checks failed: " + "; ".join(failures)

    return True, "Event notifications set to 30 minutes and default view set to day."
