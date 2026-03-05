"""Task M7: Block the sender of the 'Make $5000/week from home' spam email."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    target_email = "info@wfh-earningsguide.com"
    blocked_senders = state.get("blockedSenders", [])

    for entry in blocked_senders:
        blocked_addr = entry.get("email") or entry.get("address") or ""
        if blocked_addr == target_email:
            return True, f"Sender '{target_email}' is in blockedSenders"

    # Also check if blockedSenders is a flat list of strings
    if target_email in blocked_senders:
        return True, f"Sender '{target_email}' is in blockedSenders"

    return False, f"Sender '{target_email}' not found in blockedSenders: {blocked_senders}"
