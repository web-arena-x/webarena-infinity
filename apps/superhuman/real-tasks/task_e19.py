"""Task E19: Turn on sound notifications."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    try:
        sound_notifs = state["settings"]["general"]["soundNotifications"]
    except (KeyError, TypeError) as e:
        return False, f"Could not read settings.general.soundNotifications: {e}"

    if sound_notifs is not True:
        return False, f"soundNotifications is {sound_notifs} — expected True"

    return True, "Sound notifications are turned on."
