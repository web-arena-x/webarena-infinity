import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issue = next((i for i in state["issues"] if i["title"] == "Implement lazy loading for images and avatars"), None)
    if not issue:
        return False, "Issue 'Implement lazy loading for images and avatars' not found."

    epic = next((e for e in state["epics"] if e["title"] == "Performance Initiative"), None)
    if not epic:
        return False, "Epic 'Performance Initiative' not found."

    if issue["epicId"] != epic["id"]:
        return False, f"Issue epicId is '{issue['epicId']}', expected '{epic['id']}'."

    return True, "Issue 'Implement lazy loading for images and avatars' has epicId matching 'Performance Initiative'."
