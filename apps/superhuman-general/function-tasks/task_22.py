import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    snippets = state.get("snippets", [])

    for snippet in snippets:
        if snippet.get("id") == "snip_6" and snippet.get("name") == "Out of Office":
            if snippet.get("isShared") is True:
                return True, "Snippet 'Out of Office' (snip_6) is now shared."
            else:
                return False, f"Snippet 'Out of Office' (snip_6) isShared is {snippet.get('isShared')}, expected True."

    return False, "Snippet 'Out of Office' (snip_6) not found."
