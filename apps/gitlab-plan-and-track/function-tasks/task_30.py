import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    target = next((l for l in labels if l.get("title") == "deployment"), None)
    if not target:
        return False, "Label with title 'deployment' not found."

    color = target.get("color", "")
    if color.lower() != "#ff5733":
        return False, f"Label color is '{color}', expected '#ff5733'."

    label_type = target.get("type", "")
    if label_type != "project":
        return False, f"Label type is '{label_type}', expected 'project'."

    return True, "Label 'deployment' exists with color '#ff5733' and type 'project'."
