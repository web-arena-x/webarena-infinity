import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    target = next((l for l in labels if l.get("title") == "environment::production"), None)
    if not target:
        return False, "Label with title 'environment::production' not found."

    if target.get("scoped") is not True:
        return False, f"Label scoped is {target.get('scoped')}, expected True."

    color = target.get("color", "")
    if color.lower() != "#cc0000":
        return False, f"Label color is '{color}', expected '#cc0000'."

    label_type = target.get("type", "")
    if label_type != "group":
        return False, f"Label type is '{label_type}', expected 'group'."

    return True, "Label 'environment::production' exists with scoped=True, color '#cc0000', and type 'group'."
