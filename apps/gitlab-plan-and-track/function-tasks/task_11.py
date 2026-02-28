import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    target = next((i for i in issues if i["title"] == "File upload fails silently for files > 50MB"), None)
    if not target:
        return False, "Issue 'File upload fails silently for files > 50MB' not found."

    labels = target.get("labels", [])
    if "lbl_21" not in labels:
        return False, f"'lbl_21' (security) not in labels: {labels}."

    return True, "Issue 'File upload fails silently for files > 50MB' has the 'security' label (lbl_21)."
