import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_email = None
    for email in emails:
        if email.get("subject") == "Re: Collaboration Proposal":
            from_field = email.get("from", {})
            from_name = from_field.get("name", "").lower() if isinstance(from_field, dict) else str(from_field).lower()
            from_email = from_field.get("email", "").lower() if isinstance(from_field, dict) else ""
            if "jennifer" in from_name or "wu" in from_name or "jennifer" in from_email or "wu" in from_email:
                target_email = email
                break

    if not target_email:
        # Fall back to just subject match
        for email in emails:
            if email.get("subject") == "Re: Collaboration Proposal":
                target_email = email
                break

    if not target_email:
        return False, "Could not find email with subject 'Re: Collaboration Proposal'."

    errors = []
    if target_email.get("isSnoozed") is not True:
        errors.append(f"isSnoozed is {target_email.get('isSnoozed')}, expected True")
    snooze_until = target_email.get("snoozeUntil")
    if snooze_until is None:
        errors.append("snoozeUntil is None, expected a date/time value")

    if errors:
        return False, f"Email 'Re: Collaboration Proposal': {'; '.join(errors)}."

    return True, "Task completed successfully."
