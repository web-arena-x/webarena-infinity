import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Open issues with weight >= 13
    expected_titles = [
        "Implement GraphQL gateway for v3 API",
        "Add dark mode support for the entire application",
        "Build real-time collaborative editing for issue descriptions",
        "Add custom fields support for issues",
        "Add merge request approval rules engine",
        "Internationalization (i18n) framework setup",
        "Migrate user authentication from sessions to JWT",
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

        # Check for 1-hour timelog with 'Architecture review'
        has_timelog = any(
            t.get("issueId") == issue["id"]
            and t.get("timeSpent") == 3600
            and "architecture review" in t.get("summary", "").lower()
            for t in state.get("timelogs", [])
        )
        if not has_timelog:
            errors.append(
                f"Issue '{title}' missing 1-hour 'Architecture review' time entry."
            )

    if errors:
        return False, " ".join(errors)

    return True, f"Architecture review logged on all {len(expected_titles)} high-weight issues."
