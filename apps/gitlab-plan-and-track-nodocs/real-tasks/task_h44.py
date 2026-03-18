import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    epic = next((e for e in state["epics"] if "Accessibility Compliance" in e.get("title", "")), None)
    if epic is None:
        return False, "Accessibility Compliance epic not found."

    # Closed children #24 and #56 should be removed
    for removed_id in [24, 56]:
        if removed_id in epic.get("childIssueIds", []):
            return False, f"Closed issue #{removed_id} still in epic childIssueIds: {epic.get('childIssueIds')}."

    # Open children #22, #23, #55 should remain
    for kept_id in [22, 23, 55]:
        if kept_id not in epic.get("childIssueIds", []):
            return False, f"Open issue #{kept_id} missing from epic childIssueIds: {epic.get('childIssueIds')}."

    # #22 and #55 should have priority::high (12), not medium (13)
    for issue_id in [22, 55]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if 12 not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} does not have priority::high (id 12). Labels: {issue.get('labelIds')}."
        if 13 in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} still has priority::medium (id 13). Labels: {issue.get('labelIds')}."

    return True, "Closed children removed from Accessibility epic; #22 and #55 upgraded to priority::high."
