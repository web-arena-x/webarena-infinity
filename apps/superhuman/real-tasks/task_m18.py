"""Task M18: Disable the Social auto label."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    auto_labels = state.get("autoLabels", [])
    for entry in auto_labels:
        if entry.get("id") == "autolabel_social":
            if entry.get("isEnabled") is False:
                return True, "Social auto label (autolabel_social) is disabled"
            return False, f"Social auto label is still enabled: isEnabled={entry.get('isEnabled')}"

    return False, "Could not find autolabel_social in state['autoLabels']"
