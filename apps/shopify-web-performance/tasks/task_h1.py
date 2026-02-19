import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    # Check app is uninstalled
    app = next((a for a in state["apps"] if a["name"] == "Privy Pop Ups"), None)
    if not app:
        return False, "App 'Privy Pop Ups' not found in state."
    if app.get("installed") != False:
        return False, "App 'Privy Pop Ups' is still installed."
    # Check event exists
    event = next((e for e in state["events"] if e["title"] == "Uninstalled Privy Pop Ups"), None)
    if not event:
        return False, "Event 'Uninstalled Privy Pop Ups' not found."
    if event.get("type") != "app_uninstalled":
        return False, f"Expected event type 'app_uninstalled', got '{event.get('type')}'."
    if event.get("metric") != "cls":
        return False, f"Expected metric 'cls', got '{event.get('metric')}'."
    if event.get("impact") != "positive":
        return False, f"Expected impact 'positive', got '{event.get('impact')}'."
    return True, "Privy Pop Ups uninstalled and event annotation added correctly."
