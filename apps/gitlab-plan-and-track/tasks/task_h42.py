import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # The epic with at_risk health is Security Hardening
    sec_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Security Hardening":
            sec_epic = e
            break
    if sec_epic is None:
        return False, "Could not find epic 'Security Hardening'."

    # Find the new milestone
    ms = None
    for m in state.get("milestones", []):
        if m.get("title") == "Risk Mitigation Sprint":
            ms = m
            break
    if ms is None:
        return False, "Could not find milestone 'Risk Mitigation Sprint'."

    errors = []

    if ms.get("startDate") != "2026-03-03":
        errors.append(f"Milestone start date is '{ms.get('startDate')}', expected '2026-03-03'.")
    if ms.get("dueDate") != "2026-03-14":
        errors.append(f"Milestone due date is '{ms.get('dueDate')}', expected '2026-03-14'.")

    ms_id = ms["id"]

    # Check all open issues from Security Hardening epic are in new milestone
    epic_issues = [i for i in state.get("issues", [])
                   if i.get("epicId") == sec_epic["id"] and i.get("status") == "open"]

    if len(epic_issues) < 3:
        errors.append(f"Expected at least 3 open issues in Security Hardening epic, found {len(epic_issues)}.")

    for issue in epic_issues:
        if issue.get("milestoneId") != ms_id:
            errors.append(f"Issue '{issue.get('title')}' not moved to 'Risk Mitigation Sprint' milestone.")

    if errors:
        return False, " ".join(errors)

    return True, f"Milestone 'Risk Mitigation Sprint' created and {len(epic_issues)} Security Hardening issues moved to it."
