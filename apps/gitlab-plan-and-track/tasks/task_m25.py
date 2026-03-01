import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the lazy loading issue
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Implement lazy loading for images and avatars":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Implement lazy loading for images and avatars'."

    # Find v4.0 milestone
    ms_v40 = None
    for ms in state.get("milestones", []):
        if "v4.0" in ms.get("title", "") and "Platform Redesign" in ms.get("title", ""):
            ms_v40 = ms
            break
    if ms_v40 is None:
        return False, "Could not find milestone 'v4.0 - Platform Redesign'."

    # Find Sprint 27 iteration
    sprint27 = None
    for iteration in state.get("iterations", []):
        if iteration.get("title") == "Sprint 27":
            sprint27 = iteration
            break
    if sprint27 is None:
        return False, "Could not find iteration 'Sprint 27'."

    if target_issue.get("milestoneId") != ms_v40["id"]:
        return False, f"Issue milestoneId is '{target_issue.get('milestoneId')}', expected '{ms_v40['id']}'."

    if target_issue.get("iterationId") != sprint27["id"]:
        return False, f"Issue iterationId is '{target_issue.get('iterationId')}', expected '{sprint27['id']}'."

    return True, "Lazy loading issue moved to v4.0 - Platform Redesign and assigned to Sprint 27."
