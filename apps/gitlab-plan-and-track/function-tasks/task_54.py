import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Implement API versioning documentation"), None)
    if not target:
        return False, "Issue with title 'Implement API versioning documentation' not found."

    if target.get("startDate") != "2026-03-15":
        return False, f"Issue startDate is '{target.get('startDate')}', expected '2026-03-15'."

    if target.get("dueDate") != "2026-04-15":
        return False, f"Issue dueDate is '{target.get('dueDate')}', expected '2026-04-15'."

    return True, "Issue 'Implement API versioning documentation' exists with startDate='2026-03-15' and dueDate='2026-04-15'."
