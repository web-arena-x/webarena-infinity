import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    workspaces = state.get("workspaces", [])
    for workspace in workspaces:
        if workspace.get("name") == "Side Project Labs":
            return False, "Workspace 'Side Project Labs' still exists."

    return True, "Workspace 'Side Project Labs' has been removed."
