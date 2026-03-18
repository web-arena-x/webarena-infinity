import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    app_passwords = state.get("appPasswords", [])
    for ap in app_passwords:
        if ap.get("name") == "Mail on iPhone":
            return False, "The app password 'Mail on iPhone' still exists."

    return True, "The app password 'Mail on iPhone' has been successfully revoked."
