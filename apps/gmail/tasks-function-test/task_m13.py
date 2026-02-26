import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    spam_emails = [e for e in emails if e.get("isSpam") is True]

    if spam_emails:
        subjects = [e.get("subject", "(no subject)") for e in spam_emails]
        return False, (
            f"Found {len(spam_emails)} spam email(s) still present: {subjects}. "
            f"All spam emails should have been permanently deleted."
        )

    return True, "Task completed successfully."
