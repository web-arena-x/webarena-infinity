import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that 'alerts@domainrenewal-notice.info' has been added to blocked senders."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    blocked_senders = state.get("blockedSenders", [])
    blocked_emails = [s.get("email", "") for s in blocked_senders]

    target = "alerts@domainrenewal-notice.info"
    if target in blocked_emails:
        return True, f"'{target}' is in the blocked senders list."
    return False, f"'{target}' not found in blocked senders. Current blocked: {blocked_emails!r}."
