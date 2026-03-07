import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    roles = state["currentUser"]["careerInterests"]["roles"]
    if "UX Designer" not in roles:
        return True, "UX Designer removed from roles."
    return False, f"UX Designer still in roles. Current: {roles}."
