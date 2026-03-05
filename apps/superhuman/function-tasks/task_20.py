import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    # Get Me To Zero: all inbox emails should be archived (moved to done)
    # Drafts and scheduled emails in inbox are excluded from this check
    inbox_emails = [
        e for e in emails
        if e.get("folder") == "inbox"
        and not e.get("isDraft", False)
        and not e.get("isScheduled", False)
    ]

    if len(inbox_emails) > 0:
        subjects = [e.get("subject", "unknown") for e in inbox_emails[:5]]
        return False, f"Found {len(inbox_emails)} non-draft/non-scheduled emails still in inbox. Examples: {subjects}"

    return True, "Inbox is empty (Get Me To Zero completed). All non-draft/non-scheduled emails archived."
