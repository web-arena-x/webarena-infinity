import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state["preferences"]["general"]["convertEmoticonToEmoji"]
    if val is not False:
        return False, f"Expected convertEmoticonToEmoji to be False, got '{val}'."

    return True, "Convert emoticon to emoji disabled."
