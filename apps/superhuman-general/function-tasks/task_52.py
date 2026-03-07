import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    splits = state.get("splits", [])

    for split in splits:
        if split.get("name") == "Feeds":
            return False, "Split 'Feeds' still exists; it should have been deleted."

    return True, "Split 'Feeds' has been deleted."
