import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    milestone = next((m for m in state["milestones"] if m.get("title") == "Security Hardening"), None)
    if milestone is None:
        return False, "Milestone 'Security Hardening' not found."

    if milestone.get("startDate") != "2026-04-01":
        return False, f"Milestone startDate is '{milestone.get('startDate')}', expected '2026-04-01'."

    if milestone.get("dueDate") != "2026-05-31":
        return False, f"Milestone dueDate is '{milestone.get('dueDate')}', expected '2026-05-31'."

    ms_id = milestone["id"]

    # All open confidential issues should be in this milestone
    confidential_issues = [i for i in state["issues"] if i.get("confidential") and i.get("status") == "open"]
    if not confidential_issues:
        return False, "No open confidential issues found."

    for issue in confidential_issues:
        if issue.get("milestoneId") != ms_id:
            return False, f"Confidential issue #{issue['id']} milestoneId is {issue.get('milestoneId')}, expected {ms_id}."

    return True, f"Milestone 'Security Hardening' created and {len(confidential_issues)} confidential issues moved to it."
