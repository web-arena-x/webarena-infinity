import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    snippets = state.get("snippets", [])

    # Verify old name no longer exists
    old_snippet = next(
        (s for s in snippets if s.get("name") == "Meeting Follow-up"),
        None,
    )
    if old_snippet is not None:
        return False, "Snippet 'Meeting Follow-up' still exists (should have been renamed)."

    # Verify new name exists with the correct ID
    new_snippet = next(
        (s for s in snippets if s.get("name") == "Post-Meeting Summary"),
        None,
    )
    if new_snippet is None:
        return False, "No snippet named 'Post-Meeting Summary' found."

    if new_snippet.get("id") != "snip_1":
        return False, (
            f"Snippet 'Post-Meeting Summary' has id '{new_snippet.get('id')}' "
            f"instead of expected 'snip_1'."
        )

    return True, "Snippet 'Meeting Follow-up' renamed to 'Post-Meeting Summary' (id snip_1)."
