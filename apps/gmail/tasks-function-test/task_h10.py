import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])

    target_email = None
    for email in emails:
        subject = email.get("subject", "")
        from_field = email.get("from") or {}
        from_str = ""
        if isinstance(from_field, dict):
            from_str = (from_field.get("name", "") + " " + from_field.get("email", "")).lower()
        else:
            from_str = str(from_field).lower()
        if subject == "Re: Collaboration Proposal" and ("jennifer" in from_str or "wu" in from_str):
            target_email = email
            break

    if not target_email:
        return False, "No email found with subject 'Re: Collaboration Proposal' from someone with 'jennifer' or 'wu' in the from."

    if target_email.get("isStarred") is not True:
        return False, f"Email isStarred is {target_email.get('isStarred')}, expected True."

    email_labels = target_email.get("labels", [])
    if "label_11" not in email_labels:
        return False, f"Email does not have 'label_11' (Clients) in its labels: {email_labels}"

    if target_email.get("isRead") is not True:
        return False, f"Email isRead is {target_email.get('isRead')}, expected True."

    return True, "Task completed successfully."
