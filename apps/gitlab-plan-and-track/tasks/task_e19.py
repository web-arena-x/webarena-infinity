import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    milestones = state.get("milestones", [])

    target_title = "Update project README with new setup instructions"
    issue = next((i for i in issues if i.get("title") == target_title), None)

    if issue is None:
        return False, f"Could not find issue with title '{target_title}'."

    milestone_title = "Q1 2026 Planning"
    milestone = next((m for m in milestones if m.get("title") == milestone_title), None)

    if milestone is None:
        return False, f"Could not find milestone with title '{milestone_title}'."

    milestone_id = milestone.get("id")
    issue_milestone_id = issue.get("milestoneId")

    if issue_milestone_id != milestone_id:
        return False, (
            f"Issue '{target_title}' milestoneId is '{issue_milestone_id}', "
            f"expected '{milestone_id}' ('{milestone_title}')."
        )

    return True, f"Issue '{target_title}' is in the '{milestone_title}' milestone."
