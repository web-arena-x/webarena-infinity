import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    roles = state["currentUser"]["careerInterests"]["roles"]
    if "Frontend Developer" in roles:
        return True, "Frontend Developer added to roles."
    return False, f"Frontend Developer not in roles. Current: {roles}."
