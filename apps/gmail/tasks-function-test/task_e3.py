import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    blocked_senders = state.get("blockedSenders", [])
    target_email = "carlos.m@logisticspro.net"

    for sender in blocked_senders:
        if sender.get("email") == target_email:
            return True, "Task completed successfully."

    return False, f"Email address '{target_email}' not found in blockedSenders list."
