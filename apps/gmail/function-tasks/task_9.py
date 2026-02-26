import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"]
         if e["subject"] == "Your recommendations: Tech deals of the week"),
        None,
    )
    if not email:
        return False, "Email 'Your recommendations: Tech deals of the week' not found."

    if not email["isSpam"]:
        return False, "Email is not marked as spam."

    if "INBOX" in email["labels"]:
        return False, "Email is still in the Inbox."

    return True, "Email 'Your recommendations: Tech deals of the week' has been reported as spam."
