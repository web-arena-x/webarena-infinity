import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    blocked = [b["email"] for b in state.get("blockedSenders", [])]
    if "omar.ar@consulting.group" not in blocked:
        return False, "Email 'omar.ar@consulting.group' is not in the blocked senders list."

    return True, "Email address 'omar.ar@consulting.group' has been blocked."
