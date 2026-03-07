import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])
    labels = state.get("labels", [])

    # Find the Urgent label by name
    urgent_label = next((l for l in labels if l["name"] == "Urgent"), None)
    if urgent_label is None:
        return False, "Could not find label 'Urgent' in state."

    email = next(
        (e for e in emails if e["subject"] == "Database Performance Report - March"
         and e["from"]["name"] == "Tom Bradley"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Database Performance Report - March' from Tom Bradley."

    email_labels = email.get("labels", [])
    if urgent_label["id"] not in email_labels:
        return False, f"Email 'Database Performance Report - March' does not have the 'Urgent' label. Labels: {email_labels}"

    return True, "Label 'Urgent' applied to email 'Database Performance Report - March' from Tom Bradley."
