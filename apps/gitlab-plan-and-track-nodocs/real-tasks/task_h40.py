import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    epic = next((e for e in state["epics"] if "Performance Optimization Phase 2" in e.get("title", "")), None)
    if epic is None:
        return False, "Epic 'Performance Optimization Phase 2' not found."

    if epic.get("status") != "closed":
        return False, f"Epic status is '{epic.get('status')}', expected 'closed'."

    low_label = next((l for l in state["labels"] if l["name"] == "priority::low"), None)
    if low_label is None:
        return False, "Label 'priority::low' not found."
    low_id = low_label["id"]

    priority_ids = set()
    for l in state["labels"]:
        if l["name"].startswith("priority::") and l["id"] != low_id:
            priority_ids.add(l["id"])

    backlog_ms = next((m for m in state["milestones"] if m.get("title") == "Backlog"), None)
    if backlog_ms is None:
        return False, "Milestone 'Backlog' not found."
    backlog_id = backlog_ms["id"]

    for issue_id in [11, 12, 14, 49, 50]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("milestoneId") != backlog_id:
            return False, f"Issue #{issue_id} milestoneId is {issue.get('milestoneId')}, expected {backlog_id} (Backlog)."
        if low_id not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} missing priority::low label."
        other_priorities = [p for p in priority_ids if p in issue.get("labelIds", [])]
        if other_priorities:
            return False, f"Issue #{issue_id} still has other priority labels: {other_priorities}."

    return True, "Epic closed, all open children moved to Backlog with priority::low."
