import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    target_email = None
    for email in emails:
        if email.get("subject") == "Sarah Chen endorsed you for Cloud Architecture":
            target_email = email
            break

    if not target_email:
        return False, "Could not find email with subject 'Sarah Chen endorsed you for Cloud Architecture'."

    errors = []

    category = target_email.get("category", "")
    if category != "primary":
        errors.append(f"category is '{category}', expected 'primary'")

    labels = target_email.get("labels", [])
    if "CATEGORY_PRIMARY" not in labels:
        errors.append(f"'CATEGORY_PRIMARY' not in labels")
    if "CATEGORY_SOCIAL" in labels:
        errors.append(f"'CATEGORY_SOCIAL' still in labels")

    if errors:
        return False, (
            f"Email 'Sarah Chen endorsed you for Cloud Architecture': "
            f"{'; '.join(errors)}. Current labels: {labels}"
        )

    return True, "Task completed successfully."
