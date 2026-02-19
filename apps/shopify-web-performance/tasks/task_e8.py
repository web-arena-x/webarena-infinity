import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    opt = next((o for o in state["optimizations"] if o["title"] == "Defer Klaviyo popup script loading"), None)
    if not opt:
        return False, "Optimization 'Defer Klaviyo popup script loading' not found."
    if opt.get("status") != "dismissed":
        return False, f"Expected status 'dismissed', got '{opt.get('status')}'."
    return True, "Optimization dismissed."
