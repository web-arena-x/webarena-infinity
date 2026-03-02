import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Desktop 'SLA breach warnings' setting is disabled."""
    try:
        resp = requests.get(f"{server_url}/api/state", timeout=5)
        resp.raise_for_status()
        state = resp.json()
    except Exception as e:
        return False, f"Failed to fetch state: {e}"

    channel = next((c for c in state["notificationChannels"] if c["id"] == "notif_desktop"), None)
    if not channel:
        return False, "Desktop notification channel not found."

    setting = next((s for s in channel["settings"] if s["id"] == "desktop_sla_breach"), None)
    if not setting:
        return False, "Desktop 'SLA breach warnings' setting not found."

    if setting["enabled"] is not False:
        return False, f"desktop_sla_breach enabled is {setting['enabled']}, expected False."

    return True, "Desktop 'SLA breach warnings' setting is disabled."
