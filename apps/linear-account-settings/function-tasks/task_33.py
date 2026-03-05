import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Mobile 'Status changes on subscribed issues' setting is enabled."""
    try:
        resp = requests.get(f"{server_url}/api/state", timeout=5)
        resp.raise_for_status()
        state = resp.json()
    except Exception as e:
        return False, f"Failed to fetch state: {e}"

    channel = next((c for c in state["notificationChannels"] if c["id"] == "notif_mobile"), None)
    if not channel:
        return False, "Mobile notification channel not found."

    setting = next((s for s in channel["settings"] if s["id"] == "mobile_issue_status"), None)
    if not setting:
        return False, "Mobile 'Status changes' setting not found."

    if setting["enabled"] is not True:
        return False, f"mobile_issue_status enabled is {setting['enabled']}, expected True."

    return True, "Mobile 'Status changes' setting is enabled."
