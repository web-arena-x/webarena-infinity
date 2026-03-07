import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    actual = state["currentUser"].get("profileVisibility", "")
    if actual == "Employers":
        return True, "Profile visibility set to Employers."
    return False, f"Profile visibility is '{actual}', expected 'Employers'."
