import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Implement Content Security Policy headers"), None)
    if issue is None:
        return False, "Could not find issue titled 'Implement Content Security Policy headers'."

    milestones = state.get("milestones", [])
    milestone = next((m for m in milestones if m.get("title") == "v4.1 - Performance"), None)
    if milestone is None:
        return False, "Could not find milestone titled 'v4.1 - Performance'."

    iterations = state.get("iterations", [])
    iteration = next((it for it in iterations if it.get("title") == "Sprint 27"), None)
    if iteration is None:
        return False, "Could not find iteration titled 'Sprint 27'."

    if issue.get("milestoneId") != milestone.get("id"):
        return False, f"Issue's milestoneId '{issue.get('milestoneId')}' does not match 'v4.1 - Performance' milestone id '{milestone.get('id')}'."

    if issue.get("iterationId") != iteration.get("id"):
        return False, f"Issue's iterationId '{issue.get('iterationId')}' does not match 'Sprint 27' iteration id '{iteration.get('id')}'."

    return True, "Issue 'Implement Content Security Policy headers' is correctly moved to 'v4.1 - Performance' milestone and 'Sprint 27' iteration."
