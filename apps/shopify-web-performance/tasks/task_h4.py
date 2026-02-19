import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    app = next((a for a in state["apps"] if a["name"] == "Google Tag Manager"), None)
    if not app:
        return False, "App 'Google Tag Manager' not found."
    if not app.get("installed"):
        return False, "App 'Google Tag Manager' is not installed."
    settings = app.get("settings", {})
    if settings.get("containerId") != "GTM-W8X3K9P":
        return False, f"Expected container ID 'GTM-W8X3K9P', got '{settings.get('containerId')}'."
    if settings.get("deferLoading") != True:
        return False, f"Defer loading should be enabled (got {settings.get('deferLoading')})."
    return True, "Google Tag Manager installed and configured correctly."
