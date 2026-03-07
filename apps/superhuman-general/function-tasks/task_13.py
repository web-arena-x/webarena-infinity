import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])
    emails = state.get("emails", [])

    # Verify no label named 'Receipts' exists
    receipts_label = next((l for l in labels if l["name"] == "Receipts"), None)
    if receipts_label is not None:
        return False, f"Label 'Receipts' still exists with id '{receipts_label['id']}'."

    # Verify no emails still reference a Receipts label ID
    # We check for any label ID that might have been the Receipts label
    # by looking for orphaned label references
    for email in emails:
        email_labels = email.get("labels", [])
        for label_id in email_labels:
            # Check if this label_id still exists in the labels list
            matching_label = next((l for l in labels if l["id"] == label_id), None)
            if matching_label is None:
                return False, (
                    f"Email '{email['subject']}' still references deleted label ID '{label_id}'."
                )

    return True, "Label 'Receipts' deleted and removed from all emails."
