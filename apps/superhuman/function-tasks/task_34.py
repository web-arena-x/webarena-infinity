import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    general = settings.get("general", {})
    desktop_notifications = general.get("desktopNotifications")

    if desktop_notifications is False:
        return True, "Desktop notifications successfully disabled."

    return False, (
        f"desktopNotifications is {desktop_notifications}, expected False."
    )
