import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    if state["currentUser"]["email"] != "alex.chen@acmetech.io":
        return False, f"Expected email 'alex.chen@acmetech.io', got '{state['currentUser']['email']}'."

    return True, "Email changed to 'alex.chen@acmetech.io'."
