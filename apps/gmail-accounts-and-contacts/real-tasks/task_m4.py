# Task: Rename Gym Buddies to Fitness and change color to #4285F4.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contact_labels = state.get("contactLabels", [])
    label = next((l for l in contact_labels if l.get("id") == "clabel_5"), None)

    if label is None:
        errors.append("Label with id 'clabel_5' not found")
    else:
        if label.get("name") != "Fitness":
            errors.append(f"Expected label name 'Fitness', got '{label.get('name')}'")
        if label.get("color") != "#4285F4":
            errors.append(f"Expected label color '#4285F4', got '{label.get('color')}'")

    if errors:
        return False, "; ".join(errors)
    return True, "Label 'Gym Buddies' renamed to 'Fitness' with color #4285F4."
