import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    epic = next((e for e in state["epics"] if e.get("title") == "Backlog Bug Sweep"), None)
    if epic is None:
        return False, "Epic 'Backlog Bug Sweep' not found."

    if 1 not in epic.get("labels", []):
        return False, f"Label 'bug' (id 1) not in epic labels: {epic.get('labels')}."

    # All open Backlog issues with bug+frontend labels
    expected_children = [37, 67, 72, 97, 110, 120, 127]
    for issue_id in expected_children:
        if issue_id not in epic.get("childIssueIds", []):
            return False, f"Issue #{issue_id} not in epic childIssueIds: {epic.get('childIssueIds')}."

    # Each child must be closed
    for issue_id in expected_children:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue["status"] != "closed":
            return False, f"Issue #{issue_id} status is '{issue['status']}', expected 'closed'."

    return True, "Epic 'Backlog Bug Sweep' created with 7 bug+frontend Backlog children, all closed."
