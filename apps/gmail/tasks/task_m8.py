import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        subject = email.get("subject", "")
        if "Conference Speaker Invitation" in subject:
            labels = email.get("labels", [])
            has_travel = "label_4" in labels
            not_in_inbox = "INBOX" not in labels

            if has_travel and not_in_inbox:
                return True, "Task completed successfully."
            else:
                issues = []
                if not has_travel:
                    issues.append("'label_4' (Travel) not in labels")
                if not not_in_inbox:
                    issues.append("'INBOX' still in labels")
                return False, f"Email found but: {', '.join(issues)}. Labels: {labels}."

    return False, "Email with subject containing 'Conference Speaker Invitation' not found."
