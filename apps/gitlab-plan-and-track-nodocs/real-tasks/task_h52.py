import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    moved_issues = [19, 21, 53]

    # CI/CD epic should no longer contain the moved issues
    cicd_epic = next((e for e in state["epics"] if "CI/CD Pipeline" in e.get("title", "")), None)
    if cicd_epic is None:
        return False, "CI/CD Pipeline Modernization epic not found."
    for issue_id in moved_issues:
        if issue_id in cicd_epic.get("childIssueIds", []):
            return False, f"Issue #{issue_id} still in CI/CD epic childIssueIds."

    # Search Infrastructure epic should contain them
    search_epic = next((e for e in state["epics"] if "Search Infrastructure" in e.get("title", "")), None)
    if search_epic is None:
        return False, "Search Infrastructure Upgrade epic not found."
    for issue_id in moved_issues:
        if issue_id not in search_epic.get("childIssueIds", []):
            return False, f"Issue #{issue_id} not in Search Infrastructure epic childIssueIds."

    # Each should have iterationId 7 (Sprint 7)
    for issue_id in moved_issues:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("iterationId") != 7:
            return False, f"Issue #{issue_id} iterationId is {issue.get('iterationId')}, expected 7 (Sprint 7)."

    return True, "Issues #19, #21, #53 moved from CI/CD to Search Infrastructure epic, iteration set to Sprint 7."
