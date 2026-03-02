import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state["preferences"]["automationsAndWorkflows"]["onGitBranchCopyAutoAssign"]
    if val is not False:
        return False, f"Expected onGitBranchCopyAutoAssign to be False, got '{val}'."

    return True, "On git branch copy auto-assign disabled."
