import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    help_with = state["currentUser"]["careerInterests"]["helpWith"]
    if "Job" in help_with:
        return True, "Job added to helpWith."
    return False, f"Job not in helpWith. Current: {help_with}."
