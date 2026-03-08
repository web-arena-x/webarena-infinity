# Task: Turn off linked service notifications.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    notifications = state.get("accountSettings", {}).get("notificationSettings", {})
    linked_updates = notifications.get("linkedServiceUpdates")

    if linked_updates is False:
        return True, "Linked service update notifications are now disabled."
    else:
        return False, f"linkedServiceUpdates is {linked_updates}, expected false."
