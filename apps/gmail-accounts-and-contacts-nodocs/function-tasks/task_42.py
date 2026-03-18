import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    reply_from = state.get("replyFromSetting")

    if reply_from != "same":
        return False, f"Expected replyFromSetting 'same', got '{reply_from}'."

    return True, "Reply-from setting successfully changed to 'same'."
