import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    labels = state.get("labels", [])
    has_pending_response = False
    has_waiting_for_reply = False

    for label in labels:
        name = label.get("name", "")
        if name == "Pending Response":
            has_pending_response = True
        if name == "Waiting For Reply":
            has_waiting_for_reply = True

    if has_pending_response and not has_waiting_for_reply:
        return True, "Task completed successfully."
    elif not has_pending_response and has_waiting_for_reply:
        return False, "Label 'Waiting For Reply' still exists and 'Pending Response' not found."
    elif has_pending_response and has_waiting_for_reply:
        return False, "Both 'Pending Response' and 'Waiting For Reply' labels exist. 'Waiting For Reply' should have been renamed."
    else:
        return False, "Neither 'Pending Response' nor 'Waiting For Reply' label found."
