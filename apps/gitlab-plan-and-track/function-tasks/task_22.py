import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "File upload fails silently for files > 50MB"), None)
    if not issue:
        return False, "Issue 'File upload fails silently for files > 50MB' not found."

    if issue["dueDate"] != "2026-05-01":
        return False, f"Issue dueDate is '{issue['dueDate']}', expected '2026-05-01'."

    return True, "Issue 'File upload fails silently for files > 50MB' has dueDate set to '2026-05-01'."
