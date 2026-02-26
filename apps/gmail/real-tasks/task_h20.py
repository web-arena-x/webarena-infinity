"""Delete the Receipts label and add Finance label to all emails that previously had Receipts."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    labels = state.get("labels", [])
    emails = state.get("emails", [])

    errors = []

    # Check 1: No label with id='label_5' or name='Receipts' should exist
    receipts_label = next(
        (
            l
            for l in labels
            if l.get("id") == "label_5" or l.get("name") == "Receipts"
        ),
        None,
    )
    if receipts_label is not None:
        errors.append(
            f"Receipts label still exists: id={receipts_label.get('id')}, "
            f"name={receipts_label.get('name')}"
        )

    # Emails that previously had Receipts (label_5)
    target_ids = [19, 22, 67, 69, 88]

    for eid in target_ids:
        email = next((e for e in emails if e["id"] == eid), None)
        if email is None:
            errors.append(f"Email {eid} not found in state")
            continue

        email_labels = email.get("labels", [])

        # Check 2: All should have label_3 (Finance)
        if "label_3" not in email_labels:
            errors.append(
                f"Email {eid} ('{email.get('subject', '?')}') does not have "
                f"'label_3' (Finance) in labels: {email_labels}"
            )

        # Check 3: None should still have label_5
        if "label_5" in email_labels:
            errors.append(
                f"Email {eid} ('{email.get('subject', '?')}') still has "
                f"'label_5' (Receipts) in labels: {email_labels}"
            )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Receipts label deleted and Finance label applied to all former "
        "Receipts emails (19, 22, 67, 69, 88)."
    )
