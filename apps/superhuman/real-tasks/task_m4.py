"""Task M4: Set a reminder on Olivia Turner's Prismatica integration email for tomorrow."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails = state.get("emails", [])
    target = None
    for email in emails:
        if email.get("id") == "email_036":
            target = email
            break

    if target is None:
        return False, "Could not find email_036 (Re: Prismatica integration — timeline slipping)"

    reminder = target.get("reminder")
    if reminder is not None and reminder:
        return True, f"Reminder is set on email_036: {reminder}"
    return False, f"Reminder is not set on email_036 (reminder={reminder})"
