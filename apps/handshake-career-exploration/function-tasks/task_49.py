import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    locations = state["currentUser"]["careerInterests"]["locations"]
    if "Austin, TX" not in locations:
        return True, "Austin, TX removed from locations."
    return False, f"Austin, TX still in locations. Current: {locations}."
