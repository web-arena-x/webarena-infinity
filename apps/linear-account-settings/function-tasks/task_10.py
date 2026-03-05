import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state["preferences"]["general"]["defaultHomeView"]
    if val != "Inbox":
        return False, f"Expected default home view 'Inbox', got '{val}'."

    return True, "Default home view set to 'Inbox'."
