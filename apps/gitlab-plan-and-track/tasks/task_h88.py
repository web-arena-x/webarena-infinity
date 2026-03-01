import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find 'Developer Tooling' epic
    dt_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Developer Tooling":
            dt_epic = e
            break
    if dt_epic is None:
        return False, "Could not find epic 'Developer Tooling'."

    # Check type::feature label
    feat_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::feature":
            feat_label = lbl
            break
    if feat_label is None:
        errors.append("Could not find 'type::feature' label.")
    elif feat_label["id"] not in dt_epic.get("labels", []):
        errors.append("Epic 'Developer Tooling' missing 'type::feature' label.")

    # Check description
    desc = dt_epic.get("description", "")
    if "improve developer productivity" not in desc.lower():
        errors.append(
            f"Epic description does not contain expected text. Got: '{desc[:100]}'."
        )

    # Check issues assigned to epic
    expected_titles = [
        "Implement keyboard shortcuts for common actions",
        "Add bulk operations for issue management",
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
        if issue.get("epicId") != dt_epic["id"]:
            errors.append(
                f"Issue '{title}' epicId is '{issue.get('epicId')}', "
                f"expected '{dt_epic['id']}'."
            )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Epic 'Developer Tooling' created with type::feature label; "
        "keyboard shortcuts and bulk operations issues added."
    )
