import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find type::documentation label
    doc_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::documentation":
            doc_label = lbl
            break
    if doc_label is None:
        return False, "Could not find label 'type::documentation'."

    doc_id = doc_label["id"]

    # Expected issues (open with type::documentation in seed)
    expected_titles = [
        "Build component library documentation site",
        "Update project README with new setup instructions",
        "Write getting started guide for new developers",
        "Create API reference documentation with examples",
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
        if issue.get("status") != "closed":
            errors.append(f"Issue '{title}' should be closed, got '{issue.get('status')}'.")
        if issue.get("milestoneId") is not None:
            errors.append(f"Issue '{title}' should have no milestone, got '{issue.get('milestoneId')}'.")

    if errors:
        return False, " ".join(errors)

    return True, f"All {len(expected_titles)} documentation issues closed with milestones removed."
