"""
Task: Mark Sophie Laurent's conference invitation as read.
Verify: Email id=14 has isRead=True.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 14), None)
    if email is None:
        return False, "Email with id=14 not found in state."

    if not email.get("isRead"):
        return False, (
            f"Email id=14 ('Bonjour! Conference Speaker Invitation') is not marked as read. "
            f"isRead={email.get('isRead')}"
        )

    return True, "Email id=14 ('Bonjour! Conference Speaker Invitation') is marked as read."
