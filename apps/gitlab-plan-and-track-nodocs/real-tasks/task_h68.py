import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Epic 'Sprint 6 Escalation' with labels [11 (critical), 1 (bug)]
    epic = next((e for e in state["epics"] if e.get("title") == "Sprint 6 Escalation"), None)
    if epic is None:
        return False, "Epic 'Sprint 6 Escalation' not found."
    for label_id in [11, 1]:
        if label_id not in epic.get("labels", []):
            return False, f"Epic missing label id {label_id}. Labels: {epic.get('labels')}."

    # Children: all open Sprint 6 bugs: #28, #31, #33, #35, #41, #78, #101, #104
    expected_children = [28, 31, 33, 35, 41, 78, 101, 104]
    for issue_id in expected_children:
        if issue_id not in epic.get("childIssueIds", []):
            return False, f"Issue #{issue_id} not in epic childIssueIds: {epic.get('childIssueIds')}."

    return True, "Epic 'Sprint 6 Escalation' created with all Sprint 6 bug children."
