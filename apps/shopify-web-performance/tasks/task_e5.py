import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    match = [r for r in state["savedReports"] if r["name"] == "Product Page CLS Report"]
    if match:
        return False, "Saved report 'Product Page CLS Report' still exists."
    return True, "Saved report 'Product Page CLS Report' deleted."
