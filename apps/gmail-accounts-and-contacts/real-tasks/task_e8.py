# Task: Turn on contact changes notifications.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    notifications = state.get("accountSettings", {}).get("notificationSettings", {})
    contact_changes = notifications.get("contactChanges")

    if contact_changes is True:
        return True, "Contact changes notifications are now enabled."
    else:
        return False, f"contactChanges is {contact_changes}, expected true."
