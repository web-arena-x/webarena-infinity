import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    instafeed = next((a for a in state["apps"] if a["name"] == "Instafeed Instagram Feed"), None)
    if not instafeed:
        return False, "App 'Instafeed Instagram Feed' not found."
    if instafeed.get("installed") != False:
        return False, "App 'Instafeed Instagram Feed' is still installed."
    lucky = next((a for a in state["apps"] if a["name"] == "Lucky Orange Analytics"), None)
    if not lucky:
        return False, "App 'Lucky Orange Analytics' not found."
    if lucky.get("installed") != False:
        return False, "App 'Lucky Orange Analytics' is still installed."
    return True, "Both apps uninstalled successfully."
