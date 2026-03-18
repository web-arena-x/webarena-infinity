import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # #77 should block #102
    issue77 = next((i for i in state["issues"] if i["id"] == 77), None)
    if issue77 is None:
        return False, "Issue #77 not found."
    if not any(r.get("issueId") == 102 and r.get("type") == "blocks" for r in issue77.get("relatedIssues", [])):
        return False, f"Issue #77 does not have a 'blocks' relationship with #102. Related: {issue77.get('relatedIssues')}."

    issue102 = next((i for i in state["issues"] if i["id"] == 102), None)
    if issue102 is None:
        return False, "Issue #102 not found."
    if not any(r.get("issueId") == 77 and r.get("type") == "is_blocked_by" for r in issue102.get("relatedIssues", [])):
        return False, f"Issue #102 does not have an 'is_blocked_by' relationship with #77. Related: {issue102.get('relatedIssues')}."

    # Both should have priority::high (12)
    for issue_id, issue in [(77, issue77), (102, issue102)]:
        if 12 not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} does not have priority::high (id 12). Labels: {issue.get('labelIds')}."

    return True, "Blocks relationship from #77 to #102, both set to priority::high."
