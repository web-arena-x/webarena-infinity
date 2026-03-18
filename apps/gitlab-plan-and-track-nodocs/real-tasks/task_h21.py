import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find the incident issue
    incident = next((i for i in state["issues"] if i.get("type") == "incident"), None)
    if incident is None:
        return False, "No incident-type issue found."

    issue_id = incident["id"]

    # Check it's a child of Performance Optimization Phase 2
    epic = next((e for e in state["epics"] if "Performance Optimization Phase 2" in e.get("title", "")), None)
    if epic is None:
        return False, "Epic 'Performance Optimization Phase 2' not found."

    if issue_id not in epic.get("childIssueIds", []):
        return False, f"Issue #{issue_id} not in epic childIssueIds: {epic.get('childIssueIds')}."

    if incident.get("weight") != 21:
        return False, f"Issue #{issue_id} weight is {incident.get('weight')}, expected 21."

    return True, f"Incident issue #{issue_id} added to Performance Optimization Phase 2 epic with weight 21."
