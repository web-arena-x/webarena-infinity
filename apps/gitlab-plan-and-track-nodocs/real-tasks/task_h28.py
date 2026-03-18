import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    epic = next((e for e in state["epics"] if "Performance Optimization Phase 2" in e.get("title", "")), None)
    if epic is None:
        return False, "Epic 'Performance Optimization Phase 2' not found."

    author_id = epic.get("authorId")
    if author_id is None:
        return False, "Epic has no authorId."

    # Open child issues: 11, 12, 14, 49, 50 (13 is closed)
    expected_issues = [11, 12, 14, 49, 50]
    for issue_id in expected_issues:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if author_id not in issue.get("assigneeIds", []):
            return False, f"Epic author (id {author_id}) not in assigneeIds for issue #{issue_id}: {issue.get('assigneeIds')}."

    return True, f"Epic author (id {author_id}) assigned to all open child issues."
