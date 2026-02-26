import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])

    trashed_emails = [e for e in emails if e.get("isTrashed") is True]
    if trashed_emails:
        subjects = [e.get("subject", "(no subject)") for e in trashed_emails]
        return False, f"Found {len(trashed_emails)} trashed email(s) still remaining: {subjects}"

    return True, "Task completed successfully."
