"""
Task H3: Archive all unread emails in the Social category.
Verify: Emails with IDs 31, 33, 37, 43 (social + unread in seed) all have
isArchived=True.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    target_ids = [31, 33, 37, 43]
    not_found = []
    not_archived = []

    for tid in target_ids:
        email = next((e for e in emails if e.get("id") == tid), None)
        if email is None:
            not_found.append(tid)
            continue
        if not email.get("isArchived"):
            not_archived.append(tid)

    errors = []
    if not_found:
        errors.append(f"Emails not found: {not_found}")
    if not_archived:
        errors.append(f"Emails not archived: {not_archived}")

    if errors:
        return False, "Not all unread social emails archived. " + "; ".join(errors)

    return True, (
        f"All unread social emails ({target_ids}) are archived."
    )
