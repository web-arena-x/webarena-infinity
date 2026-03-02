import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    connected_accounts = state.get("connectedAccounts", [])

    for account in connected_accounts:
        if account.get("provider") == "GitLab":
            return False, "Connected account with provider 'GitLab' still exists in connectedAccounts."

    return True, "No connected account with provider 'GitLab' exists in connectedAccounts."
