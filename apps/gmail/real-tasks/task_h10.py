"""
Task H10: Remove all user labels from Priya's Sprint Retro email and add
Waiting For Reply.
Verify email id=29:
  - 'label_1' (Work) NOT in labels
  - 'label_9' (Projects) NOT in labels
  - 'label_18' (Waiting For Reply) in labels
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 29), None)
    if email is None:
        return False, "Email with id=29 (Sprint Retro Action Items) not found."

    email_labels = email.get("labels", [])
    errors = []

    if "label_1" in email_labels:
        errors.append("'label_1' (Work) still in labels (should be removed)")

    if "label_9" in email_labels:
        errors.append("'label_9' (Projects) still in labels (should be removed)")

    if "label_18" not in email_labels:
        errors.append("'label_18' (Waiting For Reply) not in labels (should be added)")

    if errors:
        return False, (
            f"Email id=29 label check failed: " + "; ".join(errors)
            + f". Current labels: {email_labels}"
        )

    return True, (
        "Email id=29 has Work and Projects labels removed, "
        "Waiting For Reply label added."
    )
