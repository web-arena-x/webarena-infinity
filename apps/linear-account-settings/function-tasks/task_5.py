import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    connected = state.get("connectedAccounts", [])
    for account in connected:
        if account.get("provider") == "GitHub":
            return False, "GitHub account is still connected."

    return True, "GitHub account has been disconnected."
