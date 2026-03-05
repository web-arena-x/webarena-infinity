"""Task M5: Archive Nathan Brooks' introduction email with Yuki Tanaka."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails = state.get("emails", [])
    target = None
    for email in emails:
        if email.get("id") == "email_013":
            target = email
            break

    if target is None:
        return False, "Could not find email_013 (Introduction: Alex Morgan ↔ Yuki Tanaka)"

    folder = target.get("folder")
    if folder == "done":
        return True, "email_013 is archived (folder='done')"
    return False, f"email_013 is not archived, folder='{folder}' (expected 'done')"
