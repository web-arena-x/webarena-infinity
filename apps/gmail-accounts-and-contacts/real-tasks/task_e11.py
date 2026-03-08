# Task: Delete College Alumni label.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    labels = state.get("contactLabels", [])
    for label in labels:
        if label.get("name") == "College Alumni":
            return False, "Contact label 'College Alumni' still exists."

    return True, "College Alumni label has been deleted."
