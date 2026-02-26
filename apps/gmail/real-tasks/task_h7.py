"""
Task H7: Create nested label 'Taxes' under Finance, apply to David Kim's
tax season reminder and year-end financial summary emails.
Verify:
  1. Label with name='Taxes', type='user', parentId='label_3' (Finance) exists.
  2. Emails 28 and 122 both have the new label's id in their labels.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    # --- Check 1: label exists with correct nesting ---
    labels = state.get("labels", [])
    taxes_label = None
    for label in labels:
        if label.get("name") == "Taxes" and label.get("type") == "user":
            taxes_label = label
            break

    if taxes_label is None:
        return False, "No user label named 'Taxes' found."

    if taxes_label.get("parentId") != "label_3":
        return False, (
            f"Label 'Taxes' exists but parentId={taxes_label.get('parentId')!r}, "
            f"expected 'label_3' (Finance)."
        )

    new_label_id = taxes_label.get("id")

    # --- Check 2: both emails have the new label ---
    emails = state.get("emails", [])
    target_ids = {
        28: "Tax Season Reminder: Documents Needed",
        122: "Year-End Financial Summary 2025",
    }
    missing = []

    for eid, subject in target_ids.items():
        email = next((e for e in emails if e.get("id") == eid), None)
        if email is None:
            missing.append(f"Email id={eid} ('{subject}') not found")
            continue
        email_labels = email.get("labels", [])
        if new_label_id not in email_labels:
            missing.append(
                f"Email id={eid} ('{subject}') missing label '{new_label_id}'. "
                f"Current labels: {email_labels}"
            )

    if missing:
        return False, "; ".join(missing)

    return True, (
        f"Label 'Taxes' (id={new_label_id}) is nested under Finance and "
        f"applied to emails 28 and 122."
    )
