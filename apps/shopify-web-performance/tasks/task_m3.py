import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    app = next((a for a in state["apps"] if a["name"] == "Yotpo Reviews & UGC"), None)
    if not app:
        return False, "App 'Yotpo Reviews & UGC' not found."
    if not app.get("installed"):
        return False, "App 'Yotpo Reviews & UGC' is not installed."
    if app.get("status") != "active":
        return False, f"Expected status 'active', got '{app.get('status')}'."
    return True, "App 'Yotpo Reviews & UGC' installed."
