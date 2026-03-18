import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    delegates = state.get("delegates", [])

    for d in delegates:
        if d.get("email") == "jennifer.walsh@techcorp.io":
            if d.get("status") != "pending":
                return False, f"Delegate with email 'jennifer.walsh@techcorp.io' found but status is '{d.get('status')}', expected 'pending'."
            return True, "Delegate 'jennifer.walsh@techcorp.io' exists with status 'pending'."

    return False, "No delegate found with email 'jennifer.walsh@techcorp.io'."
