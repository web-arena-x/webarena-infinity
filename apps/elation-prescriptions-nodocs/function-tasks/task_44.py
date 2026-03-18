import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    show_generic = settings.get("showGenericFirst")
    if show_generic is not False:
        return False, f"showGenericFirst is {show_generic}, expected False."

    return True, "Show generic name first has been disabled (showGenericFirst is False)."
