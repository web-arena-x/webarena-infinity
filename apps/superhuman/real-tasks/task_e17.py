"""Task E17: Star Elena's SOC 2 audit prep email."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_id = "email_125"
    target_subject = "Action required: SOC 2 Type II audit prep"

    emails = state.get("emails", [])
    email = next((e for e in emails if e["id"] == target_id), None)
    if email is None:
        return False, f"Email '{target_id}' not found (expected subject: '{target_subject}')"

    if email.get("isStarred") is not True:
        return False, f"Email '{target_id}' ('{email.get('subject', '')}') is not starred — expected isStarred == True"

    return True, f"Email '{target_id}' ('{target_subject}') is starred."
