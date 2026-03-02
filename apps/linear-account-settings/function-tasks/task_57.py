import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    authorized_apps = state.get("authorizedApps", [])

    for app in authorized_apps:
        if app.get("name") == "Statuspage":
            return False, "Authorized app 'Statuspage' still exists in authorizedApps."

    return True, "Authorized app 'Statuspage' has been removed."
