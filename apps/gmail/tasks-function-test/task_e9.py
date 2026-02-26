import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    dynamic_email = settings.get("dynamicEmail")

    if dynamic_email is False:
        return True, "Task completed successfully."
    else:
        return False, f"Dynamic email is not disabled (dynamicEmail={dynamic_email})."
