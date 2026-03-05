import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    target_subject = "URGENT: Claim your $10,000 developer grant now!"
    matching = [e for e in emails if target_subject in e.get("subject", "")]

    if len(matching) > 0:
        return False, f"Email with subject containing '{target_subject}' still exists (expected permanently deleted)."

    return True, f"Email '{target_subject}' has been permanently deleted."
