import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    providers = state.get("providers", [])
    provider = None
    for prov in providers:
        if prov.get("id") == "prov_4":
            provider = prov
            break

    if provider is None:
        return False, "Provider prov_4 (Dr. Kim) not found."

    if provider.get("sharingDefault") != 3:
        return False, f"Dr. Kim's sharingDefault is {provider.get('sharingDefault')}, expected 3."

    if provider.get("notificationTimeframe") != "24_hours":
        return False, f"Dr. Kim's notificationTimeframe is '{provider.get('notificationTimeframe')}', expected '24_hours'."

    return True, "Dr. Kim's settings updated: sharing level 3, notification 24 hours."
