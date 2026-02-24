import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    blocked_senders = state.get("blockedSenders", [])

    if "annoying@daily-deals.biz" not in blocked_senders:
        return True, "Task completed successfully."
    else:
        return False, "'annoying@daily-deals.biz' is still in blockedSenders list."
