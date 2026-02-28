import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find epic "Caching Layer Implementation"
    caching_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "Caching Layer Implementation":
            caching_epic = epic
            break
    if caching_epic is None:
        return False, "Could not find epic 'Caching Layer Implementation'."

    # Check it is closed
    if caching_epic.get("status") != "closed":
        return False, f"Epic 'Caching Layer Implementation' is not closed (status='{caching_epic.get('status')}')."

    caching_epic_id = caching_epic["id"]

    # Find epic "Database Optimization"
    db_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "Database Optimization":
            db_epic = epic
            break
    if db_epic is None:
        return False, "Could not find epic 'Database Optimization'."
    db_epic_id = db_epic["id"]

    # Expected issues from Caching Layer Implementation (by exact title from seed data)
    expected_titles = [
        "Configure CDN for static asset delivery",
        "Implement Redis session store",
    ]

    issues_by_title = {}
    for issue in state.get("issues", []):
        if issue.get("title") in expected_titles:
            issues_by_title[issue.get("title")] = issue

    missing = [t for t in expected_titles if t not in issues_by_title]
    if missing:
        return False, f"Could not find expected Caching Layer issues: {missing}"

    # Check both issues now have epicId == Database Optimization's id
    errors = []
    for title, issue in issues_by_title.items():
        if issue.get("epicId") != db_epic_id:
            errors.append(f"Issue '{title}' not moved to 'Database Optimization' epic (epicId='{issue.get('epicId')}').")

    if errors:
        return False, " ".join(errors)

    return True, "Epic 'Caching Layer Implementation' closed and its issues reassigned to 'Database Optimization' epic."
