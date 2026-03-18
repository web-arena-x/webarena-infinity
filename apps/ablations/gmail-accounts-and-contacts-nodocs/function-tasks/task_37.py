import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    app_passwords = state.get("appPasswords", [])

    matching = [ap for ap in app_passwords if ap.get("name") == "Thunderbird on MacBook"]
    if matching:
        return False, "App password 'Thunderbird on MacBook' still exists. Expected it to be revoked."

    return True, "App password 'Thunderbird on MacBook' successfully revoked."
