"""
Task M7: Block the sender of the '$5,000,000 inheritance' email in the trash.
Check that 'prince.of.lagos@hotmail.com' appears in state["blockedSenders"] (check the email field).
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    blocked_senders = state.get("blockedSenders", [])

    target_email = "prince.of.lagos@hotmail.com"

    for sender in blocked_senders:
        if isinstance(sender, dict):
            if sender.get("email") == target_email:
                return True, f"'{target_email}' is in the blocked senders list."
        elif isinstance(sender, str):
            if sender == target_email:
                return True, f"'{target_email}' is in the blocked senders list."

    return False, (
        f"'{target_email}' not found in blocked senders. "
        f"Current blocked senders: {blocked_senders}"
    )
