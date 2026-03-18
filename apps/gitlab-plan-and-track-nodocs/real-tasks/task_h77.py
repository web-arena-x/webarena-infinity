import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # v1.2 Hotfixes issues (#88, #89) moved to v1.1 Stability (milestoneId 2)
    v11 = next((m for m in state["milestones"] if "v1.1" in m.get("title", "")), None)
    if v11 is None:
        return False, "v1.1 Stability milestone not found."

    for issue_id in [88, 89]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("milestoneId") != v11["id"]:
            return False, f"Issue #{issue_id} milestoneId is {issue.get('milestoneId')}, expected {v11['id']} (v1.1)."

    # v1.2 Hotfixes milestone should be deleted
    v12 = next((m for m in state["milestones"] if "v1.2" in m.get("title", "")), None)
    if v12 is not None:
        return False, f"v1.2 Hotfixes milestone still exists (id {v12['id']})."

    return True, "v1.2 issues moved to v1.1, v1.2 milestone deleted."
