import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # New issue must exist
    issue = next((i for i in state["issues"] if i.get("title") == "Document session management best practices"), None)
    if issue is None:
        return False, "Issue 'Document session management best practices' not found."

    # Documentation label (3)
    if 3 not in issue.get("labelIds", []):
        return False, f"Issue missing documentation label (id 3). Labels: {issue.get('labelIds')}."

    # Assigned to Jun Nakamura (4) — same as issue #4
    if 4 not in issue.get("assigneeIds", []):
        return False, f"Issue not assigned to Jun Nakamura (id 4). Assignees: {issue.get('assigneeIds')}."

    # Same milestone as #4 (milestoneId 3)
    if issue.get("milestoneId") != 3:
        return False, f"Issue milestoneId is {issue.get('milestoneId')}, expected 3 (v2.0 API Overhaul)."

    new_id = issue["id"]

    # Related_to link with #4
    if not any(r.get("issueId") == 4 and r.get("type") == "related_to" for r in issue.get("relatedIssues", [])):
        return False, f"New issue does not have a 'related_to' link with #4. Related: {issue.get('relatedIssues')}."

    issue4 = next((i for i in state["issues"] if i["id"] == 4), None)
    if issue4 is None:
        return False, "Issue #4 not found."
    if not any(r.get("issueId") == new_id and r.get("type") == "related_to" for r in issue4.get("relatedIssues", [])):
        return False, f"Issue #4 does not have a 'related_to' link with new issue #{new_id}. Related: {issue4.get('relatedIssues')}."

    return True, "Issue 'Document session management best practices' created with correct properties and related_to link to #4."
