import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # #22 blocks #55
    issue22 = next((i for i in state["issues"] if i["id"] == 22), None)
    if issue22 is None:
        return False, "Issue #22 not found."
    if not any(r.get("issueId") == 55 and r.get("type") == "blocks" for r in issue22.get("relatedIssues", [])):
        return False, f"Issue #22 does not block #55. Related: {issue22.get('relatedIssues')}."

    # #55 is_blocked_by #22 AND blocks #23
    issue55 = next((i for i in state["issues"] if i["id"] == 55), None)
    if issue55 is None:
        return False, "Issue #55 not found."
    if not any(r.get("issueId") == 22 and r.get("type") == "is_blocked_by" for r in issue55.get("relatedIssues", [])):
        return False, f"Issue #55 does not have 'is_blocked_by' from #22. Related: {issue55.get('relatedIssues')}."
    if not any(r.get("issueId") == 23 and r.get("type") == "blocks" for r in issue55.get("relatedIssues", [])):
        return False, f"Issue #55 does not block #23. Related: {issue55.get('relatedIssues')}."

    # #23 is_blocked_by #55
    issue23 = next((i for i in state["issues"] if i["id"] == 23), None)
    if issue23 is None:
        return False, "Issue #23 not found."
    if not any(r.get("issueId") == 55 and r.get("type") == "is_blocked_by" for r in issue23.get("relatedIssues", [])):
        return False, f"Issue #23 does not have 'is_blocked_by' from #55. Related: {issue23.get('relatedIssues')}."

    # All three should have priority::high (12)
    for issue_id, issue in [(22, issue22), (55, issue55), (23, issue23)]:
        if 12 not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} does not have priority::high (id 12). Labels: {issue.get('labelIds')}."

    return True, "Relationship chain #22→#55→#23 created; all three set to priority::high."
