"""
Task: Remove importance marker from Jennifer Wu's collaboration proposal.
Verify: Email id=20 has isImportant=False and 'IMPORTANT' not in labels.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 20), None)
    if email is None:
        return False, "Email with id=20 not found in state."

    if email.get("isImportant") is not False:
        return False, (
            f"Email id=20 ('Re: Collaboration Proposal') still has importance marker. "
            f"isImportant={email.get('isImportant')}"
        )

    labels = email.get("labels", [])
    if "IMPORTANT" in labels:
        return False, (
            f"Email id=20 ('Re: Collaboration Proposal') still has 'IMPORTANT' in labels. "
            f"labels={labels}"
        )

    return True, (
        "Email id=20 ('Re: Collaboration Proposal') importance marker removed. "
        "isImportant=False and 'IMPORTANT' not in labels."
    )
