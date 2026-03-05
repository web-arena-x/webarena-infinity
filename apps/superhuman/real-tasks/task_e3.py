"""Task E3: Trash Olivia Turner's LinkedIn connection request."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_id = "email_031"
    target_subject = "LinkedIn: Olivia Turner wants to connect"

    emails = state.get("emails", [])
    email = next((e for e in emails if e["id"] == target_id), None)
    if email is None:
        return False, f"Email '{target_id}' not found (expected subject: '{target_subject}')"

    folder = email.get("folder", "")
    if folder != "trash":
        return False, f"Email '{target_id}' ('{email.get('subject', '')}') is in folder '{folder}' — expected 'trash'"

    return True, f"Email '{target_id}' ('{target_subject}') is in trash."
