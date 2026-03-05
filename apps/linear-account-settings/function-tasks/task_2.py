import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    if state["currentUser"]["username"] != "achen":
        return False, f"Expected username 'achen', got '{state['currentUser']['username']}'."

    return True, "Username changed to 'achen'."
