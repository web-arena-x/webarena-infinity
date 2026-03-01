import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Release Cycle cadence (the non-automatic one)
    release_cad = None
    for c in state.get("iterationCadences", []):
        if c.get("title") == "Release Cycle":
            release_cad = c
            break
    if release_cad is None:
        return False, "Could not find cadence 'Release Cycle'."

    # Find the new iteration
    patch_iter = None
    for it in state.get("iterations", []):
        if it.get("title") == "Patch Release":
            patch_iter = it
            break
    if patch_iter is None:
        return False, "Could not find iteration 'Patch Release'."

    errors = []

    if patch_iter.get("cadenceId") != release_cad["id"]:
        errors.append("Iteration 'Patch Release' is not in the Release Cycle cadence.")
    if patch_iter.get("startDate") != "2026-03-17":
        errors.append(f"Start date is '{patch_iter.get('startDate')}', expected '2026-03-17'.")
    if patch_iter.get("dueDate") != "2026-03-28":
        errors.append(f"Due date is '{patch_iter.get('dueDate')}', expected '2026-03-28'.")

    patch_id = patch_iter["id"]

    # Find security label
    sec_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "security":
            sec_label = lbl
            break
    if sec_label is None:
        return False, "Could not find label 'security'."

    sec_id = sec_label["id"]

    # Expected: open issues with security label that had no iteration in seed
    expected_titles = [
        "Add rate limiting to v3 endpoints",
        "Implement CSRF token rotation",
        "Implement audit logging for admin actions",
        "Implement two-factor authentication with TOTP",
        "Add branch protection rules UI",
        "Migrate user authentication from sessions to JWT",
    ]

    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("iterationId") != patch_id:
            errors.append(f"Issue '{title}' not assigned to 'Patch Release' iteration.")

    if errors:
        return False, " ".join(errors)

    return True, f"Iteration 'Patch Release' created in Release Cycle and {len(expected_titles)} security issues assigned."
