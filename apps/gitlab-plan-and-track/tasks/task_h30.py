import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the Release Cycle cadence
    release_cadence = None
    for c in state.get("iterationCadences", []):
        if c.get("title") == "Release Cycle":
            release_cadence = c
            break
    if release_cadence is None:
        return False, "Could not find cadence 'Release Cycle'."

    # Find iteration "Security Sprint"
    sec_iter = None
    for i in state.get("iterations", []):
        if i.get("title") == "Security Sprint":
            sec_iter = i
            break
    if sec_iter is None:
        return False, "Could not find iteration 'Security Sprint'."

    errors = []

    # Check cadence
    if sec_iter.get("cadenceId") != release_cadence["id"]:
        errors.append("Iteration 'Security Sprint' is not in the Release Cycle cadence.")

    # Check dates
    if sec_iter.get("startDate") != "2026-03-03":
        errors.append(f"Start date is '{sec_iter.get('startDate')}', expected '2026-03-03'.")
    if sec_iter.get("dueDate") != "2026-03-16":
        errors.append(f"Due date is '{sec_iter.get('dueDate')}', expected '2026-03-16'.")

    sec_iter_id = sec_iter["id"]

    # Find Security Hardening epic
    sec_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Security Hardening":
            sec_epic = e
            break
    if sec_epic is None:
        return False, "Could not find epic 'Security Hardening'."

    # Check all open issues in the epic are assigned to this iteration
    epic_issues = [i for i in state.get("issues", [])
                   if i.get("epicId") == sec_epic["id"] and i.get("status") == "open"]
    if len(epic_issues) < 3:
        errors.append(f"Expected at least 3 open issues in Security Hardening epic, found {len(epic_issues)}.")

    for issue in epic_issues:
        if issue.get("iterationId") != sec_iter_id:
            errors.append(f"Issue '{issue.get('title')}' not assigned to Security Sprint iteration.")

    if errors:
        return False, " ".join(errors)

    return True, f"Iteration 'Security Sprint' created in Release Cycle and {len(epic_issues)} issues assigned to it."
