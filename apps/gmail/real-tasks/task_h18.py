"""Unsnooze Tom Bradley's mortgage pre-approval email and add the Action Required label."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e["id"] == 83), None)
    if email is None:
        return False, "Email 83 ('Mortgage Pre-approval Documents') not found in state"

    errors = []

    if email.get("isSnoozed", True) is not False:
        errors.append(
            f"isSnoozed is {email.get('isSnoozed')}, expected False"
        )

    snooze_until = email.get("snoozeUntil")
    if snooze_until is not None:
        errors.append(
            f"snoozeUntil is '{snooze_until}', expected None/null"
        )

    email_labels = email.get("labels", [])

    if "INBOX" not in email_labels:
        errors.append(
            f"'INBOX' not in labels (unsnoozed email should be back in inbox): {email_labels}"
        )

    if "label_17" not in email_labels:
        errors.append(
            f"'label_17' (Action Required) not in labels: {email_labels}"
        )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Email 83 is unsnoozed, back in inbox, and has Action Required label."
    )
