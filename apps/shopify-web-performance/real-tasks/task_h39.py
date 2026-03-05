import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    errors = []

    # Dawn has fewest total sections (8+6+5+3+4=26) — should be published
    dawn = next((t for t in themes if t.get("name") == "Dawn (backup)"), None)
    if dawn is None:
        return False, "Could not find Dawn (backup) theme."

    if dawn.get("role") != "main":
        errors.append(f"Dawn role is '{dawn.get('role')}', expected 'main'.")

    # Dawn animations should be enabled
    if dawn.get("hasAnimations") is not True:
        errors.append(f"Dawn hasAnimations is {dawn.get('hasAnimations')}, expected True.")

    # Dawn homepage sections should be 12
    home = dawn.get("sectionsPerPage", {}).get("home")
    if home != 12:
        errors.append(f"Dawn homepage sections is {home}, expected 12.")

    # Horizon should now be unpublished
    horizon = next((t for t in themes if t.get("name") == "Horizon - Outdoors"), None)
    if horizon and horizon.get("role") != "unpublished":
        errors.append(f"Horizon role is '{horizon.get('role')}', expected 'unpublished'.")

    if errors:
        return False, " ".join(errors)
    return True, "Dawn (fewest sections) published, animations enabled, homepage sections set to 12."
