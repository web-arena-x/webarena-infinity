import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    read_statuses = settings.get("readStatuses", {})
    enabled = read_statuses.get("enabled")

    if enabled is False:
        return True, "Read statuses successfully disabled."

    return False, (
        f"readStatuses.enabled is {enabled}, expected False."
    )
