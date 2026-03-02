import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Email 'Project updates' setting is disabled."""
    try:
        resp = requests.get(f"{server_url}/api/state", timeout=5)
        resp.raise_for_status()
        state = resp.json()
    except Exception as e:
        return False, f"Failed to fetch state: {e}"

    channel = next((c for c in state["notificationChannels"] if c["id"] == "notif_email"), None)
    if not channel:
        return False, "Email notification channel not found."

    setting = next((s for s in channel["settings"] if s["id"] == "email_project_update"), None)
    if not setting:
        return False, "Email 'Project updates' setting not found."

    if setting["enabled"] is not False:
        return False, f"email_project_update enabled is {setting['enabled']}, expected False."

    return True, "Email 'Project updates' setting is disabled."
