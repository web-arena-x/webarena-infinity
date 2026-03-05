"""Task H24: Delete the 'Hiring Panel: Senior Backend Engineer' calendar event and archive the invite email."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    failures = []

    # Check cal_016 is deleted
    calendar_events = state.get("calendarEvents", [])
    for event in calendar_events:
        if event.get("id") == "cal_016":
            failures.append("cal_016 (Hiring Panel) still exists in calendarEvents")
            break

    # Check email_116 is archived
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    email = emails_by_id.get("email_116")
    if email is None:
        failures.append("email_116 not found in state")
    elif email.get("folder") != "done":
        failures.append(f"email_116 folder is '{email.get('folder')}', expected 'done'")

    if failures:
        return False, "Calendar event / email checks failed: " + "; ".join(failures)

    return True, "cal_016 deleted and email_116 archived to Done."
