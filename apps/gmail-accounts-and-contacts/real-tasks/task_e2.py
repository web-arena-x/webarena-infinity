# Task: Turn off auto-save contacts.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    account_settings = state.get("accountSettings", {})
    auto_save = account_settings.get("autoSaveContacts")

    if auto_save is False:
        return True, "Auto-save contacts is now disabled."
    else:
        return False, f"autoSaveContacts is {auto_save}, expected false."
