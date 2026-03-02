import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state["preferences"]["automationsAndWorkflows"]["gitAttachmentFormat"]
    if val != "Title and repository":
        return False, f"Expected git attachment format 'Title and repository', got '{val}'."

    return True, "Git attachment format set to 'Title and repository'."
