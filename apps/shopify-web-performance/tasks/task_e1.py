import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    name = state.get("store", {}).get("name")
    if name != "Urban Threads Boutique":
        return False, f"Expected store name 'Urban Threads Boutique', got '{name}'."
    return True, "Store name changed to 'Urban Threads Boutique'."
