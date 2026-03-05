import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    errors = []

    horizon = next((t for t in themes if t.get("name") == "Horizon - Outdoors"), None)
    if horizon is None:
        return False, "Could not find Horizon - Outdoors theme."

    # Prestige has 18 homepage sections; half = 9
    # Horizon (current live theme) should be set to 9
    home = horizon.get("sectionsPerPage", {}).get("home")
    if home != 9:
        errors.append(f"Horizon homepage sections is {home}, expected 9 (half of Prestige's 18).")

    if errors:
        return False, " ".join(errors)
    return True, "Horizon homepage sections set to 9 (half of Prestige's 18)."
