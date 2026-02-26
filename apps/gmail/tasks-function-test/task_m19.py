import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_email = None
    for email in emails:
        if email.get("subject") == "Investor Deck Review":
            target_email = email
            break

    if not target_email:
        return False, "Could not find email with subject 'Investor Deck Review'."

    errors = []
    if target_email.get("isSnoozed") is not False:
        errors.append(
            f"isSnoozed is {target_email.get('isSnoozed')}, expected False"
        )

    labels = target_email.get("labels", [])
    if "INBOX" not in labels:
        errors.append(f"'INBOX' not in labels. Current labels: {labels}")

    if errors:
        return False, f"Email 'Investor Deck Review': {'; '.join(errors)}."

    return True, "Task completed successfully."
