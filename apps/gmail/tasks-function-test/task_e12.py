import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    send_and_archive = settings.get("sendAndArchive")

    if send_and_archive is False:
        return True, "Task completed successfully."
    else:
        return False, f"Send & Archive is not disabled (sendAndArchive={send_and_archive})."
