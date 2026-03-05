import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    general = settings.get("general", {})
    sound_notifications = general.get("soundNotifications")

    if sound_notifications is True:
        return True, "Sound notifications successfully enabled."

    return False, (
        f"soundNotifications is {sound_notifications}, expected True."
    )
