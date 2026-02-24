import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    density = settings.get("density")

    if density == "compact":
        return True, "Task completed successfully."
    else:
        return False, f"settings.density is '{density}', expected 'compact'."
