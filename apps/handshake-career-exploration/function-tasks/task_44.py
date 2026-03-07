import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    post_grad = state["currentUser"]["careerInterests"]["postGraduation"]
    if "Gap year" in post_grad:
        return True, "Gap year added to post-graduation plans."
    return False, f"Gap year not in postGraduation. Current: {post_grad}."
