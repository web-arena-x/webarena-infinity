"""
Task: The Crypto Gains email in spam isn't actually spam — move it back to the inbox.
Verify: Email id=93 has isSpam=False AND "INBOX" in labels.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 93), None)
    if email is None:
        return False, "Email with id=93 not found in state."

    is_spam = email.get("isSpam")
    labels = email.get("labels", [])

    if is_spam is not False:
        return False, (
            f"Email id=93 ('Turn $100 into $100,000 with this coin!') is still marked as spam. "
            f"isSpam={is_spam}"
        )

    if "INBOX" not in labels:
        return False, (
            f"Email id=93 ('Turn $100 into $100,000 with this coin!') is not in the inbox. "
            f"labels={labels}"
        )

    return True, (
        "Email id=93 ('Turn $100 into $100,000 with this coin!') is no longer spam "
        "and is in the inbox."
    )
