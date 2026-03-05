import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    split_inbox = settings.get("splitInbox", {})
    enabled = split_inbox.get("enabled")

    if enabled is False:
        return True, "Split inbox successfully disabled."

    return False, (
        f"splitInbox.enabled is {enabled}, expected False."
    )
