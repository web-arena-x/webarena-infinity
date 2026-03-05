import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    general = settings.get("general", {})
    auto_advance = general.get("autoAdvance")

    if auto_advance is False:
        return True, "Auto-advance successfully disabled."

    return False, (
        f"autoAdvance is {auto_advance}, expected False."
    )
