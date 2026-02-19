import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    page = next((p for p in state["pages"] if p["name"] == "Style Guide Blog"), None)
    if not page:
        return False, "Page 'Style Guide Blog' not found."
    if page.get("monitored") != False:
        return False, f"Page is still monitored (monitored={page.get('monitored')})."
    return True, "Monitoring paused for 'Style Guide Blog'."
