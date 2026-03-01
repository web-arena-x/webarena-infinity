import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find good-first-issue label
    gfi_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "good-first-issue":
            gfi_label = lbl
            break
    if gfi_label is None:
        return False, "Could not find label 'good-first-issue'."

    expected_titles = [
        "Write getting started guide for new developers",
        "Fix typo in 404 error page message",
        "Add tooltip to truncated sidebar labels",
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

        # Should be closed
        if issue.get("status") != "closed":
            errors.append(f"Issue '{title}' should be closed, got '{issue.get('status')}'.")

        # Should have a 30-minute timelog with 'Resolved during onboarding'
        has_timelog = any(
            t.get("issueId") == issue["id"]
            and t.get("timeSpent") == 1800
            and "resolved during onboarding" in t.get("summary", "").lower()
            for t in state.get("timelogs", [])
        )
        if not has_timelog:
            errors.append(
                f"Issue '{title}' missing 30-min 'Resolved during onboarding' time entry."
            )

    if errors:
        return False, " ".join(errors)

    return True, f"All {len(expected_titles)} good-first-issue issues logged and closed."
