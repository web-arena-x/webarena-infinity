import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Sprint 26 and Sprint 27
    sprint26 = sprint27 = None
    for it in state.get("iterations", []):
        if it.get("title") == "Sprint 26":
            sprint26 = it
        elif it.get("title") == "Sprint 27":
            sprint27 = it
    if sprint26 is None:
        return False, "Could not find iteration 'Sprint 26'."
    if sprint27 is None:
        return False, "Could not find iteration 'Sprint 27'."

    # Expected issues: Sprint 26 open issues with at_risk or needs_attention health
    expected_titles = [
        "Migrate user settings page to React",
        "Implement Content Security Policy headers",
        "Upgrade vulnerable dependencies identified in audit",
        "Login page shows blank screen on Safari 17.2",
        "Reduce JavaScript bundle size by 40%",
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

        # Should be moved to Sprint 27
        if issue.get("iterationId") != sprint27["id"]:
            errors.append(f"Issue '{title}' not moved to Sprint 27.")

        # Should have a timelog with 'Sprint risk review'
        has_timelog = any(
            t.get("issueId") == issue["id"]
            and t.get("timeSpent") == 7200
            and "sprint risk review" in t.get("summary", "").lower()
            for t in state.get("timelogs", [])
        )
        if not has_timelog:
            errors.append(f"Issue '{title}' missing 2-hour 'Sprint risk review' time entry.")

    if errors:
        return False, " ".join(errors)

    return True, f"All {len(expected_titles)} at-risk Sprint 26 issues logged and moved to Sprint 27."
