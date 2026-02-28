import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find user "James O'Brien" by name
    james = None
    for user in state.get("users", []):
        if user.get("name") == "James O'Brien":
            james = user
            break
    if james is None:
        return False, "Could not find user 'James O'Brien'."
    james_id = james["id"]

    # Find user "Yuki Tanaka" by name
    yuki = None
    for user in state.get("users", []):
        if user.get("name") == "Yuki Tanaka":
            yuki = user
            break
    if yuki is None:
        return False, "Could not find user 'Yuki Tanaka'."
    yuki_id = yuki["id"]

    # Find user "Oliver Schmidt" for the co-assigned issue check
    oliver = None
    for user in state.get("users", []):
        if user.get("name") == "Oliver Schmidt":
            oliver = user
            break
    if oliver is None:
        return False, "Could not find user 'Oliver Schmidt'."
    oliver_id = oliver["id"]

    # Expected open issues that were James's (by title)
    expected_titles = [
        "Migrate projects API to v3",
        "Implement Content Security Policy headers",
        "File upload fails silently for files > 50MB",
        "Implement audit logging for admin actions",
        "Add project archival functionality",
        "Migrate user authentication from sessions to JWT",
    ]

    issues_by_title = {}
    for issue in state.get("issues", []):
        title = issue.get("title")
        if title in expected_titles:
            issues_by_title[title] = issue

    missing = [t for t in expected_titles if t not in issues_by_title]
    if missing:
        return False, f"Could not find expected issues: {missing}"

    # Check each issue: James NOT in assignees, Yuki IS in assignees
    errors = []
    for title, issue in issues_by_title.items():
        assignees = issue.get("assignees", [])
        if james_id in assignees:
            errors.append(f"James still assigned to '{title}'.")
        if yuki_id not in assignees:
            errors.append(f"Yuki not assigned to '{title}'.")

    # Special check: Oliver should still be assigned to "Implement Content Security Policy headers"
    csp_issue = issues_by_title.get("Implement Content Security Policy headers")
    if csp_issue is not None:
        if oliver_id not in csp_issue.get("assignees", []):
            errors.append("Oliver Schmidt was removed from 'Implement Content Security Policy headers' but should remain.")

    if errors:
        return False, " ".join(errors)

    return True, f"All of James O'Brien's open issues successfully reassigned to Yuki Tanaka."
