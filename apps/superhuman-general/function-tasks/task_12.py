import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    design_label = next((l for l in labels if l["name"] == "Design"), None)
    if design_label is None:
        return False, "No label named 'Design' found in state."

    if design_label.get("type") != "user":
        return False, f"Label 'Design' exists but has type '{design_label.get('type')}' instead of 'user'."

    return True, "Label 'Design' created successfully with type 'user'."
