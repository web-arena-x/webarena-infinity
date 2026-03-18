import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Search Infra epic children form chain: #60 -> #61 -> #62
    # Root (#60): set priority::critical (11)
    # Leaf (#62): set weight to 13

    issue60 = next((i for i in state["issues"] if i["id"] == 60), None)
    if issue60 is None:
        return False, "Issue #60 not found."
    if 11 not in issue60.get("labelIds", []):
        return False, f"Issue #60 missing priority::critical label (id 11). Labels: {issue60.get('labelIds')}."
    for pid in [12, 13, 14]:
        if pid in issue60.get("labelIds", []):
            return False, f"Issue #60 still has priority label {pid} alongside critical."

    issue62 = next((i for i in state["issues"] if i["id"] == 62), None)
    if issue62 is None:
        return False, "Issue #62 not found."
    if issue62.get("weight") != 13:
        return False, f"Issue #62 weight is {issue62.get('weight')}, expected 13."

    return True, "Dependency chain resolved: #60 set to critical, #62 weight set to 13."
