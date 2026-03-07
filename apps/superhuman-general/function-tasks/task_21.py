import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    snippets = state.get("snippets", [])

    for snippet in snippets:
        if snippet.get("name") == "Decline Politely":
            return False, "Snippet 'Decline Politely' still exists."

    return True, "Snippet 'Decline Politely' has been successfully deleted."
