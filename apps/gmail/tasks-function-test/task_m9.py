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
        if "Your tweet got 250 likes" in subject:
            target_email = email
            break

    if not target_email:
        return False, "Could not find email with subject containing 'Your tweet got 250 likes'."

    errors = []
    if target_email.get("isStarred") is not True:
        errors.append(f"isStarred is {target_email.get('isStarred')}, expected True")
    if target_email.get("isImportant") is not True:
        errors.append(f"isImportant is {target_email.get('isImportant')}, expected True")

    labels = target_email.get("labels", [])
    if "IMPORTANT" not in labels:
        errors.append(f"'IMPORTANT' not in labels. Current labels: {labels}")

    if errors:
        return False, f"Email 'Your tweet got 250 likes': {'; '.join(errors)}."

    return True, "Task completed successfully."
