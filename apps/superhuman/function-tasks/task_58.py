import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that a snippet named 'Quick Acknowledgment' exists."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    snippets = state.get("snippets", [])
    for snippet in snippets:
        if snippet.get("name") == "Quick Acknowledgment":
            return True, "Snippet 'Quick Acknowledgment' exists."

    snippet_names = [s.get("name") for s in snippets]
    return False, f"No snippet named 'Quick Acknowledgment' found. Existing snippets: {snippet_names!r}."
