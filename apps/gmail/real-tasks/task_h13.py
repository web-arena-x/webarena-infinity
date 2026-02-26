"""Create a label 'Conferences' under Work, apply to Sophie Laurent's EuroDesign Summit email and Figma Config 2026 email."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    labels = state.get("labels", [])
    emails = state.get("emails", [])

    # Step 1: Find the 'Conferences' label with parentId='label_1' (Work)
    conferences_label = None
    for label in labels:
        if label.get("name") == "Conferences" and label.get("type") == "user":
            if label.get("parentId") == "label_1":
                conferences_label = label
                break

    if conferences_label is None:
        return False, (
            "No label named 'Conferences' found with type='user' and "
            "parentId='label_1' (Work)"
        )

    conf_label_id = conferences_label.get("id")

    # Step 2: Check emails 14 and 46 have the new label
    errors = []
    for eid in [14, 46]:
        email = next((e for e in emails if e["id"] == eid), None)
        if email is None:
            errors.append(f"Email {eid} not found in state")
            continue
        email_labels = email.get("labels", [])
        if conf_label_id not in email_labels:
            errors.append(
                f"Email {eid} ('{email.get('subject', '?')}') does not have "
                f"label '{conf_label_id}' (Conferences) in its labels: {email_labels}"
            )

    if errors:
        return False, "; ".join(errors)

    return True, (
        f"'Conferences' label (id={conf_label_id}) exists under Work and is "
        "applied to emails 14 and 46."
    )
