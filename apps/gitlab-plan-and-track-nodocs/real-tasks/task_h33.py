import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    epic = next((e for e in state["epics"] if "Search Infrastructure Upgrade" in e.get("title", "")), None)
    if epic is None:
        return False, "Epic 'Search Infrastructure Upgrade' not found."

    # Issues #68, #105, #112 should be children (Backlog + feature + backend + unassigned)
    expected = [68, 105, 112]
    for issue_id in expected:
        if issue_id not in epic.get("childIssueIds", []):
            return False, f"Issue #{issue_id} not in epic childIssueIds: {epic.get('childIssueIds')}."

    return True, f"Issues {expected} added as children of Search Infrastructure Upgrade epic."
