import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that a new API key with label 'Staging Environment' was created."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    keys = state.get("apiKeys", [])

    staging_key = [k for k in keys if k.get("label") == "Staging Environment"]
    if not staging_key:
        return False, "API key 'Staging Environment' not found."

    return True, "API key 'Staging Environment' successfully created."
