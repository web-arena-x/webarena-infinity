"""Task E7: Turn off desktop notifications."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    try:
        desktop_notifs = state["settings"]["general"]["desktopNotifications"]
    except (KeyError, TypeError) as e:
        return False, f"Could not read settings.general.desktopNotifications: {e}"

    if desktop_notifs is not False:
        return False, f"desktopNotifications is {desktop_notifs} — expected False"

    return True, "Desktop notifications are turned off."
