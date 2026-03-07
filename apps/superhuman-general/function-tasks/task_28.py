import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state["settings"]

    desktop = settings.get("notifications", {}).get("desktop")
    if desktop is False:
        return True, "Desktop notifications have been disabled."
    return False, f"Desktop notifications is {desktop}, expected False."
