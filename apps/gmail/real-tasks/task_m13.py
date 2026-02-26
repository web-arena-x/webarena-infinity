"""Archive the latest Morning Brew newsletter."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()

    emails = state.get("emails", [])
    target = None
    for email in emails:
        if email.get("id") == 77:
            target = email
            break

    if target is None:
        return False, "Email with id=77 not found."

    is_archived = target.get("isArchived", False)
    labels = target.get("labels", [])

    if is_archived is True and "INBOX" not in labels:
        return True, "Email 77 (Morning Brew) is archived and removed from INBOX."

    issues = []
    if is_archived is not True:
        issues.append(f"isArchived is {is_archived!r}, expected True")
    if "INBOX" in labels:
        issues.append("'INBOX' still in labels")
    return False, f"Email 77 not properly archived: {'; '.join(issues)}."
