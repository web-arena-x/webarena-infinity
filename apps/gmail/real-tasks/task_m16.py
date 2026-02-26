"""Empty the spam folder."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()

    emails = state.get("emails", [])
    spam_emails = [e for e in emails if e.get("isSpam") is True]

    if len(spam_emails) == 0:
        return True, "No spam emails remain. Spam folder is empty."
    spam_ids = [e.get("id") for e in spam_emails]
    return False, f"Expected no spam emails, but found {len(spam_emails)} with ids: {spam_ids}."
