import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    actual = state["currentUser"]["careerInterests"]["careerCommunity"]
    if actual == "Business & Finance":
        return True, "Career community changed to Business & Finance."
    return False, f"Career community is '{actual}', expected 'Business & Finance'."
