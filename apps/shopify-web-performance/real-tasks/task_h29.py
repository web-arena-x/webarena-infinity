import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    errors = []

    horizon = next((t for t in themes if t.get("name") == "Horizon - Outdoors"), None)
    dawn = next((t for t in themes if t.get("name") == "Dawn (backup)"), None)

    if horizon is None:
        return False, "Could not find Horizon - Outdoors theme."
    if dawn is None:
        return False, "Could not find Dawn (backup) theme."

    # Horizon (updated 2026-02-18, more recently): product sections reduced by 2 (8 -> 6)
    horizon_product = horizon.get("sectionsPerPage", {}).get("product")
    if horizon_product != 6:
        errors.append(f"Horizon product sections is {horizon_product}, expected 6.")

    # Dawn (updated 2025-08-12, less recently): blog sections increased by 2 (4 -> 6)
    dawn_blog = dawn.get("sectionsPerPage", {}).get("blog")
    if dawn_blog != 6:
        errors.append(f"Dawn blog sections is {dawn_blog}, expected 6.")

    if errors:
        return False, " ".join(errors)
    return True, "Horizon product sections reduced by 2 (to 6), Dawn blog sections increased by 2 (to 6)."
