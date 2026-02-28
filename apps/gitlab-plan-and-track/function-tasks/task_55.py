import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    iterations = state.get("iterations", [])

    target = next((i for i in issues if i["title"] == "Implement keyboard shortcuts for common actions"), None)
    if not target:
        return False, "Issue 'Implement keyboard shortcuts for common actions' not found."

    march_iter = next((it for it in iterations if it["title"] == "March 2026"), None)
    if not march_iter:
        return False, "Iteration with title 'March 2026' not found."

    if target.get("iterationId") != march_iter["id"]:
        return False, f"Issue iterationId is '{target.get('iterationId')}', expected '{march_iter['id']}'."

    labels = target.get("labels", [])
    if "lbl_19" not in labels:
        return False, f"Label 'lbl_19' (needs-discussion) not found in issue labels: {labels}."

    return True, "Issue 'Implement keyboard shortcuts for common actions' has iterationId matching 'March 2026' and label 'lbl_19' (needs-discussion)."
