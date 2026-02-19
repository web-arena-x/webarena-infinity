import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify git attachment format and git branch auto-assign settings."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})

    fmt = prefs.get("gitAttachmentFormat")
    auto_assign = prefs.get("gitBranchAutoAssign")

    if fmt != "title_and_repo":
        return False, f"Expected gitAttachmentFormat='title_and_repo', got '{fmt}'."
    if auto_assign is not True:
        return False, f"Expected gitBranchAutoAssign=true, got {auto_assign}."

    return True, "Git attachment format set to 'Title and repository' and auto-assign enabled."
