import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the 'testing' label
    target_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "testing":
            target_label = lbl
            break
    if target_label is None:
        return False, "Could not find label 'testing'."

    if target_label.get("description") != "Quality assurance and test automation":
        return False, f"Label description is '{target_label.get('description')}', expected 'Quality assurance and test automation'."

    if target_label.get("color") != "#0e8a16":
        return False, f"Label color is '{target_label.get('color')}', expected '#0e8a16'."

    return True, "Label 'testing' updated with new description and color #0e8a16."
