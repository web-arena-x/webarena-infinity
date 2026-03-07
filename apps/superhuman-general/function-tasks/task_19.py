import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    snippets = state.get("snippets", [])

    snippet = next(
        (s for s in snippets if s.get("name") == "Project Update"),
        None,
    )
    if snippet is None:
        return False, "No snippet named 'Project Update' found."

    if snippet.get("isShared") is not True:
        return False, f"Snippet 'Project Update' is not shared. isShared={snippet.get('isShared')}"

    body = snippet.get("body", "")
    if "{first_name}" not in body:
        return False, f"Snippet body does not contain '{{first_name}}'. Body: {body[:200]}"

    if "{project_name}" not in body:
        return False, f"Snippet body does not contain '{{project_name}}'. Body: {body[:200]}"

    return True, "Snippet 'Project Update' created with shared flag and correct template variables."
