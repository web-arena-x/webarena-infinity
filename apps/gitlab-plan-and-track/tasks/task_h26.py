import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Platform Redesign epic
    platform_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "Platform Redesign":
            platform_epic = epic
            break
    if platform_epic is None:
        return False, "Could not find epic 'Platform Redesign'."

    # Find Q2 Planning epic
    q2_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "Q2 Planning":
            q2_epic = epic
            break
    if q2_epic is None:
        return False, "Could not find epic 'Q2 Planning'."

    if q2_epic.get("parentEpicId") != platform_epic["id"]:
        return False, f"Epic 'Q2 Planning' parentEpicId is '{q2_epic.get('parentEpicId')}', expected '{platform_epic['id']}'."

    # Find Sprint 27
    sprint27 = None
    for iteration in state.get("iterations", []):
        if iteration.get("title") == "Sprint 27":
            sprint27 = iteration
            break
    if sprint27 is None:
        return False, "Could not find iteration 'Sprint 27'."
    sprint27_id = sprint27["id"]

    q2_id = q2_epic["id"]

    # Find all open issues originally in Sprint 27 — they should now have epicId = q2_epic
    sprint27_issues = []
    for issue in state.get("issues", []):
        if issue.get("iterationId") == sprint27_id and issue.get("status") == "open":
            sprint27_issues.append(issue)

    if len(sprint27_issues) < 3:
        return False, f"Expected at least 3 open issues in Sprint 27, found {len(sprint27_issues)}."

    errors = []
    for issue in sprint27_issues:
        if issue.get("epicId") != q2_id:
            errors.append(issue.get("title"))

    if errors:
        return False, f"These Sprint 27 issues are not in the 'Q2 Planning' epic: {errors}"

    return True, f"Epic 'Q2 Planning' created as child of Platform Redesign with {len(sprint27_issues)} Sprint 27 issues."
