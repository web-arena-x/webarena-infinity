import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    protected = state.get("store", {}).get("passwordProtected")
    if protected != True:
        return False, f"Password protection is not enabled (passwordProtected={protected})."
    return True, "Password protection enabled."
