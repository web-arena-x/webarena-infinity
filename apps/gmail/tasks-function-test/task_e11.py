import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    button_labels = settings.get("buttonLabels")

    if button_labels == "text":
        return True, "Task completed successfully."
    else:
        return False, f"Button labels are not set to 'text' (buttonLabels='{button_labels}')."
