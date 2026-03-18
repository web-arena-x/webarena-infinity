import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    app_passwords = state.get("appPasswords", [])

    if len(app_passwords) != 4:
        return False, f"Expected 4 app passwords, got {len(app_passwords)}."

    matching = [ap for ap in app_passwords if ap.get("name") == "Calendar Sync App"]
    if not matching:
        return False, "No app password found with name 'Calendar Sync App'."

    return True, "App password 'Calendar Sync App' successfully created. Total count is 4."
