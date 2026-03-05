"""Task M8: Rename the Read Later label to Bookmarks."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    labels = state.get("labels", [])
    for label in labels:
        if label.get("id") == "label_8":
            name = label.get("name")
            if name == "Bookmarks":
                return True, "label_8 has been renamed to 'Bookmarks'"
            return False, f"label_8 name is '{name}', expected 'Bookmarks'"

    return False, "Could not find label with id 'label_8' in state['labels']"
