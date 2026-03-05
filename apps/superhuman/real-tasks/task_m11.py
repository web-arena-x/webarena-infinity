"""Task M11: Archive the Figma comment email from Sofia."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails = state.get("emails", [])
    target = None
    for email in emails:
        if email.get("id") == "email_042":
            target = email
            break

    if target is None:
        return False, "Could not find email_042 (Figma comment: 'This looks off — can you check?')"

    folder = target.get("folder")
    if folder == "done":
        return True, "email_042 is archived (folder='done')"
    return False, f"email_042 is not archived, folder='{folder}' (expected 'done')"
