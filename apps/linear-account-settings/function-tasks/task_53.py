import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    api_keys = state.get("apiKeys", [])

    for key in api_keys:
        if key.get("label") == "Data Export Script":
            return True, "API key 'Data Export Script' exists in apiKeys."

    return False, "API key 'Data Export Script' not found in apiKeys."
