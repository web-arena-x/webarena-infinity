import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])

    old_title = next((i for i in issues if i["title"] == "Migrate user settings page to React"), None)
    if old_title is not None:
        return False, "Issue with old title 'Migrate user settings page to React' still exists."

    new_title = next((i for i in issues if i["title"] == "Migrate user settings page to React and TypeScript"), None)
    if not new_title:
        return False, "Issue with new title 'Migrate user settings page to React and TypeScript' not found."

    return True, "Issue renamed: 'Migrate user settings page to React' no longer exists and 'Migrate user settings page to React and TypeScript' exists."
