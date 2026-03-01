import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find 'Bug Fix Sprint' iteration
    bf_iter = None
    for it in state.get("iterations", []):
        if it.get("title") == "Bug Fix Sprint":
            bf_iter = it
            break
    if bf_iter is None:
        return False, "Could not find iteration 'Bug Fix Sprint'."

    errors = []

    # Check dates
    if bf_iter.get("startDate") != "2026-03-31":
        errors.append(
            f"Iteration start date is '{bf_iter.get('startDate')}', expected '2026-03-31'."
        )
    if bf_iter.get("dueDate") != "2026-04-13":
        errors.append(
            f"Iteration due date is '{bf_iter.get('dueDate')}', expected '2026-04-13'."
        )

    # Check it belongs to Sprint Cadence
    sprint_cad = None
    for c in state.get("iterationCadences", []):
        if c.get("title") == "Sprint Cadence":
            sprint_cad = c
            break
    if sprint_cad is None:
        errors.append("Could not find 'Sprint Cadence'.")
    elif bf_iter.get("cadenceId") != sprint_cad["id"]:
        errors.append("Bug Fix Sprint is not in the Sprint Cadence.")

    # Find type::bug label
    bug_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::bug":
            bug_label = lbl
            break
    if bug_label is None:
        return False, "Could not find label 'type::bug'."

    # Expected bug issues that had no iteration
    expected_titles = [
        "Dashboard widget layout breaks at 1440px viewport",
        "File upload fails silently for files > 50MB",
        "Markdown preview renders incorrectly with nested code blocks",
        "Fix dropdown menu position clipping at viewport edges",
        "Fix typo in 404 error page message",
        "Database connection pool exhaustion under load",
        "Fix race condition in concurrent issue updates",
    ]

    bf_id = bf_iter["id"]
    moved_count = 0
    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("iterationId") != bf_id:
            errors.append(f"Issue '{title}' not moved to 'Bug Fix Sprint'.")
        else:
            moved_count += 1

    if errors:
        return False, " ".join(errors)

    return True, f"Bug Fix Sprint created; {moved_count} bug issues moved into it."
