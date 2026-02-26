import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"] if e["subject"] == "Design System Update v4.2"),
        None,
    )
    if not email:
        return False, "Email 'Design System Update v4.2' not found."

    if not email["isTrashed"]:
        return False, "Email 'Design System Update v4.2' is not in Trash."

    if "INBOX" in email["labels"]:
        return False, "Email 'Design System Update v4.2' is still in the Inbox."

    return True, "Email 'Design System Update v4.2' has been moved to Trash."
