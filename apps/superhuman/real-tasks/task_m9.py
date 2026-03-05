"""Task M9: Cancel the scheduled weekly check-in email."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails = state.get("emails", [])
    target = None
    for email in emails:
        if email.get("id") == "email_101":
            target = email
            break

    if target is None:
        return False, "Could not find email_101 (Weekly check-in)"

    is_scheduled = target.get("isScheduled")
    is_draft = target.get("isDraft")

    # The email should no longer be scheduled. It may have been converted to a draft.
    if is_scheduled is False or is_scheduled is None:
        return True, f"email_101 is no longer scheduled (isScheduled={is_scheduled}, isDraft={is_draft})"

    return False, f"email_101 is still scheduled (isScheduled={is_scheduled}, isDraft={is_draft})"
