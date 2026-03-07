import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    post_grad = state["currentUser"]["careerInterests"]["postGraduation"]
    if "Grad school" not in post_grad:
        return True, "Grad school removed from post-graduation plans."
    return False, f"Grad school still in postGraduation. Current: {post_grad}."
