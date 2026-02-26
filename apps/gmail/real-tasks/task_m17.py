"""Move the archived sprint planning notes from Sarah Chen back to the inbox."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()

    emails = state.get("emails", [])
    target = None
    for email in emails:
        if email.get("id") == 85:
            target = email
            break

    if target is None:
        return False, "Email with id=85 not found."

    is_archived = target.get("isArchived", True)
    labels = target.get("labels", [])

    if is_archived is False and "INBOX" in labels:
        return True, "Email 85 (Sprint planning notes) is unarchived and back in INBOX."

    issues = []
    if is_archived is not False:
        issues.append(f"isArchived is {is_archived!r}, expected False")
    if "INBOX" not in labels:
        issues.append("'INBOX' not in labels")
    return False, f"Email 85 not properly moved to inbox: {'; '.join(issues)}."
