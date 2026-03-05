import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that snippet 'Meeting Follow-Up' has been renamed to 'Post-Meeting Summary'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    snippets = state.get("snippets", [])
    snippet_names = [s.get("name") for s in snippets]

    has_new_name = "Post-Meeting Summary" in snippet_names
    has_old_name = "Meeting Follow-Up" in snippet_names

    if has_new_name and not has_old_name:
        return True, "Snippet renamed to 'Post-Meeting Summary' successfully."
    if has_old_name and not has_new_name:
        return False, "Snippet 'Meeting Follow-Up' still exists and has not been renamed."
    if has_old_name and has_new_name:
        return False, "Both 'Meeting Follow-Up' and 'Post-Meeting Summary' exist. The old snippet was not renamed, a new one may have been created."
    return False, f"Neither 'Meeting Follow-Up' nor 'Post-Meeting Summary' found. Existing snippets: {snippet_names!r}."
