"""Task E15: Unblock the sender promos@cheapdeals.biz."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_email = "promos@cheapdeals.biz"

    blocked_senders = state.get("blockedSenders", [])

    # Check if the target email is still in the blocked senders list
    for entry in blocked_senders:
        sender_email = entry if isinstance(entry, str) else entry.get("email", "")
        if sender_email == target_email:
            return False, f"'{target_email}' is still in blockedSenders — expected it to be removed"

    return True, f"'{target_email}' is not in blockedSenders (unblocked)."
