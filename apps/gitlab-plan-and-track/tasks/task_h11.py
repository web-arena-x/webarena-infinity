import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find user "Luca Rossi"
    luca = None
    for user in state.get("users", []):
        if user.get("name") == "Luca Rossi":
            luca = user
            break
    if luca is None:
        return False, "Could not find user 'Luca Rossi'."
    luca_id = luca["id"]

    # Find user "Chen Wei"
    chen = None
    for user in state.get("users", []):
        if user.get("name") == "Chen Wei":
            chen = user
            break
    if chen is None:
        return False, "Could not find user 'Chen Wei'."
    chen_id = chen["id"]

    # Find epic "Performance Initiative"
    performance_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "Performance Initiative":
            performance_epic = epic
            break
    if performance_epic is None:
        return False, "Could not find epic 'Performance Initiative'."
    performance_epic_id = performance_epic["id"]

    # Find child epics (those with parentEpicId == performance_epic_id)
    child_epic_ids = set()
    child_epic_ids.add(performance_epic_id)  # Include parent itself
    for epic in state.get("epics", []):
        if epic.get("parentEpicId") == performance_epic_id:
            child_epic_ids.add(epic["id"])

    if len(child_epic_ids) < 2:
        return False, "Expected child epics under 'Performance Initiative', only found the parent."

    # Find issues in any of these epics where Luca was originally assigned
    # In seed data: issue_12 "Configure read replicas for reporting queries",
    #   issue_55 "Configure CDN for static asset delivery",
    #   issue_56 "Implement Redis session store"
    expected_titles = [
        "Configure read replicas for reporting queries",
        "Configure CDN for static asset delivery",
        "Implement Redis session store",
    ]

    issues_by_title = {}
    for issue in state.get("issues", []):
        title = issue.get("title")
        if title in expected_titles:
            issues_by_title[title] = issue

    missing = [t for t in expected_titles if t not in issues_by_title]
    if missing:
        return False, f"Could not find expected issues: {missing}"

    errors = []
    for title, issue in issues_by_title.items():
        assignees = issue.get("assignees", [])
        if luca_id in assignees:
            errors.append(f"Luca Rossi still assigned to '{title}'.")
        if chen_id not in assignees:
            errors.append(f"Chen Wei not assigned to '{title}'.")

    if errors:
        return False, " ".join(errors)

    return True, "All of Luca Rossi's issues in 'Performance Initiative' and child epics reassigned to Chen Wei."
