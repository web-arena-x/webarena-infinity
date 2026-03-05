"""Task M6: Disable the Newsletters auto label."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    auto_labels = state.get("autoLabels", [])
    for entry in auto_labels:
        if entry.get("id") == "autolabel_newsletters":
            if entry.get("isEnabled") is False:
                return True, "Newsletters auto label (autolabel_newsletters) is disabled"
            return False, f"Newsletters auto label is still enabled: isEnabled={entry.get('isEnabled')}"

    return False, "Could not find autolabel_newsletters in state['autoLabels']"
