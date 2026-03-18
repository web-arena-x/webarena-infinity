import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    reply_from = state.get("replyFromSetting")
    if reply_from == "same":
        return True, "Reply-from setting is set to 'same' (reply from the address the message was sent to)."
    else:
        return False, f"Reply-from setting is '{reply_from}', expected 'same'."
