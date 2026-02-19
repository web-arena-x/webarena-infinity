import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    app = next((a for a in state["apps"] if a["name"] == "Hotjar Behavior Analytics"), None)
    if not app:
        return False, "App 'Hotjar Behavior Analytics' not found."
    if app.get("installed") != False:
        return False, f"App is still installed (installed={app.get('installed')})."
    return True, "Hotjar Behavior Analytics uninstalled successfully."
