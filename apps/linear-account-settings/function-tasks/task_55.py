import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    api_keys = state.get("apiKeys", [])

    for key in api_keys:
        if key.get("label") == "Personal Scripts":
            return False, "API key 'Personal Scripts' still exists in apiKeys."

    return True, "API key 'Personal Scripts' has been removed."
