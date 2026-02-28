import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Fix dropdown menu position clipping at viewport edges"), None)
    if issue is None:
        return False, "Could not find issue titled 'Fix dropdown menu position clipping at viewport edges'."

    milestones = state.get("milestones", [])
    milestone = next((m for m in milestones if m.get("title") == "Backlog"), None)
    if milestone is None:
        return False, "Could not find milestone titled 'Backlog'."

    if issue.get("timeEstimate") != 14400:
        return False, f"Expected timeEstimate 14400 (4 hours) but got '{issue.get('timeEstimate')}'."

    if issue.get("milestoneId") != milestone.get("id"):
        return False, f"Issue's milestoneId '{issue.get('milestoneId')}' does not match 'Backlog' milestone id '{milestone.get('id')}'."

    return True, "Issue 'Fix dropdown menu position clipping at viewport edges' has a 4-hour time estimate and is assigned to the Backlog milestone."
