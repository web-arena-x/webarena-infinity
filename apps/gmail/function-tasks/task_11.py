import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"]
         if e["subject"] == "Quarterly Team Dinner"
         and e["from"]["email"] == "sarah.chen@techcorp.io"),
        None,
    )
    if not email:
        return False, "Email 'Quarterly Team Dinner' from Sarah Chen not found."

    if not email["isMuted"]:
        return False, "Email is not muted."

    if not email["isArchived"]:
        return False, "Email is not archived (muting should archive)."

    if "INBOX" in email["labels"]:
        return False, "Email is still in the Inbox."

    return True, "Conversation 'Quarterly Team Dinner' has been muted."
