import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    epics = state.get("epics", [])
    epic = next((e for e in epics if e.get("title") == "CI/CD Pipeline Improvements"), None)
    if epic is None:
        return False, "Could not find epic titled 'CI/CD Pipeline Improvements'."

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Set up end-to-end testing with Playwright"), None)
    if issue is None:
        return False, "Could not find issue titled 'Set up end-to-end testing with Playwright'."

    if issue.get("epicId") != epic.get("id"):
        return False, f"Issue's epicId '{issue.get('epicId')}' does not match 'CI/CD Pipeline Improvements' epic id '{epic.get('id')}'."

    return True, "Epic 'CI/CD Pipeline Improvements' created and issue 'Set up end-to-end testing with Playwright' is correctly linked to it."
