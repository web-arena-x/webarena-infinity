import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    epic = next((e for e in state["epics"] if e.get("title") == "Technical Debt Cleanup"), None)
    if epic is None:
        return False, "Epic 'Technical Debt Cleanup' not found."

    tech_debt_label = next((l for l in state["labels"] if l["name"] == "tech-debt"), None)
    medium_label = next((l for l in state["labels"] if l["name"] == "priority::medium"), None)
    if not tech_debt_label or not medium_label:
        return False, "Required labels not found."

    if tech_debt_label["id"] not in epic.get("labels", []):
        return False, f"Epic missing tech-debt label. Labels: {epic.get('labels')}."
    if medium_label["id"] not in epic.get("labels", []):
        return False, f"Epic missing priority::medium label. Labels: {epic.get('labels')}."

    for issue_id in [42, 54]:
        if issue_id not in epic.get("childIssueIds", []):
            return False, f"Issue #{issue_id} not in epic childIssueIds: {epic.get('childIssueIds')}."

    return True, "Epic 'Technical Debt Cleanup' created with tech-debt and priority::medium labels, children #42 and #54."
