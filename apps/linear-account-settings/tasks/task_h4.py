import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify Figma connected account disconnected AND Figma authorized app revoked."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check connected accounts
    accounts = state.get("connectedAccounts", [])
    figma_account = [a for a in accounts if a.get("provider") == "Figma"]
    if figma_account:
        return False, "Figma connected account still exists."

    # Check authorized apps
    apps = state.get("authorizedApps", [])
    figma_app = [a for a in apps if a.get("name") == "Figma"]
    if figma_app:
        return False, "Figma authorized application still exists."

    return True, "Figma connected account disconnected and authorized app revoked."
