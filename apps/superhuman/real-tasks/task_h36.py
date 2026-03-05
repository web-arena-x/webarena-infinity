"""Task H36: Turn off auto-advance, disable show weekends, set auto-reminder delay to 7 days."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    failures = []

    general = state.get("settings", {}).get("general", {})
    if general.get("autoAdvance") is not False:
        failures.append(f"autoAdvance is {general.get('autoAdvance')}, expected False")

    calendar = state.get("settings", {}).get("calendar", {})
    if calendar.get("showWeekends") is not False:
        failures.append(f"showWeekends is {calendar.get('showWeekends')}, expected False")

    reminders = state.get("settings", {}).get("reminders", {})
    if reminders.get("autoReminderDelay") != 7:
        failures.append(f"autoReminderDelay is {reminders.get('autoReminderDelay')}, expected 7")

    if failures:
        return False, "Settings checks failed: " + "; ".join(failures)

    return True, "auto-advance off, weekends hidden, auto-reminder delay set to 7 days."
