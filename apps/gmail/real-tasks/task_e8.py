"""
Task: Remove the star from Emily Rodriguez's partnership opportunity email.
Verify: Email id=7 has isStarred=False and starType is None/null.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 7), None)
    if email is None:
        return False, "Email with id=7 not found in state."

    if email.get("isStarred") is not False:
        return False, (
            f"Email id=7 ('Partnership Opportunity - Series B Company') is still starred. "
            f"isStarred={email.get('isStarred')}"
        )

    star_type = email.get("starType")
    if star_type is not None:
        return False, (
            f"Email id=7 ('Partnership Opportunity - Series B Company') still has a starType. "
            f"starType='{star_type}' (expected None)"
        )

    return True, (
        "Email id=7 ('Partnership Opportunity - Series B Company') star removed. "
        "isStarred=False and starType=None."
    )
