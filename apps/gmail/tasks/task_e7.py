import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "Turn $100 into $100,000 with this coin!":
            is_spam = email.get("isSpam", True)
            labels = email.get("labels", [])
            in_inbox = "INBOX" in labels

            if not is_spam and in_inbox:
                return True, "Task completed successfully."
            else:
                return False, f"Email found but isSpam={is_spam}, 'INBOX' in labels={in_inbox}."

    return False, "Email with subject 'Turn $100 into $100,000 with this coin!' not found."
