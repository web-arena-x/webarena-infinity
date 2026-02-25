import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        subject = email.get("subject", "")
        if "Production database issue" in subject:
            labels = email.get("labels", [])
            has_action_required = "label_17" in labels
            is_read = email.get("isRead", False)

            issues = []
            if has_action_required:
                issues.append(f"'label_17' (Action Required) still in labels: {labels}")
            if not is_read:
                issues.append(f"isRead is {is_read}, expected true")

            if not issues:
                return True, "Task completed successfully."
            else:
                return False, f"Email found but: {'; '.join(issues)}."

    return False, "Email with subject containing 'Production database issue' not found."
