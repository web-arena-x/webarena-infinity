import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    opt = next((o for o in state["optimizations"] if o["title"] == "Compress hero banner image on homepage"), None)
    if not opt:
        return False, "Optimization 'Compress hero banner image on homepage' not found."
    if opt.get("status") != "completed":
        return False, f"Expected status 'completed', got '{opt.get('status')}'."
    return True, "Optimization marked as completed."
