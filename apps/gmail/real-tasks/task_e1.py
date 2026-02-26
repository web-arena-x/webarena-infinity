"""
Task: Star Sarah Chen's Q1 product roadmap email.
Verify: Email id=1 has isStarred=True and starType is not null.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 1), None)
    if email is None:
        return False, "Email with id=1 not found in state."

    if not email.get("isStarred"):
        return False, (
            f"Email id=1 ('Q1 Product Roadmap Review') is not starred. "
            f"isStarred={email.get('isStarred')}"
        )

    star_type = email.get("starType")
    if star_type is None:
        return False, (
            "Email id=1 is starred but starType is null. "
            "Expected a non-null starType value."
        )

    return True, (
        f"Email id=1 ('Q1 Product Roadmap Review') is starred with starType='{star_type}'."
    )
