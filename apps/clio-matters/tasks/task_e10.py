import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    notification_settings = state.get("notificationSettings")
    if notification_settings is None:
        return False, "No notificationSettings found in application state."

    matter_deletions = notification_settings.get("matter_deletions")
    if matter_deletions is not False:
        return False, f"matter_deletions is {matter_deletions}, expected False."

    return True, "Matter deletion notifications have been disabled."
