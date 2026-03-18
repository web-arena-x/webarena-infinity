import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    delegates = state.get("delegates", [])

    for d in delegates:
        if d.get("email") == "james.wu@techcorp.io":
            return False, "Delegate with email 'james.wu@techcorp.io' still exists. It should have been removed."

    return True, "Delegate 'james.wu@techcorp.io' has been successfully removed."
