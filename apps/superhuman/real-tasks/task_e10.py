"""Task E10: Mark the Pragmatic Engineer newsletter as read."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_id = "email_029"

    emails = state.get("emails", [])
    email = next((e for e in emails if e["id"] == target_id), None)
    if email is None:
        return False, f"Email '{target_id}' not found (expected subject containing 'Pragmatic Engineer')"

    subject = email.get("subject", "")
    if "Pragmatic Engineer" not in subject:
        return False, f"Email '{target_id}' has subject '{subject}' — expected it to contain 'Pragmatic Engineer'"

    if email.get("isRead") is not True:
        return False, f"Email '{target_id}' ('{subject}') is not read — expected isRead == True"

    return True, f"Email '{target_id}' ('{subject}') is marked as read."
