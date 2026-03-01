import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the renamed label (was 'UX', now 'user-experience')
    ux_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "user-experience":
            ux_label = lbl
            break
    if ux_label is None:
        return False, "Could not find label 'user-experience' (expected rename from 'UX')."

    errors = []

    # Check type changed to 'group'
    if ux_label.get("type") != "group":
        errors.append(
            f"Label type is '{ux_label.get('type')}', expected 'group'."
        )

    # Old name should not exist
    for lbl in state.get("labels", []):
        if lbl.get("title") == "UX":
            errors.append("Label 'UX' still exists (should be renamed to 'user-experience').")
            break

    # Find Frontend Modernization epic
    fe_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Frontend Modernization":
            fe_epic = e
            break
    if fe_epic is None:
        return False, "Could not find epic 'Frontend Modernization'."

    ux_id = ux_label["id"]

    # Issues that should have the label (all open in Frontend Modernization)
    expected_titles = [
        "Migrate user settings page to React",
        "Build component library documentation site",
        "Add dark mode support for the entire application",
        "Add accessibility labels to all form inputs",
        "Create reusable data table component with sorting and filtering",
    ]

    labeled_count = 0
    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if ux_id not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'user-experience' label.")
        else:
            labeled_count += 1

    if errors:
        return False, " ".join(errors)

    return True, (
        f"'UX' renamed to 'user-experience' (type: group), "
        f"applied to {labeled_count} Frontend Modernization issues."
    )
