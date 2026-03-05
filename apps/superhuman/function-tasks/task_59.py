import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the snippet 'Out of Office' has been deleted."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    snippets = state.get("snippets", [])
    for snippet in snippets:
        if snippet.get("name") == "Out of Office":
            return False, "Snippet 'Out of Office' still exists."

    return True, "Snippet 'Out of Office' has been deleted."
