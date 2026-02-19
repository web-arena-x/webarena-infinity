import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    refresh = next((t for t in state["themes"] if t["name"] == "Refresh"), None)
    if not refresh:
        return False, "Theme 'Refresh' not found."
    if not refresh.get("active"):
        return False, "Theme 'Refresh' is not active."
    dawn = next((t for t in state["themes"] if t["name"] == "Dawn"), None)
    if dawn and dawn.get("active"):
        return False, "Theme 'Dawn' is still active (should be deactivated)."
    return True, "Theme 'Refresh' activated successfully."
