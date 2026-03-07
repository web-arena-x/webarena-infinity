import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state["settings"]

    draft_type = settings.get("autoDrafts", {}).get("type")
    if draft_type == "scheduling":
        return True, "Auto Draft type changed to 'Scheduling'."
    return False, f"Auto Draft type is '{draft_type}', expected 'scheduling'."
