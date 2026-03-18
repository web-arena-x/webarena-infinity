import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    delegates = state.get("delegates", [])

    if len(delegates) != 0:
        names = [d.get("name", d.get("email")) for d in delegates]
        return False, f"Expected no delegates, but found {len(delegates)}: {', '.join(names)}"

    return True, "All delegates have been removed."
