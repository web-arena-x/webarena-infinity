import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Add loading skeletons to replace spinners"), None)
    if issue is None:
        return False, "Could not find issue titled 'Add loading skeletons to replace spinners'."

    milestones = state.get("milestones", [])
    milestone = next((m for m in milestones if m.get("title") == "v4.0 - Platform Redesign"), None)
    if milestone is None:
        return False, "Could not find milestone titled 'v4.0 - Platform Redesign'."

    epics = state.get("epics", [])
    epic = next((e for e in epics if e.get("title") == "Frontend Modernization"), None)
    if epic is None:
        return False, "Could not find epic titled 'Frontend Modernization'."

    if issue.get("milestoneId") != milestone.get("id"):
        return False, f"Issue's milestoneId '{issue.get('milestoneId')}' does not match 'v4.0 - Platform Redesign' milestone id '{milestone.get('id')}'."

    if issue.get("epicId") != epic.get("id"):
        return False, f"Issue's epicId '{issue.get('epicId')}' does not match 'Frontend Modernization' epic id '{epic.get('id')}'."

    return True, "Issue 'Add loading skeletons to replace spinners' is correctly moved to 'v4.0 - Platform Redesign' milestone and 'Frontend Modernization' epic."
