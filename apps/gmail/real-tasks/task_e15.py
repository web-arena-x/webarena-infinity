"""
Task: Mark Marcus Williams' Design System Update email as important.
Verify: Email id=6 has isImportant=True AND "IMPORTANT" in labels.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 6), None)
    if email is None:
        return False, "Email with id=6 not found in state."

    is_important = email.get("isImportant")
    labels = email.get("labels", [])

    if not is_important:
        return False, (
            f"Email id=6 ('Design System Update v4.2') is not marked as important. "
            f"isImportant={is_important}"
        )

    if "IMPORTANT" not in labels:
        return False, (
            f"Email id=6 ('Design System Update v4.2') does not have 'IMPORTANT' label. "
            f"labels={labels}"
        )

    return True, (
        "Email id=6 ('Design System Update v4.2') is marked as important "
        "and has the 'IMPORTANT' label."
    )
