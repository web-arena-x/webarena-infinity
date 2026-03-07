import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state["settings"]

    sound = settings.get("notifications", {}).get("sound")
    if sound is False:
        return True, "Sound notifications have been disabled."
    return False, f"Sound notifications is {sound}, expected False."
