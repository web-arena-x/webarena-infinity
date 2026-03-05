"""Task E4: Remove the star from Marcus Williams' production outage email."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_id = "email_004"
    target_subject = "Urgent: Production outage — payment service down (P0)"

    emails = state.get("emails", [])
    email = next((e for e in emails if e["id"] == target_id), None)
    if email is None:
        return False, f"Email '{target_id}' not found (expected subject: '{target_subject}')"

    if email.get("isStarred") is not False:
        return False, f"Email '{target_id}' ('{email.get('subject', '')}') is still starred — expected isStarred == False"

    return True, f"Email '{target_id}' ('{target_subject}') is no longer starred."
