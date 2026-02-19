import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'Monitoring Dashboard' API key was revoked."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    keys = state.get("apiKeys", [])

    monitoring_key = [k for k in keys if k.get("label") == "Monitoring Dashboard"]
    if monitoring_key:
        return False, "API key 'Monitoring Dashboard' still exists."

    return True, "API key 'Monitoring Dashboard' successfully revoked."
