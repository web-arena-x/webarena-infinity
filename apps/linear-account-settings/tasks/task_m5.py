import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'GitLab' connected account was disconnected."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    accounts = state.get("connectedAccounts", [])

    gitlab = [a for a in accounts if a.get("provider") == "GitLab"]
    if gitlab:
        return False, "GitLab connected account still exists."

    return True, "GitLab connected account successfully disconnected."
