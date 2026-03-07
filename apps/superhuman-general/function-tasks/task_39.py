import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state["settings"]

    swipe_right = settings.get("swipeRight")
    if swipe_right == "star":
        return True, "Swipe right action changed to 'Star'."
    return False, f"Swipe right action is '{swipe_right}', expected 'star'."
