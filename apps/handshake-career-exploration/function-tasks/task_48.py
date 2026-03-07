import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    locations = state["currentUser"]["careerInterests"]["locations"]
    if "Chicago, IL" in locations:
        return True, "Chicago, IL added to locations."
    return False, f"Chicago, IL not in locations. Current: {locations}."
