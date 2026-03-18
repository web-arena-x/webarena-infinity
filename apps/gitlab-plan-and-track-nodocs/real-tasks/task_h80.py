import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Milestone 'Q2 Security Sprint' with startDate 2026-04-01, dueDate 2026-04-30
    ms = next((m for m in state["milestones"] if m.get("title") == "Q2 Security Sprint"), None)
    if ms is None:
        return False, "Milestone 'Q2 Security Sprint' not found."
    if ms.get("startDate") != "2026-04-01":
        return False, f"Milestone startDate is '{ms.get('startDate')}', expected '2026-04-01'."
    if ms.get("dueDate") != "2026-04-30":
        return False, f"Milestone dueDate is '{ms.get('dueDate')}', expected '2026-04-30'."

    ms_id = ms["id"]

    # Open security (5) issues from Sprint 6/7: #1, #3, #2, #45
    # Should be in new milestone and have iterationId 8 (Sprint 8)
    for issue_id in [1, 2, 3, 45]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("milestoneId") != ms_id:
            return False, f"Issue #{issue_id} milestoneId is {issue.get('milestoneId')}, expected {ms_id} (Q2 Security Sprint)."
        if issue.get("iterationId") != 8:
            return False, f"Issue #{issue_id} iterationId is {issue.get('iterationId')}, expected 8 (Sprint 8)."

    return True, "Q2 Security Sprint milestone created, security issues from Sprint 6/7 moved in with Sprint 8."
