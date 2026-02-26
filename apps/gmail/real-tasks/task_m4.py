"""
Task M4: Snooze the CI/CD Pipeline Migration Plan email until tomorrow.
Find email id=9, check isSnoozed=True AND snoozeUntil is not None AND 'INBOX' not in labels.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    emails = state.get("emails", [])

    target_email = None
    for email in emails:
        if email.get("id") == 9:
            target_email = email
            break

    if target_email is None:
        return False, "Email id=9 (CI/CD Pipeline Migration Plan) not found."

    is_snoozed = target_email.get("isSnoozed", False)
    snooze_until = target_email.get("snoozeUntil")
    labels = target_email.get("labels", [])
    errors = []

    if not is_snoozed:
        errors.append("isSnoozed is not True")
    if snooze_until is None:
        errors.append("snoozeUntil is None")
    if "INBOX" in labels:
        errors.append("'INBOX' still in labels")

    if errors:
        return False, f"Email 9 not correctly snoozed: {'; '.join(errors)}."

    return True, f"Email 9 is snoozed until {snooze_until} and removed from INBOX."
