import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Sprint 10 in Engineering Sprints (cadenceId 1), 2026-05-12 to 2026-05-25
    sprint10 = next((it for it in state["iterations"] if it.get("title") == "Sprint 10"), None)
    if sprint10 is None:
        return False, "Iteration 'Sprint 10' not found."
    if sprint10.get("cadenceId") != 1:
        return False, f"Sprint 10 cadenceId is {sprint10.get('cadenceId')}, expected 1."
    if sprint10.get("startDate") != "2026-05-12":
        return False, f"Sprint 10 startDate is '{sprint10.get('startDate')}', expected '2026-05-12'."
    if sprint10.get("endDate") != "2026-05-25":
        return False, f"Sprint 10 endDate is '{sprint10.get('endDate')}', expected '2026-05-25'."

    sprint10_id = sprint10["id"]

    # Sprint 7 status::to-do (label 15) issues moved to Sprint 10:
    # #2, #8, #12, #19, #45, #55
    for issue_id in [2, 8, 12, 19, 45, 55]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("iterationId") != sprint10_id:
            return False, f"Issue #{issue_id} iterationId is {issue.get('iterationId')}, expected {sprint10_id} (Sprint 10)."

    return True, "Sprint 10 created, status::to-do issues moved from Sprint 7."
