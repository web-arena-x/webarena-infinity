import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Desktop 'Project updates' setting is enabled."""
    try:
        resp = requests.get(f"{server_url}/api/state", timeout=5)
        resp.raise_for_status()
        state = resp.json()
    except Exception as e:
        return False, f"Failed to fetch state: {e}"

    channel = next((c for c in state["notificationChannels"] if c["id"] == "notif_desktop"), None)
    if not channel:
        return False, "Desktop notification channel not found."

    setting = next((s for s in channel["settings"] if s["id"] == "desktop_project_update"), None)
    if not setting:
        return False, "Desktop 'Project updates' setting not found."

    if setting["enabled"] is not True:
        return False, f"desktop_project_update enabled is {setting['enabled']}, expected True."

    return True, "Desktop 'Project updates' setting is enabled."
