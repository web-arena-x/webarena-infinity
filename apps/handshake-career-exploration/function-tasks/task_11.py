import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    if "emp_08" not in state["currentUser"]["followedEmployerIds"]:
        return False, "Deloitte (emp_08) not in followedEmployerIds."
    emp = next((e for e in state["employers"] if e["id"] == "emp_08"), None)
    if not emp:
        return False, "Deloitte employer not found."
    if emp["followCount"] <= 25400:
        return False, f"Deloitte followCount not increased. Expected > 25400, got {emp['followCount']}."
    return True, "Deloitte followed successfully."
