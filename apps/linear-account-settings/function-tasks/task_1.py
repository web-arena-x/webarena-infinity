import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    if state["currentUser"]["fullName"] != "Alex Chen":
        return False, f"Expected full name 'Alex Chen', got '{state['currentUser']['fullName']}'."

    return True, "Full name changed to 'Alex Chen'."
