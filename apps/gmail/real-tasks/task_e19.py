"""
Task: Unblock the sender annoying@daily-deals.biz.
Verify: No entry in state["blockedSenders"] has email=='annoying@daily-deals.biz'.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    blocked_senders = state.get("blockedSenders", [])

    blocked_emails = [s.get("email") for s in blocked_senders]
    if "annoying@daily-deals.biz" in blocked_emails:
        return False, (
            "Sender 'annoying@daily-deals.biz' is still in the blocked senders list. "
            f"blockedSenders emails={blocked_emails}"
        )

    return True, "Sender 'annoying@daily-deals.biz' has been unblocked."
