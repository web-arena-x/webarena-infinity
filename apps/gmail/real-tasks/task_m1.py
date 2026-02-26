"""
Task M1: Add the Clients label to David Kim's tax season reminder email.
Find email id=28, check 'label_11' in labels.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    emails = state.get("emails", [])

    target_email = None
    for email in emails:
        if email.get("id") == 28:
            target_email = email
            break

    if target_email is None:
        return False, "Email id=28 (Tax Season Reminder) not found."

    labels = target_email.get("labels", [])
    if "label_11" in labels:
        return True, "Email 28 has the Clients label (label_11)."
    else:
        return False, f"Email 28 is missing the Clients label (label_11). Current labels: {labels}"
