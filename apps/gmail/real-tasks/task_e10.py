"""
Task: Mark Priya Sharma's latest API integration message as read.
Verify: Email id=2 has isRead=True.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 2), None)
    if email is None:
        return False, "Email with id=2 not found in state."

    if not email.get("isRead"):
        return False, (
            f"Email id=2 ('Re: API Integration Issue') is not marked as read. "
            f"isRead={email.get('isRead')}"
        )

    return True, "Email id=2 ('Re: API Integration Issue') is marked as read."
