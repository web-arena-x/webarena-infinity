import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # The only incident is #41 with assignees [5 (Priya), 6 (Tom)].
    # Tom (6) should be added to every unassigned Search Infra epic child.
    # Search Infrastructure Upgrade epic children: #60, #61, #62
    # All should also have priority::high (label 12).

    epic = next((e for e in state["epics"] if "Search Infrastructure" in e.get("title", "")), None)
    if epic is None:
        return False, "Search Infrastructure Upgrade epic not found."

    for issue_id in [60, 61, 62]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if 6 not in issue.get("assigneeIds", []):
            return False, f"Tom Ramirez (id 6) not in assigneeIds for issue #{issue_id}: {issue.get('assigneeIds')}."
        if 12 not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} missing priority::high label (id 12). Labels: {issue.get('labelIds')}."

    return True, "Tom Ramirez assigned to all Search Infra children with priority::high."
