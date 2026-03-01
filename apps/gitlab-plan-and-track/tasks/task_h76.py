import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Platform Redesign and Documentation Overhaul epics
    platform_epic = doc_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Platform Redesign":
            platform_epic = e
        elif e.get("title") == "Documentation Overhaul":
            doc_epic = e
    if platform_epic is None:
        return False, "Could not find epic 'Platform Redesign'."
    if doc_epic is None:
        return False, "Could not find epic 'Documentation Overhaul'."

    errors = []

    # Documentation Overhaul should be a child of Platform Redesign
    if doc_epic.get("parentEpicId") != platform_epic["id"]:
        errors.append(
            f"Documentation Overhaul parentEpicId is '{doc_epic.get('parentEpicId')}', "
            f"expected '{platform_epic['id']}'."
        )

    # Find priority::high label
    high_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::high":
            high_label = lbl
            break
    if high_label is None:
        return False, "Could not find 'priority::high' label."

    # Both documentation issues should have priority::high
    doc_issue_titles = [
        "Write getting started guide for new developers",
        "Create API reference documentation with examples",
    ]
    for title in doc_issue_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if high_label["id"] not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'priority::high' label.")

    # Epic health should be at_risk
    if doc_epic.get("healthStatus") != "at_risk":
        errors.append(
            f"Documentation Overhaul health is '{doc_epic.get('healthStatus')}', "
            f"expected 'at_risk'."
        )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Documentation Overhaul epic set as child of Platform Redesign, "
        "issues labeled priority::high, health set to at_risk."
    )
