import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find label "technical-debt"
    tech_debt_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "technical-debt":
            tech_debt_label = lbl
            break
    tech_debt_id = tech_debt_label["id"] if tech_debt_label else None

    # Find label "type::improvement"
    improvement_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::improvement":
            improvement_label = lbl
            break
    if improvement_label is None:
        return False, "Could not find label 'type::improvement'."
    improvement_label_id = improvement_label["id"]

    # Expected issues that had the technical-debt label (by exact title from seed data)
    expected_titles = [
        "Refactor notification service to use event-driven architecture",
        "Migrate from Webpack 4 to Webpack 5",
        "Replace deprecated analytics library",
    ]

    issues_by_title = {}
    for issue in state.get("issues", []):
        if issue.get("title") in expected_titles:
            issues_by_title[issue.get("title")] = issue

    missing = [t for t in expected_titles if t not in issues_by_title]
    if missing:
        return False, f"Could not find expected technical-debt issues: {missing}"

    errors = []
    for title, issue in issues_by_title.items():
        issue_labels = issue.get("labels", [])
        # Check technical-debt label is NOT present
        if tech_debt_id is not None and tech_debt_id in issue_labels:
            errors.append(f"'{title}' still has 'technical-debt' label.")
        # Check type::improvement label IS present
        if improvement_label_id not in issue_labels:
            errors.append(f"'{title}' is missing 'type::improvement' label.")

    # Also check globally: no issue should have the technical-debt label
    if tech_debt_id is not None:
        for issue in state.get("issues", []):
            if tech_debt_id in issue.get("labels", []):
                errors.append(f"Issue '{issue.get('title', issue.get('id'))}' still has 'technical-debt' label.")

    if errors:
        return False, " ".join(errors)

    return True, "'technical-debt' label removed from all issues and 'type::improvement' label added to affected issues."
