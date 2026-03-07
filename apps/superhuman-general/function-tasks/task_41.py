import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    meeting_link = settings.get("meetingLink", {})
    auto_add = meeting_link.get("autoAdd")

    if auto_add is not False:
        return False, f"Expected meetingLink.autoAdd to be False, got {auto_add}."

    return True, "Auto-add meeting link is disabled."
