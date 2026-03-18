import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Jun Nakamura (4) open issues with original weight 3:
    # #66, #73, #77, #96, #102, #117, #123
    # All should now have weight 5
    target_ids = [66, 73, 77, 96, 102, 117, 123]

    for issue_id in target_ids:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("weight") != 5:
            return False, f"Issue #{issue_id} weight is {issue.get('weight')}, expected 5."

    return True, "All of Jun's weight-3 issues updated to weight 5."
