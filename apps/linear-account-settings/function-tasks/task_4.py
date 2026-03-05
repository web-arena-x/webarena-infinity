import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    connected = state.get("connectedAccounts", [])
    for account in connected:
        if account.get("provider") == "Google":
            return False, "Google account is still connected."

    return True, "Google account has been disconnected."
