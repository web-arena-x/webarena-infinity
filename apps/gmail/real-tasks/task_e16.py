"""
Task: Unstar the contract review email from James O'Brien.
Verify: Email id=11 has isStarred=False and starType is None/null.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 11), None)
    if email is None:
        return False, "Email with id=11 not found in state."

    is_starred = email.get("isStarred")
    star_type = email.get("starType")

    if is_starred is not False:
        return False, (
            f"Email id=11 ('Contract Review: Vendor Agreement') is still starred. "
            f"isStarred={is_starred}"
        )

    if star_type is not None:
        return False, (
            f"Email id=11 ('Contract Review: Vendor Agreement') still has a starType. "
            f"starType='{star_type}'"
        )

    return True, (
        "Email id=11 ('Contract Review: Vendor Agreement') is unstarred "
        "and starType is null."
    )
