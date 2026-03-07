import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    if "emp_01" in state["currentUser"]["followedEmployerIds"]:
        return False, "Google (emp_01) still in followedEmployerIds."
    emp = next((e for e in state["employers"] if e["id"] == "emp_01"), None)
    if not emp:
        return False, "Google employer not found."
    if emp["followCount"] >= 45200:
        return False, f"Google followCount not decreased. Expected < 45200, got {emp['followCount']}."
    return True, "Google unfollowed successfully."
