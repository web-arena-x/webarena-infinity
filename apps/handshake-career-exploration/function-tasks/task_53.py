import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    industries = state["currentUser"]["careerInterests"]["industries"]
    if "Finance" not in industries:
        return True, "Finance removed from industries."
    return False, f"Finance still in industries. Current: {industries}."
