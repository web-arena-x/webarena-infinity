import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"] if e["subject"] == "Volunteer Event: Spring Health Fair"),
        None,
    )
    if not email:
        return False, "Email 'Volunteer Event: Spring Health Fair' not found."

    if not email["isArchived"]:
        return False, "Email 'Volunteer Event: Spring Health Fair' is not archived."

    if "INBOX" in email["labels"]:
        return False, "Email 'Volunteer Event: Spring Health Fair' is still in the Inbox."

    return True, "Email 'Volunteer Event: Spring Health Fair' has been archived."
