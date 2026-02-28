import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Implement keyboard shortcuts for common actions"), None)
    if issue is None:
        return False, "Could not find issue titled 'Implement keyboard shortcuts for common actions'."

    epics = state.get("epics", [])
    epic = next((e for e in epics if e.get("title") == "Platform Redesign"), None)
    if epic is None:
        return False, "Could not find epic titled 'Platform Redesign'."

    iterations = state.get("iterations", [])
    iteration = next((it for it in iterations if it.get("title") == "Sprint 27"), None)
    if iteration is None:
        return False, "Could not find iteration titled 'Sprint 27'."

    if issue.get("epicId") != epic.get("id"):
        return False, f"Issue's epicId '{issue.get('epicId')}' does not match 'Platform Redesign' epic id '{epic.get('id')}'."

    if issue.get("iterationId") != iteration.get("id"):
        return False, f"Issue's iterationId '{issue.get('iterationId')}' does not match 'Sprint 27' iteration id '{iteration.get('id')}'."

    return True, "Issue 'Implement keyboard shortcuts for common actions' is correctly linked to 'Platform Redesign' epic and 'Sprint 27' iteration."
