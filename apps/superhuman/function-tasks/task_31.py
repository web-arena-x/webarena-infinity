import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    general = settings.get("general", {})
    density = general.get("density")

    if density == "compact":
        return True, "Density successfully changed to 'compact'."

    return False, f"Density is '{density}', expected 'compact'."
