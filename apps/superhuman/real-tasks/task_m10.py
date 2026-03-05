"""Task M10: Turn off split inbox."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    settings = state.get("settings", {})
    split_inbox = settings.get("splitInbox", {})
    enabled = split_inbox.get("enabled")

    if enabled is False:
        return True, "Split inbox is disabled (settings.splitInbox.enabled == False)"
    return False, f"Split inbox is still enabled: settings.splitInbox.enabled={enabled}"
