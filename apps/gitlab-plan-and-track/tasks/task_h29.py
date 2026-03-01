import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find v5.0 - Enterprise Edition milestone
    ms_v50 = None
    for ms in state.get("milestones", []):
        if "v5.0" in ms.get("title", "") and "Enterprise" in ms.get("title", ""):
            ms_v50 = ms
            break
    if ms_v50 is None:
        return False, "Could not find milestone 'v5.0 - Enterprise Edition'."
    ms_id = ms_v50["id"]

    # Find all open issues in this milestone
    v50_issues = []
    for issue in state.get("issues", []):
        if issue.get("milestoneId") == ms_id and issue.get("status") == "open":
            v50_issues.append(issue)

    if len(v50_issues) < 5:
        return False, f"Expected at least 5 open issues in v5.0 milestone, found {len(v50_issues)}."

    # Check that every issue has a due date set
    errors = []
    for issue in v50_issues:
        due = issue.get("dueDate")
        if due is None:
            errors.append(f"{issue.get('title')} (no due date)")
        elif due != "2026-10-31":
            # Issues that already had a due date can keep it; issues that had none must be 2026-10-31
            pass  # Original due dates are fine

    if errors:
        return False, f"These v5.0 issues still have no due date: {errors}"

    # Specifically check known originally-dateless issues
    expected_titles = [
        "Add webhook support for issue state changes",
        "Implement GitLab Pages custom domain support",
        "Add merge request approval rules engine",
        "Add inline code suggestions in merge request reviews",
        "Internationalization (i18n) framework setup",
        "Migrate user authentication from sessions to JWT",
    ]

    for title in expected_titles:
        issue = next((i for i in state.get("issues", []) if i.get("title") == title), None)
        if issue is None:
            continue  # Issue may have been moved
        if issue.get("milestoneId") == ms_id and issue.get("dueDate") != "2026-10-31":
            return False, f"Issue '{title}' should have dueDate '2026-10-31', got '{issue.get('dueDate')}'."

    return True, f"All open issues in v5.0 - Enterprise Edition milestone have due dates set."
