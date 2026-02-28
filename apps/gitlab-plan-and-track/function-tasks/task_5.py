import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Dashboard widget layout breaks at 1440px viewport"), None)
    if not target:
        return False, "Issue 'Dashboard widget layout breaks at 1440px viewport' not found."

    if target.get("status") != "closed":
        return False, f"Issue status is '{target.get('status')}', expected 'closed'."

    if target.get("closedAt") is None:
        return False, "Issue closedAt is None, expected a timestamp."

    return True, "Issue 'Dashboard widget layout breaks at 1440px viewport' is closed with a closedAt timestamp."
