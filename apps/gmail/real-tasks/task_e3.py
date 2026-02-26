"""
Task: Trash the property listing email from Tom Bradley.
Verify: Email id=15 has isTrashed=True.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 15), None)
    if email is None:
        return False, "Email with id=15 not found in state."

    if not email.get("isTrashed"):
        return False, (
            f"Email id=15 ('Property Listing: 45 Oak Avenue') is not trashed. "
            f"isTrashed={email.get('isTrashed')}"
        )

    return True, "Email id=15 ('Property Listing: 45 Oak Avenue') is trashed."
