import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    if "emp_02" not in state["currentUser"]["followedEmployerIds"]:
        return False, "JPMorgan Chase (emp_02) not in followedEmployerIds."
    emp = next((e for e in state["employers"] if e["id"] == "emp_02"), None)
    if not emp:
        return False, "JPMorgan Chase employer not found."
    if emp["followCount"] <= 32100:
        return False, f"JPMorgan followCount not increased. Expected > 32100, got {emp['followCount']}."
    return True, "JPMorgan Chase followed successfully."
