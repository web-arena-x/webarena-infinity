import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    auto_labels = state.get("autoLabels", [])

    for al in auto_labels:
        if al.get("name") == "Design Review":
            if al.get("type") != "custom":
                return False, f"Auto Label 'Design Review' has type '{al.get('type')}', expected 'custom'."
            if al.get("enabled") is not True:
                return False, f"Auto Label 'Design Review' is not enabled."
            criteria = al.get("criteria", {})
            from_val = criteria.get("from", "")
            if "@designhub.io" not in from_val:
                return False, f"Auto Label 'Design Review' criteria.from is '{from_val}', expected it to contain '@designhub.io'."
            return True, "Custom Auto Label 'Design Review' created correctly with from criteria '@designhub.io'."

    return False, "No Auto Label named 'Design Review' found."
