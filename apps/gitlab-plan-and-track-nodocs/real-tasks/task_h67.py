import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # #1 blocks #2. #2 is in milestone 3, iteration 7.
    # All other open issues in milestone 3 with iteration 7 should have weight 8.
    # Targets: #8, #12, #43, #45, #55, #73, #76, #102, #113
    target_ids = [8, 12, 43, 45, 55, 73, 76, 102, 113]

    for issue_id in target_ids:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("weight") != 8:
            return False, f"Issue #{issue_id} weight is {issue.get('weight')}, expected 8."

    return True, "All open v2.0/Sprint 7 issues (excluding #2) set to weight 8."
