import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'Zendesk' authorized application was revoked."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    apps = state.get("authorizedApps", [])

    zendesk = [a for a in apps if a.get("name") == "Zendesk"]
    if zendesk:
        return False, "Zendesk authorized application still exists."

    return True, "Zendesk authorized application access successfully revoked."
