import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    position = settings.get("multipleInboxPosition")

    if position == "above":
        return True, "Task completed successfully."

    return False, (
        f"settings.multipleInboxPosition is '{position}', expected 'above'."
    )
