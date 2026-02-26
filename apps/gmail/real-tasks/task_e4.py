"""
Task: Archive the shipping update from Carlos Mendez.
Verify: Email id=19 has isArchived=True.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 19), None)
    if email is None:
        return False, "Email with id=19 not found in state."

    if not email.get("isArchived"):
        return False, (
            f"Email id=19 ('Shipping Update: Order #LP-2026-8834') is not archived. "
            f"isArchived={email.get('isArchived')}"
        )

    return True, "Email id=19 ('Shipping Update: Order #LP-2026-8834') is archived."
