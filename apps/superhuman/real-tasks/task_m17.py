"""Task M17: Move the v2 API launch go/no-go email from Done back to the inbox."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails = state.get("emails", [])
    target = None
    for email in emails:
        if email.get("id") == "email_046":
            target = email
            break

    if target is None:
        return False, "Could not find email_046 (Re: v2 API launch plan — go/no-go decision)"

    folder = target.get("folder")
    if folder == "inbox":
        return True, "email_046 is in the inbox (folder='inbox')"
    return False, f"email_046 folder is '{folder}', expected 'inbox'"
