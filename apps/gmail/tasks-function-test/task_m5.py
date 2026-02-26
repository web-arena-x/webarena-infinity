import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    labels = state.get("labels", [])
    ref_label = None
    for label in labels:
        if label.get("name", "").lower() == "reference":
            ref_label = label
            break

    if not ref_label:
        return False, "Could not find label with name 'Reference'."

    visible = ref_label.get("visible")
    if visible is False:
        return True, "Task completed successfully."

    return False, f"Label 'Reference' has visible={visible}, expected False."
