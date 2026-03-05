"""Task H9: Disable every auto label and turn off split inbox."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Check all auto labels are disabled
    auto_labels = state.get("autoLabels", [])
    if not auto_labels:
        return False, "No autoLabels found in state."

    enabled_labels = []
    for al in auto_labels:
        if al.get("isEnabled") is not False:
            enabled_labels.append(f"{al.get('id', '?')} (isEnabled={al.get('isEnabled')})")

    if enabled_labels:
        return False, f"Some auto labels still enabled: {'; '.join(enabled_labels)}"

    # Check split inbox is disabled
    settings = state.get("settings", {})
    split_inbox = settings.get("splitInbox", {})
    if split_inbox.get("enabled") is not False:
        return False, f"Split inbox enabled is {split_inbox.get('enabled')}, expected False."

    return True, "All auto labels disabled and split inbox turned off."
