import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state["settings"]

    mode = settings.get("autoReminders", {}).get("mode")
    if mode == "external":
        return True, "Auto Reminder mode changed to 'All external'."
    return False, f"Auto Reminder mode is '{mode}', expected 'external'."
