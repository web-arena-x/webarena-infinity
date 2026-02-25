import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "Re: Collaboration Proposal":
            labels = email.get("labels", [])
            if "label_17" in labels:
                return True, "Task completed successfully."
            else:
                return False, f"Email 'Re: Collaboration Proposal' found but 'label_17' not in labels: {labels}."

    return False, "Email with subject 'Re: Collaboration Proposal' not found."
