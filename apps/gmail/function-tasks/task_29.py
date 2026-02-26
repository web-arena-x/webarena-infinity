import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"]
         if "Congratulations" in e["subject"] and "won" in e["subject"]),
        None,
    )
    if not email:
        return False, "Email 'Congratulations! You won $10,000!' not found."

    if email["isTrashed"]:
        return False, "Email is still in Trash."

    if "INBOX" not in email["labels"]:
        return False, "Email is not in the Inbox."

    return True, "Email 'Congratulations! You won $10,000!' moved from Trash to Inbox."
