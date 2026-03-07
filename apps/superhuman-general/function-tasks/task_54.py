import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])
    labels = state.get("labels", [])

    # Find Work and Urgent label IDs
    work_label = None
    urgent_label = None
    for label in labels:
        if label.get("name") == "Work":
            work_label = label
        elif label.get("name") == "Urgent":
            urgent_label = label

    if not work_label:
        return False, "Label 'Work' not found in state."
    if not urgent_label:
        return False, "Label 'Urgent' not found in state."

    work_id = work_label.get("id")
    urgent_id = urgent_label.get("id")

    # Find the target email
    for email in emails:
        if (email.get("subject") == "Accessibility Audit Results" and
                "maya.patel@acmecorp.com" in str(email.get("from", ""))):
            email_labels = email.get("labels", [])

            missing = []
            if work_id not in email_labels:
                missing.append(f"Work (id={work_id})")
            if urgent_id not in email_labels:
                missing.append(f"Urgent (id={urgent_id})")

            if missing:
                return False, f"Email 'Accessibility Audit Results' is missing labels: {', '.join(missing)}. Current labels: {email_labels}"

            return True, "Both 'Work' and 'Urgent' labels applied to 'Accessibility Audit Results'."

    return False, "No email with subject 'Accessibility Audit Results' from maya.patel@acmecorp.com found."
