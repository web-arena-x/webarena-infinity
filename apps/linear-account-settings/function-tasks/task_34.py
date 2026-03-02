import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Mobile 'Issue assigned to you' setting is disabled."""
    try:
        resp = requests.get(f"{server_url}/api/state", timeout=5)
        resp.raise_for_status()
        state = resp.json()
    except Exception as e:
        return False, f"Failed to fetch state: {e}"

    channel = next((c for c in state["notificationChannels"] if c["id"] == "notif_mobile"), None)
    if not channel:
        return False, "Mobile notification channel not found."

    setting = next((s for s in channel["settings"] if s["id"] == "mobile_issue_assigned"), None)
    if not setting:
        return False, "Mobile 'Issue assigned to you' setting not found."

    if setting["enabled"] is not False:
        return False, f"mobile_issue_assigned enabled is {setting['enabled']}, expected False."

    return True, "Mobile 'Issue assigned to you' setting is disabled."
