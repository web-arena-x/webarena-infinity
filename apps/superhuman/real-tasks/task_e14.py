"""Task E14: The developer grant email in trash isn't spam — move it back to the inbox."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_id = "email_104"
    target_subject = "URGENT: Claim your $10,000 developer grant now!"

    emails = state.get("emails", [])
    email = next((e for e in emails if e["id"] == target_id), None)
    if email is None:
        return False, f"Email '{target_id}' not found (expected subject: '{target_subject}')"

    folder = email.get("folder", "")
    if folder != "inbox":
        return False, f"Email '{target_id}' ('{email.get('subject', '')}') is in folder '{folder}' — expected 'inbox'"

    return True, f"Email '{target_id}' ('{target_subject}') is in inbox."
