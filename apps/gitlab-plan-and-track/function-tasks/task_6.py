import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "Fix SQL injection vulnerability in search endpoint"), None)
    if not target:
        return False, "Issue 'Fix SQL injection vulnerability in search endpoint' not found."

    if target.get("status") != "open":
        return False, f"Issue status is '{target.get('status')}', expected 'open'."

    if target.get("closedAt") is not None:
        return False, f"Issue closedAt is '{target.get('closedAt')}', expected None."

    return True, "Issue 'Fix SQL injection vulnerability in search endpoint' is reopened with status 'open' and closedAt is None."
