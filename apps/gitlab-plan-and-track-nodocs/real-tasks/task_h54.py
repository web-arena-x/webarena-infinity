import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # #12's related issue is #11. #11 is in milestone 3 with priority::critical.
    # All open critical issues in milestone 3: #11, #33, #41 — all should have weight 13.
    for issue_id in [11, 33, 41]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("weight") != 13:
            return False, f"Issue #{issue_id} weight is {issue.get('weight')}, expected 13."

    return True, "Issues #11, #33, #41 (v2.0 critical) all have weight 13."
