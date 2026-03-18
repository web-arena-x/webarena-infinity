import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    issue14 = next((i for i in state["issues"] if i["id"] == 14), None)
    issue41 = next((i for i in state["issues"] if i["id"] == 41), None)
    if issue14 is None or issue41 is None:
        return False, "Issue #14 or #41 not found."

    # Check blocks relationship from #14 to #41
    has_blocks = any(
        r.get("issueId") == 41 and r.get("type") == "blocks"
        for r in issue14.get("relatedIssues", [])
    )
    if not has_blocks:
        return False, f"Issue #14 does not have a 'blocks' relationship with #41. Related: {issue14.get('relatedIssues')}."

    has_blocked_by = any(
        r.get("issueId") == 14 and r.get("type") == "is_blocked_by"
        for r in issue41.get("relatedIssues", [])
    )
    if not has_blocked_by:
        return False, f"Issue #41 does not have an 'is_blocked_by' relationship with #14. Related: {issue41.get('relatedIssues')}."

    # Both should have priority::critical
    critical_label = next((l for l in state["labels"] if l["name"] == "priority::critical"), None)
    if critical_label is None:
        return False, "Label 'priority::critical' not found."
    crit_id = critical_label["id"]

    if crit_id not in issue14.get("labelIds", []):
        return False, f"Issue #14 does not have priority::critical label. Labels: {issue14.get('labelIds')}."
    if crit_id not in issue41.get("labelIds", []):
        return False, f"Issue #41 does not have priority::critical label. Labels: {issue41.get('labelIds')}."

    return True, "Issues #14 and #41 linked with blocks relationship, both set to priority::critical."
