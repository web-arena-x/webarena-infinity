import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    errors = []

    prestige = next((t for t in themes if t.get("name") == "Prestige"), None)
    if prestige is None:
        return False, "Could not find Prestige theme."

    sections = prestige.get("sectionsPerPage", {})

    # Collection should match Dawn's product sections (6)
    if sections.get("collection") != 6:
        errors.append(f"Prestige collection sections is {sections.get('collection')}, expected 6.")

    # Blog should be 4
    if sections.get("blog") != 4:
        errors.append(f"Prestige blog sections is {sections.get('blog')}, expected 4.")

    if errors:
        return False, " ".join(errors)
    return True, "Prestige collection sections set to 6 (matching Dawn's product) and blog sections set to 4."
