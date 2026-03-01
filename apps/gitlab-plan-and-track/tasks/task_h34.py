import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Documentation Overhaul epic
    doc_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Documentation Overhaul":
            doc_epic = e
            break
    if doc_epic is None:
        return False, "Could not find epic 'Documentation Overhaul'."

    errors = []

    # Check epic is closed
    if doc_epic.get("status") != "closed":
        errors.append(f"Epic status is '{doc_epic.get('status')}', expected 'closed'.")

    # Find issues in the epic
    expected_titles = [
        "Write getting started guide for new developers",
        "Create API reference documentation with examples",
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
        if issue.get("status") != "closed":
            errors.append(f"Issue '{title}' is not closed.")
        if issue.get("milestoneId") is not None:
            errors.append(f"Issue '{title}' still has milestone assignment.")

    if errors:
        return False, " ".join(errors)

    return True, "Documentation Overhaul epic and both issues closed, milestones removed."
