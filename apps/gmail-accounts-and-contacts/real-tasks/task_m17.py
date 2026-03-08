# Task: Disable auto-save and show contact info.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    settings = state.get("accountSettings", {})

    auto_save = settings.get("autoSaveContacts")
    if auto_save is not False:
        errors.append(f"Expected autoSaveContacts to be false, got {auto_save}")

    show_contact_info = settings.get("collaborationSettings", {}).get("showContactInfo")
    if show_contact_info is not False:
        errors.append(f"Expected collaborationSettings.showContactInfo to be false, got {show_contact_info}")

    if errors:
        return False, "; ".join(errors)
    return True, "Auto-save contacts and show contact info both disabled."
