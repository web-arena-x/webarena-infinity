import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    errors = []

    # Prestige has the highest total sections (18+12+9+5+7=51) — should be published
    prestige = next((t for t in themes if t.get("name") == "Prestige"), None)
    if prestige is None:
        return False, "Could not find Prestige theme."

    if prestige.get("role") != "main":
        errors.append(f"Prestige role is '{prestige.get('role')}', expected 'main'.")

    # Prestige homepage sections should match Horizon's original homepage count (12)
    home_sections = prestige.get("sectionsPerPage", {}).get("home")
    if home_sections != 12:
        errors.append(f"Prestige homepage sections is {home_sections}, expected 12.")

    # Horizon should now be unpublished
    horizon = next((t for t in themes if t.get("name") == "Horizon - Outdoors"), None)
    if horizon and horizon.get("role") != "unpublished":
        errors.append(f"Horizon role is '{horizon.get('role')}', expected 'unpublished'.")

    if errors:
        return False, " ".join(errors)
    return True, "Prestige (most sections) published with homepage sections matching Horizon's original count of 12."
