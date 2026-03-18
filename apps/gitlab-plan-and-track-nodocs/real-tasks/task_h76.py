import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Sprint 6, exactly 1 assignee, status::in-progress (label 16):
    # #3, #7, #9, #11, #14, #22 — each should now have Ana Garcia (3) in assigneeIds
    target_ids = [3, 7, 9, 11, 14, 22]

    for issue_id in target_ids:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if 3 not in issue.get("assigneeIds", []):
            return False, f"Ana Garcia (id 3) not in assigneeIds for issue #{issue_id}: {issue.get('assigneeIds')}."

    return True, "Ana Garcia added to all Sprint 6 single-assignee in-progress issues."
