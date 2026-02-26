"""Archive all emails labeled Newsletters that are currently in the inbox."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    emails = state.get("emails", [])

    # These are the emails with label_6 (Newsletters) that were in INBOX
    target_ids = [72, 73, 75, 77, 78, 79, 80, 81, 112, 118]
    errors = []

    for eid in target_ids:
        email = next((e for e in emails if e["id"] == eid), None)
        if email is None:
            errors.append(f"Email {eid} not found in state")
            continue

        is_archived = email.get("isArchived", False)
        email_labels = email.get("labels", [])

        if not is_archived:
            # Also check if INBOX was removed as an alternative archiving signal
            if "INBOX" in email_labels:
                errors.append(
                    f"Email {eid} ('{email.get('subject', '?')}') is not archived "
                    f"and still has INBOX label"
                )

    if errors:
        return False, "; ".join(errors)

    return True, "All Newsletters emails from inbox have been archived."
