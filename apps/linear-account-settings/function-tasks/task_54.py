import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    api_keys = state.get("apiKeys", [])

    for key in api_keys:
        if key.get("label") == "Staging Environment":
            return False, "API key 'Staging Environment' still exists in apiKeys."

    return True, "API key 'Staging Environment' has been removed."
