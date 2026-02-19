import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    match = [e for e in state["events"] if e["title"] == "Valentines Day sale ended"]
    if match:
        return False, "Event 'Valentines Day sale ended' still exists."
    return True, "Event 'Valentines Day sale ended' removed."
