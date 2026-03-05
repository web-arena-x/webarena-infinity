"""Task M2: Create a new label called 'Board Prep'."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    labels = state.get("labels", [])
    for label in labels:
        if label.get("name") == "Board Prep":
            return True, f"Label 'Board Prep' found with id '{label.get('id')}'"

    label_names = [l.get("name") for l in labels]
    return False, f"Label 'Board Prep' not found in labels: {label_names}"
