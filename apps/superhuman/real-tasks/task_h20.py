"""Task H20: Disable team read statuses/reply indicators, turn off follow-up auto-drafts, change auto-reminders to external only."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    settings = state.get("settings", {})
    failures = []

    # Read statuses checks
    read_statuses = settings.get("readStatuses", {})
    if read_statuses.get("teamReadStatuses") is not False:
        failures.append(f"readStatuses.teamReadStatuses is {read_statuses.get('teamReadStatuses')}, expected False")
    if read_statuses.get("teamReplyIndicators") is not False:
        failures.append(f"readStatuses.teamReplyIndicators is {read_statuses.get('teamReplyIndicators')}, expected False")

    # Auto drafts check
    auto_drafts = settings.get("autoDrafts", {})
    if auto_drafts.get("followUps") is not False:
        failures.append(f"autoDrafts.followUps is {auto_drafts.get('followUps')}, expected False")

    # Reminders check
    reminders = settings.get("reminders", {})
    auto_reminders = reminders.get("autoReminders")
    if auto_reminders != "external-only":
        failures.append(f"reminders.autoReminders is '{auto_reminders}', expected 'external-only'")

    if failures:
        return False, "Settings checks failed: " + "; ".join(failures)

    return True, "Team read statuses/reply indicators disabled, follow-up auto-drafts off, auto-reminders set to external-only."
