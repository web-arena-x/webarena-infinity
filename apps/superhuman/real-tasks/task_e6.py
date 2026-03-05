"""Task E6: Mark Elena's security audit report as read."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_id = "email_012"
    target_subject = "Security audit report — critical findings"

    emails = state.get("emails", [])
    email = next((e for e in emails if e["id"] == target_id), None)
    if email is None:
        return False, f"Email '{target_id}' not found (expected subject: '{target_subject}')"

    if email.get("isRead") is not True:
        return False, f"Email '{target_id}' ('{email.get('subject', '')}') is not read — expected isRead == True"

    return True, f"Email '{target_id}' ('{target_subject}') is marked as read."
