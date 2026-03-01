import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find Hotfix 4.0.1 milestone
    hf_ms = None
    for m in state.get("milestones", []):
        if m.get("title") == "Hotfix 4.0.1":
            hf_ms = m
            break
    if hf_ms is None:
        return False, "Could not find milestone 'Hotfix 4.0.1'."

    if hf_ms.get("startDate") != "2026-03-03":
        errors.append(
            f"Milestone start date is '{hf_ms.get('startDate')}', expected '2026-03-03'."
        )
    if hf_ms.get("dueDate") != "2026-03-10":
        errors.append(
            f"Milestone due date is '{hf_ms.get('dueDate')}', expected '2026-03-10'."
        )

    # Find Sprint Cadence
    sprint_cad = None
    for c in state.get("iterationCadences", []):
        if c.get("title") == "Sprint Cadence":
            sprint_cad = c
            break
    if sprint_cad is None:
        return False, "Could not find 'Sprint Cadence'."

    # Find Hotfix Sprint iteration
    hf_iter = None
    for it in state.get("iterations", []):
        if it.get("title") == "Hotfix Sprint":
            hf_iter = it
            break
    if hf_iter is None:
        return False, "Could not find iteration 'Hotfix Sprint'. " + " ".join(errors)

    if hf_iter.get("cadenceId") != sprint_cad["id"]:
        errors.append(
            f"Iteration cadenceId is '{hf_iter.get('cadenceId')}', "
            f"expected '{sprint_cad['id']}'."
        )
    if hf_iter.get("startDate") != "2026-03-03":
        errors.append(
            f"Iteration start date is '{hf_iter.get('startDate')}', expected '2026-03-03'."
        )
    if hf_iter.get("dueDate") != "2026-03-10":
        errors.append(
            f"Iteration due date is '{hf_iter.get('dueDate')}', expected '2026-03-10'."
        )

    # Check issues assigned to both
    expected = [
        "Login page shows blank screen on Safari 17.2",
        "Email notifications sent with wrong timezone offset",
    ]
    for title in expected:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("milestoneId") != hf_ms["id"]:
            errors.append(f"Issue '{title}' not in Hotfix 4.0.1 milestone.")
        if issue.get("iterationId") != hf_iter["id"]:
            errors.append(f"Issue '{title}' not in Hotfix Sprint iteration.")

    if errors:
        return False, " ".join(errors)

    return True, (
        "Hotfix 4.0.1 milestone and Hotfix Sprint iteration created; "
        "Safari login and email notification issues assigned to both."
    )
