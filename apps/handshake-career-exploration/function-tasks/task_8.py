import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    if "emp_09" not in state["currentUser"]["followedEmployerIds"]:
        return False, "Amazon (emp_09) not in followedEmployerIds."
    emp = next((e for e in state["employers"] if e["id"] == "emp_09"), None)
    if not emp:
        return False, "Amazon employer not found."
    if emp["followCount"] <= 47600:
        return False, f"Amazon followCount not increased. Expected > 47600, got {emp['followCount']}."
    return True, "Amazon followed successfully."
