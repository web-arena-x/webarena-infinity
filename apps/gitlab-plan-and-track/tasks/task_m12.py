import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    iterations = state.get("iterations", [])
    sprint_27 = next((it for it in iterations if it.get("title") == "Sprint 27"), None)
    if sprint_27 is None:
        return False, "Could not find iteration titled 'Sprint 27'."

    issues = state.get("issues", [])

    issue_apm = next((i for i in issues if i.get("title") == "Analyze and optimize slow queries from APM logs"), None)
    if issue_apm is None:
        return False, "Could not find issue titled 'Analyze and optimize slow queries from APM logs'."

    issue_keyset = next((i for i in issues if i.get("title") == "Optimize issue list query to use keyset pagination"), None)
    if issue_keyset is None:
        return False, "Could not find issue titled 'Optimize issue list query to use keyset pagination'."

    sprint_27_id = sprint_27.get("id")

    if issue_apm.get("iterationId") != sprint_27_id:
        return False, f"Issue 'Analyze and optimize slow queries from APM logs' has iterationId '{issue_apm.get('iterationId')}' but expected Sprint 27 id '{sprint_27_id}'."

    if issue_keyset.get("iterationId") != sprint_27_id:
        return False, f"Issue 'Optimize issue list query to use keyset pagination' has iterationId '{issue_keyset.get('iterationId')}' but expected Sprint 27 id '{sprint_27_id}'."

    return True, "Both issues assigned to David Kim have been moved from Sprint 26 to Sprint 27."
