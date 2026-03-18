import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    issue46 = next((i for i in state["issues"] if i["id"] == 46), None)
    if issue46 is None:
        return False, "Issue #46 not found."

    # Not confidential
    if issue46.get("confidential"):
        return False, "Issue #46 is still confidential."

    # Milestone changed to v2.0 (id 3)
    if issue46.get("milestoneId") != 3:
        return False, f"Issue #46 milestoneId is {issue46.get('milestoneId')}, expected 3 (v2.0 API Overhaul)."

    # David Kim (11) assigned
    if 11 not in issue46.get("assigneeIds", []):
        return False, f"David Kim (id 11) not in issue #46 assigneeIds: {issue46.get('assigneeIds')}."

    # Blocks relationship with #2
    if not any(r.get("issueId") == 2 and r.get("type") == "blocks" for r in issue46.get("relatedIssues", [])):
        return False, f"Issue #46 does not block #2. Related: {issue46.get('relatedIssues')}."

    issue2 = next((i for i in state["issues"] if i["id"] == 2), None)
    if issue2 is None:
        return False, "Issue #2 not found."
    if not any(r.get("issueId") == 46 and r.get("type") == "is_blocked_by" for r in issue2.get("relatedIssues", [])):
        return False, f"Issue #2 does not have 'is_blocked_by' from #46. Related: {issue2.get('relatedIssues')}."

    return True, "Issue #46: non-confidential, milestone v2.0, David Kim assigned, blocks #2."
