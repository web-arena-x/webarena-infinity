import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # v1.2 Hotfixes milestone should be deleted
    hotfix_ms = next((m for m in state["milestones"] if "v1.2" in m.get("title", "")), None)
    if hotfix_ms is not None:
        return False, f"Milestone 'v1.2 — Hotfixes' still exists (id {hotfix_ms['id']})."

    # v1.0 Foundation should exist
    v10_ms = next((m for m in state["milestones"] if "v1.0" in m.get("title", "")), None)
    if v10_ms is None:
        return False, "Milestone 'v1.0 — Foundation' not found."

    # Issues #88 and #89 should be in v1.0
    for issue_id in [88, 89]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("milestoneId") != v10_ms["id"]:
            return False, f"Issue #{issue_id} milestoneId is {issue.get('milestoneId')}, expected {v10_ms['id']}."

    return True, "v1.2 Hotfixes deleted, issues #88 and #89 moved to v1.0 Foundation."
