import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that 'promos@cheapdeals.biz' has been removed from blocked senders."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    blocked_senders = state.get("blockedSenders", [])
    blocked_emails = [s.get("email", "") for s in blocked_senders]

    target = "promos@cheapdeals.biz"
    if target not in blocked_emails:
        return True, f"'{target}' is not in the blocked senders list (successfully unblocked)."
    return False, f"'{target}' is still in the blocked senders list. Current blocked: {blocked_emails!r}."
