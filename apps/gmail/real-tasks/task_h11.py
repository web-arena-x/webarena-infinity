"""Trash all unread primary emails that have attachments."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    emails = state.get("emails", [])

    # Emails 1, 6, 9, 26 are the unread primary emails with attachments
    target_ids = [1, 6, 9, 26]
    errors = []

    for eid in target_ids:
        email = next((e for e in emails if e["id"] == eid), None)
        if email is None:
            errors.append(f"Email {eid} not found in state")
            continue
        if not email.get("isTrashed", False):
            errors.append(
                f"Email {eid} ('{email.get('subject', '?')}') is not trashed"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "All unread primary emails with attachments have been trashed."
