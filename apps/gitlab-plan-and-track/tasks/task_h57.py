import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the new label
    co_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "sprint-carry-over":
            co_label = lbl
            break
    if co_label is None:
        return False, "Could not find label 'sprint-carry-over'."

    if co_label.get("color") != "#f97316":
        return False, f"Label color is '{co_label.get('color')}', expected '#f97316'."

    co_id = co_label["id"]

    # Find Sprint 27
    sprint27 = None
    for it in state.get("iterations", []):
        if it.get("title") == "Sprint 27":
            sprint27 = it
            break
    if sprint27 is None:
        return False, "Could not find iteration 'Sprint 27'."

    sprint27_id = sprint27["id"]

    # Expected issues (Sprint 26 open with needs_attention or at_risk health in seed)
    expected_titles = [
        "Migrate user settings page to React",
        "Implement Content Security Policy headers",
        "Upgrade vulnerable dependencies identified in audit",
        "Login page shows blank screen on Safari 17.2",
        "Reduce JavaScript bundle size by 40%",
    ]

    errors = []
    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if co_id not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'sprint-carry-over' label.")
        if issue.get("iterationId") != sprint27_id:
            errors.append(f"Issue '{title}' not moved to Sprint 27.")

    if errors:
        return False, " ".join(errors)

    return True, f"Label 'sprint-carry-over' created and applied to {len(expected_titles)} at-risk Sprint 26 issues, all moved to Sprint 27."
