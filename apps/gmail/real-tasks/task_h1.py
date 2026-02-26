"""
Task H1: Create a label 'Q1 Priority' nested under Work, then apply it to
Sarah Chen's Q1 Product Roadmap Review email.
Verify:
  1. A label with name='Q1 Priority', type='user', parentId='label_1' exists.
  2. Email id=1 contains the new label's id in its labels list.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    # --- Check 1: label exists with correct nesting ---
    labels = state.get("labels", [])
    q1_label = None
    for label in labels:
        if label.get("name") == "Q1 Priority" and label.get("type") == "user":
            q1_label = label
            break

    if q1_label is None:
        return False, "No user label named 'Q1 Priority' found."

    if q1_label.get("parentId") != "label_1":
        return False, (
            f"Label 'Q1 Priority' exists but parentId={q1_label.get('parentId')!r}, "
            f"expected 'label_1' (Work)."
        )

    new_label_id = q1_label.get("id")

    # --- Check 2: email id=1 has the new label ---
    emails = state.get("emails", [])
    email = next((e for e in emails if e.get("id") == 1), None)
    if email is None:
        return False, "Email with id=1 not found in state."

    email_labels = email.get("labels", [])
    if new_label_id not in email_labels:
        return False, (
            f"Email id=1 ('Q1 Product Roadmap Review') does not have label "
            f"'{new_label_id}'. Current labels: {email_labels}"
        )

    return True, (
        f"Label 'Q1 Priority' (id={new_label_id}) is nested under Work and "
        f"applied to email id=1."
    )
