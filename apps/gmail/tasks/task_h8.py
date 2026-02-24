import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "Project Update Meeting" and email.get("isSent") is True:
            to_list = email.get("to", [])
            has_sarah = any(
                recipient.get("email") == "sarah.chen@techcorp.io"
                for recipient in to_list
            )
            if not has_sarah:
                continue

            body = (email.get("body") or "").lower()
            if "schedule a project update meeting" in body:
                return True, "Task completed successfully."
            else:
                return False, f"Sent email to sarah.chen@techcorp.io with correct subject found, but body does not contain 'schedule a project update meeting'. Body: {email.get('body', '')[:200]}"

    return False, "No sent email with subject 'Project Update Meeting' to sarah.chen@techcorp.io found."
