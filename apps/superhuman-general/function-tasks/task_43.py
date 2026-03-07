import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    auto_archive = settings.get("autoArchive", {})
    enabled = auto_archive.get("enabled")

    if enabled is not False:
        return False, f"Expected autoArchive.enabled to be False, got {enabled}."

    return True, "Auto Archive is disabled."
