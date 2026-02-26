import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    blocked = [b["email"] for b in state.get("blockedSenders", [])]
    if "spam@marketing-blast.com" in blocked:
        return False, "Email 'spam@marketing-blast.com' is still in the blocked senders list."

    return True, "Email address 'spam@marketing-blast.com' has been unblocked."
